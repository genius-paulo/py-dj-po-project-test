from django.shortcuts import render
from django.http import HttpResponse


def calculate(request):
    expression = request.GET.get("expression")
    try:
        result = eval(expression)
    except Exception as e:
        return HttpResponse(e, status=400)
    return HttpResponse(result)
