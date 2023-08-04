from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the companies index.")

def company(request, company):
    response = "You are looking at the results for company %s."
    return HttpResponse(response % company)