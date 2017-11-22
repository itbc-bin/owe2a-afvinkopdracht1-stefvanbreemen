# Naam:stef van Breemen
# Datum:25okt2017
# Versie:

def main():
    try:
        mybool = False
        while not mybool:
            try:
                headers, seqs = lees_inhoud()
                if not headers:
                    raise StopIteration
                counter = 0
                zoekwoord = input("Geef een zoekwoord op: ")
                for line in headers:
                    if zoekwoord in line:
                        print(line)
                        print(seqs[counter])
                        print("dit is DNA:", is_dna(seqs[counter]))
                        mybool = knippen(seqs[counter])
                    counter += 1
                else:
                    raise IOError
            except TypeError:
                print("Deze sequentie is geen DNA, voer een DNA sequentie in.")
            except ValueError:
                print("De geteste restrictie enzymen knippen niet in deze sequentie")
            except StopIteration:
                print("Het bestand dat u heeft ingevoerd is leeg")
            except FileNotFoundError:
                print("Het bestand dat u zoekt is niet in de bestands map gevonden")
            except IOError:
                print("Het zoekwoord is niet gevonden in de lijst headers")
    except KeyboardInterrupt:
        print("\nhet programma is afgesloten door gebruiker")
def lees_inhoud():
    try:
        bestand = open(input("welk bestand wil je openen?:"))
        headers = []
        seqs = []
        dna = ""
        bestand = bestand.readlines()
        for line in bestand:
            if ">" in line:
                line = line.replace("\n", "")
                headers.append(line)
                dna += (" ")
            else:
                line = line.replace("\n", "")
                dna += (line)
        seqs = dna.split(" ")
        del(seqs[0])
        return (headers, seqs)
    except FileNotFoundError:
        raise FileNotFoundError

def is_dna(seqs):
    dna1 = False

    A = seqs.count("A")
    T = seqs.count("T")
    C = seqs.count("C")
    G = seqs.count("G")
    N = seqs.count("N")
    total = A+T+C+G+N
    if len(seqs) == total:
        dna1 = True
    else:
        raise TypeError
    return(dna1)
def knippen(knip):
    bestand = open("enzymen.txt")
    bestand = bestand.readlines()
    enzymen = []

    knipt = []
    kniptniet = []

    for line in bestand:
        line = line.replace("^", "").split()
        enzymen.append(line)

    for item in enzymen:

        if item[1] in knip:
            knipt.append(item[0])
        else:
            kniptniet.append(item[0])
    if kniptniet == ['DdeI', 'BspMII', 'EcoRI', 'HindIII', 'BalI', 'SmaI', 'SwaI', 'AciI', 'SspI', 'XhoI', 'AvrII', 'ApaLI', 'TaqI', 'EcoRV', 'FictIe', 'FictII']:
        raise ValueError
    else:
        print("enzymen die niet knipppen", kniptniet)
    for enzym in enzymen:
        if enzym[1] in knip:
            print("matcht met:",enzym[0]," op positie",knip.index(enzym[1]))
    return(True)


main()
