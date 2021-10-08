from django.shortcuts import render


def index(request):
    print("dklsjfskdlfjsdklfjsdf")  # sdkfjsdlfjsdlfkjdflkj
    return render(request, "personal/home.html")


def contact(request):
    return render(
        request,
        "personal/basic.html",
        {"content": ["If you would like to contact me", "abc@o2.pl"]},
    )
