from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def show_login(request):
    if request.method == 'GET':
        return render(request, 'login/login_main.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        user_password = data.get('password')
        user = authenticate(request, username = user_id, password = user_password)

        if user is not None:
            login(request, user)
            result_message = 'success'
            return JsonResponse({'result_message': result_message}, safe=False)
        else:
            result_message = 'failure'
            return JsonResponse({'result_message': result_message}, safe=False)

def logout_view(request):
    logout(request)
    return redirect('login')