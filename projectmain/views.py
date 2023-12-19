from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request, 'main.html')


def map_view(request):
    return render(request, 'maps.html')

def santashohos_view(request):
    return render(request, 'santashohos.html')
