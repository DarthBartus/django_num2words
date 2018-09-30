# django_num2words

Aplikacja w Django, składająca się z formularza, w którym przekazywana jest liczba całkowita, która następnie przez skrypt `translate.py` tłumaczona jest do wyświetlanych słów w języku polskim. Skrypt ograniczony jest do wypisywania słów do maksymalnie 999999999999, ale może zostać przeskalowany do tłumaczenia liczb większych przez rozszerzenie słownika `orderDict` w skrypcie `translate.py` i zwiększenia maksymalnej wartości w formularzu `form.py`. W przypadku tej aplikacji tłumaczenie odbywa się po stronie serwera.
