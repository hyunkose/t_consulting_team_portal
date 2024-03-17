function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function login_submit(){
    const request_url = window.location.href;
    const csrfToken = getCookie('csrftoken');
    
    user_id = document.querySelector('#form2Example1').value;
    password = document.querySelector('#form2Example2').value;
    
    fetch(request_url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
            'user_id': user_id,
            'password': password,
        })
    })
    .then((res) => {

        res.json().then((data) =>{
            login_result = data.result_message
            if(login_result === 'success'){
                window.location.href = 'http://localhost:8000/';
            }
            else if (login_result === 'failure'){
                alert('계정 정보를 다시 확인해주세요')
            }
        })

    })
}