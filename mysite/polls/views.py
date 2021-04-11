from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    return HttpResponse("hello world i'm a poll index")


