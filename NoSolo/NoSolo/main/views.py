from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {

    }

    return render(request, 'index.html', context)


def login_view(request):
    return render(request, 'accounts/login.html', {})