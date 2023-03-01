from django.shortcuts import render



def sair(request):
    user = request.user

    context = {
        'user': user,
    }
    
    return render(request, 'sair.html', context=context)