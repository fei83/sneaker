from django.shortcuts import render


def bake(request):
    return render(request, 'bake/bake.html')
