from pyx import *
import math
unit.set(xscale=2)
text.set(mode="latex")
text.preamble(r"\usepackage{amsmath}")

# plot d'une fonction definie par utilisateur
def f(x):                     
    return x*x
plotobj = g.plot(graph.data.function("y(x)=f(x)", min=0, max=10, context={"f":f}))

# plot d'une fonction interne avec echelle log, attention intervalle doit etre
# renseigne pour echelle log et doit etre correct sinon rien n'est trace
g = graph.graphxy(width=8,
                  x=graph.axis.log(min=1e-1, max=1e4),
                  y=graph.axis.lin(max=5))
g.plot(graph.data.function("y(x)=tan(log(1/x))**2"))

# barres d'erreur
g.plot(graph.data.file("errorbar.dat", x=1, y=2, dy=3),
       [graph.style.symbol(), graph.style.errorbar()])

#necessaire pour orienter texte
pg = graph.axis.painter.regular(titlepos=0.5, titledirection=None) 
g = graph.graphxy(width=10*unit.u_cm,
                  x=graph.axis.linear(title="\Large f",painter=pg),
          y=graph.axis.linear(title="$\Large \Delta \mu$",painter=pg))

#plot d'un fichier de donnees
d=g.plot(graph.data.file("fig1_1.txt",x=1,y=2),
styles=[graph.style.line([color.rgb.black,style.linestyle.solid,style.linewidth.thick])])

#ex manipulation donnes d'un fichier affichees avec symboles pleins (filled)
# ou vides (stroked) ou en ligne-points
g.plot(graph.data.file("varN",x="($3)",y="(($1)-($2))/($1)"),
       styles=[graph.style.symbol(graph.style.symbol.circle, size=0.1,
                symbolattrs=[color.rgb.black,deco.filled])])
       styles=[graph.style.line([color.rgb.black,
                                 style.linestyle.solid,
                                 style.linewidth.thick]),
               graph.style.symbol(symbolattrs=[color.rgb.black])])

#ex de fct parametrique
g.plot(graph.data.paramfunction("k", -10, 10,     
                                "x, y = k, 0",
                                context=locals()),
       styles=[graph.style.line([color.rgb.black,
                                 style.linestyle.solid,
                                 style.linewidth.thick])])

g.finish()

# --------------hachure speciales -----------------------------
p = d.path # the path is available after the graph is finished

pa = g.ygridpath(-8)
pb = g.ygridpath(15)
pc = g.xgridpath(0)
# g.stroke(pa + pb + pc, [color.rgb.red]) # pour visualiser les lignes droites
(splita,), (splitpa,) = p.intersect(pa)
(splitb,), (splitpb,) = p.intersect(pb)
(splitc,), (splitpc,) = p.intersect(pc)
(splitpcpa,), (splitpapc,) = pc.intersect(pa)
(splitpcpb,), (splitpbpc,) = pc.intersect(pb)

area1 = (pa.split([splitpapc,splitpa])[1] << # << colle les differentes regions
        p.split([splita, splitc])[1])
area1.append(path.closepath())
g.stroke(area1, [deco.filled([color.gray(0.7)])])

pos = g.pos(-7,17) # en coor du graph sinon (1,2) pour coor direct (cm)
g.text(pos[0], pos[1], r"\Large v=0")

# ----------------inset------------------------------------
g2 = g.insert(graph.graphxy(width=3*unit.u_cm,xpos=5.5,ypos=1.2,
                  x=graph.axis.linear(min=-7,max=0,title="$f$"),
          y=graph.axis.linear(min=0,max=880,title="$v$, 2mM ATP"),
                  y2=graph.axis.linear(min=0,max=88,title="$v$, 5$\mu$M ATP")))

g2.plot(graph.data.file("fig4_1.txt",x=1,y="($2)*4.1"),styles=[graph.style.symbol(
                            graph.style.symbol.circle, size=0.1,
                                  symbolattrs=[color.rgb.black,deco.filled])])

g.writeEPSfile("fig1", paperformat=document.paperformat.A4)
g.writePDFfile("axis")
