from django.shortcuts import render


def index(request):
    print("dklsjfskdlfjsdklfjsdf") # sdkfjsdlfjsdlfkjdflkj
    print("dklsjfskdlfjsdklfjsdf")
    print("dklsjfskdlfjsdklfjsdf")
    print("third print")
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me', 'abc@o2.pl']})
