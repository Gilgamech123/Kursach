from .models import *


def get_material(user_id):
    materials = Customer.objects.filter(user=user_id)
    return materials


def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users

def get_info(user_id):
    info = User.objects.filter(id=user_id)
    return info