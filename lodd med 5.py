# -*- coding: cp1252 -*-
# Et program for å trekke tilfeldige lodd

from random import *
from graphics import *

options = open("options.cfg", "r+")
valg = options.readlines()
valg = [eval(x) for x in valg]
options.close()
# valg = [xmax, ymax, årefra, åretil, bøker, loddperbok, laveste, fem?]
# vil inkl. en ekstra linje i filen

class Bok:

    def __init__(self, win):
        self.trukket = []
        self.fra = 1
        self.til = valg[4] + 1 # antall bøker
        self.win = win
        self.rekke = -1
        self.fil = open("trekt_bok.txt","a")

        self.head = Text(Point(0.1, 1), "Loddbøker")
        self.head.setStyle("bold")
        self.head.setTextColor(color_rgb(21,71,9))
        self.head.setSize(26)
        self.head.draw(win)

        self.boktekst = Text(Point(0.2, 0.8), " Bok: ")
        self.loddtekst = Text(Point(0.2, 0.7), "Lodd: ")
        self.boktekst.setSize(36)
        self.loddtekst.setSize(36)
        self.boktekst.draw(win)
        self.loddtekst.draw(win)

        self.displaytekst = Text(Point(0.5, 0.5), "")
        self.displaytekst.setSize(50)
        self.displaytekst.draw(win)

        self.entry = Entry(Point(0.1, 0.1), 15)
        self.entry.setFill("light grey")
        self.entry.setTextColor("dark grey")
        self.entry.draw(win)

    def __del__(self):
        self.fil.close()
    
    def trekk(self):
        self.displaytekst.setText("")
        lodd = [randrange(self.fra, self.til), randrange(1,valg[5])]

        # Er loddet gyldig? Nei -> finn gyldig
        if len(self.trukket) >= 500*(self.til - self.fra):
                return False
        while lodd in self.trukket:
            lodd = [randrange(self.fra, self.til), randrange(1,valg[5])]

        # Nå har vi funnet gyldig lodd
        self.trukket.append(lodd)
        self.fil.write("bok: %d, lodd: %d\n" % (lodd[0], lodd[1]))
        return lodd

    def forrige(self):
        self.displaytekst.setText("")
        self.rekke -= 1
        try:
            return self.trukket[self.rekke]
        except:
            self.rekke += 1
            return False

    def neste(self):
        self.displaytekst.setText("")
        self.rekke += 1
        try:
            return self.trukket[self.rekke]
        except:
            self.rekke -= 1
            return False

    def oppdater(self, a):
        if type(a) == type("a"):
            self.loddtekst.setText("Feil!")
            self.boktekst.undraw()
            
        self.boktekst.setText(" Bok: %2d" % a[0])
        self.loddtekst.setText("Lodd: %3d" % a[1])

    def navn(self):
        navn = self.entry.getText()
        self.displaytekst.setText(navn)
        self.entry.setText("")
        
class Are:

    def __init__(self, win):
        self.win = win
        self.fra = valg[2]
        self.til = valg[3] + 1
        self.trukket = []
        self.fil = open("trekt_are.txt", "a")

        self.head = Text(Point(0.1, 1), "ÅRESALG")
        self.head.setStyle("bold")
        self.head.setTextColor(color_rgb(21,71,9))
        self.head.setSize(26)
        self.head.draw(win)

##        self.vinnernr = Text(Point(0.3, 0.87), "")
##        self.vinnernr.setSize(30)
##        self.vinnernr.draw(win)

        if valg[7]: # fem lodd/åre
            self.text1 = Text(Point(0.37, 0.51), "")
            self.text1.setSize(27)
            self.text1.setStyle("bold")
            self.text1.setTextColor(color_rgb(21,71,9))
            self.text1.draw(win)

        else:
            self.text1 = Text(Point(0.35, 0.56), "")
            self.text1.setSize(26)
            self.text1.setStyle("bold")
            self.text1.setTextColor(color_rgb(21,71,9))
            self.text1.draw(win)

        self.text2 = Text(Point(0.35, 0.44), "")
        self.text2.setSize(26)
        self.text2.setStyle("bold")
        self.text2.setTextColor(color_rgb(21,71,9))
        self.text2.draw(win)

        self.hovedtall = Text(Point(0.48, 0.8), "")
        self.hovedtall.setSize(100)
        self.hovedtall.setFace("times roman")
        self.hovedtall.draw(win)
       

        self.logo = Image(Point(0.98, 0.86), "HML_logo_Farge2.gif")
        self.logo.draw(win)

        # for å gå tilbake til tidligere lodd
        self.rekke = -1

    def __del__(self):
        self.fil.close()

##    def activate_vinnernr(self):
##        self.vinnernr.setText("vinnernr: ")

    def undraw(self):
        self.head.undraw()
        self.text1.undraw()
        self.text2.undraw()
        self.hovedtall.undraw()
    
    def trekk(self):
        self.rekke = -1
        lodd = randrange(self.fra, self.til)

        if valg[6]: # 1 -> 10, tror det er denne
            if not lodd % 10:
                lower = lodd - 9
                higher = lodd
            lower = lodd - lodd % 10 + 1
            higher = lodd - lodd % 10 + 10
        else: # 0 - 9
            lower = lodd - lodd % 10
            higher = lodd - lodd % 10 + 9
            
        while lodd in self.trukket:
            lodd = randrange(self.fra, self.til)
            # 20 % lavere for hver åre som er trukket
            for i in trukket:
                if lower < i < higher:
                    if 0.8 < random:
                        lodd = trukket[0] # da kjører vi på nytt
                        
            if len(self.trukket) == (self.til - self.fra):
                # tom for lodd
                return False

        self.trukket.append(lodd)
        self.fil.write("Åre: %d\n" % (lodd))
        return lodd

    def forrige(self):
        self.rekke -= 1
        try:
            return self.trukket[self.rekke]
        except:
            self.rekke += 1
            return False

    def neste(self):
        self.rekke += 1
        try:
            return self.trukket[self.rekke]
        except:
            self.rekke -= 1
            return False

    def oppdater(self, a):
        # a = 5463, 124, ...
        if type(a) == type("a"):
            self.hovedtall.setText(a)
            return True

        if valg[7]: # fem lodd/åre
            if valg[6]: # 1 -> 5
                if a%10:
                    b = a%10
                else:
                    b = a%10+5
                if a%10 < 6:
                    tall1 = range(a-b+1, a+6-b)
                else:
                    tall1 = range(a-b+6, a-b+11)
                #tall2 = range(a-b+6, a-b+11)
            else: # 0 -> 4
                b = a%10
                if a%10 < 5:
                    tall1 = range(a-b, a-b+5)
                else:
                    tall1 = range(a-b+5, a-b+10)
                #tall2 = range(a-b+5, a-b+10)

            tall1 = ["%5s" % str(x) for x in tall1]
            #tall2 = ["%5s" % str(x) for x in tall2]


            self.text1.setText("   ".join(tall1))
            #self.text2.setText("   ".join(tall2))



        else: # 10 lodd/åre
            if not valg[6]: # 1 -> 10
                if a%10:
                    b = a%10
                else:
                    b = a%10+10
                tall1 = range(a-b+1, a+6-b)
                tall2 = range(a-b+6, a-b+11)
            else: # 0 -> 9
                b = a%10
                tall1 = range(a-b, a-b+5)
                tall2 = range(a-b+5, a-b+10)

            tall1 = ["%5s" % str(x) for x in tall1]
            tall2 = ["%5s" % str(x) for x in tall2]

            self.text1.setText("   ".join(tall1))
            self.text2.setText("   ".join(tall2))

        self.hovedtall.setText(str(a))
        

    def reset(self):
        self.trukket = []
        

def main():
    # print "Velkommen til lodd."
    xmax = valg[0]
    ymax = valg[1]
    win = GraphWin("Lodd", xmax, ymax)
    win.setCoords(0.0, 0.0, 1.1, 1.05)

    are = Image(Point(0.5, 0.5), "are-medium.gif")
    are.draw(win)
    
    buttons = draw_partial_screen(win)

    lodd = Are(win)

    while True:
        mus = checkmouse(win, buttons)
        if mus == 1:
            # nytt lodd
##            lodd.activate_vinnernr()
            vinner = lodd.trekk()
            if vinner: lodd.oppdater(vinner)
            else:
                lodd.oppdater("TOMT")
        elif mus == 2:
            # Forrige lodd
            vinner = lodd.forrige()
            if vinner: lodd.oppdater(vinner)
        elif mus == 3:
            vinner = lodd.neste()
            if vinner: lodd.oppdater(vinner)
        elif mus == 4:
            are.undraw()
            lodd.undraw()
            loddbok(win, buttons)
        elif mus == 5:
            win.close()
            return 0

def loddbok(win, buttons):
    lodd = Bok(win)
    g = True
    
    while g:
        mus = checkmouse(win, buttons)
        if mus == 1:
            vinner = lodd.trekk()
            if vinner: lodd.oppdater(vinner)
            else:
                lodd.oppdater("TOMT")
        elif mus == 2:
            vinner = lodd.forrige()
            if vinner: lodd.oppdater(vinner)
        elif mus == 3:
            vinner = lodd.neste()
            if vinner: lodd.oppdater(vinner)
        elif mus == 4:
            win.close()
            main()
        elif mus == 5:
            win.close()
            return 0
        else:
            lodd.navn()
    
def draw_partial_screen(win):

    fyll = Rectangle(Point(0.0, 0.0), Point(1.1, 0.06))
    fyll.setFill("light grey")
    fyll.setWidth(0)
    fyll.draw(win)
    
    buttons = [False]*5
    button_text = [False]*5
    labels = ["Nytt lodd", "Forrige lodd", "Neste lodd", "Modus", "Avslutt"]
    for i in range(5):
        buttons[i] = Rectangle(Point(0.09+0.2*i,0.0), Point(0.25 + 0.2*i, 0.05))
        buttons[i].setWidth(0)
        buttons[i].setOutline("light gray")
        buttons[i].draw(win)

        button_text[i] = Text(Point(0.17 + 0.2*i, 0.025), labels[i])
        button_text[i].setTextColor("dark grey")
        button_text[i].setSize(18)
        button_text[i].draw(win)
        
    return buttons

def checkmouse(win, buttons):
    p = win.getMouse()
    p = [p.getX(), p.getY()]
    b = []
    for i in buttons:
        b.append([i.getP1(), i.getP2()])
    b = [[[x[0].getX(), x[0].getY()], [x[1].getX(), x[1].getY()]] for x in b]

    i = 1
    for each in b:
        if (each[0][0] < p[0] < each[1][0]) and \
                (each[0][1] < p[1] < each[1][1]):
            return i
        i += 1
    return False
    
main()
