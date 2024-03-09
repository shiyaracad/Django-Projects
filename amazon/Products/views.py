from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return HttpResponse("<h1>Hello world</h1>")

def getAll(req):
    return HttpResponse("<h1>All data ...</h1>")

def getById(req,id):
    return HttpResponse(f"<h1>ID is {id}</h1>")


def html(req):
    context = {"data":[1,2,3,4,5,6,7,8] }
    return render(req,"test.html",context)