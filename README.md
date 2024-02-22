1. Info about sort type 'bubble sort' - algorythm:
 > https://www.home.umk.pl/~abak/wdimat/s/BubbleSort.html

Algorytm sortowania bąbelkowego polega na porównywaniu par elementów leżących obok siebie i, jeśli jest to potrzebne, zmienianiu ich kolejności. Czyli w pierwszym przebiegu porównujemy (i ewentualnie zamieniamy):

- Element pierwszy i drugi
- Element drugi i trzeci
- ...
- Element (n-1)-wszy i n-ty
- 
Każdy element jest tak długo przesuwany w ciągu, aż napotkany zostanie element większy od niego, wtedy w następnych krokach przesuwany jest ten większy element.

Po pierwszym przebiegu ciąg nie musi być jeszcze uporządkowany, ale na pozycji n znajdzie się maksymalny element ciągu. Zatem w drugim przebiegu można porządkować ciąg krótszy, czyli tylko elementy na pozycjach od 1 do n-1. Po drugim przebiegu, dwa ostatnie elementy są na swoich miejscach, czyli pozostaje posortować ciąg o dwa elementy krótszy, itd.

Można jeszcze bardziej usprawnić ten algorytm. Jeżeli w pewnym przebiegu algorytmu ostatnia zamiana nastąpiła na pozycji i, to w następnym przebiegu wystarczy porządkować tylko elementy na pozycjach od 1 do i-1. W takiej wersji ten algrytm jest zrealizowany w demonstracji.

Jeżeli dane wejściowe są uporządkowane, to algorytm wykonuje tylko jeden przebieg (nie jest wykonywana żadna zamiana). 

 It has a time complexity of O(n2) in the worst-case time.

2. install all requirements
 > py -m pip install -r requirements.txt

3. run pytest
 > py -m pytest .\test.py -s -vv

