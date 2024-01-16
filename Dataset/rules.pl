pcPesante(ID,Peso) :-
    prop(ID, 'Peso', Peso),
    Peso >= 3.0.

pcLeggero(ID,Peso) :-
    prop(ID, 'Peso', Peso),
    Peso =< 1.0.

pcEconomico(ID,Prezzo) :-
    prop(ID, 'Prezzo (euro)', Prezzo),
    Prezzo =< 300.

pcPrezzoMedio(ID,Prezzo) :-
    prop(ID, 'Prezzo (euro)', Prezzo),
    (Prezzo =< 300, Prezzo >= 1500).

pcCostoso(ID,prezzo) :-
    prop(ID, 'Prezzo (euro)', Prezzo),
    Prezzo >= 2000.

ris_4k(ID) :-
    prop(ID, 'larghezza Risoluzione', 3840),
    prop(ID, 'altezza Risoluzione', 2160).

tot_pc(Tot) :-
    findall(ID, prop(ID, 'larghezza Risoluzione' , _), PCList),
    length(PCList, Tot).

count_qk(Num) :-
    findall(ID, ris_4k(ID), QKList),
    length(QKList, Num).

perc_4k(Perc) :-
    tot_pc(Tot),
    findall(ID, ris_4k(ID), QKList),
    length(QKList, QKCount),
    Perc is (QKCount / Tot) * 100.

max_Price(Prezzo) :-
    findall(Val, prop(_,'Prezzo (euro)',Val), Prlist),
    max_list(Prlist, Prezzo).

min_Price(Prezzo) :-
    findall(Val, prop(_,'Prezzo (euro)',Val), Prlist),
    min_list(Prlist, Prezzo).

pc_apple_schermo_piu_piccolo(ID, MinDimensioni) :-
    prop(ID, 'Marca', 'Apple'),
    findall(Dimensioni, prop(ID, 'Dimensioni schermo', Dimensioni), ListaDimensioni),
    min_list(ListaDimensioni, MinDimensioni),
    prop(ID, 'Dimensioni schermo', MinDimensioni),
    \+ (prop(AltroID, 'Marca', 'Apple'), AltroID \= ID, prop(AltroID, 'Dimensioni schermo', AltroDimensioni), AltroDimensioni < MinDimensioni).


perc_ultrabook(Perc) :-
    tot_pc(Tot),
    findall(_, prop(_, 'tipo', 'Ultrabook'),UltList),
    length(UltList, Num),
    Perc is (Num / Tot) * 100.

count_lenovo(Num) :-
    findall(_, prop(_,'Marca','Lenovo'), LenList),
    length(LenList, Num).

pcApple_MacOSX(ID) :-
    prop(ID, 'Marca', 'Apple'),
    prop(ID, 'Sistema Operativo', 4).