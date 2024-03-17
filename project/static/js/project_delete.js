function project_delete_submit(){
    const emp_email = document.querySelector('#emp-email').value
    const client_name = document.querySelector('#client-name').value
    const project_start_date = document.querySelector('#proj-start-date').value

    const input_list = [
        emp_email,
        client_name,
        project_start_date
    ]

    for(element of input_list){
        if (!element){            
            return alert('모든 필드를 입력해주세요')
        }
    }

    const project_delete_payload = {
        emp_email: emp_email,
        client_name: client_name,
        project_start_date: project_start_date
    }

    fetch(window.location.href, {
        method: 'DELETE',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(project_delete_payload)
    })
    .then((response) => {
        response.json().then(message => alert(message.message))
    })
}

function get_emp_name(){
    const emp_email = document.querySelector('#emp-email')
    const selected_emp_email = emp_email.options[emp_email.selectedIndex]

    let emp_name_tag = document.querySelector('#emp-name')
    emp_name_tag.value = selected_emp_email.getAttribute('aria-label')
}