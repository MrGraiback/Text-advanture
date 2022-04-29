import time

def main(chars):
    print ('Dorian: Na fangen wir an....Also wer bist du? Wenn du dich an das erinern kannst')
    time.sleep (2.0)
    while True:
        test = input ('Ich bin ein Schwertkaempfer(s), Ich bin Bogenschuetze(b), Ich bin ein Haendler(h): ').strip().lower()
        time.sleep (2.5)
        if test == 'h'
            print ('Wo hast du das gelaernt?')
            time.sleep (1.0)
            chars['skill'].append('Haendler')
            chars['int'] +=2
            chars['charisma'] +=3
        elif test == 'b'
            print ('Wo hast du das gelaernt?')
            time.sleep (1.0)
            chars['skill'].append('Bogenschuetze')
            chars['int'] +=3
            chars['power'] +=2
        elif test == 's'
            print ('Wo hast du das gelaernt?')
            time.sleep (1.0)
            chars['skill'].append('Schertkaempfer')
            chars['power'] +=5
        else
            continue
        break

    while True:
        test = input ('Kann ich mich nicht mehr erinern(e), ')
