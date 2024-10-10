from django.shortcuts import render
from django.views import View
from .forms import IriCalcForm

class Index(View):
    def get(self, request):
        form = IriCalcForm()
        return render(request, 'IriCalc/index.html', {'form': form})

    def post(self, request):
        pass