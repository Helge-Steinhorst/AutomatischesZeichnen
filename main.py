# Benötigte Bibliotheken importieren
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm


import tkinter as tk
from tkinter import filedialog

import scripts.Prints
import scripts.inputs
import zeichnungen.zeichneEinspeisung

scripts.Prints.willkommen()

anzahlEinspeisungen = scripts.inputs.anzahlEinspeisung()

for i in range(anzahlEinspeisungen):
    print("Bitte geben Sie das Messgerät für die folgende Einspeisung ein:")
    print(f"Einspeisung {i + 1}:")
    messgerät = input("Messgerät: ")
    print(f"Sie haben '{messgerät}' für Einspeisung {i + 1} eingegeben.")

# --- 1. DATEIPFAD VOM BENUTZER ABFRAGEN ---

#---------------------------------------------------------------------------------------
print("\nJetzt wählen Sie bitte den Speicherort und Dateinamen für die PDF-Datei aus.")
# Ein verstecktes Hauptfenster für den Dialog erstellen
root = tk.Tk()
root.withdraw() # Wir wollen kein leeres Fenster sehen

print("Öffne das 'Speichern unter'-Fenster...")

# Den "Speichern unter"-Dialog anzeigen
# Der Benutzer wählt hier Ordner und Dateinamen aus.
DATEIPFAD = filedialog.asksaveasfilename(
    title="PDF-Datei speichern unter...",
    defaultextension=".pdf",
    filetypes=[("PDF-Dokumente", "*.pdf"), ("Alle Dateien", "*.*")]
)

# --- 2. PDF NUR ERSTELLEN, WENN EIN DATEIPFAD AUSGEWÄHLT WURDE ---

# Wenn der Benutzer auf "Abbrechen" klickt, ist DATEIPFAD leer.
if DATEIPFAD:
    try:
        # --- EINSTELLUNGEN ---
        ABSTAND_OBEN = 20 * mm  # 20 mm = 2 cm
        breite, hoehe = A4

        hoehe_beginEinspeisung = hoehe - ABSTAND_OBEN
        hoehe_beginAbgang = hoehe - 75*mm



        
        c = canvas.Canvas(DATEIPFAD, pagesize=A4)

        # --- DIE LINIE ZEICHNEN ---
        y_position = hoehe - ABSTAND_OBEN
        x_start = 20 * mm
        x_end = breite - 20 * mm


        c.setLineWidth(2)
        c.line(x_start, y_position, x_end, y_position)
        

        
        zeichnungen.zeichneEinspeisung.zeichne_eine_Einspeisung(c,breite,hoehe_beginEinspeisung,anzahlEinspeisungen,messgerät)
        c.line(x_start,hoehe_beginAbgang,x_end,hoehe_beginAbgang)




        c.save()
        print(f"\n✅ Erfolgreich! Die Datei wurde hier gespeichert:\n{DATEIPFAD}")

    except Exception as e:
        print(f"\n❌ Ein Fehler ist aufgetreten: {e}")
else:
    print("\nVorgang abgebrochen. Es wurde keine Datei erstellt.")

# --- 3. WARTEN, BIS DER BENUTZER DAS FENSTER SCHLIESST ---
print("\nDrücke die Enter-Taste, um das Programm zu beenden.")
input() # Hält das Terminalfenster offen, bis Enter gedrückt wird