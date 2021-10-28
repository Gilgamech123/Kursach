from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from .basa import *
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import *


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
        tasks = get_material(request.session["id_user"])
        information = get_info(request.session["id_user"])
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

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('repeat_password')
            pasportData = request.POST.get('pasport_data')
            snils = request.POST.get('numsnils')

            if password == password2:
                user = User.objects.create_user(username, email, password)

                customer = Customer.objeact.create(user_id=user,passport_data =pasportData, snills = snils)
                context = {

                    'customer': customer
                }
                return redirect(request, 'login.html', context=context)

        return render(request, 'registration.html')




class PageDogovor(View):
    def get(self, request):
        context = {}
        return render(request, 'dogovor.html', context=context)
