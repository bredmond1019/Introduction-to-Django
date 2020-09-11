from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            # do something code 
            print("VALIDATION SUCCESS!")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            print(name, email, text)
    return render(request, "basicapp/form_page.html", {'form': form})
