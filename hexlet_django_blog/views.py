from django.shortcuts import render


def index(request):
    return render(
        request,
        "index.html",
        context={
            "Who": "World",
        },
    )


def about(reuqest):
    return render(
        reuqest,
        'about.html',
    )