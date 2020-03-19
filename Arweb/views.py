from django.shortcuts import render,redirect
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)

# Create your views here.
def home(request):
    return render(request,'index.html')

def on(request):
    GPIO.output(12,GPIO.HIGH)
    return render(request, 'index.html')

def off(request):
    GPIO.output(12,GPIO.LOW)
    return render(request, 'index.html')

def camera(request):
    return render(request, 'index.html')