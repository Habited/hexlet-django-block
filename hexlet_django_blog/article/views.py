from django.shortcuts import render


def index(request):
    return render(
        request,
        "article/index.html",
        context={'name': "hexlet-djanjo-blog"}
    )




# Create your views here.
