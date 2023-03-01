from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as logar, logout


# Login

def validar_login(request):
	
	if request.method == 'POST':

		usuario = request.POST.get('usuario')
		senha = request.POST.get('senha')


		if len(usuario.strip()) == 0 or len(senha.strip()) == 0:
			messages.error(request, 'Campos invalidos.')
			return redirect('/auth/login/')
	
		user = authenticate(username = usuario, password = senha)

		if user is not None:
			logar(request, user)
			return redirect('/')
		else:
			messages.error(request, 'Usuario nao encontrado.')
			return redirect('/auth/login/')

def login(request):
	return render(request, 'login.html')


# Cadastro

def validar_cadastro(request):

	if request.method == 'POST':

		nome = request.POST.get('usuario')
		email = request.POST.get('email')
		senha = request.POST.get('senha')

		if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
			messages.error(request, 'Campos invalidos.')
			return redirect('/auth/cadastro/')

		try:
			user = User.objects.create_user(
				username=nome,
				email=email,
				password=senha,
			)
			user.save()

			messages.error(request, 'Cadastro feito com sucesso.')
			return redirect('/auth/login/')
		except:
			messages.error(request, 'Erro interno do sistema. Tente novamente mais tarde!')
			return redirect('/auth/cadastro/')


def cadastro(request):
	return render(request, 'register.html')


def sair_da_conta(request):
	logout(request)
	return redirect('/sair/saiu_da_conta/')