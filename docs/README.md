# Prezentace

Sem budeme dávat odkazy na prezentace z workshopu.

- [Pandas](https://nbviewer.jupyter.org/github/sedlakovi/interactive-dashboards/blob/master/pandas.ipynb)
- [Vizualizace dat](https://docs.google.com/presentation/d/1FH0bQPWmnc0yKnKPWI4bgRP-DgRUY2IxC7_dzQhxYig/edit?usp=sharing)
- [Plotly](https://nbviewer.jupyter.org/github/sedlakovi/interactive-dashboards/blob/master/plotly.ipynb)
- [Dash](https://docs.google.com/presentation/d/1o8NWfC4TjvxJ3u8SIzr5BldppWFBQGM7yWvYEuBgdEY/edit?usp=sharing)
- [Dash - cvičení](https://github.com/sedlakovi/interactive-dashboards/blob/master/dash_cviceni.md)


# Cheat sheety

- [Plot.ly](https://github.com/sedlakovi/interactive-dashboards/blob/master/docs/plotly_cheat_sheet.pdf)
- [Seznámení s daty](https://github.com/sedlakovi/data-storytelling/blob/master/postup_data.md)
- [Gramatika vizualizace](https://github.com/sedlakovi/data-storytelling/blob/master/grammar_of_graphics.md)
- [Originál Pandas](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)
- [Soubor cheat sheetů od DataCamp](http://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf)
- [Prezentace v Jupyteru](https://github.com/sedlakovi/data-storytelling/blob/master/prezentace_jupyter_notebook.md)
- [Markdown](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html)


# Datové zdroje

- [FiveThrtyEight](https://data.fivethirtyeight.com/)
- [Seznam vzorových sad dat z R](http://vincentarelbundock.github.io/Rdatasets/datasets.html)
- [Data z Kaggle (pro stažení je nutné zdarma se zaregistrovat)](https://www.kaggle.com/datasets)


# Užitečné odkazy

- [Galerie webů vytvořených v Dashi](https://dash.plot.ly/gallery) (včetně zdrojových kódů)
- [Dash Recipes](https://github.com/plotly/dash-recipes) - kuchařka aplikací vytvořených při odpovídání na otázky na Dash fóru.
- [Grafy v Plotly](https://plot.ly/python/basic-charts/)

# Instalace

Pro tento kurz si potřebujete nainstalovat

- Python 3
- Pandas (pro zpracování dat)
- Jupyter Notebook (tam si budeme zkoušet grafy předtím, než je dáme do aplikace)
- Plot.ly (kreslí grafy)
- Dash (vytváří webový dashboard)

## Kroky

### 1.

Nainstalujte Python **3**. Můžete použít [návod z kurzu vizualizace](https://sedlakovi.github.io/data-storytelling/#instalace) nebo třeba
[materiály od PyLadies](https://naucse.python.cz/course/pyladies/beginners/install/).

**Důležité** - pokud máte v uživatelském jménu do Windows mezery nebo např. háčky, čárky, zvolte "Customize installation" a vyberte cestu, která nebude uvnitř "C:\Users\Vaše jméno". Jinak můžete mít problém v pozdějších krocích s instalací balíčků.

Pozn.: Na Linuxu budete potřebovat ještě zvlášť nainstalovat `pip`. V Ubuntu pomocí
`sudo apt install python3-pip`.

### 2.

V terminálu spusťte:

    pip3 install --upgrade pandas numpy jupyter plotly dash dash-html-components dash-core-components dash-table dash-daq

_Tip: Na Windows se do terminálu kopíruje pravým tlačítkem myši._

Instalace by měla skončit se slovy `Successfully installed`, po kterých následuje výpis hromady balíčků s verzemi.

![Instalace balíčků hotova](packages-finish.jpg)

Pokud instalace končí jinak, pravděpodobně v systému něco chybí a je potřeba to
doinstalovat.

### 3.

Nyní zkontrolujte instalaci.

## Kontrola instalace

### 1.

Stáhněte si [testovací skript](dash-kontrola.py) (klikněte pravým tlačítkem a "uložit
odkaz jako...").

### 2.

Na Windows můžete zkusit skript spustit dvojklikem. Měl by zůstat otevřený terminál.

Jestli nefunguje spuštění dvojklikem, spusťte skript z příkazové řádky. Například jestli se skript
stáhnul do `Downloads`, spustíte:

```
# Windows
py -3 Downloads\dash-kontrola.py

# MacOs, Linux
python3 Downloads/dash-kontrola.py
```

Měli byste vidět zhruba toto:

```
 * Serving Flask app "dash-kontrola" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)
 ```

### 3.

Podívejte se na odkaz, který je vypsaný v terminálu, tj.
[http://127.0.0.1:8050/](http://127.0.0.1:8050/)
Pokud vidíte smysluplné slovo, instalaci jste provedli úspěšně, gratulujeme!
