def marcaturaDellaStringa(x):
    print("La stringa selezionata è:", x)


def ordinamentoParole(x):

    if not x.endswith("$"):
        x += "$"

    n = len(x)

    rotazioni = [x[i:] + x[:i] for i in range(n)]

    rotazioni_ordinate = sorted(rotazioni)

    bwt_risultato = "".join(r[-1] for r in rotazioni_ordinate)

    return bwt_risultato


def esegui_bwt(testo):

    marcaturaDellaStringa(testo)

    risultato = ordinamentoParole(testo)

    return risultato