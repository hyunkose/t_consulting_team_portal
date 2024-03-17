function emp_info_submit(){
    const emp_email = document.querySelector('#email').value
    const emp_status_obj = document.querySelector('#emp-status')

    const emp_status = emp_status_obj.options[emp_status_obj.selectedIndex].text
    const rest_start_date = document.querySelector('#rest-start-date').value
    const rest_end_date = document.querySelector('#rest-end-date').value
    const leave_date = document.querySelector('#leave-date').value

    const input_list = [
        emp_email,
        emp_status,
        rest_start_date,
        rest_end_date,
        leave_date,
    ]

    for(element of input_list){
        if (!element){            
            return alert('모든 필드를 입력해주세요')
        }
    }

    const status_payload = {
        emp_email: emp_email,
        emp_status: emp_status,
        rest_start_date: rest_start_date,
        rest_end_date: rest_end_date,
        leave_date: leave_date
    }

    fetch(window.location.href, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(status_payload)
    })
    .then((response) => alert('등록이 완료되었습니다'))
    .catch(console.log('post request error'))
}

function get_emp_name(){
    const emp_email = document.querySelector('#email')
    const selected_emp_email = emp_email.options[emp_email.selectedIndex]

    let emp_name_tag = document.querySelector('#emp-name')
    emp_name_tag.value = selected_emp_email.getAttribute('aria-label')
}

function show_date_field(){
    const emp_status = document.querySelector('#emp-status')
    const selected_emp_status = emp_status.options[emp_status.selectedIndex].text
    
    let rest_start_date_label = document.querySelector('#rest-start-date-label')
    let rest_start_date = document.querySelector('#rest-start-date')
    let rest_end_date_label = document.querySelector('#rest-end-date-label')
    let rest_end_date = document.querySelector('#rest-end-date')

    let leave_date_label = document.querySelector('#leave-date-label')
    let leave_date = document.querySelector('#leave-date')

    rest_list = [
        rest_start_date_label,
        rest_start_date,
        rest_end_date_label,
        rest_end_date
    ]

    leave_list = [
        leave_date_label,
        leave_date
    ]

    if(selected_emp_status === '휴직'){
        leave_list.map((element) => element.style.display = 'none')
        rest_list.map((element) => element.style.display = 'block')
    } else if(selected_emp_status === '퇴사'){
        rest_list.map((element) => element.style.display = 'none')
        leave_list.map((element) => element.style.display = 'block')
    } else if(selected_emp_status === '선택'){
        leave_list.map((element) => element.style.display = 'none')
        rest_list.map((element) => element.style.display = 'none')
    }
}