from multiprocessing import context
from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def inicio(request):
    form=RegisterForm()
    context = {
        "el_form":form
    }
    return render(request, "inicio.html", context)
