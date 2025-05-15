

from django.shortcuts import render, HttpResponse

# Create your views here.

def bot(request):
    return render(request, 'chatbot.html')