from django.shortcuts import render, HttpResponse

ROOT_TEMPLATE_PATH = 'core/pages/'


def home(request):
    html_response = render(request, ROOT_TEMPLATE_PATH + 'home.html')
    return HttpResponse(html_response)


def about_me(request):
    html_response = render(request, ROOT_TEMPLATE_PATH + 'about_me.html')
    return HttpResponse(html_response)


def portfolio(request):
    html_response = render(request, ROOT_TEMPLATE_PATH + 'portfolio.html')
    return HttpResponse(html_response)


def contact(request):
    html_response = render(request, ROOT_TEMPLATE_PATH + 'contact.html')
    return HttpResponse(html_response)
