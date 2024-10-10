from django import forms 




class IriCalcForm(forms.Form):
    current_level = forms.IntegerField()
    current_iridescent_shards = forms.IntegerField()
    iridescent_shards_needed = forms.IntegerField()
    current_xp = forms.IntegerField()
    xpon = forms.BooleanField(required=False)

