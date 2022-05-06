import time
def main(chars):
    wait = lambda : time.sleep(1.0)
    print ('Das ist ein Abenteur im Jahre 1520....')
    time.sleep(2.0)
    print ("Sie wachen in einem Zelt auf. ")
    time.sleep(2.0)
    print ("Ein Man naehert sich und fragt dich: ")
    time.sleep(2.0)
    while True:
        chars ['name'] = input ("A do bist endlich wach. Wie heisst du den? ").strip()
        if chars['name']:
            break

    print ("Mann: Hmmmm...also " + chars ['name'] + ", wir haben dich beim Fluss bewustloss gefunden in hierher gebracht.")
    time.sleep(3.0)
    print ("Mann: Du bist in der naehe der Stadt Hum und mein name ist Ralph Holtzmann. Ich bin der Arzt hier.")
    time.sleep(3.5)
    print ("Ralph: Geht es dir gut?")
    time.sleep(2.0)

    while True:
        thx = input ("Ja super(j)\nEs ging mir schon besser(e)\nNein füle mich schlecht(n): ").strip().lower()
        if thx == "j":
            print ("Na das sind ja gute Neuigkeiten.")
            chars["hp"] += 99
            time.sleep(2.0)
        elif thx == "e":
            print ("Das heisst gehen kannst du ja.")
            chars["hp"] += 49
            time.sleep(2.0)
        elif thx == "n":
            print ('Ralph: Klingt schlecht. ')
            chars['hp'] += 19
            time.sleep(2.0)
        else:
            continue
        break

    print ('Ralph: Na ruhe dich noch ein bisschen aus.')
    time.sleep (2.5)
    print ('Es vergehen ein 3 Tage')
    time.sleep (3.0)
    print ('In der Zwischenzeit hast du erfahren das du dich im Lande Westfallen befindest.')
    time.sleep (3.5)
    print ('Auch erfaerst du das dieses Land im Krieg mit einem anderen ist.')
    time.sleep (3.0)
    print ('Du hast gehoert wie die Soldaten sich ueber den Kreig unterhalten.\nUnd das kommische ist das sie die Feinde \'die Schwarzen\' nennen....')
    time.sleep (5.0)
    print ('Aber dann erfaerst du auch warum die Soldaten den Feind so nennen.\nSie nennen ihn so weil sie schwarze Ruestungen tragen...Lustig')
    time.sleep (4.0)
    print ('Am 3 Tag langweiligst du dich im Zelt.')
    time.sleep (3.0)
    print ('Ralph kommt mit einem anderen Mann in Ruestung rein.')
    time.sleep (2.5)
    print ('Ralph: Das hir ist unser Kommandant, Dorian Nolan')
    time.sleep (2.5)
    print ('Dorian: Also ' + chars ['name'] + ', wie gesagt wir haben dich bei dem Fluss gefunden.')
    time.sleep (3.5)
    print ('Dorian: Dich haben meine Spaeher entdeckt.')
    time.sleep (2.5)
    print ('Dorian: Da wir im Krieg sind muss ich feststellen das du kein Spion bist.')
    time.sleep (3.0)
