## Introduction: Improved Styling with CSS

<p class="p__1qg33Igem5pAgn4kPMirjw">
The goal of this unit is to dig deeper into CSS and improve your ability
to style websites. You will also learn more about navigation design.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After this unit, you will be able to:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Apply more custom colors and fonts
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Style navigation elements like links and buttons
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Create secondary (breadcrumb) navigation
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Learning is social. Whatever you’re working on, be sure to connect with
the Codecademy community in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/">forums</a>.
Remember to check in with the community regularly, including for things
like asking for code reviews on your project work and providing code
reviews to others in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/c/project/1833">projects
category</a>, which can help to reinforce what you’ve learned.
</p>

## COLOR

### Introduction to Color

<p class="p__1qg33Igem5pAgn4kPMirjw">
CSS supports a wide variety of colors. These include <em>named
colors</em>, like
<code class="code__2rdF32qjRVp7mMVBHuPwDS">blue</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">black</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">limegreen</code>, along with
colors described by a numeric value. Using a numeric system allows us to
take advantage of the whole spectrum of colors that browsers support. In
this lesson, we’re going to explore all the color options CSS offers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Colors in CSS can be described in three different ways:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Named colors</em> — English words that describe colors, also called
<em>keyword colors</em>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>RGB</em> — numeric values that describe a mix of red, green, and
blue
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>HSL</em> — numeric values that describe a mix of hue, saturation,
and lightness
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ll learn about and explore the benefits of each of these in-depth.
Using only named colors, you may feel like you’re picking labeled
crayons out of a box. By the end of this lesson, you’ll feel like a
painter mixing paints on a palette.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Proceed to the next exercise when you are ready to begin.
</p>

**Solutions**

``` html
```

## COLOR

### Foreground vs Background

<p class="p__1qg33Igem5pAgn4kPMirjw">
Before discussing the specifics of color, it’s important to make two
distinctions about color. Color can affect the following design aspects:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The foreground color
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The background color
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Foreground color is the color that an element appears in. For example,
when a heading is styled to appear green, the <em>foreground color</em>
of the heading has been styled.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Conversely, when a heading is styled so that its background appears
yellow, the <em>background color</em> of the heading has been styled
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In CSS, these two design aspects can be styled with the following two
properties:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> - this property
styles an element’s foreground color.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code> -
this property styles an element’s background color.
</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">red</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the text of the heading will appear in red, and
the background of the heading will appear blue.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, change the foreground color of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> heading to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">midnightblue</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, set the background color of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> heading to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">aqua</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice how only the background area behind heading changed.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## COLOR

### Hexadecimal

<p class="p__1qg33Igem5pAgn4kPMirjw">
One syntax that we can use to specify colors is called
<em>hexadecimal</em>. Colors specified using this system are called
<em>hex colors</em>. A hex color begins with a hash character
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">\#</code>) which is followed
by three or six characters. The characters represent values for red,
blue and green.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">darkseagreen</span><span class="mtk9">: </span><span class="mtk4">#</span><span class="mtk9">8</span><span class="mtk4">FBC8F</span></span><br><span><span class="mtk4">sienna</span><span class="mtk9">:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">#A0522D</span></span><br><span><span class="mtk4">saddlebrown</span><span class="mtk9">:&nbsp;&nbsp;</span><span class="mtk4">#</span><span class="mtk9">8</span><span class="mtk4">B4513</span></span><br><span><span class="mtk4">brown</span><span class="mtk9">:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">#A52A2A</span></span><br><span><span class="mtk4">black</span><span class="mtk9">:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">#</span><span class="mtk9">000000 </span><span class="mtk4">or</span><span class="mtk9"> </span><span class="mtk4">#</span><span class="mtk9">000</span></span><br><span><span class="mtk4">white</span><span class="mtk9">:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">#FFFFFF</span><span class="mtk9"> </span><span class="mtk4">or</span><span class="mtk9"> </span><span class="mtk1">#FFF</span></span><br><span><span class="mtk4">aqua</span><span class="mtk9">:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">#</span><span class="mtk9">00</span><span class="mtk4">FFFF</span><span class="mtk9"> </span><span class="mtk4">or</span><span class="mtk9"> </span><span class="mtk4">#</span><span class="mtk9">0</span><span class="mtk4">FF</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, you may notice that there are both letters and
numbers in the values. This is because the hexadecimal number system has
16 digits (0-15) instead of 10 (0-9) like in the standard decimal
system. To represent 10-15, we use A-F.
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value">Here</a>
is a list of many different colors and their hex values.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice that <code class="code__2rdF32qjRVp7mMVBHuPwDS">black</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">white</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">aqua</code> are all
represented with both three characters and six characters. This can be
done with hex colors whose number pairs are the same characters. In the
example above, <code class="code__2rdF32qjRVp7mMVBHuPwDS">aqua</code>
can be represented as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#0FF</code> because both of
the first two characters are
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code> and the second and
third pairs of characters are both
<code class="code__2rdF32qjRVp7mMVBHuPwDS">F</code>s. Keep in mind that
all three character hex colors can be represented with six characters
(by repeating each character twice) but the same is not true in reverse.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can include hex colors just as you would include named colors:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color:
#9932cc;</code>, and the letters can be uppercase or lowercase.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the browser is a web page that uses named colors and hex colors.
We’re going to translate the named colors into hex, to be more
consistent. The colors won’t visually change, yet.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, find the CSS rule that uses the named
color <code class="code__2rdF32qjRVp7mMVBHuPwDS">darkseagreen</code> and
change it to its hex value,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#8FBC8F</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Find the four other named colors of the roast types and convert them to
their hex values, as shown here:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sienna</code>:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#A0522D</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">saddlebrown</code>:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#8B4513</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">brown</code>:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#A52A2A</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">black</code>:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#000000</code>
</li>
</ul>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## COLOR

### RGB Colors

<p class="p__1qg33Igem5pAgn4kPMirjw">
There is another syntax for representing RGB values, commonly referred
to as “RGB value” or just “RGB”, that uses decimal numbers rather than
hexadecimal numbers, and it looks like this:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">rgb(</span><span class="mtk9">23</span><span class="mtk1">,</span><span class="mtk9"> 45</span><span class="mtk1">,</span><span class="mtk9"> 23</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Each of the three values represents a color component, and each can have
a decimal number value from 0 to 255. The first number represents the
amount of red, the second is green, and the third is blue. These colors
are exactly the same as hex, but with a different syntax and a different
number system.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In general, hex and RGB color representations are equivalent. Which you
choose is a matter of personal taste. That said, it’s good to choose one
and be consistent throughout your CSS, because it’s easier to compare
hex to hex and RGB to RGB.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, find the hex value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#8FBC8F</code> and change it
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">rgb(143, 188, 143)</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, find the hex value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#A0522D</code> and change it
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">rgb(160, 82, 45)</code>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, find the hex value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#8B4513</code> and change it
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">rgb(139, 69, 19)</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## COLOR

### Hex and RGB

<p class="p__1qg33Igem5pAgn4kPMirjw">
The hexadecimal and rgb color system can represent many more colors than
the small set of CSS named colors. We can use this new set of colors to
refine our web page’s style.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In both hex and RGB, we have three values, one for each color. Each can
be one of 256 values. Specifically,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">256 \* 256 \* 256 =
16,777,216</code>. That is the amount of colors we can now represent.
Compare that to the roughly 140 named CSS colors!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Recall that we started with named colors, converted them to hex, and
then converted some of the hex colors to rgb. Unless we made a mistake,
all of the colors should still be the same, visually. Let’s use our
broadened palette to make some more refined color choices.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.green</code> rule in
<strong>style.css</strong>, change the background color to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#9EB599</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Run the code. Can you tell the difference?
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.light</code> rule in
<strong>style.css</strong>, change the background color to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#683C2C</code>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.city</code> rule in
<strong>style.css</strong>, change the background color to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#4C352D</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.vienna</code> rule in
<strong>style.css</strong>, change the background color to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#352926</code>.
</p>

<span aria-live="assertive">Checkpoint 5 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">5.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.italian</code> rule
in <strong>style.css</strong>, change the background color to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#141212</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Run the code one more time. These new colors are a lot closer to the
real-life color of each type of coffee. How does the subtle difference
feel?
</p>

<span aria-live="assertive">Checkpoint 6 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## COLOR

### Hue, Saturation, and Lightness

<p class="p__1qg33Igem5pAgn4kPMirjw">
The RGB color scheme is convenient because it’s very close to how
computers represent colors internally. There’s another equally powerful
system in CSS called the hue-saturation-lightness color scheme,
abbreviated as <em>HSL</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The syntax for HSL is similar to the decimal form of RGB, though it
differs in important ways. The first number represents the degree of the
hue, and can be between 0 and 360. The second and third numbers are
percentages representing saturation and lightness respectively. Here is
an example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">hsl</span><span class="mtk9">(120</span><span class="mtk1">,</span><span class="mtk9"> 60</span><span class="mtk4">%</span><span class="mtk1">,</span><span class="mtk9"> 70</span><span class="mtk4">%</span><span class="mtk9">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Hue</em> is the first number. It refers to an angle on a color
wheel. Red is 0 degrees, Green is 120 degrees, Blue is 240 degrees, and
then back to Red at 360. You can see an example of a color wheel below.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/courses/learn-css-color/color_wheel_4_background.svg" alt="color wheel" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Saturation</em> refers to the intensity or purity of the color. The
saturation increases towards 100% as the color becomes richer. The
saturation decreases towards 0% as the color becomes grayer.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Lightness</em> refers to how light or dark the color is. Halfway, or
50%, is normal lightness. Imagine a sliding dimmer on a light switch
that starts halfway. Sliding the dimmer up towards 100% makes the color
lighter, closer to white. Sliding the dimmer down towards 0% makes the
color darker, closer to black.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
HSL is convenient for adjusting colors. In RGB, making the color a
little darker may affect all three color components. In HSL, that’s as
easy as changing the lightness value. HSL is also useful for making a
set of colors that work well together by selecting various colors that
have the same lightness and saturation but different hues.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the browser is a simple page with different colored rectangles.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, modify the lightness of the background
color of the class selector
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.midground</code> to be
<code class="code__2rdF32qjRVp7mMVBHuPwDS">25%</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Change the saturation of the background color of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.foreground</code> class
selector to <code class="code__2rdF32qjRVp7mMVBHuPwDS">50%</code>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Change the hue of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">body</code> selector’s
background color to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">240</code> degrees.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## COLOR

### Opacity and Alpha

<p class="p__1qg33Igem5pAgn4kPMirjw">
All of the colors we’ve seen so far have been opaque, or
non-transparent. When we overlap two opaque elements, nothing from the
bottom element shows through the top element. In this exercise, we’ll
change the <em>opacity</em>, or the amount of transparency, of some
colors so that some or all of the bottom elements are visible through a
covering element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To use opacity in the HSL color scheme, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hsla</code> instead of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hsl</code>, and four values
instead of three. For example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">hsla</span><span class="mtk9">(34</span><span class="mtk1">,</span><span class="mtk9"> 100</span><span class="mtk4">%</span><span class="mtk1">,</span><span class="mtk9"> 50</span><span class="mtk4">%</span><span class="mtk1">,</span><span class="mtk9"> 0</span><span class="mtk4">.</span><span class="mtk9">1);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The first three values work the same as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hsl</code>. The fourth value
(which we have not seen before) is the <em>alpha</em>. This last value
is sometimes called opacity.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Alpha is a decimal number from zero to one. If alpha is zero, the color
will be completely transparent. If alpha is one, the color will be
opaque. The value for half-transparent would be
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0.5</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can think of the alpha value as, “the amount of the background to
mix with the foreground”. When a color’s alpha is below one, any color
behind it will be blended in. The blending happens for each pixel; no
blurring occurs.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The RGB color scheme has a similar syntax for opacity,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rgba</code>. Again, the first
three values work the same as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rgb</code> and the last value
is the alpha. Here’s an example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">rgba</span><span class="mtk9">(234</span><span class="mtk1">,</span><span class="mtk9"> 45</span><span class="mtk1">,</span><span class="mtk9"> 98</span><span class="mtk1">,</span><span class="mtk9"> 0</span><span class="mtk4">.</span><span class="mtk9">33);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A little unconventional, but still worth mentioning is how hex colors
can also have an alpha value. By adding a two-digit hexadecimal value to
the end of the six-digit representation
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">#52BC8280</code>), or a
one-digit hexadecimal value to the end of the three-digit representation
(#F003), you can change the opacity of a hexadecimal color. Hex opacity
ranges from <code class="code__2rdF32qjRVp7mMVBHuPwDS">00</code>
(transparent) to <code class="code__2rdF32qjRVp7mMVBHuPwDS">FF</code>
(opaque).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Alpha can only be used with HSL, RGB, and hex colors; we cannot add the
alpha value to name colors like
<code class="code__2rdF32qjRVp7mMVBHuPwDS">green</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There is, however, a named color keyword for zero opacity,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">transparent</code>. It’s
equivalent to <code class="code__2rdF32qjRVp7mMVBHuPwDS">rgba(0, 0, 0,
0)</code>, and it’s used like any other color keyword:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">transparent</span><span class="mtk9">;</span></span><br></div></code></pre></pre>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Give the element with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.foreground</code> an alpha
value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">0.6</code>. Remember
to change <code class="code__2rdF32qjRVp7mMVBHuPwDS">hsl</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hsla</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Give the element with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.midground</code> an alpha
value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">0.4</code> using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hsla</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Run the code, and notice how all the colors blend depending on how they
overlap.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Modify the <code class="code__2rdF32qjRVp7mMVBHuPwDS">body</code> rule’s
background color to have a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rgba(0, 255, 0, 0.1)</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
How does opacity change the background?
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## COLOR

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ve completed our extensive tour of the colors in CSS! Let’s review
the key information we’ve learned.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are four ways to represent color in CSS:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Named colors—there are more than 140 named colors, which you can review
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/named-color">here
on MDN</a>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Hexadecimal or hex colors
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Hexadecimal is a number system that has sixteen digits, 0 to 9 followed
by “A” to “F”.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Hex values always begin with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\#</code> and specify values
of red, blue, and green using hexadecimal numbers such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#23F41A</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Six-digit hex values with duplicate values for each RGB value can be
shorted to three digits.
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
RGB
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
RGB colors use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rgb()</code> syntax with one
value for red, one value for blue and one value for green.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
RGB values range from 0 to 255 and look like this:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rgb(7, 210, 50)</code>.
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
HSL
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
HSL stands for hue (the color itself), saturation (the intensity of the
color), and lightness (how light or dark a color is).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Hue ranges from 0 to 360 and saturation and lightness are both
represented as percentages like this:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hsl(200, 20%, 50%)</code>.
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
You can add opacity to color in RGB and HSL by adding a fourth value,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code>, which is
represented as a percentage.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Great job! Feel empowered to add a bit of color to each of your
projects!
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Proceed when you’re ready to move on!
</p>

**Solutions**

``` html
```

## WEB DEVELOPMENT FOUNDATIONS

### Paint Store

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you will follow step-by-step instructions to improve a
vibrant, color-rich web page for a home paint business. It displays
information about using color in a home and color swatches with varying
lightness, saturation, and hue.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The page is almost ready to be published. You’ll be making the following
color-related changes:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Exchange some named colors with hexadecimal color values.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Add some semi-transparent overlays to the banner and footer using RGBA.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Fill in the first color column of the swatch samples using HSL colors.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The website’s existing <strong>index.html</strong> and
<strong>style.css</strong> document files are displayed in the text
editor.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

## TYPOGRAPHY

### Typography

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, we’ll focus on <em>typography</em>, the art of arranging
text on a page. We’ll look at:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
How to style and transform fonts.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
How to lay text out on a page.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
and how to add external fonts to your web pages.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Some of the most important information a user will see on a web page
will be textual. Styling text to make page content accessible and
engaging can significantly improve user experience. Let’s begin!
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the browser, we have a blog site with fonts of different sizes and
styles. In the following exercises, we’ll learn how to manipulate fonts
to create engaging interfaces.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Once you have an idea of the general layout of the page, proceed to the
next exercise.
</p>

**Solutions**

``` html
```

## TYPOGRAPHY

### Font Family

<p class="p__1qg33Igem5pAgn4kPMirjw">
You may remember from the
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/content-items/1368d1ea90382cbe44b60eeac19e9573/exercises/font-family">Visual
Rules</a> lesson that the font of an element can be changed using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> Arial</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the font family for all
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code> heading
elements have been set to Arial.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s talk about some things to keep in mind when setting
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> values.
</p>
<h5 id="heading-multi-word-values">
Multi-Word Values
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When specifying a typeface with multiple words, like Times New Roman, it
is recommended to use quotation marks
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">’ ’</code>) to group the
words together, like so:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">'Times New Roman'</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<h5 id="heading-web-safe-fonts">
Web Safe Fonts
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There is a selection of fonts that will appear the same across all
browsers and operating systems. These fonts are referred to as <em>web
safe fonts</em>. You can check out a complete list of web safe fonts
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.cssfontstack.com/">here</a>.
</p>
<h5 id="heading-fallback-fonts-and-font-stacks">
Fallback Fonts and Font Stacks
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Web safe fonts are good <em>fallback fonts</em> that can be used if your
preferred font is not available.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> Caslon</span><span class="mtk1">,</span><span class="mtk9"> Georgia</span><span class="mtk1">,</span><span class="mtk9"> </span><span class="mtk8">'Times New Roman'</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, Georgia and Times New Roman are fallback fonts to
Caslon. When you specify a group of fonts, you have what is known as a
<em>font stack</em>. A font stack usually contains a list of
similar-looking fonts. Here, the browser will first try to use the
Caslon font. If that’s not available, it will try to use a similar font,
Georgia. And if Georgia is not available, it will try to use Times New
Roman.
</p>
<h5 id="heading-serif-and-sans-serif">
Serif and Sans-Serif
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You may be wondering what features make a font similar to another font.
The fonts Caslon, Georgia, and Times New Roman are <em>Serif</em> fonts.
Serif fonts have extra details on the ends of each letter, as opposed to
<em>Sans-Serif</em> fonts, which do not have the extra details.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/courses/web-101/htmlcss1-diagram__fontanatomy.svg" alt="Serif and Sans-Serif fonts" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">serif</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sans-serif</code> are also
keyword values that can be added as a final fallback font if nothing
else in the font stack is available.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> Caslon</span><span class="mtk1">,</span><span class="mtk9"> Georgia</span><span class="mtk1">,</span><span class="mtk9"> </span><span class="mtk8">'Times New Roman'</span><span class="mtk1">,</span><span class="mtk9"> </span><span class="mtk5">serif</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this final example, the font stack has 4 fonts. If the first 3 fonts
aren’t available, the browser will use whatever serif font is available
on the system.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, change the font family of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code> element to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Georgia</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, change the font family of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.editorial</code> elements to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Trebuchet MS</code>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, use a font stack to give the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.editorial</code> elements
fallback fonts of <code class="code__2rdF32qjRVp7mMVBHuPwDS">Times New
Roman</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">serif</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## TYPOGRAPHY

### Font Weight

<p class="p__1qg33Igem5pAgn4kPMirjw">
In CSS, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> property
controls how bold or thin text appears. It can be specified with
keywords or numerical values.
</p>
<h4 id="heading-keyword-values" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Keyword Values
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code>
property can take any one of these keyword values:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">bold</code>: Bold font
weight.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">normal</code>: Normal font
weight. This is the default value.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lighter</code>: One font
weight lighter than the element’s parent value.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">bolder</code>: One font
weight bolder than the element’s parent value
</li>
</ul>
<h4 id="heading-numerical-values" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Numerical Values
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Numerical values can range from 1 (lightest) to 1000 (boldest), but it
is common practice to use increments of 100. A font weight of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">400</code> is equal to the
keyword value <code class="code__2rdF32qjRVp7mMVBHuPwDS">normal</code>,
and a font weight of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">700</code> is equal to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">bold</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.left-section</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-weight</span><span class="mtk1">:</span><span class="mtk9"> 700</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.right-section</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-weight</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">bold</span><span class="mtk1">;</span><span class="mtk9"> </span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, text in elements of both
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.left-section</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.right-section</code> classes
will appear bold.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It’s important to note that not all fonts can be assigned a numeric font
weight, and not all numeric font weights are available to all fonts.
It’s a good practice to look up the font you are using to see which
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> values are
available.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, change the font weight of elements with
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.banner p</code> selector
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">lighter</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, change the font-weight of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.header</code> class to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">900</code>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## TYPOGRAPHY

### Font Style

<p class="p__1qg33Igem5pAgn4kPMirjw">
You can also italicize text with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-style</code> property.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h3</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-style</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">italic</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">italic</code> value
causes text to appear in italics. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-style</code> property
also has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">normal</code>
value which is the default.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The web page features three sections, “Garamond”, “Helvetica”, and
“Space Mono”. Each of these sections includes a line with the name of
the font creator, such as “Claude Garamond”. Let’s italicize the
creator’s name on each of these cards.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, in the font card section, set the font
style of <code class="code__2rdF32qjRVp7mMVBHuPwDS">.font-card
.creator</code> to italic.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## TYPOGRAPHY

### Text Transformation

<p class="p__1qg33Igem5pAgn4kPMirjw">
Text can also be styled to appear in either all uppercase or lowercase
with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">text-transform</code>
property.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">text-transform</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">uppercase</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The code in the example above formats all
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code> elements to
appear in <code class="code__2rdF32qjRVp7mMVBHuPwDS">uppercase</code>,
regardless of the case used for the heading within the HTML code.
Alternatively, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lowercase</code> value could
be used to format text in all lowercase.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Since text can be directly typed in all uppercase or lowercase within an
HTML file, what is the point of a CSS rule that allows you to format
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Letter_case">letter
case</a>?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Depending on the type of content a web page displays, it may make sense
to always style a specific element in all uppercase or lowercase
letters. For example, a website that reports breaking news may decide to
format all <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code>
heading elements such that they always appear in all uppercase, as in
the example above. It would also avoid uppercase text in the HTML file,
which could make code difficult to read.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, transform the text in the main heading
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code>) to appear
uppercase.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## TYPOGRAPHY

### Text Layout

<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ve learned how text can be defined by font family, weight, style,
and transformations. Now you’ll learn about some ways text can be
displayed or laid out within the element’s container.
</p>
<h5 id="heading-letter-spacing">
Letter Spacing
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-spacing</code>
property is used to set the horizontal spacing between the individual
characters in an element. It’s not common to set the spacing between
letters, but it can sometimes help the readability of certain fonts or
styles. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-spacing</code>
property takes length values in units, such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2px</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0.5em</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">letter-spacing</span><span class="mtk1">:</span><span class="mtk9"> 2px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, each character in the paragraph element will be
separated by 2 pixels.
</p>
<h5 id="heading-word-spacing">
Word Spacing
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can set the space between words with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">word-spacing</code> property.
It’s also not common to increase the spacing between words, but it may
help enhance the readability of bolded or enlarged text. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">word-spacing</code> property
also takes length values in units, such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">3px</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0.2em</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">word-spacing</span><span class="mtk1">:</span><span class="mtk9"> 0.3em</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the word spacing is set to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0.3em</code>. For word
spacing, using <code class="code__2rdF32qjRVp7mMVBHuPwDS">em</code>
values are recommended because the spacing can be set based on the size
of the font.
</p>
<h5 id="heading-line-height">
Line Height
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/courses/updated_images/htmlcss1-diagram__leading_updated_1-01.svg" alt="diagram of line height property" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">line-height</code> property
to set how tall we want each line containing our text to be. Line height
values can be a unitless number, such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1.2</code>, or a length
value, such as <code class="code__2rdF32qjRVp7mMVBHuPwDS">12px</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">5%</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2em</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">line-height</span><span class="mtk1">:</span><span class="mtk9"> 1.4</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the height between lines is set to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1.4</code>. Generally, the
unitless value is preferred since it is responsive based on the current
font size. In other words, if the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">line-height</code> is
specified by a unitless number, changing the font size will
automatically readjust the line height.
</p>
<h5 id="heading-text-alignment">
Text Alignment
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">text-align</code>
property, which you may already be familiar with from the
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-css/lessons/css-visual-rules/exercises/text-align">CSS
Visual Rules lesson</a>, aligns text to its parent element.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">text-align</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">right</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code> element is
aligned to the right side, instead of the default left.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s put these new properties to work! In <strong>style.css</strong>,
set the letter spacing of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code> element to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0.3em</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, set the word spacing in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.banner p</code> ruleset to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0.25em</code>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, set the line height in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.banner p</code> ruleset to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1.4</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, set the text alignment of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code> elements to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify</code>.
</p>

<span aria-live="assertive">Checkpoint 5 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## TYPOGRAPHY

### Web Fonts

<p class="p__1qg33Igem5pAgn4kPMirjw">
Previously, we learned about web safe fonts, a group of fonts supported
across browsers and operating systems. However, the fonts you can use
for your website are limitless—<em>web fonts</em> allow you to express
your unique style through a multitude of different fonts found on the
web.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Free font services, like
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://fonts.google.com/">Google
Fonts</a> and
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://fonts.adobe.com">Adobe
Fonts</a>, host fonts that you can link to from your HTML document with
a provided <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code>
element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can also use fonts from paid font distributors like
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.fonts.com/">fonts.com</a>
by downloading and hosting them with the rest of your site’s files. You
can create a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code> ruleset in
your CSS stylesheet to link to the relative path of the font file.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Both techniques for including web fonts into your site allow you to go
beyond the sometimes “traditional” appearance of web safe fonts. In the
next two exercises, you’ll learn exactly how to use each of these
techniques!
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Explore the different example fonts shown on the right, as well as the
links to font services above. When you are ready, click “Next” to learn
how to use them!
</p>

**Solutions**

``` html
```

## TYPOGRAPHY

### Web Fonts Using <link>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Online font services, like
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://fonts.google.com/">Google
Fonts</a>, make it easy to find and link to fonts from your site. You
can browse and select fonts that match the style of your website.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Typography/google-fonts-styles-page.png" alt="Google Fonts Roboto Styles Page" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When you select a font in Google Fonts, you’ll be shown all of the
different styles available for that particular font. You can then select
the styles you want to use on your site.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Typography/google-fonts-font-families.png" alt="Showing Selected Font Families" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When you’re done selecting a font and its styles, you can review your
selected font family, and a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code> element will
be automatically generated for you to use on your site!
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;head&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk16">&lt;!-- Add the link element for Google Fonts along w</span><span class="mtk16">ith other metadata --&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;link</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">"https://fonts.googleapis.com/css2?family=Roboto:w</span><span class="mtk8">ght@100&amp;display=swap"</span><span class="mtk1"> </span><span class="mtk7">rel</span><span class="mtk1">=</span><span class="mtk8">"stylesheet"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/head&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The generated <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code>
element needs to be added to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<head\></code> element in
your HTML document for it to be ready to be used in your CSS.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">'Roboto'</span><span class="mtk1">,</span><span class="mtk9"> </span><span class="mtk5">sans-serif</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can then create
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code>
declarations in your CSS, just like how you learned to do with other
fonts!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The font at the bottom of the page, under the Monospaced section, needs
to be “Space Mono”. Let’s fix it by linking to the Space Mono Google
Font!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Navigate to
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://fonts.google.com/">Google
Fonts</a> and select the “Space Mono” font. In the list of style
variations, find “Regular 400” and click “+ Select this style”.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Copy the provided
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code> element, and
paste it into the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<head\></code> element
inside <strong>index.html</strong>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.space</code> ruleset, create
a declaration using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property,
with <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Space Mono’,
monospace;</code> as the value.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## TYPOGRAPHY

### Web Fonts Using @font-face

<p class="p__1qg33Igem5pAgn4kPMirjw">
Fonts can also be added using a
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face"><code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code>
ruleset</a> in your CSS stylesheet instead of using a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code> element in
your HTML document. As mentioned earlier, fonts can be downloaded just
like any other file on the web. They come in a few different file
formats, such as:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
OTF (OpenType Font)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
TTF (TrueType Font)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
WOFF (Web Open Font Format)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
WOFF2 (Web Open Font Format 2)
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The different formats are a progression of standards for how fonts will
work with different browsers, with WOFF2 being the most progressive.
It’s a good idea to include TTF, WOFF, and WOFF2 formats with your
<code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code> rule to
ensure compatibility on all browsers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s take a look at how to use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code> using the
same Roboto font as before:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Typography/google-fonts-download.png" alt="Google Fonts Download" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Within the “Selected Families” section, you can use the “Download”
button to download the font files to your computer. The files will be
downloaded as a single format, in this case, TTF. You can use a tool
such as
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://google-webfonts-helper.herokuapp.com/fonts">Google
Web Fonts Helper</a> to generate additional file types for WOFF and
WOFF2.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When you have the files you need, move them to a folder inside your
website’s working directory, and you’re ready to use them in a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code> ruleset!
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">@font-face</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">'MyParagraphFont'</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;src: url('fonts/Roboto</span><span class="mtk7">.woff2</span><span class="mtk9">') format('woff2')</span><span class="mtk1">,</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url('fonts/Roboto</span><span class="mtk7">.woff</span><span class="mtk9">') format('woff')</span><span class="mtk1">,</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url('fonts/Roboto</span><span class="mtk7">.ttf</span><span class="mtk9">') format('truetype');</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s take a look at the example above, line by line:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code> at-rule
is used as the selector. It’s recommended to define the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code> ruleset at
the top of your CSS stylesheet.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Inside the declaration block, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property
is used to set a custom name for the downloaded font. The name can be
anything you choose, but it must be surrounded by quotation marks. In
the example, the font is named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘MyParagraphFont’</code>, as
this font will be used for all paragraphs.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">src</code> property
contains three values, each specifying the relative path to the font
file and its format. In this example, the font files are stored inside a
folder named <code class="code__2rdF32qjRVp7mMVBHuPwDS">fonts</code>
within the working directory.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Note that the ordering for the different formats is important because
our browser will start from the top of the list and search until it
finds a font format that it supports. Read more on format prioritization
on
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://css-tricks.com/snippets/css/using-font-face-in-css/">CSS-Tricks</a>.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Once the <code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code>
at-rule is defined, you can use the font in your stylesheet!
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">'MyParagraphFont'</span><span class="mtk1">,</span><span class="mtk9"> </span><span class="mtk5">sans-serif</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Like using any other fonts, you can use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property
to set the font on any HTML element. The downloaded font can be
referenced with the name you provided as the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property’s
value in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code> ruleset—in
this case,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘MyParagraphFont’</code>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s change the font of the banner using local font files. If you open
up the <strong>fonts/</strong> directory using the file navigator in the
code editor, you’ll notice that we have added local font files
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Glegoo-Regular.woff2</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Glegoo-Regular.woff</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Glegoo-Regular.ttf</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
At the top of <strong>style.css</strong>, create a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code> ruleset and
give it the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘GlegooBanner’</code> as
its value.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Within the <code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code>
rule, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">src</code>
property with the following paths and formats as values, in the
following order:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">url(‘../fonts/Glegoo-Regular.woff2’)</code>
and a format of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘woff2’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">url(‘../fonts/Glegoo-Regular.woff’)</code>
and a format of <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘woff’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">url(‘../fonts/Glegoo-Regular.ttf’)</code>
and a format of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘truetype’</code>
</li>
</ul>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.banner p</code>
ruleset, add a declaration that sets the font family to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘GlegooBanner’</code>, with a
font size of <code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Press “Run” to see the changes in the browser.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## TYPOGRAPHY

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great job! You learned how to style an important aspect of the user
experience—typography.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s review what you’ve learned so far:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Typography</em> is the art of arranging text on a page.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Text can appear bold or thin with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> property.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Text can appear in italics with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-style</code> property.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The vertical spacing between lines of text can be modified with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">line-height</code> property.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Serif</em> fonts have extra details on the ends of each letter.
<em>Sans-Serif</em> fonts do not.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Fallback fonts</em> are used when a certain font is not installed on
a user’s computer.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">word-spacing</code>
property changes how far apart individual words are.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-spacing</code>
property changes how far apart individual letters are.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">text-align</code>
property changes the horizontal alignment of text.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Google Fonts provides free fonts that can be used in an HTML file with
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code> tag or
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code>
property.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Local fonts can be added to a document with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">@font-face</code> property
and the path to the font’s source.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Using your new knowledge of CSS typography, feel free to edit the code
further to make the web page more appealing!
</p>

## WEB DEVELOPMENT FOUNDATIONS

### Typography

<p class="p__1qg33Igem5pAgn4kPMirjw">
Aoife Conleavy is a novelist who has been writing about her travels for
nearly two decades. Before the launch of her new novel <em>Tide
Blade</em>, which features the stories of real-life characters in
Morocco, the author wants to spruce up her professional website. You’ll
modify the typography on her site, changing the size, style, and font
families, to make the page easier to read.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Using your understanding of typography, help Aoife Conleavy improve the
readability of her site for her readers.
</p>

## WEB DEVELOPMENT FOUNDATIONS

### Challenge Project: Build Your Own Cheat Sheet

<h4 id="heading-overview" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Overview
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This project is slightly different than others you have encountered thus
far on Codecademy. Instead of a step-by-step tutorial, this project
contains a series of open-ended requirements which describe the project
you’ll be building. There are many possible ways to correctly fulfill
all of these requirements, and you should expect to use the internet,
Codecademy, and other resources when you encounter a problem that you
cannot easily solve.
</p>
<h4 id="heading-project-goals" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Project Goals
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you’ll be building your own reference cheat sheet to
help you build more websites in the future! Although there are great
places to learn HTML & CSS like Codecademy, the best reference for
yourself is often your own notes and projects.
</p>
<h4 id="heading-setup-instructions" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Setup Instructions
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you choose to do this project on your computer instead of Codecademy,
you can download what you’ll need by clicking the “Download” button
below. If you need help setting up your computer, read our
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/articles/visual-studio-code">article
about setting up a text editor for HTML/CSS development</a>.
</p>

## LEARN LINKS AND BUTTONS

### Introduction

<p class="p__1qg33Igem5pAgn4kPMirjw">
Imagine that you are a user who has arrived at the website loaded in the
web browser here. What can you interact with, what can you click on to
navigate the site? Before clicking anything, scroll through the page and
try to guess how elements might behave when clicked. After this, click
through and see what actually works. Even if you were totally correct in
your assumptions about what was clickable (because you are a competent
user of web interfaces or are very lucky!), many users would struggle to
interact with this page effectively. This site is a particularly bad
example of interface design, and there is a lot of room for improvement.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Part of the reason it is so hard to know how to interact with this
website is that there are few to no <em>signifiers</em>. To simplify an
admittedly complex concept, signifiers (and the related
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Affordance">concept
of affordances</a>) are indicators that offer clues about how to
interact with new objects or situations. For example, a drawer handle’s
shape helps indicate to a user how they might interact with it (grab it
with their hand and pull to open).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Showing interactivity and clickability through signifiers is a
fundamental aspect of user interface design. In this lesson, we will
cover some of the high-level best practices for demonstrating
interaction and interactivity and some implementations using CSS.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Proceed to the next exercise when you are ready to continue.
</p>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Browser Link Styles

<p class="p__1qg33Igem5pAgn4kPMirjw">
Web browsers have always taken account of the importance of using
signifiers for navigation. By default, browsers include a <em>user agent
stylesheet</em>, a set of default styles included with the browser
(“user agent”) for use on all web pages. The HTML5 specification defines
a set of
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.w3.org/TR/html5/rendering.html">default
behavior for rendering content</a>. These styles are used to ensure that
a raw HTML file is styled to be reasonably readable by any user, and
user agent stylesheets include styling for headings, tables, links, and
more basic HTML elements. Most users do not see these styles too often,
because designers override them with their own custom designs. However,
it’s important to note that maintaining a consistent user experience
pattern, like the default behavior applied by browsers, is important for
creating a consistent experience.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Traditionally, links are differentiated from regular text using blue
text and underlines to draw users’ attention to their clickability. Many
websites and user agent stylesheets still use these link styles.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Browsers also style two other link states: clicked (‘active’), and
previously visited. In most user agent stylesheets, clicked (but not yet
followed) links appear with red text, and previously visited links are
styled with purple text.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
If you’d like to see the current state of styling, you can open
<strong>initial.css</strong>. The basic layout is okay, but, no links
are properly styled. Throughout this exercise, you’ll make all your
changes to <strong>style.css</strong>. Let’s start by reinstating some
of the classic browser link styles. First, add a CSS rule to make
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code> tags blue by
setting the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code>
property to <code class="code__2rdF32qjRVp7mMVBHuPwDS">blue</code> in
order to distinguish links.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Starting to look better already! Now, add an underline to the link text
inside <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code> tags
using the CSS
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration"><code class="code__2rdF32qjRVp7mMVBHuPwDS">text-decoration</code>
property</a>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Link Styling

<p class="p__1qg33Igem5pAgn4kPMirjw">
The most important aspect of styling links is differentiating links from
surrounding text. The default blue-text, underlined link style
accomplishes this differentiation using two CSS properties:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">text-decoration</code>. These
are both good ways to differentiate a link, and they are strong,
familiar signifiers to most web users. Additionally, you could use CSS
properties for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code>, or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">border</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Link styles should not be replicated in other page text. Link color
should sufficiently contrast the text colors in the rest of the design.
For example, if links are underlined, other text should not be.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Anchor_text">Anchor
text</a>, the text itself of a link, should be descriptive of the linked
resource. Although this is not strictly a design problem, it is
important for usability, accessibility, and
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Search_engine_optimization">SEO</a>.
For example, the link at the beginning of this paragraph would be much
more difficult to parse with a screen reader if it were re-written as
follows:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="markdown" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">Text for links, known as anchor text, should be </span><span class="mtk4">&lt;a</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk19">=</span><span class="mtk8">"https://en.wikipedia.org/wiki/Anchor_text"</span><span class="mtk1"> </span><span class="mtk7">rel</span><span class="mtk19">=</span><span class="mtk8">"noopener noreferrer"</span><span class="mtk1"> </span><span class="mtk7">target</span><span class="mtk19">=</span><span class="mtk8">"_blank"</span><span class="mtk4">&gt;</span><span class="mtk1">descriptive</span><span class="mtk4">&lt;/a&gt;</span><span class="mtk1">.</span></span><br></div></code></pre></pre>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s make the default link style match our color scheme a bit better.
Leave the underline, but change the link color to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#466995</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Tooltips and Titles

<p class="p__1qg33Igem5pAgn4kPMirjw">
In addition to providing descriptive anchor text, it is sometimes
helpful to provide additional context to explain links. This context can
be particularly helpful when a link contains or consists of an image,
icon, or another non-text element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Additional context can be provided as text using the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title">HTML
<code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code> attribute</a>.
Although the <code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code>
attribute can be provided to any HTML element, it is often extremely
useful as additional context or advisory text for clickable elements.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Most browsers will display the text of a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code> attribute as a
<a target="_blank" title="Wikipedia's entry to tooltips" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Tooltip">tooltip</a>,
meaning when a user hovers their cursor over an element, the text will
appear in a small box near the cursor.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To add tooltips to a clickable element like a link, add it as the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code> attribute.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;p&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;a</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">"https://www.codecademy.com"</span><span class="mtk1"> </span><span class="mtk7">title</span><span class="mtk1">=</span><span class="mtk8">"Codecademy is an online learning platform"</span><span class="mtk4">&gt;</span><span class="mtk1">Codecademy</span><span class="mtk4">&lt;/a&gt;</span><span class="mtk1"> is the best place to learn to code!</span></span><br><span><span class="mtk4">&lt;/p&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Mouse over the word “Codecademy” below to see this behavior in action!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<a target="_blank" title="Codecademy is an online learning platform" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com">Codecademy</a>
is the best place to learn to code!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>NOTE</strong>: The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code> attribute is
HTML’s built-in way of creating tooltips, but is known to
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title#accessibility_concerns">cause
a variety of accessibility issues</a>. Developers have come up with a
number of ways to create tooltips that are more accessible, but this
generally requires using CSS and JavaScript, which fall out of the scope
of this lesson. When creating tooltips in the wild, you should research
ways to make them accessible for everyone.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s add some clarifying information to links via tooltips and the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code> attribute. In
<strong>index.html</strong>, you can find three links within the text of
the first question that read “running,” “swimming,” and “biking.” Add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code> attribute to
each of these links to describe them.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Hover States and Cursors

<p class="p__1qg33Igem5pAgn4kPMirjw">
In addition to styling elements themselves, other signifiers and visual
feedback can be utilized during user interaction. The
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/:hover">CSS
pseudo-class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:hover</code></a> can be used
to style elements on mouse hover. For instance, to change the color of
link anchor text from blue to orange when a user hovers over it, the
following CSS could be used:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">a</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">a</span><span class="mtk9">:</span><span class="mtk4">hover</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">orange</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The first rule sets link colors to blue by default, and when a user
mouses over a link, the second rule will override the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> attribute of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code> tag and cause
the text to turn orange. When the user moves the cursor away from the
link, the text color will revert to blue.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In addition to any text style changes when hovering over a link, the
user’s cursor should change from the default appearance to a pointing
hand. The
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Examples">CSS
<code class="code__2rdF32qjRVp7mMVBHuPwDS">cursor</code> property</a> is
used to control this behavior. For example, to add this behavior to all
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code> tags, the
following rule could be used:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">a</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">cursor</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">pointer</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Luckily, this behavior is generally included in browser user agent
stylesheets, and it also exists in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.w3.org/TR/html5/rendering.html">HTML5
default styles</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Hover state styling should never be used as the sole indication that
something is a link. Users should not be forced to move their mouse over
an entire document to tell what might be clickable. Additionally, hover
states are not accessible in mobile browsers. Mobile devices do not
generally have on-screen cursors, and users must actually touch the
device (and possibly trigger a click event) to interact.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Time to add some hover styling to the page links. Add a rule to remove
the underline
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration"><code class="code__2rdF32qjRVp7mMVBHuPwDS">text-decoration</code>
property</a> on mouse hover. Keep the color the same so that the links
are still differentiated from other text.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Add a declaration to also change the cursor to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">pointer</code>. Even though
this behavior is seen when the mouse is hovered over, you should add it
to the rule for all
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code> tags, as the
browser will only change cursor styles on hover by default. Putting the
rule on an <code class="code__2rdF32qjRVp7mMVBHuPwDS">a:hover</code>
rule can cause unwanted behavior in some cases.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Link States

<p class="p__1qg33Igem5pAgn4kPMirjw">
Links have four main states: normal (not clicked), hover, active
(clicked), and visited. These four states have associated
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes">CSS
pseudo-classes</a>:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:link</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:hover</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:active</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:visited</code>. These four
states can be used to give a full range of visual feedback to users
about the status of their link interaction.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Each state should still make it clear that the element in question is a
link, meaning it should not make text identical to non-link text or
alter the link’s appearance so much that users could perceive its
behavior differently.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The ordering of link state pseudo-class rules is important to reveal the
proper information. When a user hovers and then clicks a link, those
styles should always override the static styling surrounding a user’s
history with the link (unvisited
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:link</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:visited</code>). The proper
order of these rules is:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:link</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:visited</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:hover</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:active</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This ordering will ensure that the rules
<a target="blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Cascade_and_inheritance">cascade
properly</a> and the user can receive the most applicable visual
feedback about the state of the link.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s add styling for different link states using pseudo-classes. Start
by creating a rule to set the color to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#466995</code> for any
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:visited</code>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code> tag.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Oops, if you click on any of the question links at the top of the page
and then scroll back up, you’ll notice that the links you’ve already
visited have now blended in with the background! These links are
internal to the page and serve to scroll the window, so we can eliminate
the separate <code class="code__2rdF32qjRVp7mMVBHuPwDS">:visited</code>
style. Create a rule to set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> of any
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:visited</code>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.question-link</code> class
elements to <code class="code__2rdF32qjRVp7mMVBHuPwDS">#ffffff</code>.
Because the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">question-link</code> class is
more specific than
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code> tags in general,
this rule should override.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now, let’s add some behavior to cover the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:active</code> states. Create
a rule to set all
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code> tags’ active
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#DBE9EE</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now, interact with the links to see the active state change. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.question-link</code>
elements at the top of the page may seem to be behaving oddly. Because
of the specificity of the class selector of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.question-link</code> versus
the tag selector of <code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code>,
question links aren’t triggering the same active behavior as all
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code> tags. They are,
however, showing their
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:visited</code> pseudo-class
if they’ve already been clicked. To remedy this, add a rule to style
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:active</code>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.question-link</code>s.
</p>

<span aria-live="assertive">Checkpoint 5 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Skeuomorphism and Flat Design

<p class="p__1qg33Igem5pAgn4kPMirjw">
Buttons are another fundamental element of user interaction and
navigation. They are called ‘buttons’ because they are often modeled on
the appearance and behavior of real-life buttons. The concept of UI
elements that replicate or imitate real-life counterparts is known as
<em>skeuomorphism</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In design, skeuomorphism is helpful for lowering the learning curve for
users. If users can draw a metaphor between a familiar real-life object
and an interface element, they are more likely to know how to use it
without training. In the example of the button, if a web button appears
similar to a real-life button on a physical interface, users can
reliably figure out that the way to interact with the button is to press
it.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Flat design</em> is an alternative approach to skeuomorphism which
embraces the fact that computer interfaces do not necessarily need to
model real-life interfaces. As users grow more familiar with digital
displays and interfaces, designers have felt less need to model physical
interactions and instead rely on other signifiers to indicate
interactive elements. To generalize, flat design uses simplicity and
lack of clutter for its UI elements.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
There are two contrasting buttons in the workspace. Interact with them
to see how their styling changes (they won’t actually execute any
actions, just change appearance). You can examine their styles in
<strong>style.css</strong> if you are interested.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When ready, click the <strong>Run</strong> button and move on to the
next exercise to implement some of these styles yourself.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Buttons: Skeuomorphic styling

<p class="p__1qg33Igem5pAgn4kPMirjw">
Skeuomorphic button design aims to imitate the appearance and
interactivity of a real-life button, often including a ‘raised’
appearance while the button is unpressed and a ‘pressed’ appearance when
clicked.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Skeuomorphic button design can be implemented using image files, CSS
rules, or a combination of both. CSS styles should be preferred over
image files if possible, since they are faster to load, have smaller
file sizes, and allow for a more consistent scaling and appearance
across different screen sizes and resolutions. Modern CSS3 has support
for many 2-D and 3-D effects and animations and can create many
skeuomorphic button designs on its own.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If using CSS rules, the use of hover and/or active states is important
in order to model interaction with a real button. For example, to
implement a bare minimum 3-D button design, the following CSS ruleset
could be used:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">button</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 5px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 1px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">black</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-radius</span><span class="mtk1">:</span><span class="mtk9"> 5px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">text-decoration</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">none</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">box-shadow</span><span class="mtk1">:</span><span class="mtk9"> 0px 5px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">button</span><span class="mtk9">:</span><span class="mtk4">hover</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">cursor</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">pointer</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">button</span><span class="mtk9">:</span><span class="mtk4">active</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin-top</span><span class="mtk1">:</span><span class="mtk9"> 5px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">black</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">box-shadow</span><span class="mtk1">:</span><span class="mtk9"> 0px 0px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A button element can then be created with the following HTML:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;button&gt;</span><span class="mtk1">Click me</span><span class="mtk4">&lt;/button&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The default state of this
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<button\></code> has some
basic ‘buttony’ appearance with a rounded border
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">border</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">border-radius</code>
properties) and a slightly raised appearance with the use of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">box-shadow</code>. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:hover</code> cursor is added
for visual feedback. When the button is clicked
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">:active</code>), the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">box-shadow</code> is removed,
and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-top</code>
moves the button down by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">5px</code>, making it appear
to be pressed.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The above example is only one very basic implementation of a 3-D button;
there are many additional (and more attractive) ways to create
skeuomorphic buttons.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s update the buttons on the page to have a raised appearance.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Start by creating a rule that will apply to all elements with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.answer</code> class. Set a
1-pixel, solid
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/border">border</a>
with the color
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#466995</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Add a small
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius">border-radius</a>
to all corners of <code class="code__2rdF32qjRVp7mMVBHuPwDS">10px</code>
in order to round the edges.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Add a
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow">box-shadow</a>
to give the button a raised appearance. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">box-shadow</code> should have
an <code class="code__2rdF32qjRVp7mMVBHuPwDS">offset-x</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0px</code> and an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">offset-y</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">4px</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now, let’s alter the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:active</code> state to make
the button appear to depress downwards when clicked.
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-top</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">24px</code> and the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-bottom</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">16px</code>. This will make
the button appear to move downward.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">box-shadow</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0px 0px</code>. This will
make the box-shadow disappear.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, change the color styling so that the button offers some additional
visual feedback:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#C0D6DF</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#ffffff</code>
</li>
</ul>

<span aria-live="assertive">Checkpoint 5 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Buttons: Flat Design

<p class="p__1qg33Igem5pAgn4kPMirjw">
Flat design is so-called because of its 2-D appearance. Elements appear
flat on the screen, and designers must rely on other styling and
signifiers to indicate clickability.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Flat design buttons commonly appear as rectangles, rounded rectangles,
or circles. These shapes are used ubiquitously for button elements, so
users often perceive them as buttons and expect them to be clickable.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Since there are fewer obvious signifiers surrounding buttons in a flat
design, they should be visually distinct from other page elements.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In flat designs in particular, button text is very important for
clarity—the possibility of user confusion is reduced by pairing buttons
with specific, descriptive labels. A button with ‘Click here’ leaves
many more open questions than a button that reads ‘Submit form’.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ve reset the button styling so that we can quickly create a flat
style.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Begin by creating a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.answer</code> ruleset, and
then, add in a rule for a solid, one-pixel border with the color
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#466995</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now add some <code class="code__2rdF32qjRVp7mMVBHuPwDS">:active</code>
state styles for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">answer</code> class.
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#C0D6DF</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Set the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#ffffff</code>.
</li>
</ul>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Buttons: Hover States

<p class="p__1qg33Igem5pAgn4kPMirjw">
Just as with links, buttons should make use of hover states and the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">cursor: pointer</code>
declaration. All the caveats about the shortcomings of hover states on
mobile devices apply to buttons, but their use is still encouraged.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Users expect buttons to be clickable. Since buttons can consist of any
number of total elements (rectangular/circular body, text, image(s)),
all elements should be clickable, should display their clickability, and
should result in the same behavior.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s make sure all the buttons have correct hover states. Currently,
our <code class="code__2rdF32qjRVp7mMVBHuPwDS">answer:active</code>
rules change both the background-color and the text color of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">answer</code> class elements.
Let’s split these up so that there are two stages of interaction.
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Create a new rule for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">answer:hover</code> that sets
the background color to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#C0D6DF</code> and remove the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code>
declaration from your
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.answer:active</code> rule.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Make sure that the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:hover</code> rule comes
before the <code class="code__2rdF32qjRVp7mMVBHuPwDS">:active</code>
rule so that the styles cascade correctly.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN LINKS AND BUTTONS

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great work! You’ve made this survey site much easier to understand and
interact with! Let’s review what changes you made to improve usability:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Added styles to make links recognizable and distinguishable from
ordinary text.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Added link styles that depend upon mouse interaction state, providing
users with visual feedback for cursor hovering and mouse clicks.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Added additional context text with the HTML
<code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code> attribute.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Styled buttons to be easily recognizable (in both skeuomorphic and flat
design styles) using box shapes, border, hover, and active states.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember that the styles that you implemented here are only one of
countless ways to communicate clickability and provide users with visual
feedback. There is a huge amount of opportunity for variety and
creativity while still following best practices and common user
experience patterns.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Congratulations! Feel free to continue tweaking or improving the style
in the workspace or move on when you’re ready.
</p>

**Solutions**

``` html
```

## Affordances, Signifiers, and Clickability

<h3 id="heading-clickability" class="h3__3B1DSzXTW-ux1viDSStOux">
Clickability
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For users on the web, the mouse click is perhaps the most fundamental
human-computer interaction. The web <em>became</em> the web partially
through the power of <em>hypertext</em>, or text in one document that
links to other documents or resources. To this day, users navigate the
web largely through mouse clicks (and finger taps on mobile and tablet
devices).
</p>
<h3 id="heading-affordances" class="h3__3B1DSzXTW-ux1viDSStOux">
Affordances
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Objects <em>afford</em> the ability of users to interact with them in
various ways. For instance, a bench affords a person the ability to sit
on it, but if it is not affixed to the ground, it also affords the user
the ability to turn it over, throw (if the user is physically able), or
perform any number of other actions. Even though the designer was
probably not designing the bench with throwing in mind as the primary
user behavior, the object still affords this action. Potentials for
interaction are collectively called the <em>affordances</em> of an
object.
</p>
<h3 id="heading-signifiers" class="h3__3B1DSzXTW-ux1viDSStOux">
Signifiers
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Signifiers</em> are aspects of an object that a designer uses to
indicate potential and intended affordances of an object. For example, a
teacup with no handle affords the ability to lift it and drink out of
it. But designers and potters often add handles to <em>signify</em> that
users can and should lift up the object and take a sip. The handle is an
example of a common <em>user experience pattern</em>.
</p>
<h3 id="heading-ux-patterns" class="h3__3B1DSzXTW-ux1viDSStOux">
UX Patterns
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
User experience (UX) patterns establish reusable solutions to common
problems. Handles are ubiquitous—they are used on objects of all shapes,
sizes, and purposes to indicate that users can initiate an action by
grabbing the handle with their hand(s).
</p>
<h3 id="heading-affordances-and-signifiers-in-web-design" class="h3__3B1DSzXTW-ux1viDSStOux">
Affordances and Signifiers in Web Design
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In computer interactions, the possible affordances of any computer are
usually relatively limited. Consider a web application in a browser—a
user can essentially click, execute key commands or type, and
potentially execute touch events or voice commands. Because of the
relatively limited range of affordances, using proper signifiers is
especially important to direct users properly. Users can click anywhere
on a page, but not every click will have a result. Often, websites and
applications use a combination of visual feedback and common UX patterns
to help solve this issue. In web browsers, one common example of visual
feedback is the cursor image itself: it can demonstrate what behavior
might be expected from a click: a pointing hand indicating that an
interaction will occur, an i-beam shape indicating that text can be
selected, a four-directional arrow showing that an element can be moved,
and
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/cursor">many
more cursor styles and interactions</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As stated above, the hovering, pointing hand cursor is a nearly
universal pattern to indicate that an element or text is clickable. But
users do not want to hover a cursor over every element to determine if
it is clickable, and mobile devices do not even have the ability to
hover a cursor! For this reason, designers also use signifiers to
demonstrate elements that afford interaction. On the web, these
signifiers come in the form of CSS styles that differentiate clickable
from non-clickable elements. A ubiquitous example is the styling of
hyperlinks—hyperlinks should be easily differentiated from other text in
a block by different colors, underline styles, or font weights.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There is no universal “right answer” to the issues surrounding
signifiers and affordances on the web, but web designers should always
keep these ideas in mind while creating web designs and interfaces.
</p>
<h3 id="heading-further-reading" class="h3__3B1DSzXTW-ux1viDSStOux">
Further Reading
</h3>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.jnd.org/dn.mss/signifiers_not_affordances.html">Signifiers,
Not Affordances</a> by Don Norman. This article discusses a bit of the
history of thought around affordances and signifiers, and their
importance in design.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="http://ui-patterns.com/">UI
Patterns.com</a> has many examples of solutions to common design
patterns in web design.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Want to learn more? Check out our
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/catalog/subject/web-design">courses
on web design</a>.
</p>

## WEB DEVELOPMENT FOUNDATIONS

### The Summit

<p class="p__1qg33Igem5pAgn4kPMirjw">
Time to put some navigation design knowledge to the test! Your goal is
to improve the user experience of this ski lodge landing page.
Currently, none of the clickable elements are very clear or offer good
visual feedback to users.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The exact implementation and styling will be up to you; take the
opportunity to be creative in your designs! Keep in mind that slick
styling is cool, but it is just as important to clearly demonstrate to
users how to interact with the site. We’ll provide some hints along the
way if you’re stuck.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

## LEARN SECONDARY NAVIGATION

### Introduction

<p class="p__1qg33Igem5pAgn4kPMirjw">
Consider the website to the right. We can see that the site is listing
hotels in Singapore. Do you know if this site offers any other
categories of travel products (tours, flights, experiences) or products
in other regions? There is no way to tell from the current view.
</p>
<h5 id="heading-what-is-primary-vs-secondary-navigation">
What is primary vs secondary navigation?
</h5>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
The primary navigation system typically contains the most important
links and buttons that need to be displayed on every single page of the
site.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Secondary navigation, or breadcrumb navigation, usually consists of a
clickable list of pages or attributes that led to the current page. It
can help users understand the extent of the site and also where they are
currently.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, a shopping site may have a breadcrumb trail leading to a
pair of shoes like so:
</p>

<img src="https://content.codecademy.com/courses/ui-breadcrumbs/UI_breadcrumb.svg" class="img__1JGFO2nlisObc3KeOSGPRp">

</li>
</ul>
<h5 id="heading-why-do-we-call-them-breadcrumbs">
Why do we call them breadcrumbs?
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Think about the story of Hansel and Gretel, where the kids drop
breadcrumbs as they walked in the woods so that they would be able to
find their way back.
</p>
<h5 id="heading-benefit-of-using-breadcrumbs">
Benefit of using breadcrumbs
</h5>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Breadcrumb navigation provides a lot of benefits for users that come to
random pages in a website through direct links or search results. Even
if they enter to a seemingly random page on our site, they already have
an idea of where they are in the website. The breadcrumb also hints at
the extent of the site. For the example above, users could safely assume
the site had shoes for other categories, shoes in different styles, and
shoes in more colors.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Breadcrumbs also provide a way for a user to quickly jump backward in
their navigation of the site. For example, if a user wanted to browse
another style of shoe, they could click directly on the “Shoes” page and
navigate to their desired style. Without the breadcrumbs, they would
likely need to click “back” twice in their browser or start their search
over from the home page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The decision to use breadcrumbs is a judgment call depending on the
type, depth, and complexity of your site. In this lesson, we’ll discuss
some of the benefits of including breadcrumb navigation, how to
implement it using HTML and CSS, and some of the pitfalls to avoid.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Proceed to the next exercise when you are ready to continue.
</p>

**Solutions**

``` html
```

## LEARN SECONDARY NAVIGATION

### Simple Example of Breadcrumbs

<p class="p__1qg33Igem5pAgn4kPMirjw">
As you saw in the introduction, it is difficult to understand where you
are on a website that lacks breadcrumb navigation. By adding it to a
site, users can get a quick feel for where they are on a site.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It also hints at the breadth of the site. If a user sees something like
“Fashion \> Shoes” in the breadcrumb structure, they could reasonably
expect the site contains other clothing items or accessories besides
shoes.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Breadcrumbs are usually displayed as a horizontal list of pages and take
up minimal space. Users expect to find them in the header, left-aligned,
and below any primary navigation. Typically they are separated with a
“\>” or a “/“ symbol.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s practice setting CSS rules to conform to the expectations for
breadcrumb navigation. You will start with a plain looking list, but by
the end you will have created a breadcrumb!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Breadcrumbs are typically displayed next to each other, on the same
line. First, set the display property to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">inline</code> for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.breadcrumb \> li</code>
selector in order to put list items on the same line.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Another common feature of breadcrumbs is that they are separated by a
symbol, often <strong>\></strong> or <strong>/</strong>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Instead of having to manually add this to all of the breadcrumbs in our
breadcrumb trail, we can use a CSS pseudo-element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This requires some complicated CSS, but it will save us time in the long
run!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.breadcrumb
li+li::before</code> is the selector that we want! View the hint if you
want more information about how this complicated selector works!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <code class="code__2rdF32qjRVp7mMVBHuPwDS">styles.css</code>, find
the selector (<code class="code__2rdF32qjRVp7mMVBHuPwDS">.breadcrumb
li+li::before</code>). Set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">content</code> property to
“\>” to place the greater than sign between each adjacent breadcrumb.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Another feature of breadcrumbs is that they are often not underlined.
Underlines are used to communicate that text within paragraph elements
can be clicked, but we want our users to recognize breadcrumbs as part
of the site navigation, rather than just like any other clickable text.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remove the link underline by changing the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">text-decoration</code>
property of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">breadcrumb
a</code> selector to have the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">none</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Breadcrumbs should change when you hover over them to highlight their
clickability.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Change the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code>
property of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.breadcrumb
a:hover</code> selector to have the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">red</code>.
</p>

<span aria-live="assertive">Checkpoint 5 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN SECONDARY NAVIGATION

### Where do Breadcrumbs Lead

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous examples, if you clicked on any of the breadcrumbs, it
wouldn’t take you to a new page. This is because we have set
<code class="code__2rdF32qjRVp7mMVBHuPwDS">href=“\#”</code>. With this
value, a click on the link will cause the page to scroll to the top of
the current page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In a full site, these breadcrumbs would link to their respective pages.
This is accomplished by setting the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> property to the
appropriate page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Since breadcrumbs are typically relative to the current page, the
breadcrumb list on each page needs to be different. However, as a user
moves around the breadcrumb list, they should expect the breadcrumb
style and list to stay consistent.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, if the breadcrumb list was:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Fashion \> Shoes \> Flats \>
Brown</code>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
and a user clicked on “Flats”, the breadcrumb list on that page should
look like:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Fashion \> Shoes \>
Flats</code>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It would be confusing for a user if the categories or order of them
changed like:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Shoes \> Shopping \>
Flats</code>
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The code on the right has a simple breadcrumb structure implemented.
However, these breadcrumbs don’t link anywhere.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Within <strong>brownshoes.html</strong>, update the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> property for the
breadcrumb links so they link to the correct pages. Our other pages are
within the same directory as <strong>brownshoes.html</strong> so you
won’t need to add any additional path:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
shoes -\> <strong>shoes.html</strong>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
flats -\> <strong>flats.html</strong>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
brown -\> leave this as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘\#’</code> since we are
already on that page
</li>
</ul>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Using the breadcrumbs we can now navigate to the generic flats and shoes
pages.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now these pages need an appropriate breadcrumb list.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Add breadcrumbs to <strong>flats.html</strong> with links to the
appropriate pages.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Add breadcrumbs to <strong>shoes.html</strong> with links to the
appropriate pages. Since “shoes” is the starting breadcrumb, this page
will only have one breadcrumb that links to this page
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘\#’</code>).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This single breadcrumb may not look useful, but users expect the site to
stay consistent.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN SECONDARY NAVIGATION

### Where am I?

<p class="p__1qg33Igem5pAgn4kPMirjw">
This provides a basic breadcrumb structure that will display like the
image below:
<img src="https://content.codecademy.com/courses/ui-breadcrumbs/simpleBreadcrumb.png" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the exercises, you will replicate this behavior for our travel
website.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the code to the right, we’ve included the page “Singapore Hotels”. It
currently has no breadcrumbs - you’ll be adding them!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The first step is to create an HTML unordered list within
<strong>index.html</strong> below the jumbotron div. The list should
have the class of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">“breadcrumb”</code> and the
list items should be “Asia”, “Singapore”, “Tourism”, and “Hotels”.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For now, set the breadcrumb items to link to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">“\#”</code>.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Add CSS to <strong>breadcrumb.css</strong> to configure the display of
the breadcrumbs. (We’ve already added a bit of CSS to remove some of the
existing styling within <strong>style.css</strong>).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can style the breadcrumbs how you like, but at a minimum, it should
set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.breadcrumb li</code>
elements to display inline and you should use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.breadcrumb
li+li::before</code> selector to insert a “\>” between the items.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you’d like to see our approach, please look in the hint.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN SECONDARY NAVIGATION

### Breadcrumb Styles

<p class="p__1qg33Igem5pAgn4kPMirjw">
The previous exercise demonstrated the most basic styling for
breadcrumbs. When designing your own site, you’ll need to make a
judgment call if this approach is sufficient. If you want to invite the
user to interact with the breadcrumbs, you can style them to make them a
more prominent part of the page design.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The example below makes use of a couple of CSS tricks to create an arrow
effect. We’re using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">::before</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">::after</code>
pseudo-elements to add filled rectangles (with empty content) before and
after each list item:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">li</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">::</span><span class="mtk4">before</span><span class="mtk1">,</span><span class="mtk9"> </span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">li</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">::</span><span class="mtk4">after</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">content</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">""</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">absolute</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">darkcyan</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-style</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">solid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-width</span><span class="mtk1">:</span><span class="mtk9"> 15px 5px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By setting a portion of the border to transparent, it creates the “tail”
of the arrow:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">li</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">::</span><span class="mtk4">before</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">left</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">-</span><span class="mtk9">10px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-left-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">transparent</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This effect works because the element borders are drawn from the center
of the element. We use similar CSS to draw the head of the arrow.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ll walk through the individual steps in the exercises so you can see
how each step affects the resulting look.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the pane to the right, <strong>breadcrumb.css</strong> contains the
styles from our previous breadcrumb implementation. Remove the existing
“\>” symbols from between the list items.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Replace the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.breadcrumb
a</code> CSS section with:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk4">#fff</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">darkcyan</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">text-decoration</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">none</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">relative</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 30px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">line-height</span><span class="mtk1">:</span><span class="mtk9"> 30px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">text-align</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">center</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin-right</span><span class="mtk1">:</span><span class="mtk9"> 15px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 0&nbsp;5px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Change the existing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.breadcrumb li</code> from
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display: inline</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">float: left</code>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">li</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">float</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">left</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the browser, you should see that we have created the “body” of the
arrows.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, we create the before and after pseudo-elements. Copy the following
CSS and see how it affects the output:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">::</span><span class="mtk4">before</span><span class="mtk1">,</span></span><br><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">::</span><span class="mtk4">after</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">content</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">""</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">absolute</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">darkcyan</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-style</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">solid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-width</span><span class="mtk1">:</span><span class="mtk9"> 15px 5px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll notice that we have added pseudo-elements, but they are on top of
our existing elements.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The total width of our pseudo-elements is 10px, since the border has 5px
on the left and 5px on the right. Given this, move the pseudo-elements
to the proper location using the following CSS:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">::</span><span class="mtk4">before</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">left</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">-</span><span class="mtk9">10px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">::</span><span class="mtk4">after</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">left</span><span class="mtk1">:</span><span class="mtk9"> 100%</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>

<span aria-live="assertive">Checkpoint 5 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">5.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The last step is to use the CSS trick to turn these into arrows. Style
the after elements as “heads” by setting the border color to transparent
except for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">border-left-color</code>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">::</span><span class="mtk4">after</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">left</span><span class="mtk1">:</span><span class="mtk9"> 100%</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">transparent</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-left-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">darkcyan</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>

<span aria-live="assertive">Checkpoint 6 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">6.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Style the before elements as “tails” by setting the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">border-left-color</code> to
transparent for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:before</code> elements.
</p>

<span aria-live="assertive">Checkpoint 7 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">7.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
These breadcrumbs are looking how we want, but lets add a hover state
for a little more style:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">:</span><span class="mtk4">hover</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">:</span><span class="mtk4">hover</span><span class="mtk9">::</span><span class="mtk4">before</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-left-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">transparent</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span class="mtk7">.breadcrumb</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">:</span><span class="mtk4">hover</span><span class="mtk9">::</span><span class="mtk4">after</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-left-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>

<span aria-live="assertive">Checkpoint 8 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN SECONDARY NAVIGATION

### Breadcrumb Types

<p class="p__1qg33Igem5pAgn4kPMirjw">
There are three major types of breadcrumbs:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Location
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Attribute
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Path
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ve seen the first two types in our examples so far.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Location</strong> based breadcrumbs are based on where you are
with respect to the navigation structure of the website. In our previous
shoe shopping example, the first three
<code class="code__2rdF32qjRVp7mMVBHuPwDS">li</code> elements are
location based. We are in the “shoes” section of the website, which is
contained within the “fashion” section, which is contained within the
“shopping” section.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Attribute</strong> based breadcrumbs are based on the attributes
of the page or product that you are browsing. In our previous example,
the final two <code class="code__2rdF32qjRVp7mMVBHuPwDS">li</code>
elements are attribute based. We are shopping for shoes that are “flats”
and “brown”. Since the order of these attributes is not prescriptive,
you’ll see some sites display these at the same level in the UI. If you
want to allow users to remove attributes, provide an (x) button or
similar to indicate they can be removed.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Finally, breadcrumbs can be based on a user’s unique
<strong>path</strong> through the site. For example, if they landed on
the home page, browsed to the about page and finally the registration
page, their breadcrumb trail may look like:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Home \> About \>
Register</code>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note that this breadcrumb trail will be different for each user and each
visit. For even mildly complex sites, the number of steps will become
large. To simplify the display, the beginning of the trail is often
abbreviated:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">… \> About \> Register</code>
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the pane to the right, we have the basic breadcrumbs structure for
the travel website. We’ve added a couple of attribute based breadcrumbs.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">attribute</code> class
to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">li</code> elements
that are attribute based and a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">location</code> class to the
breadcrumbs that are location based.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Modify the CSS to only put the “\>” character between location based
breadcrumbs.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Color the “attribute” anchor tags gray to indicate that they are
different than the “location” ones.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Add a “close” indication using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">:after</code> pseudoselector:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.attribute</span><span class="mtk9"> </span><span class="mtk4">a</span><span class="mtk9">::</span><span class="mtk4">after</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">content</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">" x"</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-size</span><span class="mtk1">:</span><span class="mtk9"> 8px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">vertical-align</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">super</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note that this functionality has not been implemented, we are focused on
the display of the page only.
</p>

<span aria-live="assertive">Checkpoint 5 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

**Solutions**

``` html
```

## LEARN SECONDARY NAVIGATION

### Breadcrumb Pitfalls

<p class="p__1qg33Igem5pAgn4kPMirjw">
Sometimes it is not appropriate to use breadcrumbs as a means of
secondary navigation within a website. Users expect breadcrumbs to
behave a certain way and attempts to deviate from this may confuse them.
Most users are expecting breadcrumbs to expose the hierarchy of the site
or display attributes of the page they are on.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Path based breadcrumbs are unique to a user’s journey and are not
commonly implemented. Only use this type of breadcrumbs if there is a
compelling reason for it.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
While breadcrumbs are common, it is not the primary way users will
navigate a site. Don’t make the breadcrumbs the only navigation
structure.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In general, the rule of not adding anything extraneous to the design
applies here. If the site only contains a few pages or if the pages in
the breadcrumbs are already available through primary navigation, there
is little reason to include breadcrumbs in the design.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a moment to observe how we’ve implemented breadcrumbs in the
mini-browser.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After you’ve taken note of your observations, continue to the next
exercise.
</p>

**Solutions**

``` html
```

## LEARN SECONDARY NAVIGATION

### Summary

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson we covered the concept of using breadcrumbs as a
secondary navigation method for a site:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Use breadcrumbs to indicate where a user is and the extent of the site
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Breadcrumbs are implemented using unordered lists in HTML with custom
CSS styling
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Three types of breadcrumbs exist:
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>location</strong> - based on hierarchical structure of site
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>attribute</strong> - based on attributes of current page or item
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>path</strong> - unique to a user’s journey on the site
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Path-based breadcrumbs can be confusing, only use if needed
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Ensure breadcrumbs will add value before adding to a site
</li>
</ul>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Our completed styled breadcrumbs are shown on the right.
</p>

**Solutions**

``` html
```

## WEB DEVELOPMENT FOUNDATIONS

### FreshDeals: Blueberries

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the browser to the right, you should see a site for buying groceries.
The currently selected product is “Organic Blueberries”. If you landed
on this page, you may have some questions.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Can I buy anything besides blueberries?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Is everything on this site organic or can I buy conventional produce?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Does this site offer non-produce items?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By adding breadcrumbs to this site, you will be adding a UI element that
hints to some of the questions above. By doing so, users will have a
better feeling for what the site provides and the optional attributes of
the product they are purchasing.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We are focused on the layout of this page and will be implementing the
breadcrumbs via HTML and CSS. The links to the breadcrumbs will not
function.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Check off the project steps as you complete them.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

## What are Wireframes?

<iframe frameborder="0" allowfullscreen="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" title="What are wireframes?" width="100%" height="100%" src="https://www.youtube.com/embed/CbIMO5EcCD8?autoplay=0&amp;mute=0&amp;controls=1&amp;origin=https%3A%2F%2Fwww.codecademy.com&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;iv_load_policy=3&amp;modestbranding=1&amp;enablejsapi=1&amp;widgetid=1" id="widget2" data-gtm-yt-inspected-76="true">
</iframe>

## From Design to Website

<iframe frameborder="0" allowfullscreen="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" title="From Design to Website" width="100%" height="100%" src="https://www.youtube.com/embed/XTMYbqJaEOY?autoplay=0&amp;mute=0&amp;controls=1&amp;origin=https%3A%2F%2Fwww.codecademy.com&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;iv_load_policy=3&amp;modestbranding=1&amp;enablejsapi=1&amp;widgetid=1" id="widget2" data-gtm-yt-inspected-76="true">
</iframe>

## Everything You Need to Know about Wireframes and Prototypes

<p class="p__1qg33Igem5pAgn4kPMirjw">
→
<strong><a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://theblog.adobe.com/everything-you-need-to-know-about-wireframes-and-prototypes/">Everything
You Need to Know about Wireframes and Prototypes</a></strong>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this article, you will learn about wireframes and prototypes: what
they are, why they’re useful and how they’re involved with the user
experience design process. This is helpful if you’d like to understand
the design process before development and how multiple iterations of a
design must be critiqued and revised in order to present the ideal
product to the user. After you finish reading the article, return to
this page and complete the following assessments.
</p>

<svg viewBox="0 0 1000 1000" height="24" width="24" aria-label="Loading assessment">
<title>
Spinner
</title>
<circle fill="currentColor" cx="937.5" cy="500" r="62.5"></circle><path fill="currentColor" d="M1000 500H875c0-22.2-1.9-44-5.6-65.1l123.1-21.7h.1c4.8 28.2 7.4 57.2 7.4 86.8z"></path><path opacity=".96" fill="currentColor" d="M992.5 413.2l-123.1 21.7c-3.8-21.8-9.5-42.9-16.9-63.2L969.9 329l.1-.1c9.8 27.1 17.4 55.2 22.5 84.3z"></path><path opacity=".92" fill="currentColor" d="M969.9 328.9l-.1.1-117.3 42.7c-7.5-20.6-16.8-40.4-27.7-59.2L933 249.9l.1-.1a503.3 503.3 0 0 1 36.8 79.1z"></path><path opacity=".88" fill="currentColor" d="M933.1 249.9l-108.2 62.6c-10.9-18.9-23.6-36.9-37.6-53.5l95.7-80.4c18.7 22.2 35.4 46.1 50.1 71.3z"></path><path opacity=".84" fill="currentColor" d="M883 178.6L787.3 259c-14.1-16.7-29.5-32.2-46.2-46.2l80.3-95.8c22.3 18.7 42.9 39.3 61.6 61.6z"></path><path opacity=".8" fill="currentColor" d="M821.4 116.9L741 212.7c-16.7-14-34.6-26.6-53.5-37.6l62.4-108.2.1-.1c25.3 14.8 49.2 31.5 71.4 50.1z"></path><path opacity=".76" fill="currentColor" d="M750.1 66.9l-62.5 108.2c-18.8-10.9-38.6-20.1-59.2-27.7L671 30.1l.1-.1c27.5 10.1 53.9 22.4 79 36.9z"></path><path opacity=".72" fill="currentColor" d="M671.1 30l-.1.1-42.7 117.4c-20.3-7.4-41.4-13.1-63.2-16.9l21.7-123v-.1c29.1 5.1 57.2 12.7 84.3 22.5z"></path><path opacity=".68" fill="currentColor" d="M586.8 7.5l-21.7 123.1c-21.1-3.7-42.9-5.6-65.1-5.6V0c29.6 0 58.6 2.6 86.8 7.5z"></path><path opacity=".64" fill="currentColor" d="M500 0v125c-22.2 0-44 1.9-65.1 5.6l-21.7-123v-.1C441.4 2.6 470.4 0 500 0z"></path><path opacity=".6" fill="currentColor" d="M413.2 7.6l21.7 123.1c-21.8 3.8-42.9 9.5-63.2 16.9L329 30.1l-.1-.1c27.1-9.9 55.2-17.4 84.3-22.4z"></path><path opacity=".56" fill="currentColor" d="M329 30.1l42.7 117.4c-20.6 7.5-40.4 16.8-59.2 27.7L250 67l-.1-.1C275 52.4 301.4 40.1 329 30.1z"></path><path opacity=".04" fill="currentColor" d="M371.7 852.5L329 969.9l-.1.1c-27.6-10-53.9-22.4-79-36.9l.1-.1 62.5-108.2c18.7 10.9 38.6 20.1 59.2 27.7z"></path><path opacity=".52" fill="currentColor" d="M250 67l62.5 108.2c-18.9 11-36.9 23.6-53.5 37.6L178.6 117c22.2-18.7 46.1-35.4 71.4-50z"></path><path opacity=".08" fill="currentColor" d="M312.5 824.8L250 933l-.1.1c-25.2-14.6-49.1-31.4-71.4-50.1l80.4-95.7c16.7 13.9 34.6 26.6 53.6 37.5z"></path><path opacity=".48" fill="currentColor" d="M178.6 117l80.4 95.8c-16.7 14.1-32.2 29.5-46.2 46.2L117 178.6c18.7-22.3 39.3-42.9 61.6-61.6z"></path><path opacity=".12" fill="currentColor" d="M258.9 787.2L178.6 883c-22.3-18.7-42.9-39.3-61.6-61.6l95.8-80.3c14 16.7 29.4 32.1 46.1 46.1z"></path><path opacity=".44" fill="currentColor" d="M117 178.6l95.8 80.4c-14 16.6-26.6 34.5-37.6 53.5L67 250l-.1-.1c14.7-25.2 31.4-49.1 50.1-71.3z"></path><path opacity=".16" fill="currentColor" d="M212.8 741.1L117 821.4c-18.7-22.2-35.4-46.1-50.1-71.4l.1-.1 108.2-62.4c11 19 23.6 36.9 37.6 53.6z"></path><path opacity=".4" fill="currentColor" d="M67 250l108.2 62.5c-10.9 18.8-20.1 38.6-27.7 59.2L30.1 329l-.1-.1c10-27.6 22.4-53.9 36.9-79l.1.1z"></path><path opacity=".2" fill="currentColor" d="M175.2 687.6L67 750l-.1.1C52.4 725 40 698.7 30 671.1l.1-.1 117.4-42.7c7.6 20.6 16.8 40.5 27.7 59.3z"></path><path opacity=".36" fill="currentColor" d="M30.1 329l117.4 42.7c-7.4 20.3-13.1 41.4-16.9 63.2l-123-21.7h-.1c5.1-29 12.6-57.2 22.5-84.2h.1z"></path><path opacity=".24" fill="currentColor" d="M147.5 628.3L30.1 671l-.1.1c-9.9-27.1-17.4-55.2-22.5-84.2h.1l123.1-21.7c3.7 21.7 9.4 42.8 16.8 63.1z"></path><path opacity=".32" fill="currentColor" d="M7.6 413.2l123.1 21.7c-3.7 21.1-5.6 42.9-5.6 65.1H0c0-29.6 2.6-58.6 7.6-86.8z"></path><path opacity=".28" fill="currentColor" d="M130.6 565.1l-123 21.7h-.1A506.7 506.7 0 0 1 0 500h125c0 22.2 1.9 44 5.6 65.1z"></path><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="1s" begin="0" repeatCount="indefinite"></animateTransform>
</svg>

<svg viewBox="0 0 1000 1000" height="24" width="24" aria-label="Loading assessment">
<title>
Spinner
</title>
<circle fill="currentColor" cx="937.5" cy="500" r="62.5"></circle><path fill="currentColor" d="M1000 500H875c0-22.2-1.9-44-5.6-65.1l123.1-21.7h.1c4.8 28.2 7.4 57.2 7.4 86.8z"></path><path opacity=".96" fill="currentColor" d="M992.5 413.2l-123.1 21.7c-3.8-21.8-9.5-42.9-16.9-63.2L969.9 329l.1-.1c9.8 27.1 17.4 55.2 22.5 84.3z"></path><path opacity=".92" fill="currentColor" d="M969.9 328.9l-.1.1-117.3 42.7c-7.5-20.6-16.8-40.4-27.7-59.2L933 249.9l.1-.1a503.3 503.3 0 0 1 36.8 79.1z"></path><path opacity=".88" fill="currentColor" d="M933.1 249.9l-108.2 62.6c-10.9-18.9-23.6-36.9-37.6-53.5l95.7-80.4c18.7 22.2 35.4 46.1 50.1 71.3z"></path><path opacity=".84" fill="currentColor" d="M883 178.6L787.3 259c-14.1-16.7-29.5-32.2-46.2-46.2l80.3-95.8c22.3 18.7 42.9 39.3 61.6 61.6z"></path><path opacity=".8" fill="currentColor" d="M821.4 116.9L741 212.7c-16.7-14-34.6-26.6-53.5-37.6l62.4-108.2.1-.1c25.3 14.8 49.2 31.5 71.4 50.1z"></path><path opacity=".76" fill="currentColor" d="M750.1 66.9l-62.5 108.2c-18.8-10.9-38.6-20.1-59.2-27.7L671 30.1l.1-.1c27.5 10.1 53.9 22.4 79 36.9z"></path><path opacity=".72" fill="currentColor" d="M671.1 30l-.1.1-42.7 117.4c-20.3-7.4-41.4-13.1-63.2-16.9l21.7-123v-.1c29.1 5.1 57.2 12.7 84.3 22.5z"></path><path opacity=".68" fill="currentColor" d="M586.8 7.5l-21.7 123.1c-21.1-3.7-42.9-5.6-65.1-5.6V0c29.6 0 58.6 2.6 86.8 7.5z"></path><path opacity=".64" fill="currentColor" d="M500 0v125c-22.2 0-44 1.9-65.1 5.6l-21.7-123v-.1C441.4 2.6 470.4 0 500 0z"></path><path opacity=".6" fill="currentColor" d="M413.2 7.6l21.7 123.1c-21.8 3.8-42.9 9.5-63.2 16.9L329 30.1l-.1-.1c27.1-9.9 55.2-17.4 84.3-22.4z"></path><path opacity=".56" fill="currentColor" d="M329 30.1l42.7 117.4c-20.6 7.5-40.4 16.8-59.2 27.7L250 67l-.1-.1C275 52.4 301.4 40.1 329 30.1z"></path><path opacity=".04" fill="currentColor" d="M371.7 852.5L329 969.9l-.1.1c-27.6-10-53.9-22.4-79-36.9l.1-.1 62.5-108.2c18.7 10.9 38.6 20.1 59.2 27.7z"></path><path opacity=".52" fill="currentColor" d="M250 67l62.5 108.2c-18.9 11-36.9 23.6-53.5 37.6L178.6 117c22.2-18.7 46.1-35.4 71.4-50z"></path><path opacity=".08" fill="currentColor" d="M312.5 824.8L250 933l-.1.1c-25.2-14.6-49.1-31.4-71.4-50.1l80.4-95.7c16.7 13.9 34.6 26.6 53.6 37.5z"></path><path opacity=".48" fill="currentColor" d="M178.6 117l80.4 95.8c-16.7 14.1-32.2 29.5-46.2 46.2L117 178.6c18.7-22.3 39.3-42.9 61.6-61.6z"></path><path opacity=".12" fill="currentColor" d="M258.9 787.2L178.6 883c-22.3-18.7-42.9-39.3-61.6-61.6l95.8-80.3c14 16.7 29.4 32.1 46.1 46.1z"></path><path opacity=".44" fill="currentColor" d="M117 178.6l95.8 80.4c-14 16.6-26.6 34.5-37.6 53.5L67 250l-.1-.1c14.7-25.2 31.4-49.1 50.1-71.3z"></path><path opacity=".16" fill="currentColor" d="M212.8 741.1L117 821.4c-18.7-22.2-35.4-46.1-50.1-71.4l.1-.1 108.2-62.4c11 19 23.6 36.9 37.6 53.6z"></path><path opacity=".4" fill="currentColor" d="M67 250l108.2 62.5c-10.9 18.8-20.1 38.6-27.7 59.2L30.1 329l-.1-.1c10-27.6 22.4-53.9 36.9-79l.1.1z"></path><path opacity=".2" fill="currentColor" d="M175.2 687.6L67 750l-.1.1C52.4 725 40 698.7 30 671.1l.1-.1 117.4-42.7c7.6 20.6 16.8 40.5 27.7 59.3z"></path><path opacity=".36" fill="currentColor" d="M30.1 329l117.4 42.7c-7.4 20.3-13.1 41.4-16.9 63.2l-123-21.7h-.1c5.1-29 12.6-57.2 22.5-84.2h.1z"></path><path opacity=".24" fill="currentColor" d="M147.5 628.3L30.1 671l-.1.1c-9.9-27.1-17.4-55.2-22.5-84.2h.1l123.1-21.7c3.7 21.7 9.4 42.8 16.8 63.1z"></path><path opacity=".32" fill="currentColor" d="M7.6 413.2l123.1 21.7c-3.7 21.1-5.6 42.9-5.6 65.1H0c0-29.6 2.6-58.6 7.6-86.8z"></path><path opacity=".28" fill="currentColor" d="M130.6 565.1l-123 21.7h-.1A506.7 506.7 0 0 1 0 500h125c0 22.2 1.9 44 5.6 65.1z"></path><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="1s" begin="0" repeatCount="indefinite"></animateTransform>
</svg>

<svg viewBox="0 0 1000 1000" height="24" width="24" aria-label="Loading assessment">
<title>
Spinner
</title>
<circle fill="currentColor" cx="937.5" cy="500" r="62.5"></circle><path fill="currentColor" d="M1000 500H875c0-22.2-1.9-44-5.6-65.1l123.1-21.7h.1c4.8 28.2 7.4 57.2 7.4 86.8z"></path><path opacity=".96" fill="currentColor" d="M992.5 413.2l-123.1 21.7c-3.8-21.8-9.5-42.9-16.9-63.2L969.9 329l.1-.1c9.8 27.1 17.4 55.2 22.5 84.3z"></path><path opacity=".92" fill="currentColor" d="M969.9 328.9l-.1.1-117.3 42.7c-7.5-20.6-16.8-40.4-27.7-59.2L933 249.9l.1-.1a503.3 503.3 0 0 1 36.8 79.1z"></path><path opacity=".88" fill="currentColor" d="M933.1 249.9l-108.2 62.6c-10.9-18.9-23.6-36.9-37.6-53.5l95.7-80.4c18.7 22.2 35.4 46.1 50.1 71.3z"></path><path opacity=".84" fill="currentColor" d="M883 178.6L787.3 259c-14.1-16.7-29.5-32.2-46.2-46.2l80.3-95.8c22.3 18.7 42.9 39.3 61.6 61.6z"></path><path opacity=".8" fill="currentColor" d="M821.4 116.9L741 212.7c-16.7-14-34.6-26.6-53.5-37.6l62.4-108.2.1-.1c25.3 14.8 49.2 31.5 71.4 50.1z"></path><path opacity=".76" fill="currentColor" d="M750.1 66.9l-62.5 108.2c-18.8-10.9-38.6-20.1-59.2-27.7L671 30.1l.1-.1c27.5 10.1 53.9 22.4 79 36.9z"></path><path opacity=".72" fill="currentColor" d="M671.1 30l-.1.1-42.7 117.4c-20.3-7.4-41.4-13.1-63.2-16.9l21.7-123v-.1c29.1 5.1 57.2 12.7 84.3 22.5z"></path><path opacity=".68" fill="currentColor" d="M586.8 7.5l-21.7 123.1c-21.1-3.7-42.9-5.6-65.1-5.6V0c29.6 0 58.6 2.6 86.8 7.5z"></path><path opacity=".64" fill="currentColor" d="M500 0v125c-22.2 0-44 1.9-65.1 5.6l-21.7-123v-.1C441.4 2.6 470.4 0 500 0z"></path><path opacity=".6" fill="currentColor" d="M413.2 7.6l21.7 123.1c-21.8 3.8-42.9 9.5-63.2 16.9L329 30.1l-.1-.1c27.1-9.9 55.2-17.4 84.3-22.4z"></path><path opacity=".56" fill="currentColor" d="M329 30.1l42.7 117.4c-20.6 7.5-40.4 16.8-59.2 27.7L250 67l-.1-.1C275 52.4 301.4 40.1 329 30.1z"></path><path opacity=".04" fill="currentColor" d="M371.7 852.5L329 969.9l-.1.1c-27.6-10-53.9-22.4-79-36.9l.1-.1 62.5-108.2c18.7 10.9 38.6 20.1 59.2 27.7z"></path><path opacity=".52" fill="currentColor" d="M250 67l62.5 108.2c-18.9 11-36.9 23.6-53.5 37.6L178.6 117c22.2-18.7 46.1-35.4 71.4-50z"></path><path opacity=".08" fill="currentColor" d="M312.5 824.8L250 933l-.1.1c-25.2-14.6-49.1-31.4-71.4-50.1l80.4-95.7c16.7 13.9 34.6 26.6 53.6 37.5z"></path><path opacity=".48" fill="currentColor" d="M178.6 117l80.4 95.8c-16.7 14.1-32.2 29.5-46.2 46.2L117 178.6c18.7-22.3 39.3-42.9 61.6-61.6z"></path><path opacity=".12" fill="currentColor" d="M258.9 787.2L178.6 883c-22.3-18.7-42.9-39.3-61.6-61.6l95.8-80.3c14 16.7 29.4 32.1 46.1 46.1z"></path><path opacity=".44" fill="currentColor" d="M117 178.6l95.8 80.4c-14 16.6-26.6 34.5-37.6 53.5L67 250l-.1-.1c14.7-25.2 31.4-49.1 50.1-71.3z"></path><path opacity=".16" fill="currentColor" d="M212.8 741.1L117 821.4c-18.7-22.2-35.4-46.1-50.1-71.4l.1-.1 108.2-62.4c11 19 23.6 36.9 37.6 53.6z"></path><path opacity=".4" fill="currentColor" d="M67 250l108.2 62.5c-10.9 18.8-20.1 38.6-27.7 59.2L30.1 329l-.1-.1c10-27.6 22.4-53.9 36.9-79l.1.1z"></path><path opacity=".2" fill="currentColor" d="M175.2 687.6L67 750l-.1.1C52.4 725 40 698.7 30 671.1l.1-.1 117.4-42.7c7.6 20.6 16.8 40.5 27.7 59.3z"></path><path opacity=".36" fill="currentColor" d="M30.1 329l117.4 42.7c-7.4 20.3-13.1 41.4-16.9 63.2l-123-21.7h-.1c5.1-29 12.6-57.2 22.5-84.2h.1z"></path><path opacity=".24" fill="currentColor" d="M147.5 628.3L30.1 671l-.1.1c-9.9-27.1-17.4-55.2-22.5-84.2h.1l123.1-21.7c3.7 21.7 9.4 42.8 16.8 63.1z"></path><path opacity=".32" fill="currentColor" d="M7.6 413.2l123.1 21.7c-3.7 21.1-5.6 42.9-5.6 65.1H0c0-29.6 2.6-58.6 7.6-86.8z"></path><path opacity=".28" fill="currentColor" d="M130.6 565.1l-123 21.7h-.1A506.7 506.7 0 0 1 0 500h125c0 22.2 1.9 44 5.6 65.1z"></path><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="1s" begin="0" repeatCount="indefinite"></animateTransform>
</svg>

## WEB DEVELOPMENT FOUNDATIONS

### Challenge Project: Build a Website Design System

<h4 id="heading-overview" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Overview
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This project is slightly different than others you have encountered thus
far on Codecademy. Instead of a step-by-step tutorial, this project
contains a series of open-ended requirements which describe the project
you’ll be building. There are many possible ways to correctly fulfill
all of these requirements, and you should expect to use the internet,
Codecademy, and other resources when you encounter a problem that you
cannot easily solve.
</p>
<h4 id="heading-project-goals" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Project Goals
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you’ll be building your own basic design system for a
website. In essence, you’ll be building a website to help you build MORE
websites in the future! On your site, you’ll collect all the colors,
fonts, and some of the repeating styles.
</p>
<h4 id="heading-setup-instructions" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Setup Instructions
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you choose to do this project on your computer instead of Codecademy,
you can download what you’ll need by clicking the “Download” button
below. If you need help setting up your computer, read our
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/articles/visual-studio-code">article
about setting up a text editor for HTML/CSS development</a>.
</p>

## Review: Improved Styling with CSS

<p class="p__1qg33Igem5pAgn4kPMirjw">
Congratulations! The goal of this unit was to introduce more
intermediate topics in CSS styles. You also learned more about
navigation design.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Having completed this unit, you are now able to:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Apply more custom colors and fonts
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Style navigation elements like links and buttons
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Create secondary (breadcrumb) navigation
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you are interested in learning more about these topics, here are some
additional resources:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Book:
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://bookshop.org/books/html-and-css-design-and-build-websites/9781118008188">HTML
& CSS</a>, Jon Duckett, Chapters 11 (pp. 246-262) and 12 (pp. 264-298)
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Learning is social. Whatever you’re working on, be sure to connect with
the Codecademy community in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/">forums</a>.
Remember to check in with the community regularly, including for things
like asking for code reviews on your project work and providing code
reviews to others in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/c/project/1833">projects
category</a>, which can help to reinforce what you’ve learned.
</p>
