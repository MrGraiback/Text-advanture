import time

def main(chars):
    print ('Dorian: Na fangen wir an....Also wer bist du? Wenn du dich an das erinern kannst')
    time.sleep (3.0)
    while True:
        test = input ('Ich bin ein Schwertkaempfer(s),\nIch bin Bogenschuetze(b),\nIch bin ein Haendler(h): ').strip().lower()
        if test == 's':
            print ('Ein bisschen Training un du kannst mit uns gegen die Schwarzen ziehen')
            time.sleep (3.0)
            #chars['skill'].append('Haendler')
            chars['int'] +=2
            chars['charisma'] +=3
        elif test == 'b':
            print ('Ein bisschen Training un du kannst mit uns gegen die Schwarzen ziehen')
            time.sleep (3.0)
            #chars['skill'].append('Bogenschuetze')
            chars['int'] +=3
            chars['power'] +=2
        elif test == 'h':
            print ('Heandler kann man immer brauchen')
            time.sleep (3.0)
            #chars['skill'].append('Schertkaempfer')
            chars['power'] +=5
        else:
            continue
        break

    print ('Dorian: Na dan naechste Frage, woher kommst du den? Ich hoffe nicht aus Nordfallen...')
    time.sleep (3.5)
    while True:
        test = input ('Kann ich mich nicht mehr erinern(e),\nIch glaube aus Westfallen, aus dem Dorf Nirleb(n),\nKann sein das ich aus Nordfallen komm, ich glaube das dorf hiess Niew(w). ').strip().lower()
        if test =='e':
            print ('Dorian: Ich hoffe es feallt dir noch ein. Aber passt schon')
            time.sleep (3.0)
            chars['int'] +=2
            chars['charisma'] +=1
        elif test == 'n':
            time.sleep[3.0]
            print ('Dorian: Klingt seltsam...aber ich glaube ich kenne so ein Dorf. Ich werde dich beobachten lassen')
            chars['charisma'] +=1
        elif test == 'w':
            ('Na ja, dafuer warst du ja ehrlich. In dieser Armee haben wir eh ein paar ays Nordfallen. \nAber wenn etwas seltsames passiert wirst du Probleme bekommen')
            chars['charisma'] +=2
            time.sleep (3.0)
        else:
            continue
        break
