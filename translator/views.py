from django.shortcuts import render
from .form import TranslateForm
from .translate import translate

def translator(request):
    if request.method == 'POST':
        form = TranslateForm(request.POST)

        if form.is_valid():
            translated = ''
            try:
                translated = translate(form.cleaned_data['toTranslate'])
            except ValueError:
                translated = 'Podaj prawidłową liczbę!'
            return render(request, 'translator.html', {'form': form, 'translated':translated})

    else:
        form = TranslateForm()

    return render(request, 'translator.html', {'translated': ""})
