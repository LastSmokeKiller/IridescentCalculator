from django.shortcuts import render
from django.views import View
from .forms import IriCalcForm
from .models.model_iridescentcalc import IridescentCalc

class Index(View):
    def get(self, request):
        form = IriCalcForm()
        return render(request, 'IriCalc/index.html', {'form': form})

    def post(self, request):
        form  = IriCalcForm(request.POST)

        if form.is_valid():

            # Setting up calculator variables being used
            current_level = int(form.cleaned_data['current_level'])
            current_iridescent = int(form.cleaned_data['current_iridescent_shards'])
            current_xp = int(form.cleaned_data['current_xp'])
            iridescent_needed = int(form.cleaned_data['iridescent_shards_needed'])
            xpon = bool(form.cleaned_data['xpon'])
            xp_needed = 0
            level_needed = 0
            iridescent_left = 0

            # Creating calculator object and Calculating level, xp needed, and iridescent shards left over
            iricalc = IridescentCalc(current_level, current_iridescent, current_xp, iridescent_needed, xpon)
            level_needed = iricalc.CalculateLvl()
            xp_needed = iricalc.getXP()
            iridescent_left = iricalc.getIriLeft()

            # context for values being returned
            context = {
                'levels_needed': level_needed,
                'xp_needed': xp_needed,
                'iridescent_left': iridescent_left,
            }

        # render the template
        return render(request, 'IriCalc/results.html', context)
