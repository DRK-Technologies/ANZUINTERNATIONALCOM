from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def our_story(request):
    return render(request, 'myapp/ourstory.html')

def global_presence(request):
    return render(request, 'myapp/globalpresence.html')

def out_team(request):
    return render(request, 'myapp/ourteam.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def services(request):
    return render(request, 'myapp/services.html')

def import_services(request):
    return render(request, 'myapp/importservices.html')

def export_services(request):
    return render(request, 'myapp/exportservices.html')

def logistics_shipping(request):
    return render(request, 'myapp/logistics_shipping.html')

def warehousing_distribution(request):
    return render(request, 'myapp/warehousing.html')

def cashew(request):
    return render(request, 'myapp/cashew.html')
def golisoda(request):
    return render(request, 'myapp/golisoda.html')
def exportpallets(request):
    return render(request, 'myapp/exportpallets.html')

