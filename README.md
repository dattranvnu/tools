## Introduction: Fundamentals of CSS

<p class="p__1qg33Igem5pAgn4kPMirjw">
The goal of this unit is to introduce you to CSS, one of the languages
essential to developing websites. You will learn how to apply styles to
HTML documents using CSS.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After this unit, you will be able to:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Understand how CSS is used for web development
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Use CSS to add initial styling to your website
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Understand the Box Model in CSS
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Add positioning using CSS
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Read CSS documentation
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

## SETUP AND SYNTAX

### Intro to CSS

<p class="p__1qg33Igem5pAgn4kPMirjw">
While
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/learn-html">HTML</a>
is the fundamental structure of every web page, it can be visually
unappealing on its own. Cascading Style Sheets or <em>CSS</em> is a
language web developers use to style the HTML content on a web page. If
you’re interested in modifying colors, font types, font sizes, images,
element positioning, and more, CSS is the tool for the job!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, you’ll learn how to set up your CSS file structure and
select which HTML elements you wish to style.
</p>

#### Instructions

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at the code in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code> and observe
how it displays in the browser to the right. This is plain HTML without
any styling. Let’s take a quick look at the power of CSS.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Copy and paste the following line of code onto line 5:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;link</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">"style.css"</span><span class="mtk1"> </span><span class="mtk7">rel</span><span class="mtk1">=</span><span class="mtk8">"stylesheet"</span><span class="mtk4">&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
What happens when you press the Run button?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Take some time to explore and experiment with the code in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code> file.
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

#### Solutions

``` html
```

## SETUP AND SYNTAX

### CSS Anatomy

<p class="p__1qg33Igem5pAgn4kPMirjw">
The diagram on the right shows two different methods, or
<em>syntaxes</em>, for writing CSS code. The first syntax shows CSS
applies as a <em>ruleset</em>, while the second shows it written as an
<em>inline style</em>. Two different methods of writing CSS may seem a
bit intimidating at first, but it’s not as bad as it looks!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/css/anatomy?page_req=catalog">anatomy</a>
of both methods does share common features. Notice how both syntaxes
contain a <em>declaration</em>. Declarations are the core of CSS. They
apply a style to the selected element. Here, the
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/paragraphs?page_req=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code></a>
element has been selected in both syntaxes and will be styled to display
the text in blue.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Understanding that a declaration is used to style a selected element is
key to learning how to style HTML documents with CSS! The terms below
explain each of the labels in the diagram on the right.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Ruleset Terms:</strong>
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Selector</em>—The beginning of the ruleset used to target the
element that will be styled.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Declaration Block</em>—The code in-between (and including) the curly
braces (<code class="code__2rdF32qjRVp7mMVBHuPwDS">{ }</code>) that
contains the CSS declaration(s).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Declaration</em>—The group name for a property and value pair that
applies a style to the selected element.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Property</em>—The first part of the declaration that signifies what
visual characteristic of the element is to be modified.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Value</em>—The second part of the declaration that signifies the
value of the property.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Inline Style Terms:</strong>
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Opening Tag</em>—The start of an
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements?page_req=catalog">HTML
element</a>. This is the element that will be styled.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Attribute</em>—The style
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/attributes?page_req=catalog">attribute</a>
is used to add CSS inline styles to an HTML element.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Declaration</em>—The group name for a property and value pair that
applies a style to the selected element.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Property</em>—The first part of the declaration that signifies what
visual characteristic of the element is to be modified.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Value</em>—The second part of the declaration that signifies the
value of the property.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Don’t worry about memorizing all of these—you will get acquainted with
them more and more as the course progresses! Feel free to come back and
use this exercise as a reference later on.
</p>

#### Instructions

<p class="p__1qg33Igem5pAgn4kPMirjw">
Study the diagrams to become familiar with the CSS syntax and the new
terms that will be used throughout the course.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Click the “Next” button when you are ready to write some code!
</p>

#### Solutions

``` html
```

## SETUP AND SYNTAX

### Inline Styles

<p class="p__1qg33Igem5pAgn4kPMirjw">
Although CSS is a different language than HTML, it’s possible to write
CSS code directly within HTML code using <em>inline styles</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To style an HTML element, you can add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute
directly to the opening tag. After you add the attribute, you can set it
equal to the CSS style(s) you’d like applied to that element.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;p</span><span class="mtk1"> </span><span class="mtk7">style</span><span class="mtk1">=</span><span class="mtk8">'color: red;'</span><span class="mtk4">&gt;</span><span class="mtk1">I'm learning to code!</span><span class="mtk4">&lt;/p&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The code in the example above demonstrates how to use inline styling.
The paragraph element has a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute within
its opening tag. Next, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute is set
equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">color: red;</code>,
which will set the color of the paragraph text to red within the
browser.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you’d like to add <em>more</em> than one style with inline styles,
simply keep adding to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute. Make
sure to end the styles with a semicolon
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">;</code>).
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;p</span><span class="mtk1"> </span><span class="mtk7">style</span><span class="mtk1">=</span><span class="mtk8">'color: red; font-size: 20px;'</span><span class="mtk4">&gt;</span><span class="mtk1">I'm learning to code!</span><span class="mtk4">&lt;/p&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It’s important to know that inline styles are a quick way of directly
styling an HTML element, but are rarely used when creating websites. But
you may encounter circumstances where inline styling is necessary, so
understanding how it works, and recognizing it in HTML code is good
knowledge to have. Soon you’ll learn the proper way to add CSS code!
</p>

#### Instructions

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>, use
inline styling to set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> of the first
paragraph (the first
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code> element) to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">green</code>.
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

#### Solutions

``` html
```

## SETUP AND SYNTAX

### Internal Stylesheet

<p class="p__1qg33Igem5pAgn4kPMirjw">
As previously stated, inline styles are not the best way to style HTML
elements. If you wanted to style, for example, multiple
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements/h1-h6?page_req=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code>
elements</a>, you would have to add inline styling to each element
manually. In addition, you would also have to maintain the HTML code
when additional <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code>
elements are added.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Fortunately, HTML allows you to write CSS code in its own dedicated
section with a
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<style\></code></a>
element nested inside of the
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements/head?page_req=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<head\></code></a>
element. The CSS code inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<style\></code> element is
often referred to as an <em>internal stylesheet</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
An internal stylesheet has certain benefits and use cases over inlines
styles, but once again, it’s not best practice (we’ll get there, we
promise). Understanding how to use internal stylesheets is nonetheless
helpful knowledge to have.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To create an internal stylesheet, a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<style\></code> element must
be placed inside of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<head\></code> element.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;head&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;style&gt;</span></span><br><span><span> </span></span><br><span><span> </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/style&gt;</span></span><br><span><span class="mtk4">&lt;/head&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After adding opening and closing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<style\></code> tags in the
head section, you can begin writing CSS code.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;head&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;style&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">p</span><span class="mtk1"> </span><span class="mtk4">{</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk7">color:</span><span class="mtk1"> </span><span class="mtk4">red;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk7">font-size:</span><span class="mtk1"> </span><span class="mtk14">20px</span><span class="mtk4">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">}</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/style&gt;</span></span><br><span><span class="mtk4">&lt;/head&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The CSS code in the example above changes the color of all paragraph
text to red and also changes the size of the text to 20 pixels. Note how
the syntax of the CSS code matches (for the most part) the syntax you
used for inline styling. The main difference is that you can specify
which elements to apply the styling.
</p>

#### Instructions

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s move the inline style that was added to the paragraph into an
internal stylesheet.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Start by adding an empty
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<style\></code> element in
the head of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>.
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
Inside of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<style\></code> element, add
a CSS ruleset targeting the paragraph (the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code> element). You
can leave the declaration block empty for now.
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
Next, place just the declaration from the inline style into the empty
declaration block in the inline stylesheet.
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
Finally, delete the inline style from the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code> element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice how the styling works the same in the stylesheet as it did in the
inline style!
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

#### Solutions

``` html
```

## SETUP AND SYNTAX

### External Stylesheet

<p class="p__1qg33Igem5pAgn4kPMirjw">
Developers avoid mixing code by storing HTML and CSS code in separate
files (HTML files contain only HTML code, and CSS files contain only CSS
code).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can create an external stylesheet by using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.css</code> file name
extension, like so:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
With an external stylesheet, you can write all the CSS code needed to
style a page without sacrificing the readability and maintainability of
your HTML file.
</p>

#### Instructions

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at
<code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>. Cut the
CSS code ruleset in between the opening and closing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<style\></code> tags and
paste it directly into the file called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Delete the remaining
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<style\></code> element (now
empty) from <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>
and press the Run button.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Hmm, the font changes didn’t take effect? Click the Next button to find
out why.
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

#### Solutions

``` html
```

## SETUP AND SYNTAX

### Linking the CSS File

<p class="p__1qg33Igem5pAgn4kPMirjw">
Perfect! We successfully separated structure (HTML) from styling (CSS),
but the web page still looks bland. Why?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When HTML and CSS codes are in separate files, the files must be linked.
Otherwise, the HTML file won’t be able to locate the CSS code, and the
styling will not be applied.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can use the
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements/link?page_req=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code></a>
element to link HTML and CSS files together. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code> element must
be placed within the head of the HTML file. It is a self-closing tag and
requires the following attributes:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> — like the anchor
element, the value of this attribute must be the address, or path, to
the CSS file.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rel</code> — this attribute
describes the relationship between the HTML file and the CSS file.
Because you are linking to a stylesheet, the value should be set to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stylesheet</code>.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When linking an HTML file and a CSS file together, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code> element will
look like the following:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;link</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">'https://www.codecademy.com/stylesheets/style.css'</span><span class="mtk1"> </span><span class="mtk7">rel</span><span class="mtk1">=</span><span class="mtk8">'stylesheet'</span><span class="mtk4">&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note that in the example above, the path to the stylesheet is a URL:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="plaintext" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">https://www.codecademy.com/stylesheets/style.css</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Specifying the path to the stylesheet using a URL is one way of linking
a stylesheet.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If the CSS file is stored in the same
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Directory_(computing)">directory</a>
as your HTML file, then you can specify a
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/general/file-paths?page_req=catalog">relative
path</a> instead of a URL, like so:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;link</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">'./style.css'</span><span class="mtk1"> </span><span class="mtk7">rel</span><span class="mtk1">=</span><span class="mtk8">'stylesheet'</span><span class="mtk4">&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Using a relative path is very common way of linking a stylesheet.
</p>

#### Instructions

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s link the stylesheet
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code> to the HTML
file <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
First, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code>
element within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<head\></code> section.
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
Next, add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code>
attribute to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code> element and
set it equal to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at the web page in the browser to the right. Do you notice
any changes yet?
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
Finally, add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">rel</code>
attribute and set it to the correct value. Keep an eye on the first
paragraph’s font—it should appear different from the destinations’
descriptions when your stylesheet is linked correctly.
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

#### Solutions

``` html
```

## SETUP AND SYNTAX

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great work so far! By understanding how to incorporate CSS code into
your HTML file, as well as learning some of the key terms, you’re on
your way to creating spectacular websites with HTML and CSS.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s review what you learned so far:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The basic anatomy of CSS syntax written for both inline styles and
stylesheets.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Some commonly used CSS terms, such as <em>ruleset</em>,
<em>selector</em>, and <em>declaration</em>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
CSS inline styles can be written inside the opening HTML tag using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Inline styles can be used to style HTML, but it is not the best
practice.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
An internal stylesheet is written using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<style\></code> element
inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<head\></code>
element of an HTML file.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Internal stylesheets can be used to style HTML but are also not best
practice.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
An external stylesheet separates CSS code from HTML, by using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.css</code> file extension.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
External stylesheets are the best approach when it comes to using HTML
and CSS.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
External stylesheets are linked to HTML using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<link\></code> element.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Take this knowledge to the next lesson, where you start learning how to
select HTML elements to style!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here are a few more resources to add to your toolkit:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/css">Codecademy
Docs: CSS</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/workspaces/new">Codecademy
Workspaces: CSS</a>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Make sure to bookmark these links so you have them at your disposal.
</p>

## SELECTORS

### Type

<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember that <em>declarations</em> are a fundamental part of CSS
because they apply a style to a selected element. But how do you decide
which elements will get the style? With a
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/css/selectors?page_req=catalog"><em>selector</em></a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A selector is used to target the specific HTML element(s) to be styled
by the declaration. One selector you may already be familiar with is the
<em>type</em> selector. Just like its name suggests, the type selector
matches the <em>type</em> of the element in the HTML document.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous lesson, you changed the color of a paragraph element.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">green</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This is an instance of using the type selector! The element type is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code>, which comes from
the HTML <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code>
element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Some important notes on the type selector:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The type selector does not include the angle brackets.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Since element types are often referred to by their opening tag name, the
type selector is sometimes referred to as the <em>tag name</em> or
<em>element</em> selector.
</li>
</ul>

#### Instructions

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Open <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code>. On
line 5, add a ruleset using the type selector to target all
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code> elements. Leave
the declaration block (<code class="code__2rdF32qjRVp7mMVBHuPwDS">{
}</code>) empty for now.
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
Inside the curly braces of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> selector, add the
declaration below:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">maroon</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note that the content of the web page will update because we’ve already
linked <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>.
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

#### Solutions

``` html
```

## SELECTORS

### Universal

<p class="p__1qg33Igem5pAgn4kPMirjw">
You learned how the <em>type selector</em> selects all elements of a
given type. Well, the <em>universal selector</em> selects all elements
of <em>any</em> type.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Targeting all of the elements on the page has a few specific use cases,
such as resetting default browser styling, or selecting all
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/t/what-are-parent-elements-and-child-elements-in-html-and-css/283224">children</a>
of a parent element. Don’t worry if you don’t understand the use cases
right now—we will get to them later on in our Learn CSS journey.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The universal selector uses the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\*</code> character in the
same place where you specified the type selector in a ruleset, like so:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span><span class="mtk9"> </span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> Verdana</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the code above, every text element on the page will have its font
changed to <code class="code__2rdF32qjRVp7mMVBHuPwDS">Verdana</code>.
</p>

#### Instructions

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
To see how the universal selector targets all elements on a page, copy
the rule below and paste it on the first line of
<strong>style.css</strong>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 1px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">red</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Then, click “Run”.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Since the universal selector targets all elements, every element on the
page now has a red border. Not a visually pleasing look, but you can see
how all of the elements have been modified.
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

#### Solutions

``` html
```
