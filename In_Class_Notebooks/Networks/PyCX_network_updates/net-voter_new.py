# Simple Network Dynamics simulator in Python
#
# *** The Voter Model of Opinion Formation on a Network ***
#
# Copyright 2010-2013 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import networkx as NX
import random as RD
import pylab as PL

n = 100
p = 0.1
k = 4

def init():
    global g, positions

    g = NX.erdos_renyi_graph(n, p)
    for nd in g.nodes():
        g.node[nd]['state'] = RD.choice(range(k))
    positions = NX.spring_layout(g)

def draw():
    PL.cla()
    NX.draw(g, with_labels = False, pos = positions,
            node_color = [g.node[n]['state'] for n in g.nodes()],
            vmin = 0, vmax = k - 1, cmap = PL.cm.jet)

def step():
    global g
    listener = RD.choice(list(g.nodes()))
    if list(g.neighbors(listener)) != []:
        speaker = RD.choice(list(g.neighbors(listener)))
        g.node[listener]['state'] = g.node[speaker]['state']
    
import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
