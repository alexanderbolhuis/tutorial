from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage, AccessRecord, Topic
from first_app import forms


# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)


def first_app(request):
    return HttpResponse("<h1>Welcome</h1>")


def form_page(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form': form})
