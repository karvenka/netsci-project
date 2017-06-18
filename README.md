# Correlation-based network for Equities
-----------------------

This script creates a correlation-based network for companies. It computes correlations using the closing stock prices .


### Dependencies

* [pandas](http://pandas.pydata.org/) <sup>[how to install](http://pandas.pydata.org/pandas-docs/stable/install.html)</sup>
* [networkx](http://networkx.lanl.gov/) <sup>[how to install](http://networkx.github.io/documentation/latest/install.html)</sup>
* [GraphViz](http://www.graphviz.org/) and [pygraphviz](http://networkx.lanl.gov/pygraphviz/index.html). In Ubuntu:
     `sudo apt-get install graphviz graphviz-dev;
     sudo pip install pygraphviz`
* An Internet access to fetch the stock data from [Yahoo Finance](http://finance.yahoo.com).

### How to run the script

    python cnetwork.py
 
### Using ipython notebook

The code was exported from [ipython notebook](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html). You can import it back.

First, [install](http://ipython.org/install.html) the notebook if needed. For Ubuntu:

    sudo apt-get install ipython-notebook

Run it with the options:

    ipython notebook --pylab=inline

You will see a prompt for importing files:

> To import a notebook, drag the file onto the listing below or click here. 

### References

A review paper on correlation-based financial networks:

Michele Tumminello, Fabrizio Lillo, Rosario N. Mantegna, [Correlation, hierarchies, and networks in financial markets](http://scholar.google.com/scholar?cluster=8884168592694206922&hl=en&as_sdt=0,5), _Journal of Economic Behavior and Organization_, Volume 75, Issue 1, July 2010, Pages 40-58.

__Keywords__: 
* Multivariate analysis
* Hierarchical clustering
* Correlation based networks
* Bootstrap validation
* Factor models
* Kullback–Leibler distance
