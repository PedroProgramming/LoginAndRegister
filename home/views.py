from django.shortcuts import render
from django.contrib.auth.decorators import login_required




@login_required(login_url='/auth/login/')
def home(request):

    if request.user.is_authenticated:
        user = request.user

        context = {
            'user': user
        }

        return render(request, 'home.html', context=context)