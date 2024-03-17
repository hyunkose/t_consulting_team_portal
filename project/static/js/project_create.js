function proj_info_submit(){
    const emp_email = document.querySelector('#emp-email option:checked').value
    const client_name = document.querySelector('#client-name').value
    const client_location = document.querySelector('#client-location').value
    const proj_start_date = document.querySelector('#proj-start-date').value
    const proj_end_date = document.querySelector('#proj-end-date').value
    const jobs = document.querySelector('#jobs').value

    const input_list = [
        emp_email,
        client_name,
        client_location,
        proj_start_date,
        proj_end_date,
        jobs,
    ]
    
    for(element of input_list){
        if (!element){            
            return alert('모든 필드를 입력해주세요')
        }
    }

    const project_payload = {
        emp_email: emp_email,
        client_name: client_name,
        client_location: client_location,
        proj_start_date: proj_start_date,
        proj_end_date: proj_end_date,
        jobs: jobs
    }

    fetch(window.location.href, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(project_payload)
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