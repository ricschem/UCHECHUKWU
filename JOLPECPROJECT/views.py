#view creation

from django.shortcuts import HttpResponse, render

#PASSING DATA TO THE TEMPLATE FILES
def mbu(request):
    return render(request, 'mbu.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def history(request):
    return render(request, 'history.html')

def mechanical(request):
    return render(request, 'mechanical.html')


def electrical(request):
    return render(request, 'electrical.html')


def civil(request):
    return render(request, 'civil.html')


def ejecsmodel(request):
    return render(request, 'ejecsmodel.html')

def sidebar(request):
    return render(request, 'sidebar.html')


def slider(request):
    return render(request, 'slider.html')

def barnav(request):
    return render(request, 'barnav.html')


def carousel(request):
    return render(request, 'carousel.html')

def learn(request):
    return render(request, 'learn.html')

def footer(request):
    return render(request, 'footer.html')


def lemu(request):
    return render(request, 'lemu.html')

def barside(request):
    return render(request, 'barside.html')


def learnsidebar(request):
    return render(request, 'learnsidebar.html')

def anyisidebar(request):
    return render(request, 'anyisidebar.html')















