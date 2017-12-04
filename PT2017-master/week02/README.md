# Strings and files

String methods
_______________________

<table border="1" class="docutils" id="index-20">
<thead valign="bottom">
<tr class="row-odd"><th class="head">Operation</th>
	<th class="head">Result</th>
	<th class="head">Notes</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even">
	<td>
		<code class="docutils literal"><span class="pre">x</span> <span class="pre">in</span> <span class="pre">s</span></code>
	</td>
	<td>
		<code class="docutils literal"><span class="pre">True</span></code> if an item (character of substring) of <em>s</em> is
		equal to <em>x</em>, else <code class="docutils literal"><span class="pre">False</span></code>
	</td>
	<td>
		<pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">"gg"</span> <span class="ow">in</span> <span class="s2">"eggs"</span><br/><span class="go">True</span></pre>
	</td>
</tr>
<tr class="row-odd">
	<td>
		<code class="docutils literal"><span class="pre">x</span> <span class="pre">not</span> <span class="pre">in</span> <span class="pre">s</span></code>
	</td>
	<td>
		<code class="docutils literal"><span class="pre">False</span></code> if an item (character of substring) of <em>s</em> is
		equal to <em>x</em>, else <code class="docutils literal"><span class="pre">True</span></code></td>
		<td><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">"xx"</span> <span class="ow">not in</span> <span class="s2">"eggs"</span><br/><span class="go">True</span></pre></td>
</tr>
<tr class="row-even">
	<td>
		<code class="docutils literal"><span class="pre">s</span> <span class="pre">+</span> <span class="pre">t</span></code>
	</td>
	<td>
		the concatenation of <em>s</em> and
		<em>t</em>
	</td>
	<td>Concatenating strings always results in a new string. Repeating concatenating in loop is slow, so can build a list <em>l</em> and use <pre>str.join(l)</pre> with <em>str</em> separator at the end for fast concatenating.</td>
</tr>
<tr class="row-odd">
	<td>
		<code class="docutils literal"><span class="pre">s</span> <span class="pre">*</span> <span class="pre">n</span></code> or
		<code class="docutils literal"><span class="pre">n</span> <span class="pre">*</span> <span class="pre">s</span></code>
	</td>
	<td>equivalent to adding <em>s</em> to
		itself <em>n</em> times
	</td>
	<td>
		<pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">"kbtu"</span> <span class="ow">*</span> <span class="s2">3</span><br/><span class="go">'kbtukbtukbtu'</span></pre>
	</td>
</tr>
<tr class="row-even">
	<td>
		<code class="docutils literal"><span class="pre">s[i]</span></code>
	</td>
	<td>
		<em>i</em>th character of <em>s</em>, origin 0
	</td>
	<td>
		<pre><span></span>s = 'kazakhstan'<br/><span class="gp">&gt;&gt;&gt; </span><span class="s2">s[2]</span><br/><span class="go">'t'</span></pre>
	</td>
</tr>
<tr class="row-odd">
	<td>
		<code class="docutils literal"><span class="pre">s[i:j]</span></code>
	</td>
	<td>slice of <em>s</em> from <em>i</em> to <em>j</em></td>
	<td>
		<pre><span></span>s = 'kazakhstan'<br/><span class="gp">&gt;&gt;&gt; </span><span class="s2">s[2]</span><br/><span class="go">'z'</span></pre>
	</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">s[i:j:k]</span></code></td>
	<td>slice of <em>s</em> from <em>i</em> to <em>j</em>
		with step <em>k</em></td>
		<td>
			<pre><span></span>s = 'kazakhstan'<br/><span class="gp">&gt;&gt;&gt; </span><span class="s2">s[2:5]</span><br/><span class="go">'zak'</span></pre>

		</td>
	</tr>
	<tr class="row-odd">
		<td>
			<code class="docutils literal"><span class="pre">len(s)</span></code>
		</td>
		<td>length of <em>s</em></td>
		<td>
			<pre><span></span>s = 'kazakhstan'<br/><span class="gp">&gt;&gt;&gt; </span><span class="s2">len(s)</span><br/><span class="go">10</span></pre>
		</td>
	</tr>
	<tr class="row-even">
		<td><code class="docutils literal"><span class="pre">min(s)</span></code></td>
		<td>smallest (alphabetically) character of <em>s</em></td>
		<td>
			<pre><span></span>s = 'kazakhstan'<br/><span class="gp">&gt;&gt;&gt; </span><span class="s2">min(s)</span><br/><span class="go">'a'</span></pre>
		</td>
	</tr>
	<tr class="row-odd">
		<td><code class="docutils literal"><span class="pre">max(s)</span></code></td>
		<td>largest (alphabetically) character of <em>s</em></td>
		<td>
			<pre><span></span>s = 'kazakhstan'<br/><span class="gp">&gt;&gt;&gt; </span><span class="s2">max(s)</span><br/><span class="go">'z'</span></pre>

		</td>
	</tr>
	<tr class="row-even">
		<td>
			<code class="docutils literal"><span class="pre">s.index(x[,</span> <span class="pre">i[,</span> <span class="pre">j]])</span></code>
		</td>
		<td>index of the first occurrence
			of <em>x</em> in <em>s</em> (at or after
			index <em>i</em> and before index <em>j</em>)
		</td>
		<td>
			<pre><span></span>s = 'kazakhstan'<br/><span class="gp">&gt;&gt;&gt; </span><span class="s2">s.index('k', 1, 10)</span><br/><span class="go">4</span></pre>
			index raises <em>ValueError</em> when x is not found in s. 
		</td>
	</tr>
	<tr class="row-odd">
		<td>
			<code class="docutils literal"><span class="pre">s.count(x)</span></code>
		</td>
		<td>total number of occurrences of
			<em>x</em> in <em>s</em></td>
		<td>
			<pre><span></span>s = 'kazakhstan'<br/><span class="gp">&gt;&gt;&gt; </span><span class="s2">s.count('a')</span><br/><span class="go">3</span></pre>
		</td>
	</tr>
	<tr class="row-odd">
		<td>
			<code class="docutils literal"><span class="pre">s.replace(x, y)</span></code>
		</td>
		<td>replace of occurrences of
			<em>x</em> in <em>s</em> by <em>y</em></td>
		<td>
			<pre><span></span>s = 'kazakhstan'<br/><span class="gp">&gt;&gt;&gt; </span><span class="s2">s.replace('k', 'q')</span><br/><span class="go">'qazaqhstan'</span></pre>
		</td>
	</tr>
</tbody>
</table> 
