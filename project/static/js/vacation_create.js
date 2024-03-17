function vacation_info_submit(){
    const emp_email = document.querySelector('#emp-email option:checked').value
    const this_vacation_amt = document.querySelector('#this-vacation-amt').value
    const vacation_start_date = document.querySelector('#vacation-start-date').value
    const vacation_end_date = document.querySelector('#vacation-end-date').value
    const vacation_type = document.querySelector('#vacation-type option:checked').value

    const input_list = [
        emp_email,
        this_vacation_amt,
        vacation_start_date,
        vacation_end_date,
        vacation_type,
    ]

    for(element of input_list){
        if (!element){            
            return alert('모든 필드를 입력해주세요')
        }
    }

    const vacation_payload = {
        emp_email: emp_email,
        this_vacation_amt: this_vacation_amt,
        vacation_start_date: vacation_start_date,
        vacation_end_date: vacation_end_date,
        vacation_type: vacation_type
    }

    fetch(window.location.href, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(vacation_payload)
    })
    .then((response) => alert('등록이 완료되었습니다'))
    .catch(console.log('post request error')) 
}

function get_emp_name(){
    const emp_email = document.querySelector('#emp-email')
    const selected_emp_email = emp_email.options[emp_email.selectedIndex]

    let emp_name_tag = document.querySelector('#emp-name')
    emp_name_tag.value = selected_emp_email.getAttribute('aria-label')
}