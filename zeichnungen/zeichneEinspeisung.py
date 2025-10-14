from reportlab.lib.units import mm

def zeichne_eine_Einspeisung(c, breite, y_start, nummer):
    # Zeichne eine Einspeisung an der gegebenen Position
    quadrat_seite = 5*mm
    x_start = breite  # Zentriert auf der Seite
    c.setStrokeColorRGB(0, 0, 1)  # Blau für Einspeisung
    c.setLineWidth(2)
    c.line(x_start, y_start, x_start, y_start-50*mm)  # Vertikale Linie
    y_ende = y_start - 50*mm

    c.rect(x_start - quadrat_seite/2, y_ende - quadrat_seite, quadrat_seite, quadrat_seite)  # Quadrat am Ende

    c.drawString(x_start + quadrat_seite, y_ende - quadrat_seite/2, f"Einspeisung {nummer}")