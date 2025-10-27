from django.shortcuts import render


def index(request):
    return render(
        request,
        "index.html",
        context={
            "who": "hexlet-djanjo-blog",
        },
    )


def about(reuqest):
    return render(
        reuqest,
        'about.html',
    )