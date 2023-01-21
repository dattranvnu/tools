## CHANGING THE BOX MODEL

### Box Model: Content-Box

<p class="p__1qg33Igem5pAgn4kPMirjw">
Many properties in CSS have a default value and don’t have to be
explicitly set in the stylesheet.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, the default
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> of text is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">normal</code>, but this
property-value pair is not typically specified in a stylesheet.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The same can be said about the box model that browsers assume. In CSS,
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">box-sizing</code>
property controls the type of box model the browser should use when
interpreting a web page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The default value of this property is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">content-box</code>. This is
the same box model that is affected by border thickness and padding.
</p>

#### Instructions

<p class="p__1qg33Igem5pAgn4kPMirjw">
Study the diagram to the right. It illustrates the default box model
used by the browser,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">content-box</code>. When
you’re done, continue to the next exercise.
</p>

#### Solutions

``` html
```

## CHANGING THE BOX MODEL

### Box Model: Border-Box

<p class="p__1qg33Igem5pAgn4kPMirjw">
Fortunately, we can reset the entire box model and specify a new one:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">box-sizing</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">border-box</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The code in the example above resets the box model to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code> for all
HTML elements. This new box model avoids the dimensional issues that
exist in the former box model you learned about.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this box model, the height and width of the box will remain fixed.
The border thickness and padding will be included inside of the box,
which means the overall dimensions of the box do not change.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">Hello World</span><span class="mtk4">&lt;/h1&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">box-sizing</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">border-box</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 1px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">black</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 10px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the height of the box would remain at 200 pixels
and the width would remain at 300 pixels. The border thickness and
padding would remain entirely <em>inside</em> of the box.
</p>

#### Instructions

<p class="p__1qg33Igem5pAgn4kPMirjw">
Study the diagram to the right. It illustrates the new box model,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code>. Pay
attention to how the total width
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">200px</code>) and the
padding affect the inner width of the element.
</p>

#### Solutions

``` html
```

## CHANGING THE BOX MODEL

### The New Box Model

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that you know about the new box model, let’s actually implement it
in the browser.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">box-sizing</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">border-box</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It’s that simple! In the example above, the universal selector
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">\*</code>) targets all
elements on the web page and sets their box model to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code> model.
</p>

#### Instructions

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, change the box model for all elements on
the web page to the new box model.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You probably didn’t see a difference in the web page to the right -
that’s ok! The new box model simply makes sure that the dimensions of
elements remains the same regardless of border width and padding.
</p>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

#### Solutions

``` html
```

## CHANGING THE BOX MODEL

### Review: Changing the Box Model

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, you learned about an important limitation of the default
box model: box dimensions are affected by border thickness and padding.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s review what you learned:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In the default box model, box dimensions are affected by border
thickness and padding.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">box-sizing</code>
property controls the box model used by the browser.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The default value of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">box-sizing</code> property is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">content-box</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The value for the new box model is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code> model
is not affected by border thickness or padding.
</li>
</ol>

#### Instructions

<p class="p__1qg33Igem5pAgn4kPMirjw">
Take some time to experiment with your new knowledge of the box model in
<strong>style.css</strong>. When you’re done, proceed to the next unit.
</p>

#### Solutions

``` html
```

## DISPLAY AND POSITIONING

### Flow of HTML

<p class="p__1qg33Igem5pAgn4kPMirjw">
A browser will render the elements of an HTML document that has no CSS
from left to right, top to bottom, in the same order as they exist in
the document. This is called the <em>flow</em> of elements in HTML.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In addition to the properties that it provides to style HTML elements,
CSS includes properties that change how a browser <em>positions</em>
elements. These properties specify where an element is located on a
page, if the element can share lines with other elements, and other
related attributes.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, you will learn five properties for adjusting the
position of HTML elements in the browser:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">clear</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Each of these properties will allow us to position and view elements on
a web page. They can be used in conjunction with any other styling
properties you may know.
</p>
