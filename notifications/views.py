from django.http.response import HttpResponse
from django.shortcuts import render

from . tasks import update_table


def update_status(request):
    update_table()
    return HttpResponse()
    
