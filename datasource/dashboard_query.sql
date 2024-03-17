
/* 
  조인조건 1
  1) 조건: 마스터 날짜 > 기준 날짜
  2) 조건 설명: Tableau 화면 내 조회일자 (마스터 날짜) 기준으로 특정 사원이 입사한 이후의 날짜에만 사원 정보가 나타나도록 조건 부여
*/
WITH merge_process_1 AS (
    SELECT md.std_dt,
		   ei.emp_cd,
           ei.emp_name,
           ei.email,
           ei.emp_level,
           ei.hired_date,
           ei.total_vacations
    FROM master_date AS md
    LEFT JOIN employee_info AS ei
    ON md.std_dt >= ei.std_dt
),

/*
  조인조건 2
  1) 조건: 사원 코드 = 사원 코드 AND 마스터 날짜 >= 프로젝트 시작일 AND 마스터 날짜 <= 프로젝트 종료일
  2) 조건 설명: Tableau 화면 내 조회 일자 (마스터 날짜) 기준으로 사원의 프로젝트 파견 정보가 프로젝트 투입 기간에만 나타나도록 조건 부여
*/
merge_process_2 AS (
	SELECT mp1.std_dt,
	       mp1.emp_cd,
	       mp1.emp_name,
	       mp1.email,
	       mp1.emp_level,
	       mp1.hired_date,
	       mp1.total_vacations,
		   ps.client,
		   ps.project_start_date,
		   ps.project_end_date,
		   ps.client_location,
		   ps.jobs
	FROM merge_process_1 AS mp1
	LEFT JOIN project_info AS ps
	ON mp1.std_dt >= ps.project_start_date 
		AND mp1.std_dt <= ps.project_end_date 
		AND mp1.emp_cd = ps.emp_cd
),

/*
  조인조건 3
  1) 조건: 사원 코드 = 사원 코드 AND 마스터 날짜 >= 휴가 시작일 AND 마스터 날짜 <= 휴가 종료일
  2) 조건 설명: Tableau 화면 내 조회 일자 (마스터 날짜) 기준으로 사원이 신청한 휴가 정보가 휴가를 보내는 일자에만 찍히도록 조건 부여
*/
merge_process_3 AS (
	SELECT mp2.std_dt,
	       mp2.emp_cd,
	       mp2.emp_name,
	       mp2.email,
	       mp2.emp_level,
	       mp2.hired_date,
	       mp2.total_vacations,
	       mp2.client,
	       mp2.project_start_date,
	       mp2.project_end_date,
           mp2.client_location,
           mp2.jobs,
		   vi.vacation_start_date,
		   vi.vacation_end_date,
		   vi.vacation_type,
		   vi.vacation_days
	FROM merge_process_2 AS mp2
	LEFT JOIN vacation_info AS vi
	ON mp2.std_dt >= vi.vacation_start_date
		AND mp2.std_dt <= vi.vacation_end_date
		AND mp2.emp_cd = vi.emp_cd
),

/*
  조인조건 4
  1) 조건: 사원 코드 = 사원 코드
          AND
		 재직 상태 매칭 (CASE 조건문)
         (1) “재직 중” 데이터의 경우
                  → 기준 날짜 >= 데이터 입력 일자 
         (2) “휴직 중“ 데이터의 경우
                  → 기준 날짜  >= 휴직 시작일 AND 기준 날짜 <= 휴직 종료일
         (3) “퇴사” 데이터의 경우
                  → 기준 날짜 <= 퇴사일
  2) 조건 설명: Tableau 화면 내 조회 일자 (마스터 날짜) 기준으로  사원의 재직 상태에 따라 다른 조인 조건을 부여

*/
merge_process_4 AS (
	SELECT mp3.std_dt,
	       mp3.emp_cd,
	       mp3.emp_name,
	       mp3.email,
	       mp3.emp_level,
	       mp3.hired_date,
	       mp3.total_vacations,
	       mp3.client,
	       mp3.project_start_date,
	       mp3.project_end_date,
	       mp3.client_location,
	       mp3.jobs,
	       mp3.vacation_start_date,
	       mp3.vacation_end_date,
	       mp3.vacation_type,
	       mp3.vacation_days,
		   es.status,
		   es.leave_date,
		   es.rest_start_date,
		   es.rest_end_date
	FROM merge_process_3 AS mp3
	LEFT JOIN employee_status AS es
	ON mp3.emp_cd = es.emp_cd
		AND CASE
			WHEN es.status = '재직' AND mp3.std_dt >= es.std_dt THEN 1
			WHEN es.status = '휴직' AND mp3.std_dt >= es.rest_start_date AND mp3.std_dt <= es.rest_end_date THEN 1
			WHEN es.status = '퇴사' AND mp3.std_dt >= es.leave_date THEN 1
			END = 1
),

/* 전처리 작업 1
  로직 설명: 조인 과정에서 중복되어 나타나는 휴직 사원의 재직 정보 제거 (휴직 기간동안에 중복되어 나타나는 "재직" 정보 제거, "휴직" 정보만 남기는 로직
*/
merge_process_5 AS (
	SELECT std_dt,
	       emp_cd,
	       emp_name,
	       email,
	       emp_level,
	       hired_date,
	       total_vacations,
	       client,
	       project_start_date,
	       project_end_date,
	       client_location,
	       jobs,
	       vacation_start_date,
	       vacation_end_date,
	       vacation_type,
	       vacation_days,
		   status,
		   leave_date,
		   rest_start_date,
		   rest_end_date

	FROM merge_process_4
	GROUP BY std_dt, emp_cd
	HAVING status = MAX(status)
		OR rest_start_date = MAX(rest_start_date)
),

/*전처리 작업 2
  로직 설명: Tableau 화면 내 캘린더 차트에서 휴가를 신청한 사원이 1명 이상인 날짜에 한해 색상 구분을 주기 위해 마스터 날짜 기준 일별 휴가 신청인원 컬럼 생성
*/
merge_process_6 AS (
	SELECT std_dt, COUNT(DISTINCT vacation_type) AS num_of_vacation_emp
	FROM merge_process_5
	GROUP BY std_dt
),

/* 전처리 작업 3
  로직 설명: 전처리 작업 2 단계에서 생성한 파생 컬럼 메인 데이터 원본에 merge하여 추가
*/
merge_process_7 AS(
	SELECT mp5.*, num_of_vacation_emp
	FROM merge_process_5 AS mp5
	LEFT JOIN merge_process_6 AS mp6 
	ON mp5.std_dt = mp6.std_dt
),

/* 전처리 작업 4
  로직 설명: 사원 별 휴가 소진 일수 파생 컬럼 추가 생성 작업
*/
merge_process_8 AS (
	SELECT std_dt,
		   emp_cd,
		   vacation_start_date,
		   MIN(vacation_days) AS vacation_days_unique
	FROM merge_process_7
	GROUP BY emp_cd, vacation_start_date
)

/* 전처리 작업 5
  로직 설명: 전처리 작업 4에서 생성한 사원 별 휴가 소진일수 컬럼을 메인 데이터 원본에 추가

*/
SELECT mp7.*, mp8.vacation_days_unique
FROM merge_process_7 AS mp7
LEFT JOIN merge_process_8 AS mp8
ON mp7.emp_cd = mp8.emp_cd AND mp7.std_dt = mp8.std_dt