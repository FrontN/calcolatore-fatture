import time
import os

P_STAMPA = [0.30, 0.25, 0.20]
P_RIFERIMENTO = [0, 10, 30]

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def calcolo_fattura(numero_copie, prezzi_stampa, punti_riferimento):
    """
    Calcola il prezzo delle copie date in input.
    Il prezzo delle copie dipende dal numero di copie e dai prezzi di stampa delle copie
    che sono diversi in base al numero di copie. Il prezzo delle copie viene calcolato
    sommando il prezzo delle copie che rientrano in ogni punto di riferimento.
    :param numero_copie: numero di copie
    :param prezzi_stampa: prezzi di stampa per ogni punto di riferimento
    :param punti_riferimento: punti di riferimento per ogni prezzo di stampa
    :return: prezzo delle copie
    :rtype: str
    """
    if len(prezzi_stampa) != len(punti_riferimento):
        return "La lunghezza di prezzi_stampa deve essere uguale alla lunghezza di punti_riferimento."

    riferimento = sorted(punti_riferimento)

    fattura = 0
    for i, p in enumerate(riferimento[::-1]):
        if p != 0 and p < numero_copie:
            A = numero_copie - p
            fattura += A * prezzi_stampa[-(i +1)]
            numero_copie -= A
    fattura += numero_copie * prezzi_stampa[0]
    return f"{fattura:.2f}€"

def main():
    """
    Esegue un loop finch non viene inserito un numero di copie valido.
    Richiede all'utente di inserire il numero di copie e stampa il prezzo delle copie.
    Se viene inserito un numero di copie non valido, stampa un messaggio di errore e
    ripete la richiesta dopo 1.5 secondi.
    """
    while True:
        try:
            clear_screen()
            nb_copie = int(input("Inserisci il numero di copie: "))
            if nb_copie < 0:
                print("Il numero di copie deve essere un intero positivo.")
                time.sleep(1.5)
                clear_screen()
                continue
            print(calcolo_fattura(nb_copie, P_STAMPA, P_RIFERIMENTO))
            break
        except ValueError:
            print("Devi inserire un numero intero.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
