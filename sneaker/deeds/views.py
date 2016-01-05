from django.shortcuts import render


def deeds(request):
 return render(request, 'deeds/deeds.html')