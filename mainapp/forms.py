from django import forms

class WeatherForm(forms.Form):
    place = forms.CharField(label='Search by place', max_length=100)