from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def data_processing(username, password, repeat_password, age):
    users = ['Ivan', 'Olga', 'Vladimir', 'Anna']
    info = {}

    if password == repeat_password and int(age) >= 18 and username not in users:
        text = f'Приветствуем, {username}!'
        info = {'error': text}
    else:
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
    return info


def sign_up_by_django(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        context = {}
        info_dict = data_processing(username, password, repeat_password, age)
        context['text'] = info_dict['error']

        return render(request, 'fifth_task/registration_page.html', context)

    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_html(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            context = {}
            info_dict = data_processing(username, password, repeat_password, age)
            context['text'] = info_dict['error']
            context['form'] = form

            return render(request, 'fifth_task/registration_page.html', context)
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})
