import time
def main(chars):
    wait = lambda : time.sleep(1.0)
    print ("Das ist ein Abenteur im Jahre 1520. Sie wachen in einem Zelt nahe dem in Dorf auf.")
    time.sleep(1.5)
    print ("Ein Man naehert sich und fragt dich: ")
    time.sleep(1.0)
    while True:
        chars ['name'] = input ("Wie heisst du? ").strip()
        if chars['name']:
            break

    print ("Mann: Hmmmm...also " + chars ['name'] + ", wir haben dich beim Fluss bewustloss gefunden in hierher gebracht.")
    time.sleep(2.0)
    print ("Mann: Du bist in der naehe der Stadt Hum und mein name ist Ralph Holtzmann. Ich bin der Arzt hier.")
    time.sleep(1.5)
    print ("Ralph: Geht es dir gut?")
    time.sleep(1.0)

    while True:
        thx = input ("ja super(j)/es ging mir schon besser(e)/nein füle mich schlecht(n): ").strip().lower()
        time.sleep (2.5)
        if thx == "j":
            print ("Na das sind ja gute Neuigkeiten.")
            chars["hp"] += 99
            time.sleep(1.5)
        elif thx == "e":
            print ("Das heisst gehen kannst du ja.")
            chars["hp"] += 49
            time.sleep(1.5)
        elif thx == "n":
            print ('Ralph: Klingt schlecht, ')
            chars['hp'] += 19
            time.sleep(1.5)
        else:
            continue
        break

    print ('Ralph: Na ruhe dich noch ein bisschen aus.')
    time.sleep (1.0)
    print ('Es vergehen ein 3 Tage')
    time.sleep (3.0)
    print ('Am 3 Tag langweiligen Sie sich im Zelt.')
    time.sleep (1.0)
    print ('Ralph kommt mit einem anderen Mann in Ruestung rein.')
    time.sleep (1.5)
    print ('Ralph: Das hir ist unser Kommandant, Dorian Nolan')
    time.sleep (1.0)
    print ('Dorian: Also ' + chars ['name'] + ', wie gesagt wir haben dich bei dem Fluss gefunden.')
    time.sleep (2.0)
    print ('Dorian: Dich haben meine Spaeher entdeckt.')
    time.sleep (1.0)
    print ('Dorian: Da wir im Krieg sind muss ich feststellen das du kein Spion bist.')
    time.sleep (1.5)
