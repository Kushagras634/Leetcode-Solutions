<h2><a href="https://leetcode.com/problems/integer-replacement/">397. Integer Replacement</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a positive integer <code style="user-select: auto;">n</code>,&nbsp;you can apply one of the following&nbsp;operations:</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">If <code style="user-select: auto;">n</code> is even, replace <code style="user-select: auto;">n</code> with <code style="user-select: auto;">n / 2</code>.</li>
	<li style="user-select: auto;">If <code style="user-select: auto;">n</code> is odd, replace <code style="user-select: auto;">n</code> with either <code style="user-select: auto;">n + 1</code> or <code style="user-select: auto;">n - 1</code>.</li>
</ol>

<p style="user-select: auto;">Return <em style="user-select: auto;">the minimum number of operations needed for</em> <code style="user-select: auto;">n</code> <em style="user-select: auto;">to become</em> <code style="user-select: auto;">1</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 8
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> 8 -&gt; 4 -&gt; 2 -&gt; 1
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 7
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation: </strong>7 -&gt; 8 -&gt; 4 -&gt; 2 -&gt; 1
or 7 -&gt; 6 -&gt; 3 -&gt; 2 -&gt; 1
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 4
<strong style="user-select: auto;">Output:</strong> 2
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 2<sup style="user-select: auto;">31</sup> - 1</code></li>
</ul>
</div>