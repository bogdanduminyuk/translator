from django.shortcuts import render
from translator_app.forms import InputForm


def index(request):
    form = InputForm()
    return render(request, 'translator_app/index.html', {'form': form})
