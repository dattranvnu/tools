## SEMANTIC HTML

### Introduction to Semantic HTML

<p class="p__1qg33Igem5pAgn4kPMirjw">
When building web pages, we use a combination of non-semantic HTML and
<em>Semantic HTML</em>. The word semantic means “relating to meaning,”
so semantic elements provide information about the content between the
opening and closing tags.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By using Semantic HTML, we select HTML elements based on their meaning,
not on how they are presented. Elements such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<span\></code> are not
semantic elements since they provide no context as to what is inside of
those tags.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, instead of using a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> element to
contain our header information, we could use a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code> element,
which is used as a heading section. By using a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code> tag instead
of a <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>, we
provide context as to what information is inside of the opening and
closing tag.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Why use Semantic HTML?</strong>
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Accessibility:</strong> Semantic HTML makes webpages accessible
for mobile devices and for people with disabilities as well. This is
because screen readers and browsers are able to interpret the code
better.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>SEO:</strong> It improves the website SEO, or <em>Search Engine
Optimization</em>, which is the process of increasing the number of
people that visit your webpage. With better SEO, search engines are
better able to identify the content of your website and weight the most
important content appropriately.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Easy to Understand:</strong> Semantic HTML also makes the
website’s source code easier to read for other web developers.
</p>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To better understand this, you can think of comparing non-semantic HTML
to going into a store with no signs on the aisles. Since the aisles
aren’t labeled, you don’t know what products are in those aisles.
However, stores that do have signs for each aisle make it a lot easier
to find the items you need, just like Semantic HTML.
</p>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Analyze the diagram and take note of key differences between
non-semantic and semantic code.
</p>

## SEMANTIC HTML

### Header and Nav

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s take a look at some semantic elements that assist in the structure
of a web page. A
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/semantic-html/header?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code></a>
is a container usually for either navigational links or introductory
content containing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h6\></code> headings.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The example below shows
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code> in action:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;header&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Everything you need to know about pizza!</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk4">&lt;/header&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This can be compared to the code below which uses a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> tag instead of
a <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code> tag:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"header"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;Everything you need to know about pizza!</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By using a <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code>
tag, our code becomes easier to read. It is much easier to identify what
is inside of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h1\></code>’s parent tags,
as opposed to a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> tag which
would provide no details as to what was inside of the tag.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/semantic-html/nav?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<nav\></code></a>
is used to define a block of navigation links such as menus and tables
of contents. It is important to note that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<nav\></code> can be used
inside of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code> element but
can also be used on its own.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s take a look at the example below:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;header&gt;</span><span class="mtk1"> </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;nav&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;ul&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;&lt;a</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">"#home"</span><span class="mtk4">&gt;</span><span class="mtk1">Home</span><span class="mtk4">&lt;/a&gt;&lt;/li&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;&lt;a</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">"#about"</span><span class="mtk4">&gt;</span><span class="mtk1">About</span><span class="mtk4">&lt;/a&gt;&lt;/li&gt;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;/ul&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/nav&gt;</span></span><br><span><span class="mtk4">&lt;/header&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By using <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<nav\></code> as a
way to label our navigation links, it will be easier for not only us,
but also for web browsers and screen readers to read the code.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that we’ve learned about the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<nav\></code> elements let’s
add them into our code!
</p>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the code editor, find the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div id=“header”\></code>
tag and change it to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> When changing an opening tag, you must find the
corresponding closing tag and change that as well. If you don’t, you’ll
see some red in your code to indicate the error.
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
Now, find the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div
id=“nav”\></code> tag and change it to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<nav\></code>.
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

## SEMANTIC HTML

### Main and Footer

<p class="p__1qg33Igem5pAgn4kPMirjw">
Two more structural elements are
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<main\></code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<footer\></code>. These
elements along with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<nav\></code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code> help
describe where an element is located based on conventional web
development standards.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The element
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/semantic-html/main?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<main\></code></a>
is used to encapsulate the dominant content within a webpage. This tag
is separate from the
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/semantic-html/footer?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<footer\></code></a>
and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<nav\></code> of a
web page since these elements don’t contain the principal content. By
using <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<main\></code> as
opposed to a <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element, screen readers and web browsers are better able to identify
that whatever is inside of the tag is the bulk of the content.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
So how does <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<main\></code>
look when incorporated into our code? That’s a great question.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;main&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;header&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">Types of Sports</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/header&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;article&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h3&gt;</span><span class="mtk1">Baseball</span><span class="mtk4">&lt;/h3&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The first game of baseball was played in Coo</span><span class="mtk1">perstown, New York in the summer of 1839.</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/article&gt;</span></span><br><span><span class="mtk4">&lt;/main&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As we see above,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<main\></code> contains an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<header\></code> tag with
child elements that hold the most important information related to the
page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The content at the bottom of the subject information is known as the
<em>footer</em>, indicated by the
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/semantic-html/footer?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<footer\></code></a>
element. The footer contains information such as:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Contact information
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Copyright information
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Terms of use
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Site Map
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Reference to top of page links
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;footer&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">Email me at Codey@Codecademy.com</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk4">&lt;/footer&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the footer is used to contain contact information.
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<footer\></code> tag is
separate from the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<main\></code> element and
typically located at the bottom of the content.
</p>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the code editor, find the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div id=“main”\></code> tag
and change it to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<main\></code>.
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
Now, find the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div
id=“footer”\></code> tag and change it to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<footer\></code>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

## SEMANTIC HTML

### Article and Section

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that we covered the body of Semantic HTML, let’s focus on what can
go in the body. The two elements we’re going to focus on now are
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/semantic-html/section?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code></a>
defines elements in a document, such as chapters, headings, or any other
area of the document with the same theme. For example, content with the
same theme such as articles about cricket can go under a single
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code>. A
website’s home page could be split into sections for the introduction,
news items, and contact information.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here is an example of how to use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;section&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;h2&gt;</span><span class="mtk1">Fun Facts About Cricket</span><span class="mtk4">&lt;/h2&gt;</span><span class="mtk1"> </span></span><br><span><span class="mtk4">&lt;/section&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the code above we created a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code> element to
encapsulate the code. In
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code> we added a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h2\></code> element as a
heading.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/semantic-html/article?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code></a>
element holds content that makes sense on its own.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code> can hold
content such as articles, blogs, comments, magazines, etc. An
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code> tag would
help someone using a screen reader understand where the article content
(that might contain a combination of text, images, audio, etc.) begins
and ends.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here is an example of how to use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;section&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;h2&gt;</span><span class="mtk1">Fun Facts About Cricket</span><span class="mtk4">&lt;/h2&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;article&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">A single match of cricket can last up to 5&nbsp;days.</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/article&gt;</span></span><br><span><span class="mtk4">&lt;/section&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the code above, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code> element
containing a fact about cricket was placed inside of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code> element.
It is important to note that a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code> element
could also be placed in an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code> element
depending on the context.
</p>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the code find and replace
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div id=“section”\></code>
with <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code> and
replace the corresponding closing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\</div\></code> with a
closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">\</section\></code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> When removing the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> tag, make sure
you remove the id attached to it!
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
Now encapsulate the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<h2\></code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code> tag with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code>.
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

## SEMANTIC HTML

### The Aside Element

<p class="p__1qg33Igem5pAgn4kPMirjw">
The
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/semantic-html/aside?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">\<aside\></code></a>
element is used to mark additional information that can enhance another
element but isn’t required in order to understand the main content. This
element can be used alongside other elements such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<section\></code>. Some
common uses of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<aside\></code> element are
for:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Bibliographies
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Endnotes
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Comments
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Pull_quote">Pull
quotes</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Editorial sidebars
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Additional information
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here’s an example of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<aside\></code> being used
alongside <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;article&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">The first World Series was played between Pittsbur</span><span class="mtk1">gh and Boston in 1903 and was a&nbsp;nine-game series.</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk4">&lt;/article&gt;</span></span><br><span><span class="mtk4">&lt;aside&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;Babe Ruth once stated, “Heroes get remembered, </span><span class="mtk1">but legends never die.” </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk4">&lt;/aside&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As shown above, the information within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code> is the
important content. Meanwhile the information within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<aside\></code> enhances the
information in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<article\></code> but is not
required in order to understand it.
</p>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Remove the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div
id=“aside”\></code> tag and replace it with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<aside\></code> tag. Don’t
forget about the closing tag!
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
