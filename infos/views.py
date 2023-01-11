from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def homepage(request):
    return render(request, "infos/homepage.html", {'navbar':'homepage'} )

def me(request):
    return render(request, "infos/me.html", {'navbar':'me'} )

def contact(request):
    return render(request, "infos/contact.html", {'navbar':'contact'} )
