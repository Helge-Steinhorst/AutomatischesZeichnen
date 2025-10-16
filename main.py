# Benötigte Bibliotheken importieren
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

from PIL import Image, ImageDraw, ImageFont


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
    title="PNG-Datei speichern unter...",
    defaultextension=".png",
    filetypes=[("PNG-Bild", "*.png"), ("Alle Dateien", "*.*")]
)

# --- 2. PDF NUR ERSTELLEN, WENN EIN DATEIPFAD AUSGEWÄHLT WURDE ---

# Wenn der Benutzer auf "Abbrechen" klickt, ist DATEIPFAD leer.
if DATEIPFAD:
    try:
        # --- BILD-EINSTELLUNGEN (NEU) ---
        DPI = 300  # Punkte pro Zoll, für eine gute Qualität
        
        # A4-Maße in Millimetern
        A4_MM_BREITE = 210
        A4_MM_HOEHE = 297

        # Umrechnung von mm in Pixel basierend auf DPI
        breite = int((A4_MM_BREITE / 25.4) * DPI)
        hoehe = int((A4_MM_HOEHE / 25.4) * DPI)

        # Umrechnung der Abstände in Pixel
        def mm_to_px(mm):
            return int((mm / 25.4) * DPI)

        ABSTAND_OBEN = mm_to_px(20)
        ABSTAND_SEITE = mm_to_px(20)
        
        hoehe_beginEinspeisung = ABSTAND_OBEN
        hoehe_beginAbgang = mm_to_px(75)

        # Erstelle ein leeres, weißes Bild und ein Zeichenobjekt
        img = Image.new('RGB', (breite, hoehe), 'white')
        draw = ImageDraw.Draw(img)

        # --- DIE LINIEN ZEICHNEN ---
        # GEÄNDERT: Zeichenbefehle für Pillow verwenden
        x_start = ABSTAND_SEITE
        x_end = breite - ABSTAND_SEITE

        # Obere Hauptlinie (Sammelschiene)
        draw.line(
            [(x_start, hoehe_beginEinspeisung), (x_end, hoehe_beginEinspeisung)], 
            fill='black', 
            width=3  # Pillow verwendet 'width' statt 'setLineWidth'
        )
        
        # Untere Hauptlinie
        draw.line(
            [(x_start, hoehe_beginAbgang), (x_end, hoehe_beginAbgang)],
            fill='black',
            width=3
        )

        # --- ZEICHNUNGEN FÜR JEDE EINSPIESUNG HINZUFÜGEN ---
        # Wir rufen die Zeichenfunktion für jedes gespeicherte Messgerät auf.
        # HINWEIS: Ihre Funktion 'zeichne_eine_Einspeisung' muss angepasst werden!
        zeichnungen.zeichneEinspeisung.zeichne_eine_Einspeisung(
                draw,                  # Das 'draw'-Objekt statt des 'canvas'
                breite,                # Breite in Pixeln
                hoehe_beginEinspeisung, # Y-Position in Pixeln
                anzahlEinspeisungen,   # Die Gesamtzahl
                messgerät         # Der Name des Messgeräts
        )

        # --- BILD SPEICHERN ---
        # GEÄNDERT: 'save'-Methode des Bildobjekts
        img.save(DATEIPFAD)
        print(f"\n✅ Erfolgreich! Die Datei wurde hier gespeichert:\n{DATEIPFAD}")

    except Exception as e:
        print(f"\n❌ Ein Fehler ist aufgetreten: {e}")
else:
    print("\nVorgang abgebrochen. Es wurde keine Datei erstellt.")

# --- 3. WARTEN, BIS DER BENUTZER DAS FENSTER SCHLIESST ---
print("\nDrücke die Enter-Taste, um das Programm zu beenden.")
input()