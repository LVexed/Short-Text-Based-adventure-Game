import time
import random
import sys


Starten = ""
möglichePlayerLocations = ["Zellen", "Hof", "Bibliothek", "Barracken", "Sanctum"]
playerlocation = "Zellen"
visitedNameless = False
visitedBarracken = False
BibliothekWeg = False
zelle2TürRätsel = "krieg"
Gesundheit = 100
SpielBeendet = False

Archive = {
  "bibliothek": {
    "Baylons Archiv": {
      "beschreibung": "Eine akademische Sammlung fundierter Zaubersprüche, Formeln und arkaner Vorlesungen.",
      "buecher": [
        {"titel": "Grundlagen der Evokation", "inhalt": "Ein einführendes Lehrbuch über das sichere Leiten von magischer Energie durch die Hände."},
        {"titel": "Die arkane Flamme", "inhalt": "Anleitungen zur Erschaffung von magischem Licht, das keine Hitze abstrahlt."},
        {"titel": "Nützliche Alltagshexerei", "inhalt": "Kleine Zauber, um verlorene Schlüssel zu finden oder Milch frisch zu halten."},
        {"titel": "Levitationsgesänge", "inhalt": "Harmonische Tonfolgen, die das Gewicht von schweren Objekten kurzzeitig aufheben."},
        {"titel": "Schattenweberei", "inhalt": "Ein Traktat über die Kunst, visuelle Illusionen in dunklen Ecken zu platzieren."},
        {"titel": "Die Geometrie der Runen", "inhalt": "Schutz- und Warnsymbole für Haustüren und Schatztruhen."},
        {"titel": "Trugbilder des Geistes", "inhalt": "Wie man die visuelle Wahrnehmung von Beobachtern sanft ablenkt."},
        {"titel": "Stilles Zaubern", "inhalt": "Atemtechniken, um Zaubersprüche rein durch Konzentration und ohne Worte zu wirken."},
        {"titel": "Belebung der Materie", "inhalt": "Theoretische Ansätze, um kleinen Holzfiguren für wenige Minuten Leben einzuhauchen."},
        {"titel": "Bannkreise im Wandel", "inhalt": "Schutzbarrieren gegen elementare Zugluft und magische Störungen."},
        {"titel": "Wetterkunde für Magier", "inhalt": "Kleine Rituale, um dichten Nebel zu lichten oder leichten Nieselregen zu erzeugen."},
        {"titel": "Die Kunst der Transmutation", "inhalt": "Ein Leitfaden, um die Farbe von Metallen oberflächlich zu verändern."},
        {"titel": "Empathische Resonanz", "inhalt": "Ein philosophisches Werk über das Erspüren von Emotionen im Raum."},
        {"titel": "Kinetische Schilde", "inhalt": "Die Erschaffung einer unsichtbaren Barriere gegen herabfallende Gegenstände."},
        {"titel": "Das Echo der Mauern", "inhalt": "Zauber, die Geräusche vergangener Stunden in leeren Räumen hörbar machen."},
        {"titel": "Das Paradoxon des Raumes", "inhalt": "Ein komplexer Band über Teleportation. Eine Notiz am Rand besagt: 'Reise nicht in Gedanken um die Welt. Das größte Rätsel der Teleportation entfaltet sich erst in absoluter Nähe.'"},
        {"titel": "Auren und Farben", "inhalt": "Wie man die magische Grundstimmung eines Raumes visuell sichtbar macht."},
        {"titel": "Der verlangsamte Moment", "inhalt": "Ein Zauber, der die Fallgeschwindigkeit einer Teetasse verringert, um Scherben zu vermeiden."},
        {"titel": "Spiegeldimensionen", "inhalt": "Theorien darüber, ob die Welt hinter dem Spiegel ein eigener Raum ist."},
        {"titel": "Funkenleitung", "inhalt": "Sichere Methoden, um statische Elektrizität aus der Kleidung abzuleiten."},
        {"titel": "Gegenzauber im Alltag", "inhalt": "Wie man die ungeschickten Missgeschicke von Zauberlehrlingen schnell neutralisiert."},
        {"titel": "Lieder der Erholung", "inhalt": "Beruhigende Melodien, die den natürlichen Heilungsprozess des Körpers unterstützen."},
        {"titel": "Geistige Projektion", "inhalt": "Die Kunst, das eigene Bewusstsein in den Nebenraum zu schicken, um nach dem Rechten zu sehen."},
        {"titel": "Verständnis der Fauna", "inhalt": "Zauber, die ein vages Gespür für die Wünsche von Haus- und Nutztieren vermitteln."},
        {"titel": "Formen der Entwaffnung", "inhalt": "Ein friedlicher Leitfaden, um Angreifern sanft die Waffen aus der Hand gleiten zu lassen."}
      ]
    },
    "Archiv des Entstandes": {
      "beschreibung": "Chroniken über die drei tragenden Elemente und die infernalischen Ursprünge der Turmarchitektur.",
      "buecher": [
        {"titel": "Die Dynamik des Feuers", "inhalt": "Studien über die thermischen Strömungen und die Lebensdauer magischer Flammen."},
        {"titel": "Fluss und Form", "inhalt": "Wie das Element Wasser sich jeder Umgebung anpasst und Stein formen kann."},
        {"titel": "Das Fundament der Erde", "inhalt": "Geologische Abhandlungen über die Stabilität von magisch verdichtetem Granit."},
        {"titel": "Das erste Infernale Ritual", "inhalt": "Bericht über den rituellen Pakt mit den Mächten der Tiefe, um den Turm immun gegen Erdbeben zu machen."},
        {"titel": "Magma-Synthese", "inhalt": "Die kontrollierte Verschmelzung von flüssiger Erde und reinem Feuer."},
        {"titel": "Die Bändigung der Gezeiten", "inhalt": "Wie man die Anziehungskraft des Mondes nutzt, um Turmbrunnen steigen zu lassen."},
        {"titel": "Dunkle Geometrie", "inhalt": "Ein Lehrbuch über das Zeichnen von Pentagrammen im Fundament, um magische Energie zu bündeln."},
        {"titel": "Thermische Speicher", "inhalt": "Wie die Hitze des Feuers in den Steinmauern für den Winter konserviert wird."},
        {"titel": "Die Verträge von Gestern", "inhalt": "Die originalen, in dunkles Leder gebundenen Abkommen mit Unterwelts-Entitäten bezüglich des Turmbaus."},
        {"titel": "Bodenstabilisierung", "inhalt": "Rituale, die den Erdboden daran hindern, unter dem enormen Gewicht des Turms nachzugeben."},
        {"titel": "Dampf und Druck", "inhalt": "Die Verbindung von Wasser und Hitze zur Energiegewinnung für die oberen Etagen."},
        {"titel": "Rituelle Architektonik", "inhalt": "Pläne, die zeigen, wie der Turm durch unheilige Symmetrien seine Höhe halten kann."},
        {"titel": "Die Sprache des Steins", "inhalt": "Wie man die innere Struktur von Bergen liest, um die perfekten Bausteine zu finden."},
        {"titel": "Die Brunnen der Tiefe", "inhalt": "Die rituell gesicherten Wasserleitungen, die tief aus der Unterwelt in den Turm führen."},
        {"titel": "Ascheverwertung", "inhalt": "Wie die Rückstände magischer Feuer für rituelle Kreide verwendet werden."},
        {"titel": "Das Ritual der ewigen Glut", "inhalt": "Die Beschwörung eines infernalen Feuers im Keller, das den Turm seit Jahrhunderten heizt."},
        {"titel": "Hydrologische Siegel", "inhalt": "Magische Barrieren, die verhindern, dass Grundwasser in die Archive eindringt."},
        {"titel": "Das Abkommen des Aufstiegs", "inhalt": "Dokumentation des finalen Paktes, der dem Turm seine schwebenden Elemente verlieh."},
        {"titel": "Erzbindung", "inhalt": "Wie man magische Metalle direkt in das Steinfundament einweiht."},
        {"titel": "Die Logik des Abgrunds", "inhalt": "Eine Abhandlung darüber, warum satanische Rituale für diese Art der Monumentalarchitektur mathematisch notwendig sind."},
        {"titel": "Wasserläufe der Arkanistik", "inhalt": "Wie fließendes Wasser magische Ströme im Turm umleiten und filtern kann."},
        {"titel": "Der flammende Schild", "inhalt": "Ein Schutzritual, das die Außenwand bei Angriffen in eine feurige Barriere hüllt."},
        {"titel": "Elementare Symbiose", "inhalt": "Wie Erde, Wasser und Feuer im Gleichgewicht gehalten werden, um den Turm zu stabilisieren."},
        {"titel": "Die Weihe der Turmspitze", "inhalt": "Das abschließende Ritual, das die infernalen Energien des Fundaments mit dem Himmel verband."},
        {"titel": "Stille im Gemäuer", "inhalt": "Ein Isolationszauber, der die lauten Echos der infernalen Rituale im Keller neutralisiert."}
      ]
    },
    "Archiv des ???": {
      "beschreibung": "Ein verstaubtes, fast vergessenes Regal in einer namenlosen Nische des Turms.",
      "buecher": [
        {"titel": "Das Flüstern der Leere", "inhalt": "Ein Buch mit völlig leeren Seiten. Wenn man das Ohr an den Einband hält, hört man eine ferne Weibliche Stimme die das Wort Seele sagt."},
        {"titel": "Chroniken des Absonderlichen", "inhalt": "Aufzeichnungen über die unorthodoxen Experimente eines bestimmten Magiers, dessen Name im gesamten Buch ordentlich geschwärzt wurde. Er versuchte unter anderem, die Schwerkraft von Suppenlöffeln umzukehren und Zeitmagie beim Brotbacken anzuwenden. Seine Methoden galten dem Konzil als zu exzentrisch."},
        {"titel": "Das Paradoxon der Zeit", "inhalt": "Eine philosophische Abhandlung über die Frage, ob eine umgefallene Sanduhr die Zeit anhält."},
        {"titel": "Unmögliche Geometrie", "inhalt": "Skizzen von architektonischen Formen, die theoretisch faszinierend, aber praktisch völlig unbaubar sind."},
        {"titel": "Das letzte vergessene Wort", "inhalt": "Ein Buch, das nur ein einziges, langes Wort enthält. Man vergisst seine Bedeutung, sobald man den Raum verlässt."}
      ]
    }
  }
}

Bibliothek = ["Erdgeschoss", "Baylons Archiv", "Archiv des Entstandes", "Archiv des ???"]
schloss_1 = "wärme"
schloss_2 = "wasser"
Zellenpassage = False
buchPassage = False
türPassage = False

flurPlan = """
              ---------+----------+----------+-----------
                       |          |          |           
                       |    1     |    2     |           
                       |          |          |           
            -----------+--------| +--------| +-----------
                                             
            -----------+--------| +--------| +-----------
                       |          |          |           
                       |    3     |    4     |           
                       |          |          |           
            -----------+----------+----------+-----------
            """

taschenmesserhaltbarkeit = 100
schlosshaltbarkeit = 100
alter = random.randint(18, 60)
geschicklichkeit = random.randint(1, 10)
charisma = random.randint(1, 10)
arkanesWissen = random.randint(1, 4)
akrobatik = geschicklichkeit / alter * 20
Stärke = random.randint(1, 3)

Charakterwerte = {"Alter": alter,
                   "Geschicklichkeit": geschicklichkeit,
                   "Charisma": charisma,
                   "Arkanes Wissen": arkanesWissen,
                   "Akrobatik": akrobatik,
                   "Stärke": Stärke}

schlossMöglicheKombinationen_1 = ["Wärme", "Herbst", "Abwehr", "Intakt"]
schlossMöglicheKombinationen_2 = ["Wissen", "Genuss", "Wasser", "Spitze"]
Inventar = ["Allzwecktaschenmesser"]
Itemdict = {"Allzwecktaschenmesser": "Ein altes Taschenmesser, das Herstellerlogo ist zerkratzt und der Klappmechanismus rostet.",
            "skelletenBuch": "Wer das Licht erlischt, der wird in Dunkelheit verweilen. Wer die Nässe spürt, der will die Flamme lichterloh brennen lassen. Wer die Kälte spürt, der sich die ... herbei wünscht",
            "Notiz_1": "Eine sehr neue Notiz, es sind keine sichtbaren Schäden vorhanden. Die Nummer 7 steht in der oberen Ecke.",
            "Notiz_2": "Eine leicht abgenutzte Notiz. Leichte Risse und Flecken sind erkennbar. Die nummer ist nicht ganz sichtbar, es sieht aus wie eine 8 oder vielleicht eine 0?",
            "Notiz_3": "Eine schäbige alte Notiz, sie ist angerissen und die Tinte ist verschmiert. Die Nummer 4 steht in der oberen Ecke.",
            "mysteriöserSchlüssel": "Ein alter eiserner Schlüssel, der an einem Verstorbenen gefunden wurde. Er ist kalt und schwer.",
            "baylonsBuch": "Das Buch ist in einer nicht lesbaren Schrift verfasst. Es vibriert leicht in der Hand."
            }


def Schmerz(schmerz_grad="1"):
    global Gesundheit
    if schmerz_grad == "1":
        printSlow("Sie spüren einen drückenden Schmerz.")
        printSlow("Sie verlieren 5 Gesundheit.")
        Gesundheit -= 5
    elif schmerz_grad == "2":
        printSlow("Sie spüren einen stechenden Schmerz.")
        printSlow("Sie verlieren 10 Gesundheit.")
        Gesundheit -= 10
    elif schmerz_grad == "3":
        printSlow("Sie spüren einen unerträglichen Schmerz!")
        printSlow("Sie verlieren 20 Gesundheit.")
        Gesundheit -= 20
    print(f"[Gesundheit: {Gesundheit}]")
    if Gesundheit <= 0:
        printSlow("Ihre Sicht verschwimmt...")
        printSlow("--- ENDE: Im Turm gestorben... ---")
        sys.exit()
        
def Buchlesen(Archivname, buch_Index):
    try:
        buecher_liste = Archive["bibliothek"][Archivname]["buecher"]
        if 0 <= buch_Index < len(buecher_liste):
            buch = buecher_liste[buch_Index]
            print("\n" + "="*40)
            print(f"TITEL: {buch['titel']}")
            print("="*40)
            print(buch["inhalt"])
            print("="*40 + "\n")
        else:
            print("Diese Buchnummer existiert hier nicht.")
    except KeyError:
        print("Dieses Archiv existiert nicht.")

def printSlow(text, delay=0.03):
    for Buchstabe in text:
        sys.stdout.write(Buchstabe)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def wartepunkte(delay, text="..."):
    for i in range(0, 4):
        sys.stdout.write(text[0])
        sys.stdout.flush()
        time.sleep(delay)
    print()

def examine(n):
    if n in Itemdict:
        return Itemdict[n]
    return "..."

def inventar_anzeigen():
    print("\n--------- INVENTAR ---------")
    if not Inventar:
        print("Ihr Inventar ist leer.")
    for i, item in enumerate(Inventar, start=1):
        print(f"{i}. {item}")
    while True:
        auswahl = input("\nNummer wählen (0 zum Schließen): ").strip()
        if auswahl == "0":
            break
        try:
            index = int(auswahl) - 1
            if 0 <= index < len(Inventar):
                item = Inventar[index]
                print("\n-> " + str(examine(item)))
            else:
                print("Ungültige Auswahl.")
        except ValueError:
            print("Bitte eine Zahl eingeben.")



printSlow(f"Ihre Attribute wurden gewürfelt: Alter {Charakterwerte['Alter']}, Stärke {Charakterwerte['Stärke']}, Arkanes Wissen {Charakterwerte['Arkanes Wissen']}.")
printSlow("Ob diese nützlichen werden könnten?")

while Starten != "y":
    Starten = input("Spiel starten? y/n: ").strip().lower()

while Gesundheit > 0 and not SpielBeendet:
    if playerlocation == "Zellen":
        printSlow("\n---------- Kapitel 1: Die nötigen Aufgaben ----------")
        printSlow("Sie erwachen in einem dunklen Turm. Das Letzte, an das Sie sich erinnern können, war die vergangene Nacht.")
        printSlow("Sie sehen eine Kerze leuchten, das sanfte Licht krallt sich an den nassen Steinwänden entlang.")
        printSlow("Durch den sanften Kerzenschein sehen Sie eine alte hölzerne Tür mit Fenster.")

    zellenPassageAltWeg = False

    while not Zellenpassage:
        command = input("> Tür öffnen? (y/n/i für Inventar): ").strip().lower()
        if command == "y":
            printSlow("Die Kerkertür scheint verschlossen zu sein.")
            zellenPassageAltWeg = False
            Zellenpassage = True
        elif command == "n":
            printSlow("Sie entscheiden sich, die Tür vorerst in Ruhe zu lassen und schauen sich um.")
            zellenPassageAltWeg = True
            Zellenpassage = True
        elif command == "i":
            inventar_anzeigen()
        else:
            print("Ungültige Eingabe.")

    if zellenPassageAltWeg:
        printSlow("Sie setzen sich auf den kalten nassen Boden. Sie spüren mit ihrer Hand an den Wänden entlang.")
        printSlow("Der Pfad ihrer Hand stoppt, als sie einen kalten, länglichen Gegenstand berühren. Es fühlt sich an wie ein Knochen...")
        printSlow("Ein Skelett liegt einsam in dem Raum, neben ihm sein vertrauenswürdiges Buch.")        
        
        while not buchPassage:
            command = input("> Buch öffnen (y/n/i)?: ").strip().lower()
            if command == "y":
                print("Sie öffnen das alte Buch. Informationen:\n" + str(examine("skelletenBuch")))
                if "skelletenBuch" not in Inventar: Inventar.append("skelletenBuch")
                buchPassage = True
            elif command == "n": 
                printSlow("Sie nehmen das Buch ungelesen mit.")
                if "skelletenBuch" not in Inventar: Inventar.append("skelletenBuch")
                buchPassage = True
            elif command == "i":
                inventar_anzeigen()

        printSlow("In ihrer Not entdecken sie eine Luke im Boden. Die Luke ist mit 3 Schlössern versehen.")
        
        command = input("> Doch nochmal die Tür versuchen? (y/n): ").strip().lower()
        if command == "y":
            print("Die Tür bleibt stumm und verschlossen. Die Luke ist der einzige Weg.")
        elif command == "n":
            printSlow("Die Tür führt mich nur in die irre, ich untersuche die Luke.")
        else:
            command = input("Gebe etwas gültiges ein").strip().lower()
            
        printSlow("\nDas erste Schloss ist ein loderndes Rot und benötigt ein 5-stelliges Wort.")
        printSlow("Das mittlere ein aquafarbiges Blau (6-stelliges Wort).")
        printSlow("Das letzte Schloss ist braun, alt und verrostet.")
        
        printSlow("Erstes Schloss. Folgende Wörter liegen nahe:")
        for Wort in schlossMöglicheKombinationen_1:
            printSlow("- " + Wort)

        command = ""
        while command != schloss_1:
            command = input("Geben Sie ein Wort ein (oder 'i'): ").strip().lower()
            if command == "i":
                inventar_anzeigen()
            elif command != schloss_1:
                print("Das Schloss klemmt...")

        printSlow("Das erste Schloss klickt offen!")

        printSlow("Zweites Schloss. Folgende Wörter:")
        for Wort in schlossMöglicheKombinationen_2:
            printSlow("- " + Wort)
        printSlow("Es tropft von der Decke...")
        
        command = ""
        while command != schloss_2:
            command = input("Geben Sie ein Wort ein (oder 'i'): ").strip().lower()
            if command == "i":
                inventar_anzeigen()
            elif command != schloss_2:
                print("Das Schloss klemmt...")

        printSlow("Das zweite Schloss öffnet sich!")
        
        printSlow("Das letzte Schloss ist zu verrostet, um die Buchstaben zu lesen.")
        
        command = ""
        while command != "y":
            command = input("Möchten Sie versuchen, das Schloss mit dem Taschenmesser aufzubrechen? (y/i): ").strip().lower()
            if command == "i":
                inventar_anzeigen()
            
        printSlow("Sie rammen das Taschenmesser in das Schloss. Es knackt laut und die Luke schwingt auf!")
        printSlow("Sie klettern in eine dunkle Nebenzelle...")
        
        printSlow("Ein Buch sticht ins Auge. Es hat einen familiären Gesang... Die sanfte Stimme bittet dich, das Buch wieder mit Baylon zu vereinigen.")
        command = input("> 'Baylons Buch' mitnehmen? (y/n): ").strip().lower()
        if command == "y":
            Inventar.append("baylonsBuch")
            printSlow("Sie spüren eine seltsame Wärme, als sie es einstecken.")
        else:
            printSlow("Sie nehmen das Buch nicht mit, könnte dies zum verhängnis werden?")
            
        printSlow("Eine Treppe führt zu einer Tür mit einem Rätsel:")
        printSlow("Ich schlemme laut, während ich am Königstisch sitze.\nIch bin das Instrument der Sünder.\nIch bin der Soldat doch auch der General.\nIch bin die sorge der Bürger doch die Liebe der Herrscher.")
        
        command = ""
        while command != zelle2TürRätsel:
            command = input("Es ist der... ").strip().lower()
            if command != zelle2TürRätsel:
                Schmerz("1")
                print("Falsch. Versuchen Sie es erneut.")
                
        printSlow("Das Wort hallt wider, die Tür schwenkt mit Wucht auf")
        BibliothekWeg = True
        playerlocation = "Hof"

    elif not zellenPassageAltWeg:
        printSlow("Sie versuchen die Tür zu öffnen, doch sie ist verschlossen. Das Schloss ist rostig.")
        printSlow("Nach einer kurzen Überlegung versinken Sie in Verzweiflung, aus Nervosität und Angst wühlen Sie wild in der Tasche, Sie fühlen etwas Kaltes und Metallisches, es ist das Allzwecktaschenmesser.")
        
        while not türPassage and schlosshaltbarkeit > 0:
            command = input("> 1 Taschenmesser reinrammen\n> 2 Als Dietrich benutzen\n> 3 Als Rostlöser benutzen\n: ").strip()
            if command == "1":
                if Charakterwerte["Stärke"] > 2:
                    print("Ihre Stärke reicht aus! Die Tür bricht auf, aber die Klinge bricht ab.")
                    if "Allzwecktaschenmesser" in Inventar:
                        Inventar.remove("Allzwecktaschenmesser")
                    türPassage = True
                else:
                    schaden = random.randint(1, 75)
                    schlosshaltbarkeit -= schaden
                    print(f"Sie rammen das Taschenmesser mit voller Kraft in das Schloss, die Tür knackt doch lässt sich noch nicht öffnen. Ihr Taschenmesser verliert 7.5% Haltbarkeit.\nDer Schlüsselmechanismus des Schlosses wird dabei {max(0, schlosshaltbarkeit)}% beschädigt.")
                    taschenmesserhaltbarkeit -= 7.5
            elif command == "2":
                if Charakterwerte["Geschicklichkeit"] >= 5:
                    printSlow("Mit ruhigen Händen knacken Sie das Schloss")
                    türPassage = True
                else:
                    schaden = random.randint(1, 75)
                    schlosshaltbarkeit -= schaden
                    print(f"Sie versuchen das Taschenmesser als Dietrich zu benutzen, doch es passiert nichts, Sie zerstören nur das Schloss weiter.\nDer Schlüsselmechanismus des Schlosses wird dabei {max(0, schlosshaltbarkeit)}% beschädigt.")
            elif command == "3":
                rostLevel = random.randint(1, 100)
                if rostLevel >= 65:
                    printSlow("Sie benutzen das Taschenmesser als Rostlöser, Das Schloss zerbröselt und die Tür öffnet sich!")
                    türPassage = True
                elif 50 < rostLevel < 65:
                    schaden = random.randint(1, 75)
                    schlosshaltbarkeit -= schaden
                    print(f"Sie benutzen das Taschenmesser als Rostlöser, langsam kratzen sie den Rost weg.\nDer Schlüsselmechanismus wird dabei {max(0, schlosshaltbarkeit)}% beschädigt.")
                else:
                    printSlow("Der Rost ist zäh, Sie rutschen ab und beschädigen dabei das Taschenmesser, es verliert 3.5% Haltbarkeit.")
                    taschenmesserhaltbarkeit -= 3.5
                    
        if 0 < taschenmesserhaltbarkeit < 25:
            Itemdict["Allzwecktaschenmesser"] = "Ein altes Taschenmesser, das Herstellerlogo ist zerkratzt und der Klappmechanismus rostet, es ist jedoch stark beschädigt und könnte jederzeit brechen."
        elif taschenmesserhaltbarkeit < 75:          
            Itemdict["Allzwecktaschenmesser"] = "Ein altes Taschenmesser, das Herstellerlogo ist zerkratzt und der Klappmechanismus rostet, die Klinge ist verbogen und abgenutzt, es könnte bald brechen."

        if türPassage:
            printSlow("Erleichtert betreten Sie einen sanft beleuchteten Flur.")
            printSlow("Plötzlich hören Sie kräftige Fußschritte, Der Wärter kommt!")
            
            if taschenmesserhaltbarkeit < 25 or "Allzwecktaschenmesser" not in Inventar:
                command = input("> 1 In einem fremden Raum verstecken?\n> 2 Zurück in die Zelle rennen?\n> 3 Sich in einer düsteren Ecke verstecken?\n: ").lower().strip()
            else:
                command = input("> 1 In einem fremden Raum verstecken?\n> 2 Zurück in die Zelle rennen?\n> 3 Sich in einer düsteren Ecke verstecken?\n> 4 Das Taschenmesser als Waffe benutzen?\n: ").lower().strip()
            
            if command == "1":
                print(flurPlan)
                command_room = input("> In den 1ten Raum rennen?\n> In den 2ten Raum rennen?\n> In den 3ten Raum rennen?\n> In den 4ten Raum rennen?\n: ").lower().strip()
                
                if command_room == "1" or command_room == "4":
                    printSlow("Die Tür ist verschlossen.")
                    wartepunkte(0.4, "...\n")
                else:
                    printSlow("Sie rennen in einen der Räume, es ist dunkel und staubig, aber er ist beleuchtet.")
                    printSlow("Sie schließen die Tür hinter sich und verriegeln sie, indem sie einen Stuhl davor stellen. Die Fußschritte werden leiser, als sie in der Ferne verstummen.")
            elif command == "2":
                printSlow("Sie rennen zurück in ihre Zelle und warten bis die Fußstapfen verstummen.")
            elif command == "3" or command == "4":
                if command == "4":
                    printSlow("Nur ein Narr würde sein Leben auf die Waage stellen.")
                printSlow("Sie verstecken sich in einer düsteren unbeleuchteten Ecke.")
                printSlow("Die Fußstapfen so nahe...")
                wartepunkte(0.25)
                print("Sie sehen den Rücken des Mannes, der den Flur entlang ging. Es sieht so aus, als würde er die Zellen kontrollieren.")
                printSlow("Hoffentlich werden sie nicht gesehen....")
                
            printSlow("Am Ende des Flurs erreichen Sie den Innenhof.")
            playerlocation = "Hof"
            BibliothekWeg = True

    
    while playerlocation == "Hof" and Gesundheit > 0:
        printSlow("\n---------- Kapitel 2: Der Hof ----------")
        Karte =  """
                             .----||----.
             ???        =|    DER HOF       |=     Bibliothek
                             '----||----'
                              Barracken
        """
        print(Karte)
        command = input("> 1 Zellgebäude\n> 2 Bibliothek\n> 3 Barracken\n> 4 Namenloser Pfad (???)\n: ").strip()
        
        if command == "1":
            if not BibliothekWeg:
                    printSlow("Nur ein Narr würde seine freiheit opfern damit er keine entscheidung treffen muss.")
                    wartepunkte(0.75)
                    continue
            else:
                printSlow("Es scheint verschlossen zu sein...")
        elif command == "2":
            playerlocation = "Bibliothek"
            printSlow("\nSie betreten die Bibliothek.")
            while playerlocation == "Bibliothek":
                print("\nVerfügbare Archive:")
                for ort in Bibliothek:
                    print(f"- {ort}")
                archiv_eingabe = input("Welches Archiv betreten? ('n' für Zurück): ").strip()
                
                if archiv_eingabe in Bibliothek and archiv_eingabe != "Erdgeschoss":
                    aktuelles_archiv = Archive["bibliothek"][archiv_eingabe]
                    print(f"\n{aktuelles_archiv['beschreibung']}")
                    for index, buch in enumerate(aktuelles_archiv["buecher"], 1):
                        print(f"[{index}] {buch['titel']}")
        
                    buch_auswahl = input("Buchnummer eingeben: ").strip()
                    if buch_auswahl.isdigit():
                        Buchlesen(archiv_eingabe, int(buch_auswahl)-1)
                elif archiv_eingabe.lower() == "n":
                    playerlocation = "Hof"

        elif command == "3":
            if visitedBarracken:
                printSlow("In den Barracken gibt es nichts Neues.")
            else:
                printSlow("Sie betreten die zerstörten Barracken. An einem toten Arbeiter finden Sie etwas.")
                command = input("Schlüssel aufnehmen? (y/n): ").strip().lower()
                if command == "y":
                    Inventar.append("mysteriöserSchlüssel")
                    print("Schlüssel eingesteckt.")
                    visitedBarracken = True
                else:
                    printSlow("Sie nehmen den Schlüssel nicht mit aber warum nicht....?")
                printSlow("An der Wand steht das Wort 'Ekstase' in Blut geschrieben...")
                
        elif command == "4":
            if not visitedNameless:
                printSlow("Sie betreten den Namenlosen Pfad. Eine massive, finstere Eisentür versperrt den Weg.")
                printSlow("An der Tür hängen drei Notizen, die Sie einstecken:")
                Inventar.extend(["Notiz_1", "Notiz_2", "Notiz_3"])
                print("- Notiz 1: 'Wer in die Leere flüstert, der wird das Wort der Seele hören ")
                print("- Notiz 2: 'Der Schlüssel führt zum Sieg, doch die Reihenfolge ist der wahre Krieg.")
                print("- Notiz 3: Der Text ist verschmiert.")
                printSlow("Ich sollte mir die Notizen im inventar näher ansehen")
                inventar_anzeigen()
                visitedNameless = True
                printSlow("Die Tür hat 3 spezielle Schlösser. Sammeln Sie Wissen, bevor Sie es versuchen!")
            else:
                printSlow("\nSie stehen wieder vor dem massiven Eisentor des Namenlosen Pfades.")
                command = input("Möchten Sie versuchen, das Tor zu entsiegeln? (y/n/i): ").strip().lower()
                
                if command == "i":
                    inventar_anzeigen()
                elif command == "y":
                    printSlow("\n--- DAS TOR DES PFADES ---")
                    
                    
                    wort = input("1. Schloss: 'Sprich das Wort, das in der Leere gehört wird': ").strip().lower()
                    if wort != "seele":
                        Schmerz("2")
                        print("Die Tür stößt Sie zurück.")
                        continue
                        
                    
                    print("Das zweite Schloss ist ein schweres Eisenschloss.")
                    if "mysteriöserSchlüssel" not in Inventar:
                        print("Ihnen fehlt der passende Schlüssel. Sie können nicht weiter.")
                        continue
                    else:
                        printSlow("Der mysteriöse Schlüssel aus den Barracken passt perfekt und dreht sich!")
                        
                   
                    print("3. Schloss: Ein Zahlenrad mit drei Ringen, Erinnern Sie sich an die Notizen und ihre Zahlen.")
                    zahl = input("Geben Sie die 3-stellige Kombination ein: ").strip()
                    if zahl != "704":
                        Schmerz("3")
                        print("Falsch!")
                        continue
                        
                    printSlow("Das Tor öffnet sich...")
                    playerlocation = "Altar"
                    break

    if playerlocation == "Altar":
        printSlow("\n---------- Kapitel 3: Der Altar des Wächters ----------")
        print("Sie betreten einen runden Raum, In der Mitte befindet sich ein antiker Stein-Altar.")
        print("Hinter dem Altar eine Leuchtende Tür.")
        
        
        if Charakterwerte["Arkanes Wissen"] >= 3:
            printSlow("Sie haben ein hohes Wissen der Magie, dies wird ihnen zu gunsten fallen.")
            hoheswissen = True
        else:
            printSlow("Sie sind ungelernt in den Arkanen Wegen, dies wird ihnen die Entscheidung erschweren. ")
            hoheswissen = False

        print("Was tun Sie?")
        printSlow("1: Durch die Leuchtende Tür gehen und hoffen das man dem Turm entkommt.")
        
        if "baylonsBuch" in Inventar:
            printSlow("2: Baylons Buch auf den Altar legen.")
        else:
            printSlow("2: Versuchen etwas auf den leeren Altar zu legen")
        printSlow("3: Das loderne Feuer entzünden. (Turm zerstören)")
        
        final_choice = input("Ihre Wahl: ").strip()
        
        if final_choice == "1":
            if hoheswissen == True:
                printSlow("Die Tür Schwenkt durch ihre reine präsenz auf....")
                printSlow("Sie gehen durch die Tür auf eine grüne Naturreiche wiese")
                printSlow("--- ENDE 1: Die Flucht ---")
                printSlow("Sie sind dem Turm entkommen aber sie fragen sich trotzdem noch wie sie jemals in dem turm aufgewacht sind...")
                SpielBeendet = True
            else:
                printSlow("Die Tür lässt sich nicht öffnen")
                printSlow("Sie rennen mit wucht mehrmals gegen die Tür doch sie haben nicht die Stärke um sie zu brechen.")
                printSlow("--- ENDE 2: Die weile ---")
                printSlow("Sie sehen keinen Weg mehr zum entkommen nun verweilen sie in den Leeren Zellen des Turmes")
                SpielBeendet = True
            
        elif final_choice == "2" and "baylonsBuch" in Inventar:
            printSlow("Sie platzieren das  Buch auf dem Altar.")
            printSlow("Die Runen des Altars leuchten auf")
            printSlow("Das Buch Schlägt auf. Nun können sie es endlich lesen, im buche steht : 'Willkomen zurück Baylon'")
            printSlow("--- ENDE 3: Der Wächter des Turmes ---")
            print("Sie entkommen nicht, denn sie sind nun der Wächter des Turmes. Ist dies ein Tugend oder doch ein Fluch....")
            SpielBeendet = True
        elif final_choice == "2" and "baylonsBuch" not in Inventar:
            printSlow("Sie legen einen Gegenstand auf den Altar....")
            wartepunkte(0.5)
            printSlow("Der altar fährt in den Steinpodest hinein und das Tor des Namenlosen Pfades Schließt sich")
            printSlow("--- ENDE 4: Der töricht verweilt nun die Tage  ---")
            printSlow("Ihre Torheit brachte sie dazu Den wächter des turmes mit einer Falschen opfergabe zu verärgern")
            printSlow("Nun verweilen sie im Altarraum, ob sie noch einen anderen Gefangenen vor dem verdursten sehen? ")
        elif final_choice == "3":
            printSlow("Sie entzünden die uralten Feuerkruge ")
            printSlow("Das Höllenfeuer erwacht und verschlingt langsam den altar, den Hof, Die Bibliothen bis nichts mehr des Turmes verbleibt.")
            printSlow("\n--- ENDE 5: Die Gier nun ihr Ende ---")
            print("Aus Gier und Zerstörungswut haben Sie den Turm zum Einsturz gebracht. Sie verbrennen in den Boshaften Flammen. Ihr Skelett wird in Jahrhunderten vielleicht von einem neuen Abenteurer gefunden.")
            SpielBeendet = True
            
        else:
            print("Sie zögern zu lange, Der Turm stürtzt ein.")
            printSlow("--- ENDE 6: Warum denn genau dieses ende ---")
            SpielBeendet = True

print("Ende")
sys.exit()