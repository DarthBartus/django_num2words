from django import forms


class TranslateForm(forms.Form):
    toTranslate = forms.CharField(label = 'Numer do przetłumaczenia', max_length=12)