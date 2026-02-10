# Analiza i Prognoza Rynku Gier Wideo (1980-2016)

Projekt analityczny mający na celu zbadanie trendów sprzedaży gier wideo oraz budowę modelu ekonometrycznego estymującego wartość rynku. Analiza opiera się na danych historycznych obejmujących sprzedaż globalną i regionalną.

##  Zakres analizy

* **Statystyka opisowa:** Analiza rozkładu sprzedaży, dominanty, średnie.
* **Wizualizacja danych:** Wykresy trendów sprzedaży w czasie, podział na platformy i gatunki.
* **Modelowanie:** Próba estymacji wartości rynku (zgodnie z metodologią opisaną w projekcie, $R^2 \approx 0.99$).
* **Wnioskowanie:** Analiza cykli życia konsol i popularności gatunków.

##  Technologie i Biblioteki

* **Python 3**
* **Jupyter Notebook** (`.ipynb`) - środowisko interaktywnej analizy.
* **Pandas & NumPy** - przetwarzanie i manipulacja danymi.
* **Matplotlib & Seaborn** - wizualizacja danych.
* **Statsmodels/Scipy** - testy statystyczne i modelowanie (w kontekście analizy korelacji i regresji).

## Pliki w repozytorium

* `Projekt_Sprzedaz_Gier.ipynb` - Główny notatnik z kodem, wykresami i opisem wniosków.
* `Projekt.py` - Skrypt Python zawierający logikę analizy.
* `Video_Games_Sales_as_at_22_Dec_2016.csv` - Surowy zbiór danych wykorzystany w analizie.
* `Projekt_Sprzedaz_Gier.html` - Wyeksportowany raport w formacie HTML.

##  Jak otworzyć analizę

Aby wyświetlić interaktywną wersję analizy:
1.  Zainstaluj Jupyter Notebook:
    ```bash
    pip install notebook pandas seaborn matplotlib
    ```
2.  Uruchom w konsoli:
    ```bash
    jupyter notebook
    ```
3.  Otwórz plik `Projekt_Sprzedaz_Gier.ipynb`.
