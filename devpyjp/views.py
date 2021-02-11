from django.shortcuts import get_object_or_404, render

import ipdb;


def about(request):
    # ipdb.set_trace()
    return render(request, '/about.html')


def home(request):
    return render(request, '/home.html')
