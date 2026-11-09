
def marcaturaDellaStringa(x):
    print("la stringa selezionata e': ", x)
    
def ordinamentoParole(x):

    stringa_finale = x + "$"
    n = len(stringa_finale)
    

    rotazioni = {stringa_finale[i:] + stringa_finale[:i] for i in range(n)}
    
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
    
            if rotazioni[j] < rotazioni[min_idx]:
                min_idx = j
        
    
        rotazioni[i], rotazioni[min_idx] = rotazioni[min_idx], rotazioni[i]
    
    
    bwt_risultato = "".join([r[-1] for r in rotazioni])
    
    return bwt_risultato


inserimento_parola = input("inserisci la parola in qui vorresti avviare la BWT: ")
marcaturaDellaStringa(inserimento_parola)
print(ordinamentoParole(inserimento_parola))