function emp_info_submit(){
    const emp_name = document.querySelector('#emp-name').value
    const emp_email = document.querySelector('#emp-email').value
    const emp_level = document.querySelector('#emp-level option:checked').value
    const emp_hired_date = document.querySelector('#emp-start-date').value
    const total_vacations = document.querySelector('#total-vacations').value

    const input_list = [
        emp_name,
        emp_email,
        emp_level,
        emp_hired_date,
        total_vacations,
    ]

    for(element of input_list){
        if (!element){            
            return alert('모든 필드를 입력해주세요')
        }
    }
    
    const emp_payload = {
        emp_name: emp_name,
        emp_email: emp_email,
        emp_level: emp_level,
        emp_hired_date: emp_hired_date,
        total_vacations: total_vacations,
    }

    fetch(window.location.href, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(emp_payload)
    })
    .then((response) => alert('등록이 완료되었습니다'))
    .catch(console.log('post request error'))
}


