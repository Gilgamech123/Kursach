from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from .basa import *
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import *
from .forms import  *


class PageLogin(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context=context)

    def post(self, request):
        login = request.POST.get("login")
        password = request.POST.get("password")
        users = autoriz(login, password)
        if not users:
            context = {
                "message": "Введен не правильный пароль или логин"
            }
            return render(request, 'login.html', context=context)
        else:

            request.session["id_user"] = users[0].id
            return HttpResponseRedirect('home.html')

class PageHome(View):
    def get(self, request):
        if 'id_user' in request.session.keys():
            tasks = get_material(request.session['id_user'])
            information = get_info(request.session['id_user'])
            context = {
                'tasks': tasks,
                'information': information
            }
        return render(request, 'home.html', context=context)


class PageIndex(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)




# Create your views here.
class PageRegistration(View):
    def get(self, request):
        context = {}
        return render(request, 'registration.html', context=context)

    def post(self, request):
        if 'registration' in request.POST:
            if request.method == 'POST':
                reg=LoginForm(request.POST)
                if reg.is_valid():
                    reg.save()
                    return HttpResponseRedirect('login.html')
                else:
                    error="Ошибка формы"
            context = {
                'reg':reg,
                'error':error
            }
        return render(request, 'registration.html', context=context)



class PageDogovor(View):
    def get(self, request):
        context = {}
        return render(request, 'dogovor.html', context=context)
