from django.shortcuts import render


def index(request):  # test comment
    return render(request, "personal/home.html")


def contact(request):
    context = {
        "content": ["If you would like to contact me", "abc@o2.pl"],
        "header2": "The H2 header",
    }
    return render(
        request,
        "personal/basic.html",
        context,
    )
