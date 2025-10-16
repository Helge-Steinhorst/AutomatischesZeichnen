from reportlab.lib.units import mm

from PIL import Image, ImageDraw, ImageFont

def mm_to_px(mm, dpi=300):
    """Rechnet Millimeter in Pixel um, basierend auf einer DPI-Einstellung."""
    return int((mm / 25.4) * dpi)

def zeichne_eine_Einspeisung(draw, breite_px, y_start_px, anzahl, messgerät):
    """
    Zeichnet eine einzelne Einspeisung auf ein Pillow 'draw'-Objekt.

    Args:
        draw (ImageDraw.Draw): Das Zeichenobjekt von Pillow.
        breite_px (int): Die Gesamtbreite des Zeichenbereichs in Pixeln.
        y_start_px (int): Die Y-Startposition (Sammelschiene) in Pixeln.
        index (int): Der Index der aktuellen Einspeisung (z.B. 0 für die erste).
        anzahl (int): Die Gesamtzahl der Einspeisungen.
        messgerät (str): Der Text, der für das Messgerät angezeigt werden soll.
    """
    # --- EINSTELLUNGEN IN PIXEL UMRECHNEN ---
    quadrat_seite_px = mm_to_px(5)
    linie1_laenge_px = mm_to_px(25)
    linie2_start_abstand_px = mm_to_px(5)
    linie2_ende_abstand_px = mm_to_px(30)
    text_abstand_px = mm_to_px(3) # Kleiner Abstand für den Text vom Quadrat

    abstand_pro_einspeisung = breite_px / (anzahl + 1)

    # --- POSITION BERECHNEN ---
    # Verteilt alle Einspeisungen gleichmäßig über die Breite
    for i in range(anzahl):
        
        x_pos = abstand_pro_einspeisung * (i + 1)
        # --- ZEICHNEN MIT PILLOW ---
        # 1. Erste vertikale Linie von der Sammelschiene nach unten
        y_nach_linie1 = y_start_px + linie1_laenge_px
        draw.line(
            [(x_pos, y_start_px), (x_pos, y_nach_linie1)],
            fill='black',
            width=2
        )
        # 2. Quadrat (Messgerät-Symbol) zeichnen
        # Pillow braucht die obere linke und untere rechte Ecke
        x1_quadrat = x_pos - (quadrat_seite_px / 2)
        y1_quadrat = y_nach_linie1
        x2_quadrat = x_pos + (quadrat_seite_px / 2)
        y2_quadrat = y_nach_linie1 + quadrat_seite_px
        draw.rectangle(
            [(x1_quadrat, y1_quadrat), (x2_quadrat, y2_quadrat)],
            outline='black',
            width=2
        )
        # 3. Text für das Messgerät hinzufügen
        # anchor='lm' bedeutet, dass der Text links von der Koordinate beginnt
        # und vertikal zentriert ist.

        try:
            # Versuchen, eine gängige Schriftart zu laden. 
            # Passen Sie den Pfad für Ihr System an.
            # Windows: "arial.ttf", "calibri.ttf"
            # macOS/Linux: "Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
            font_path = "arial.ttf" 
            schriftart_klein = ImageFont.truetype(font_path, 25) # Schriftgröße 25
            schriftart_gross = ImageFont.truetype(font_path, 50) # Schriftgröße 50

        except IOError:
            print(f"Schriftart-Datei '{font_path}' nicht gefunden. Verwende Standard-Schriftart.")
            schriftart_klein = ImageFont.load_default()
            schriftart_gross = ImageFont.load_default()

        y_text_mitte = y_nach_linie1 + (quadrat_seite_px / 2)
        draw.text(
        (x2_quadrat + text_abstand_px, y_text_mitte),
        str(messgerät),
            fill='black',
            anchor='lm', # "left-middle"
            font=schriftart_klein
        )

        # 4. Zweite vertikale Linie unter dem Messgerät
        y_start_linie2 = y1_quadrat + linie2_start_abstand_px
        y_ende_linie2 = y1_quadrat + linie2_ende_abstand_px
        draw.line(
            [(x_pos, y_start_linie2), (x_pos, y_ende_linie2)],
            fill='black',
            width=2
        )