from django.shortcuts import render

# Create your views here.

def contact(request):

    return render(request, 'contact.html')


def about_us(request):

    return render(request, 'about_us.html')


def privace_policy(request):

    return render(request, 'privacy_policy.html')


def order_history(request):

    return render(request, 'order_history.html')