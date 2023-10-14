"""
File: my_drawing.py
Name: Sunny
----------------------
This program draws a cat in the shower.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    This program prints out a cat in the shower.
    Wish you a nice day!
    """
    window = GWindow(width=800, height=500, title='ShowerCat')

    bg = GRect(width=800,height=500)
    bg.filled = True
    bg.color = 'antiquewhite'
    bg.fill_color = 'antiquewhite'
    window.add(bg)

    face = GOval(width=150, height=140, x=300, y=200)
    face.filled = True
    face.color = 'darkorange'
    face.fill_color = 'darkorange'
    window.add(face)

    face2 = GOval(width=190, height=100, x=280, y=240)
    face2.filled = True
    face2.color = 'darkorange'
    face2.fill_color = 'darkorange'
    window.add(face2)

    body = GOval(width=140, height=120, x=300, y=300)
    body.filled = True
    body.color = 'darkorange'
    body.fill_color = 'darkorange'
    window.add(body)


    ear1 = GPolygon()
    ear1.add_vertex((350,170))
    ear1.add_vertex((320,275))
    ear1.add_vertex((380,275))
    ear1.filled = True
    ear1.color ='darkorange'
    ear1.fill_color = 'darkorange'
    window.add(ear1)

    ear2 = GPolygon()
    ear2.add_vertex((400, 170))
    ear2.add_vertex((370, 275))
    ear2.add_vertex((430, 275))
    ear2.filled = True
    ear2.color = 'darkorange'
    ear2.fill_color = 'darkorange'
    window.add(ear2)

    eye1 = GOval(width=15, height=20, x=340, y=240)
    eye1.filled = True
    eye1.fill_color = 'black'
    window.add(eye1)
    eye2 = GOval(width=15, height=20, x=390, y=240)
    eye2.filled = True
    eye2.fill_color = 'black'
    window.add(eye2)

    nose1= GPolygon()
    nose1.add_vertex((365,270))
    nose1.add_vertex((380,270))
    nose1.add_vertex((372,280))
    nose1.filled = True
    nose1.fill_color = 'black'
    window.add(nose1)

    soap1 = GOval(width=30, height=30)
    soap1.filled = True
    soap1.fill_color = 'skyblue'
    soap1.color = 'skyblue'
    window.add(soap1, x=280, y=320)

    soap2 = GOval(width=30, height=30)
    soap2.filled = True
    soap2.fill_color = 'skyblue'
    soap2.color = 'skyblue'
    window.add(soap2, x=260, y=310)

    soap3 = GOval(width=50, height=30)
    soap3.filled = True
    soap3.fill_color = 'skyblue'
    soap3.color = 'skyblue'
    window.add(soap3, x=300, y=310)

    soap4 = GOval(width=48, height=35)
    soap4.filled = True
    soap4.fill_color = 'skyblue'
    soap4.color = 'skyblue'
    window.add(soap4, x=340, y=315)

    soap6 = GOval(width=33, height=30)
    soap6.filled = True
    soap6.fill_color = 'skyblue'
    soap6.color = 'skyblue'
    window.add(soap6, x=384, y=310)

    soap5 = GOval(width=33, height=30)
    soap5.filled = True
    soap5.fill_color = 'skyblue'
    soap5.color = 'skyblue'
    window.add(soap5, x=315, y=320)

    soap7 = GOval(width=40, height=40)
    soap7.filled = True
    soap7.fill_color = 'skyblue'
    soap7.color = 'skyblue'
    window.add(soap7, x=410, y=310)

    soap8 = GOval(width=40, height=40)
    soap8.filled = True
    soap8.fill_color = 'skyblue'
    soap8.color = 'skyblue'
    window.add(soap8, x=445, y=330)

    tub = GPolygon()
    tub.add_vertex((280,350))
    tub.add_vertex((300, 420))
    tub.add_vertex((460, 420))
    tub.add_vertex((489,350))
    tub.filled = True
    tub.fill_color = 'white'
    tub.color = 'white'
    window.add(tub)

    tub1 = GOval(width=160, height=40, x=300, y=400)
    tub1.filled = True
    tub1.fill_color = 'white'
    tub1.color = 'white'
    window.add(tub1)

    tub2 = GRect(width=10, height=290, x=475, y=60)
    tub2.filled = True
    tub2.fill_color = 'white'
    tub2.color = 'white'
    window.add(tub2)

    tub3 = GPolygon()
    tub3.add_vertex((475,60))
    tub3.add_vertex((430,80))
    tub3.add_vertex((470,100))
    tub3.filled = True
    tub3.fill_color = 'white'
    tub3.color = 'white'
    window.add(tub3)

    drop = GArc(35,40,40,80)
    drop.filled = True
    drop.fill_color = 'skyblue'
    drop.color = 'skyblue'
    window.add(drop, x=400, y=150)

    drop1 = GArc(35, 40, 40, 80)
    drop1.filled = True
    drop1.fill_color = 'skyblue'
    drop1.color = 'skyblue'
    window.add(drop1, x=420, y=130)

    drop3 = GArc(35, 40, 40, 80)
    drop3.filled = True
    drop3.fill_color = 'skyblue'
    drop3.color = 'skyblue'
    window.add(drop3, x=415, y=100)

    soap11 = GOval(width=30, height=30)
    soap11.filled = True
    soap11.fill_color = 'antiquewhite'
    soap11.color = 'skyblue'
    window.add(soap11, x=280, y=200)

    soap12 = GOval(width=25, height=25)
    soap12.filled = True
    soap12.fill_color = 'antiquewhite'
    soap12.color = 'skyblue'
    window.add(soap12, x=270, y=170)

    label1 = GLabel('HAVE', x=80, y=150)
    label1.filled = True
    label1.font = '-40'
    label1.fill_color = 'black'
    label1.color = 'brown'
    window.add(label1)
    label2 = GLabel('A', x=80, y=200)
    label2.filled = True
    label2.font = '-40'
    label2.fill_color = 'black'
    label2.color = 'indianred'
    window.add(label2)
    label3 = GLabel('NICE', x=80, y=250)
    label3.filled = True
    label3.font = '-40'
    label3.fill_color = 'black'
    label3.color = 'lightcoral'
    window.add(label3)
    label4 = GLabel('DAY', x=80, y=300)
    label4.filled = True
    label4.font = '-40'
    label4.fill_color = 'black'
    label4.color = 'rosybrown'
    window.add(label4)


if __name__ == '__main__':
    main()
