from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'contents':['IF you would like to contact me, please E-mail me : ','kashishsehgal73@gmail.com']})

