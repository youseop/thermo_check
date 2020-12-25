from django.shortcuts import render


def oauthlogin(request):
    return render(request, 'oauthlogin.html')