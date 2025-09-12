import random

def slump_tal():
    return random.randint(1, 10)

def gissa_tal(rätt_tal):
    gissningar = 0
    while True:
        try:
            gissning = int(input("Gissa ett tal mellan 1 och 10: "))
            gissningar += 1
            if gissning == rätt_tal:
                print(f"Rätt! Du gissade rätt på {gissningar} försök.")
                return gissningar
            elif gissning < rätt_tal:
                print("För lågt!")
            else:
                print("För högt!")
        except ValueError:
            print("Skriv ett heltal!")

def beräkna_poäng(gissningar):
    return max(0, 10 - gissningar + 1)

def spela():
    rätt_tal = slump_tal()
    gissningar = gissa_tal(rätt_tal)
    poäng = beräkna_poäng(gissningar)
    print(f"Du fick {poäng} poäng!")

def main():
    while True:
        spela()
        igen = input("Vill du spela igen? (ja/nej): ").strip().lower()
        if igen != "ja":
            print("Tack för att du spelade!")
            break

if __name__ == "__main__":
    main()
