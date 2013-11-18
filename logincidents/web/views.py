# Create your views here.
from django.shortcuts import HttpResponse,redirect
from django.shortcuts import render_to_response,get_object_or_404



def home(request):
    c={'user':request.user}
    return render_to_response('home.html',c)