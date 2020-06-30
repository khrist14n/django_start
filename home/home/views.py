from django.shortcuts import render, HttpResponse

def index(request):
    message = '<h1>Hola Mundo</h1>'
    return HttpResponse(message)

def home(request):
    message = 'Este texto puede ser lo que yo quiera'
    return render(
            request,
            'index.html',
            {
                'message':message
            }
        )