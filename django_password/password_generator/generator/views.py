from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def generate_password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+-?:;')

    length = int(request.GET.get('length', 12))
    password = ''

    for _ in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})
