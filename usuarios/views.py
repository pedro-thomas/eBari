from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_dashboard')  # redireciona para o painel após login bem-sucedido
        else:
            # Mensagem de erro
            pass
    return render(request, 'login.html')