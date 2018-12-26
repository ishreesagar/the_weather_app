from django import forms

class city_name(forms.Form):
    name = forms.CharField(max_length = 100)