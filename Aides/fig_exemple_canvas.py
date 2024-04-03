from pyx import *
import math
text.set(mode="latex")
text.preamble(r"\usepackage{amsmath}")
unit.set(xscale=1.6)

def arrows(x0, y0, x1, y1, text1, text2, dist, short, tdist1, tdist2):
    length = ((x1-x0)**2 + (y1-y0)**2)**0.5
    c = canvas.canvas()
    p1 = path.line(0+short, 0.5*dist, length-short, 0.5*dist)
    p2 = path.line(length-short, -0.5*dist, 0+short, -0.5*dist)
    angle = math.degrees(math.atan2(y1-y0, x1-x0))
    p1 = p1.transformed(trafo.translate(x0, y0)*trafo.rotate(angle))  
    p2 = p2.transformed(trafo.translate(x0, y0)*trafo.rotate(angle))
# transf is applied from the right
    c.stroke(p1, [deco.earrow.normal])
    c.stroke(p2, [deco.earrow.normal])
    pos = p1.trafo(0.5*p1.arclen()).apply(0, tdist1)
    c.text(pos[0], pos[1], text1, [text.halign.center, text.vshift.mathaxis])
    pos = p2.trafo(0.5*p2.arclen()).apply(0,tdist2)
    c.text(pos[0], pos[1], text2, [text.halign.center, text.vshift.mathaxis])
# horizontal alignment + vshift on mathaxis
    return c

def point(x, y, atext):
    c = canvas.canvas()
    c.text(x, y, atext, [text.halign.center, text.vshift.mathaxis])
    r = 0.22
    c.stroke(path.circle(x, y, r))
    return c

def tick(x, y, atext):
    c = canvas.canvas()
    c.text(x, y-0.4, atext, [text.halign.center, text.vshift.mathaxis])
    t=0.1 #largueur trait sur axe
    c.stroke(path.line(x,y-t,x,y+t))
    return c

def tick2(x, y, atext,tdist):
    c = canvas.canvas()
    c.text(x-0.4-tdist, y, atext, [text.halign.center, text.vshift.mathaxis])
    t=0.1 #largueur trait sur axe
    c.stroke(path.line(x-t,y,x+t,y))
    return c



# intial coordinates
x0=0
y0=0
p=3 #period

c = canvas.canvas()
c.stroke(path.line(x0-0.5*p,y0-0.5*p,x0+4.5*p,y0-0.5*p), [deco.earrow.normal])
c.insert(tick(x0,y0-0.5*p,"$-1$"))
c.insert(tick(x0+p,y0-0.5*p,"$0$"))
c.insert(tick(x0+2*p,y0-0.5*p,"$1$"))
c.text(x0+2*p,y0-0.5*p-p/2-0.1,"\Large n")
c.insert(tick(x0+3*p,y0-0.5*p,"$2$"))
c.insert(tick(x0+4*p,y0-0.5*p,"$3$"))

c.stroke(path.line(x0-0.5*p,y0-0.5*p,x0-0.5*p,y0+1.5*p), [deco.earrow.normal])
#c.insert(tick2(x0-0.5*p,y0-p,"$-1$",0.1))
c.insert(tick2(x0-0.5*p,y0,"$ 0$",-0.1))
c.insert(tick2(x0-0.5*p,y0+p,"$ 1$",-0.1))
c.text(x0-0.5*p-p/2,y0+p+0.2,"\Large y")

c.insert(point(x0, y0, "$b$"))
c.insert(point(x0+p, y0, "$a$"))
c.insert(point(x0+2*p, y0, "$b$"))
c.insert(point(x0+3*p, y0, "$a$"))
c.insert(point(x0+4*p, y0, "$b$"))

c.insert(point(x0+p, y0+p, "$a$"))
c.insert(point(x0+2*p, y0+p, "$b$"))
c.insert(point(x0+3*p, y0+p, "$a$"))

c.insert(point(x0+4*p, y0+p, "$b$"))
c.insert(point(x0, y0+p, "$b$"))
#c.insert(point(x0+3*p, y0-p, "$a$"))

c.insert(arrows(x0,y0,x0+p,y0, r"$\overrightarrow{\omega_b}^0$",
                r"$\overleftarrow{\omega_a}^0$", 0.15, 0.25, 0.4, 0.5))
c.insert(arrows(x0+p,y0,x0+2*p,y0, r"",
                r"", 0.15, 0.25, 0.4,0.5))
c.insert(arrows(x0+2*p,y0,x0+3*p,y0, r"",
                r"", 0.15, 0.25, 0.4, 0.5))
c.insert(arrows(x0+3*p,y0,x0+4*p,y0, r"$\overrightarrow{\omega_a}^0$",
                r"$\overleftarrow{\omega_b}^0$", 0.15, 0.25, 0.4,0.5))
c.insert(arrows(x0+p,y0,x0+2*p,y0+p, r"$\overrightarrow{\omega_a}^1$",
                r"$\overleftarrow{\omega_b}^{-1}$", 0.15, 0.25, 0.4,0.6))
#c.insert(arrows(x0+p,y0,x0+2*p,y0-p, r"$\overrightarrow{\omega_a}^{-1}$",
#                r"$\overleftarrow{\omega_b}^1$", 0.15, 0.25, 0.55,0.55))
c.insert(arrows(x0+2*p+0.1,y0+p-0.1,x0+3*p,y0, r"$\overrightarrow{\omega_b}^{-1}$",
                r"$\overleftarrow{\omega_a}^1$", 0.15, 0.25, 0.55,0.55))
#c.insert(arrows(x0+2*p,y0-p,x0+3*p,y0, r"$\overrightarrow{\omega_b}^1$",
#                r"$\overleftarrow{\omega_a}^{-1}$", 0.15, 0.25, 0.35,0.7))

c.writeEPSfile("fig0", paperformat=document.paperformat.A4)


