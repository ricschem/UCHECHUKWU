from django.shortcuts import render, HttpResponse

def Appview(request):
    return HttpResponse('This is Jolpec App')


from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import JolpecForm

# Create your views here.


def jolpec_logo(request):

    if request.method == 'POST':
        form = JolpecForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = JolpecForm()
    return render(request, 'images.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')

