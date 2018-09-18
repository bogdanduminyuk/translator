from django.shortcuts import render, redirect
from translator_app.forms import InputForm
from django.http import JsonResponse
from .stubs import generate_input_data


def index(request):
    form = InputForm()

    if request.method == "POST":
        form = InputForm(request.POST)

        data = generate_input_data()

        if form.is_valid():
            return render(request, 'translator_app/loading.html', {
                    "total": data["total"],
                    "current_word": data["words"][0],
                })

    return render(request, 'translator_app/index.html', {'form': form})


def loading(request):
    if request.method == "GET":
        data = generate_input_data()
        idx = int(request.GET['idx'])
        response = {}

        if idx < data['total']:
            word = data["words"][idx]

            response["idx"] = idx + 1
            response["word"] = word
            response["total"] = data["total"]
            return JsonResponse(response)
        else:
            response["url"] = "/result"
            response["complete"] = True
            return JsonResponse(response)

    else:
        return render(request, 'translator_app/loading.html', {})


def result(request):
    return render(request, 'translator_app/result.html', {})
