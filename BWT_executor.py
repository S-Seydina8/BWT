
def marcaturaDellaStringa(x):
    print("la stringa selezionata e': ", x)
    
def ordinamentoLettere(x):
    lettere = list(x)
    n = len(lettere)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lettere[j].lower() < lettere[min_idx].lower():
                min_idx = j

        # ordinare parole in totale
        lettere[i], lettere[min_idx] = lettere[min_idx], lettere[i]
    
    # fusione delle parole    
    return "".join(lettere)


inserimento_parola = input("inserisci la parola in qui vorresti avviare la BWT: ")
marcaturaDellaStringa(inserimento_parola)
print(ordinamentoLettere(inserimento_parola))