

from django.shortcuts import render, HttpResponse

# Create your views here.

def weather(request):
    return render(request, 'chatbot.html')