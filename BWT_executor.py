def marcaturaDellaStringa(x):
    print("La stringa selezionata è:", x)


# ordinamento delle parole a logica del BWT tramite select sort
def ordinamentoParole(x):

    if not x.endswith("$"):
        x += "$"

    n = len(x)

    rotazioni = [x[i:] + x[:i] for i in range(n)]

    rotazioni_ordinate = sorted(rotazioni)

    bwt_risultato = "".join(r[-1] for r in rotazioni_ordinate)

    return bwt_risultato

# esecuzione della logica BWT dalle altre funzioni
def esegui_bwt(testo):

    marcaturaDellaStringa(testo)

    risultato = ordinamentoParole(testo)

    return risultato