from django.shortcuts import render


def track(request):
 return render(request, 'track/track.html')