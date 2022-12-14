# ScamShield

# Wydarzenie[^event]

<img src="https://itwiz.pl/wp-content/uploads/2022/10/16x9.jpg" height = 100% width = 100%>

### **Nazwa:**      *#Supervision_hack*
### **Termin:**     *21 / 23 października 2022 r.*
### **Miejsce:**    *PGE Narodowy, Warszawa*

___

## Opis

Projekt stworzony został w ramach uczestnictwa w wydarzeniu **#Supervision_hack**. Był to pierwszy organizowany przez UKNF maraton programowania, mający na celu stworzenie innowacyjnych rozwiązań dla rynku finansowego oraz podniesienie poziomu cyberbezpieczeństwa. [Więcej informacji...](https://supervisionhack.pl/)

## Wyzwanie

Hackathon składał się z dwóch wyzwań: **#KarateKIID** oraz **Catch'em all**.
Nasz projekt konkurował w ramach drugiego z wyżej wymienionych wyzwań. Szczegóły powierzonego zadania do wykonania można sprawdzić [tutaj](https://github.com/ITA-Flowers/ScamShield/blob/master/Challenge_Catch'em-all.pdf).

___

# Projekt[^project]

<img src="https://raw.githubusercontent.com/ITA-Flowers/ScamShield/master/browser_extension/images/banner_b_f.png">


## [Prezentacja]("https://raw.githubusercontent.com/ITA-Flowers/ScamShield/master/Prezentacja_ScamShield.pptx")

## [Dokumentacja]("https://raw.githubusercontent.com/ITA-Flowers/ScamShield/master/Dokumentacja-API-ScamShield.docx")

___

# API[^api]

### Główne zadanie do wykonania podczas konkursu zaimplementowane zostało przez nas w ramach języka **Python**, z wykorzystaniem framework'u **Flask**.

___

## **Endpoint** 
```
/api/url
```

## **Request Body**
``` json
{
    "url" : "https://www.example.com/"
}

```

## **Response OK**
``` json
{
    "domain" : "https://www.example.com/",
    "phishing_estimate" : "7"
}

```

## **Response Bad Request**
``` json
{
    "error" : "0"
}

```

___

# Algorytmy skanowania[^alghoritms]

## Protokół
W przypadku używania http istnieje zwiększone ryzyko, zatem zwiększamy punktacje phishingową.

## Wiek strony

Sprawdzamy wiek strony, w celu wyłapania młodych stron. Istnieje duże ryzyko, że są stronami phishingowymi.

## SSL

SSL strony jest pobierany i porównywany z rankingiem SSL z których pochodzi najwięcej stron phishingowych.

SSL jest również sprawdzane z blacklist’ą przydzielonych certyfikatów.

## JavaScript

Żadna uczciwa strona nie szyfruje swoich URL. Zatem w poszukiwaniu stron oszustów wyszukujemy w kodzie javascript stron podejrzanych, użyć przestarzałych metod szyfrowania np. unescaped().

## Porównanie HTML

Pobieramy ze strony jej tytuł, algorytm przy jego pomocy wyszukuje stronę html którą uznaje za oryginalną. Następnie szyfrujemy zawartości stron i porównujemy oba wyniki. W sytuacji w której nie ma tytułu, od razu strona trafia do zwiększonego ryzyka, ponieważ przeglądarki wykorzystują tytuły do pozycjonowania stron.

## Serwisy sklepowe

Portale aukcyjne są sprawdzane pod kątem numerów ogłoszeń dzięki czemu możemy się dowiedzieć czy akcje są fałszywe.

___

# Instalacja API[^install]
pip upgrade

    python -m pip install --upgrade pip

download github repo

    git clone https://github.com/ITA-Flowers/ScamShield.git

Change dir to api workdir

    cd ./ScamShield/api 

install virtual enviroment python module

    python -m pip install virtualenv

create virtual enviroment for API

    python -m venv ./.venv

activate venv

    ./.venv/Scripts/activate

install required modules
    
    python -m pip install -r ./requirements

run API
    
    flask run

default server host and port:

**HOST**: *0.0.0.0*

**PORT**: *8080*

**OPTIONAL** you could set server host address and port ``` by:
    
    flask run --host '0.0.0.0' --port 8080

**ALTERNATIVE** run API

    python ./app.py

___

# Testowanie[^tests]

### [Zestaw testowy](https://github.com/ITA-Flowers/ScamShield/blob/master/api/test_domains.txt)

### [Skrypt](https://github.com/ITA-Flowers/ScamShield/blob/master/api/script.py)

### [Wyniki](https://github.com/ITA-Flowers/ScamShield/blob/master/api/results.txt)

### [Błędy](https://github.com/ITA-Flowers/ScamShield/blob/master/api/errors.txt)

___

## Przeglądarka mobilna

Ponad to, co określone zostało w treści zadania konkursowego zrealizowaliśmy prototyp przeglądarki internetowej w wersji mobilnej jako model aplikacji mobilnej dla systemów operacyjnych **Android**, wykorzystując język **Java**. W pełni zintegrowana z naszym API, ustawiona przez potencjalnego użytkownika jako przeglądarka domyślna chroni nie tylko podczas swobodnego przeglądania stron internetowych, ale również otwierając linki z SMS'ów czy wiadomości e-mail.

___

## Rozszerzenie do przeglądarki

Rozszerzenie zaimplementowane, w ramach języka **JavaScript**, zintegrowane z naszym API ma identyczne zadanie jak wyżej wspomniana przeglądarka na urządzenia mobilne, z tym, że wykonywać je będzie podczas korzystania z przegladarki internetowej za pomocą komputera osobistego.

___

# Rezultat konkursu[^result]

## Jury wybrało 5 najlepszych spośród 15 zespołów do starcia finałowego. Wśród nich znaleźli się również **TheFlowers**, jednak w rezultacie starcie nie dane im było stanąć na podium.


## Projekt jednak nadal pozostaje w **TOP 5** najlepszych zaprezentowanych rozwiązań tego zadania.

<img src="https://raw.githubusercontent.com/ITA-Flowers/ScamShield/master/challenge_final.png">

___

> [^event]: Wydarzenie
> [^project]: Projekt
> [^api]: API
> [^alghoritms]: Algorytmy
> [^install]: Instalacja
> [^tests]: Testowanie
> [^result]: Rezultat