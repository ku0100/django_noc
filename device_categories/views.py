from django.shortcuts import render
from django.http import HttpResponse
from .models import Type, Device
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("This is the Device Categories Page")

def deviceList(request, device_type):
    all_devices = Device.objects.filter(category__device_category__iexact=device_type)
    template = loader.get_template('device_categories/index.html')
    context = {
        'all_devices': all_devices,
    }
    return render(request, 'device_categories/index.html', context)

    # return HttpResponse("You are looking at devices that are %s." % device_type)