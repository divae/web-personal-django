from django.shortcuts import render, HttpResponse


def home(request):
    html_response = render(request, 'core/home.html')
    return HttpResponse(html_response)


def about_me(request):
    html_response = render(request, 'core/about_me.html')
    return HttpResponse(html_response)


def portfolio(request):
    html_response = render(request, 'core/portfolio.html')
    return HttpResponse(html_response)


def contact(request):
    html_response = render(request, 'core/contact.html')
    return HttpResponse(html_response)
