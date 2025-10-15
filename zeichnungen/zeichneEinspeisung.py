from reportlab.lib.units import mm

def zeichne_eine_Einspeisung(c, breite, y_start, anzahl,messgerät):
    # Zeichne eine Einspeisung an der gegebenen Position
    quadrat_seite = 5*mm
    x_start = breite  # Zentriert auf der Seite
    #c.setStrokeColorRGB(0, 0, 0)  # Blau für Einspeisung
    c.setLineWidth(2)

    breite = breite / (anzahl + 1)

    for i in range(anzahl):
        x_start = breite * (i + 1)
        c.line(x_start, y_start, x_start, y_start-25*mm)  # Vertikale Linie
        y_Mess = y_start - 25*mm
        c.rect(x_start - quadrat_seite/2, y_Mess - quadrat_seite, quadrat_seite, quadrat_seite)  # Quadrat am Ende
        c.drawString(x_start + quadrat_seite, y_Mess - quadrat_seite/2, f"{messgerät}")
        c.line(x_start, y_Mess-5*mm, x_start, y_Mess-30*mm)  # Vertikale Linie
    