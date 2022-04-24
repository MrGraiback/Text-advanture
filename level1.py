import time
def main(chars):
    wait = lambda : time.sleep(1.0)
    print ("Das ist ein Abenteur im Jahre 1520. Sie wachen in einem Haus in Dorf auf.")
    time.sleep(1.5)
    print ("Ein Man naehert sich und fragt dich ")
    time.sleep(1.0)
    while True:
        chars ['name'] = input ("Wie heisst du? ").strip()
        if chars['name']:
            break
    print ("Mann: Hmmmm...also " + chars ['name'] + " wir haben dich beim Fluss bewustloss gefunden in hierher gebracht")
    time.sleep(2.0)
    print ("Mann: Du bist im Dorf Hum und mein name ist Ralph Holtzmann. Ich bin ein Holzfaeller hier.")
    time.sleep(1.5)
    print ("Ralph: Geht es dir gut?")
    time.sleep(1.0)
    while True:
        thx = input ("ja super(j)/es ging mir schon besser(e)/nein füle mich schlecht(n): ").strip().lower()
        if thx == "j":
            print ("Na das sind ja gute Neuigkeiten")
            file = open('chars.py', 'w')
            chars["hp"] += 99
        elif thx == "e":
            print ("Das heisst gehen kannst du ja")
            chars["hp"] += 49
        elif thx == "n":
            print ("Dan ruhe dich mal ein paar Tage aus")
        else:
            continue
        break
    
