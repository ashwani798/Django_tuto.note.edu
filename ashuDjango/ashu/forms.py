from django import forms
from .models import ashuvarity


class ashuvarityform(forms.Form):
    ashu_varity = forms.ModelChoiceField(queryset=ashuvarity.objects.all(), label="select ashuvariety")