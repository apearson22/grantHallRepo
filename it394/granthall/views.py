from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    emplate = loader.get_template('granthall/index.html') #Get the template we created
return HttpResponse(template.render(context, request)) #Render the template with the context

# Create your views here.
