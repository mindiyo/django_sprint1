from django.shortcuts import render


def about(request):
    return render(request, 'about.html')  # Отображаем шаблон about.html


def rules(request):
    return render(request, 'rules.html')  # Отображаем шаблон rules.html
