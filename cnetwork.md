<div class="highlight"><pre><span class="c">## FOC-CRISIS school, 24-27 Oct 2012, Lucca</span>
<span class="c">##</span>
<span class="c">## Tutorial: Analysing financial networks in Python</span>
<span class="c">## by Michelangelo Puliga (ETH Zurich)</span>
<span class="c">##</span>
<span class="c">## http://nbviewer.ipython.org/3950921/</span>
</pre></div>



<div class="highlight"><pre><span class="c">## Preliminary arrangements: which companies and dates to choose?</span>

<span class="c"># UNH replaced KFT on 24 Sep 2012; the first change since 2009.</span>
<span class="c"># http://www.bloomberg.com/news/2012-09-14/unitedhealth-replaces-kraft-in-</span>
<span class="c"># dow-jones-industrial-average-1-.html</span>
<span class="c"># =&gt;</span>
<span class="c"># We can take the data e.g. from 01 Jan 2010 to 23 Sep 2012,</span>
<span class="c"># when the Dow Jones companies stayed the same</span>
</pre></div>



<div class="highlight"><pre><span class="c"># Dow Jones companies</span>
<span class="n">companies</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;MMM&#39;</span><span class="p">,</span> <span class="s">&#39;AA&#39;</span><span class="p">,</span> <span class="s">&#39;AXP&#39;</span><span class="p">,</span> <span class="s">&#39;T&#39;</span><span class="p">,</span> <span class="s">&#39;BAC&#39;</span><span class="p">,</span>
             <span class="s">&#39;BA&#39;</span><span class="p">,</span> <span class="s">&#39;CAT&#39;</span><span class="p">,</span> <span class="s">&#39;CVX&#39;</span><span class="p">,</span> <span class="s">&#39;CSCO&#39;</span><span class="p">,</span> <span class="s">&#39;DD&#39;</span><span class="p">,</span>
             <span class="s">&#39;XOM&#39;</span><span class="p">,</span> <span class="s">&#39;GE&#39;</span><span class="p">,</span> <span class="s">&#39;HPQ&#39;</span><span class="p">,</span> <span class="s">&#39;HD&#39;</span><span class="p">,</span> <span class="s">&#39;INTC&#39;</span><span class="p">,</span>
             <span class="s">&#39;IBM&#39;</span><span class="p">,</span> <span class="s">&#39;JNJ&#39;</span><span class="p">,</span> <span class="s">&#39;JPM&#39;</span><span class="p">,</span> <span class="s">&#39;MDC&#39;</span><span class="p">,</span> <span class="s">&#39;MRK&#39;</span><span class="p">,</span>
             <span class="s">&#39;MSFT&#39;</span><span class="p">,</span> <span class="s">&#39;PFE&#39;</span><span class="p">,</span> <span class="s">&#39;PG&#39;</span><span class="p">,</span> <span class="s">&#39;KO&#39;</span><span class="p">,</span> <span class="s">&#39;TRV&#39;</span><span class="p">,</span>
             <span class="s">&#39;UTX&#39;</span><span class="p">,</span> <span class="s">&#39;VZ&#39;</span><span class="p">,</span> <span class="s">&#39;WMT&#39;</span><span class="p">,</span> <span class="s">&#39;DIS&#39;</span><span class="p">,</span> <span class="s">&#39;KFT&#39;</span><span class="p">]</span>
</pre></div>



<div class="highlight"><pre><span class="c">## Download the data</span>

<span class="kn">from</span> <span class="nn">pandas.io.data</span> <span class="kn">import</span> <span class="o">*</span>

<span class="n">data</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">companies</span><span class="p">:</span>
    <span class="n">raw_data</span> <span class="o">=</span> <span class="n">DataReader</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="s">&#39;yahoo&#39;</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="s">&#39;01/01/2009&#39;</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s">&#39;23/09/2012&#39;</span><span class="p">)</span>
    <span class="n">data</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">raw_data</span><span class="p">[</span><span class="s">&#39;Close&#39;</span><span class="p">]</span>  <span class="c"># we need closing prices only</span>
</pre></div>



<div class="highlight"><pre><span class="c">## A quick visualization</span>

<span class="kn">import</span> <span class="nn">pylab</span>
<span class="kn">import</span> <span class="nn">random</span> <span class="kn">as</span> <span class="nn">rn</span>

<span class="n">colors</span> <span class="o">=</span> <span class="s">&#39;bcgmry&#39;</span>
<span class="n">rn</span><span class="o">.</span><span class="n">seed</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">companies</span><span class="p">)</span>  <span class="c"># for choosing random colors</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="s">&#39;111&#39;</span><span class="p">)</span>  <span class="c"># all time series on a single figure</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">companies</span><span class="p">:</span>
    <span class="n">data</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">style</span><span class="o">=</span><span class="n">colors</span><span class="p">[</span><span class="n">rn</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">colors</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)])</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>



<div class="highlight"><pre><span class="c">## Compute correlation matrix</span>

<span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
<span class="n">n</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">companies</span><span class="p">)</span>
<span class="n">corr_matrix</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="n">n</span><span class="p">,</span> <span class="n">n</span><span class="p">))</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">j</span><span class="p">:</span>
            <span class="n">corr_matrix</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="n">companies</span><span class="p">[</span><span class="n">i</span><span class="p">]]</span><span class="o">.</span><span class="n">corr</span><span class="p">(</span>
                                               <span class="n">data</span><span class="p">[</span><span class="n">companies</span><span class="p">[</span><span class="n">j</span><span class="p">]],</span>
                                               <span class="n">method</span><span class="o">=</span><span class="s">&#39;pearson&#39;</span><span class="p">)</span>

<span class="c"># Output</span>
<span class="n">np</span><span class="o">.</span><span class="n">set_printoptions</span><span class="p">(</span><span class="n">precision</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="k">print</span> <span class="n">corr_matrix</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>



<div class="highlight"><pre><span class="c">## Remove weak correlations to construct a graph</span>
<span class="n">threshold</span> <span class="o">=</span> <span class="mf">0.7</span>
<span class="n">corr_matrix</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">corr_matrix</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">threshold</span><span class="p">)]</span> <span class="o">=</span> <span class="mi">0</span>

<span class="c"># Output</span>
<span class="k">print</span> <span class="n">corr_matrix</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>



<div class="highlight"><pre><span class="c"># Constructing a graph</span>
<span class="kn">import</span> <span class="nn">networkx</span> <span class="kn">as</span> <span class="nn">nx</span>
<span class="n">G</span> <span class="o">=</span> <span class="n">nx</span><span class="o">.</span><span class="n">Graph</span><span class="p">(</span><span class="n">corr_matrix</span><span class="p">)</span>
</pre></div>



<div class="highlight"><pre><span class="c"># Connected components: color them differently</span>

<span class="n">rn</span><span class="o">.</span><span class="n">seed</span> <span class="o">=</span> <span class="mi">5</span>  <span class="c"># for choosing random colors</span>
<span class="n">components</span> <span class="o">=</span> <span class="n">nx</span><span class="o">.</span><span class="n">connected_components</span><span class="p">(</span><span class="n">G</span><span class="p">)</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">components</span><span class="p">:</span>
    <span class="n">component</span> <span class="o">=</span> <span class="n">G</span><span class="o">.</span><span class="n">subgraph</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
    <span class="n">nx</span><span class="o">.</span><span class="n">draw_graphviz</span><span class="p">(</span><span class="n">component</span><span class="p">,</span>
        <span class="n">node_color</span> <span class="o">=</span> <span class="n">colors</span><span class="p">[</span><span class="n">rn</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">colors</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)],</span>
        <span class="n">node_size</span> <span class="o">=</span> <span class="p">[</span><span class="n">component</span><span class="o">.</span><span class="n">degree</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="o">*</span> <span class="mi">100</span> <span class="o">+</span> <span class="mi">15</span>
                     <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">component</span><span class="o">.</span><span class="n">nodes</span><span class="p">()],</span>
        <span class="n">edge_color</span> <span class="o">=</span> <span class="p">[</span><span class="n">corr_matrix</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">]</span> <span class="o">*</span> <span class="mf">0.5</span>
                      <span class="k">for</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span><span class="p">)</span> <span class="ow">in</span> <span class="n">component</span><span class="o">.</span><span class="n">edges</span><span class="p">()],</span>
        <span class="n">with_labels</span> <span class="o">=</span> <span class="bp">True</span><span class="p">,</span>
        <span class="n">labels</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">([(</span><span class="n">x</span><span class="p">,</span> <span class="n">companies</span><span class="p">[</span><span class="n">x</span><span class="p">])</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">component</span><span class="o">.</span><span class="n">nodes</span><span class="p">()])</span>
        <span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="k">print</span> <span class="s">&quot;Smallest components (size &lt; 5):&quot;</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">components</span><span class="p">:</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">5</span><span class="p">:</span>
        <span class="k">print</span> <span class="p">[</span><span class="n">companies</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">i</span><span class="p">]</span>

<span class="k">print</span> <span class="s">&quot;Companies with degrees &lt; 5:&quot;</span>
<span class="k">print</span> <span class="p">[(</span><span class="n">companies</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">degrees</span><span class="p">[</span><span class="n">i</span><span class="p">])</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span> <span class="k">if</span> <span class="n">degrees</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">5</span><span class="p">]</span>
</pre></div>



<div class="highlight"><pre><span class="c">## Explore graph properties</span>

<span class="n">nodes</span><span class="p">,</span> <span class="n">edges</span> <span class="o">=</span> <span class="n">G</span><span class="o">.</span><span class="n">order</span><span class="p">(),</span> <span class="n">G</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
<span class="k">print</span> <span class="s">&quot;Number of nodes:&quot;</span><span class="p">,</span> <span class="n">nodes</span>
<span class="k">print</span> <span class="s">&quot;Number of edges:&quot;</span><span class="p">,</span> <span class="n">edges</span>
<span class="k">print</span> <span class="s">&quot;Average degree:&quot;</span><span class="p">,</span> <span class="n">edges</span> <span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
</pre></div>



<div class="highlight"><pre><span class="c">## Count degrees</span>

<span class="n">degrees</span> <span class="o">=</span> <span class="n">G</span><span class="o">.</span><span class="n">degree</span><span class="p">()</span>
<span class="n">values</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">degrees</span><span class="o">.</span><span class="n">values</span><span class="p">()))</span>
<span class="n">counts</span> <span class="o">=</span> <span class="p">[</span><span class="n">degrees</span><span class="o">.</span><span class="n">values</span><span class="p">()</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">values</span><span class="p">]</span>
</pre></div>



<div class="highlight"><pre><span class="c"># Generate colors -</span>
<span class="c"># http://stackoverflow.com/questions/876853/generating-</span>
<span class="c"># color-ranges-in-python</span>

<span class="kn">import</span> <span class="nn">colorsys</span>
<span class="n">ncolors</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">values</span><span class="p">)</span>
<span class="n">HSV_tuples</span> <span class="o">=</span> <span class="p">[(</span><span class="n">x</span> <span class="o">*</span> <span class="mf">1.0</span> <span class="o">/</span> <span class="n">ncolors</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">ncolors</span><span class="p">)]</span>
<span class="n">RGB_tuples</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">colorsys</span><span class="o">.</span><span class="n">hsv_to_rgb</span><span class="p">(</span><span class="o">*</span><span class="n">x</span><span class="p">),</span> <span class="n">HSV_tuples</span><span class="p">)</span>
</pre></div>



<div class="highlight"><pre><span class="c"># Plot degree distribution</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s">&#39;Degree&#39;</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s">&#39;Number of nodes&#39;</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&#39;Dow Jones network: degree distribution&#39;</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">values</span><span class="p">,</span> <span class="n">counts</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">RGB_tuples</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="k">print</span> <span class="s">&quot;Highest degree:&quot;</span><span class="p">,</span> <span class="nb">max</span><span class="p">(</span><span class="n">values</span><span class="p">)</span>
</pre></div>


