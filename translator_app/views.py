from django.shortcuts import render
from django.http import HttpResponse

from translator_app.forms import InputForm


def index(request):
    if request.method == "POST":
        # request.POST.dict()

        form = InputForm(request.POST)
        if form.is_valid():
            print("valid")
        else:
            print("not valid")

        # return HttpResponse

    else:
        form = InputForm()

    return render(request, 'translator_app/index.html', {'form': form})


def loading(request):
    return render(request, 'translator_app/loading.html', {})
