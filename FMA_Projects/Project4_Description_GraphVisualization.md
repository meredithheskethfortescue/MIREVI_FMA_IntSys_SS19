# Graphen-Visualisierung  (4 Punkte)

## Kurzbeschreibung

Zu erstellen ist ein Python-Programm, mit dem ein ungerichteter Graph erstellt und visualisiert werden kann. Auf diesen Graphen soll der [Dijkstra-Algorithmus](https://en.wikipedia.org/wiki/Dijkstra's_algorithm) angewendet werden. Als Gewichtungsfunktion kann die euklidische Distanz verwendet werden.

Minimale Anforderungen:

- Dem Graphen Knoten hinzuzufügen
- Knoten Koordinaten zuzuweisen
- Kanten hinzuzufügen
- Kanten zu gewichten
- Visualisierung des Graphen
  Knoten als Kreise oder Punkte; Kanten als Linien
- Schrittweise Visualisierung des Dijkstra-Algorithmus
  Entweder mit einem Plot pro schritt, oder mit einem sich aktualisierenden Plot (siehe Step-by-Step Visualisierung)

Optionale Features:

- GUI zum interaktiven Erzeugen des Graphen (z.B. mit Tkinter, PyQt oder PyQtGraph)
  oder parsen eines Kommandozeilenaufrufes (mit Pythons `argparse` Modul)
- Zufälliges Erstellen eines Graphen
- Nummerierung der Knoten; Beschriftung der Kantengewichte



## Hinweis zur Step-by-Step Visualisierung

Die simpelste und gebräuchlichste Bibliothek zur Visualisierung in Python ist `matplotlib`.
Matplotlib ist allerdings eher für die statische Visualisierung von Daten gedacht, weshalb das Updaten eines Frames relativ umständlich und inperformant ist. Deshalb hier der Code, um dies dennoch schnell bewerkstelligen zu können:

**ACHTUNG: Dieser Code funktioniert nicht mit dem Scientific Mode der PyCharm-Professional Version!**
In der Community Edition tritt dies nicht auf. In der Professional Edition muss unter `File >> Settings... >> Tools >> Python Scientific >> Show plots in tool window` der Haken entfernt werden.

```python
import random
import time
import matplotlib.pyplot as plt


def dijkstra():
    """Returns a random path"""
    path = [(random.randint(0, 10), random.randint(0, 10)),
            (random.randint(0, 10), random.randint(0, 10)),
            (random.randint(0, 10), random.randint(0, 10)),
            (random.randint(0, 10), random.randint(0, 10)),
            (random.randint(0, 10), random.randint(0, 10)),
            (random.randint(0, 10), random.randint(0, 10))]
    return path


if __name__ == '__main__':
    """Example of an updating plot with matplotlib"""
    
    path_initial = dijkstra()
    # set up plot window
    plt.ion()  # interactive mode on
    fig = plt.figure()  # get figure
    ax = fig.add_subplot(111)
    line, = ax.plot([v[0] for v in path_initial],
                    [v[1] for v in path_initial],
                    c='#AAAAAA')  # show window with initial frame

    while True:  # keep updating plot until aborted
        path_updated = dijkstra()  # get new path
        line.set_xdata([v[0] for v in path_updated])
        line.set_ydata([v[1] for v in path_updated])
        plt.draw()  # redraw plot
        fig.canvas.flush_events()
        time.sleep(1)  # wait

```

## Abgabe

Die Abgabe erfolgt in Form einer Kurzpräsentation am Ende der FMA-Übungen. Bestehen Sie bei einem Abgabetermin nicht, können Sie bei der nächsten Übung erneut eine Lösung einreichen. Bei der Kurzpräsentation sollen Sie Ihr Ergebnis vorzeigen und kurz erklären, wie Sie zu Ihrer Lösung gekommen sind. Durch kurze Nachfragen wird überprüft, ob Sie Ihre Arbeit selbst erstellt und verstanden haben. Bestehender Code (wie in der Vorlesung präsentiert) darf verwendet werden, Sie müssen diesen jedoch vollständig verstanden haben. Wurde die Aufgabe korrekt und vollständig erfüllt, gibt es die oben genannte Anzahl an Punkten. Es werden keine Teilpunkte vergeben: die Aufgabe wurde entweder bestanden oder nicht.