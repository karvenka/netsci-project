# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

## FOC-CRISIS school, 24-27 Oct 2012, Lucca
##
## Tutorial: Analysing financial networks in Python
## by Michelangelo Puliga (ETH Zurich)
##
## Homework by Olga Pustovalova
## PhD student in Computer Science, IMT Lucca
## olga.pustovalova@imtlucca.it
##
## http://nbviewer.ipython.org/3950921/

# <codecell>

# Create a correlation-based network for 30 Dow Jones companies.
# Compute correlations using the closing stock prices for each of 30 companies.

# <codecell>

## Preliminary arrangements: which companies and dates to choose?

# UNH replaced KFT on 24 Sep 2012; the first change since 2009.
# http://www.bloomberg.com/news/2012-09-14/unitedhealth-replaces-kraft-in-
# dow-jones-industrial-average-1-.html
# =>
# We can take the data e.g. from 01 Jan 2010 to 23 Sep 2012,
# when the Dow Jones companies stayed the same

# <codecell>

# Dow Jones companies
companies = ['MMM', 'AA', 'AXP', 'T', 'BAC',
             'BA', 'CAT', 'CVX', 'CSCO', 'DD',
             'XOM', 'GE', 'HPQ', 'HD', 'INTC',
             'IBM', 'JNJ', 'JPM', 'MDC', 'MRK',
             'MSFT', 'PFE', 'PG', 'KO', 'TRV',
             'UTX', 'VZ', 'WMT', 'DIS', 'KFT']

# <codecell>

## Download the data

from pandas.io.data import *

data = dict()
for i in companies:
    raw_data = DataReader(i, 'yahoo', start='01/01/2009', end='23/09/2012')
    data[i] = raw_data['Close']  # we need closing prices only

# <codecell>

## A quick visualization: stock prices for each Dow Jones company

import pylab
import random as rn

colors = 'bcgmry'
rn.seed = len(companies)  # for choosing random colors
pylab.subplot('111')  # all time series on a single figure

for i in companies:
    data[i].plot(style=colors[rn.randint(0, len(colors) - 1)])
pylab.show()

# <codecell>

## Compute correlation matrix

import numpy as np
n = len(companies)
corr_matrix = np.zeros((n, n))

for i in range(0, n):
    for j in range(0, n):
        if i < j:
            corr_matrix[i][j] = data[companies[i]].corr(
                                                    data[companies[j]],
                                                    method='pearson')

# Output
np.set_printoptions(precision=2)
print corr_matrix[0]

# <codecell>

## Remove weak correlations to construct a graph
threshold = 0.7
corr_matrix[np.where(abs(corr_matrix) < threshold)] = 0

# Output
print corr_matrix[0]

# <codecell>

# Constructing a graph
import networkx as nx
G = nx.Graph(corr_matrix)

# <codecell>

## Explore graph properties

nodes, edges = G.order(), G.size()
print "Number of nodes:", nodes
print "Number of edges:", edges
print "Average degree:", edges / float(nodes)

# <codecell>

## Count degrees

degrees = G.degree()
values = sorted(set(degrees.values()))
counts = [degrees.values().count(x) for x in values]

# <codecell>

# Connected components: color them differently

rn.seed = 5  # for choosing random colors
components = nx.connected_components(G)

for i in components:
    component = G.subgraph(i)
    nx.draw_graphviz(component,
        node_color = colors[rn.randint(0, len(colors) - 1)],
        node_size = [component.degree(i) * 100 + 15
                     for i in component.nodes()],
        edge_color = [corr_matrix[i][j] * 0.5
                      for (i, j) in component.edges()],
        with_labels = True,
        labels = dict([(x, companies[x]) for x in component.nodes()])
        )
pylab.show()

print "Smallest components (size < 5):"
for i in components:
    if len(i) < 5:
        print [companies[j] for j in i]

print "Companies with degrees < 5:"
print [(companies[i], degrees[i]) for i in range(0, n) if degrees[i] < 5]

# <codecell>

# Generate colors -
# http://stackoverflow.com/questions/876853/generating-
# color-ranges-in-python

import colorsys
ncolors = len(values)
HSV_tuples = [(x * 1.0 / ncolors, 0.5, 0.5) for x in range(ncolors)]
RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)

# <codecell>

# Plot degree distribution
pylab.xlabel('Degree')
pylab.ylabel('Number of nodes')
pylab.title('Dow Jones network: degree distribution')
pylab.bar(values, counts, color=RGB_tuples)
pylab.show()

print "Highest degree:", max(values)

