## LANGUAGES FOR WEB DEVELOPMENT

### Hypertext and the World Wide Web

Languages for Web Development

<span class="gamut-yj8jvy-Text e8i0p5k0" aria-hidden="true">Hypertext
and the World Wide Web</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The H and T in HTML stands for
<strong>h</strong>yper<strong>t</strong>ext. Hypertext is text that is
linked to other text. This diagram shows different websites that are
connected to each other through links, which are represented by arrows.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
What’s so hyper about hypertext? The prefix <em>hyper</em> indicates
that the text expands beyond the traditional constraints of the written
word. Instead of reading documents from beginning to end, like you would
read a book, someone going through hypertext can <em>browse</em>. By
clicking on links from one document to another, the user can navigate to
whatever page they find the most interesting and carve their own unique
path through the web.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Many modern websites provide rich user experiences, with features like
embedded videos, animations, and interactivity, so it doesn’t
necessarily feel like you are just navigating from one HTML page to the
next. But despite all of the advances that have taken place with the
growth of the web, at its core the web is still just a collection of
hyperlinked documents.
</p>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Review the structure of links shown in the diagram, then continue to the
next exercise when you are ready.
</p>

## LANGUAGES FOR WEB DEVELOPMENT

### Adding Hyperlinks

Languages for Web Development

<span class="gamut-yj8jvy-Text e8i0p5k0" aria-hidden="true">Adding
Hyperlinks</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s explore how hypertext works by adding a link to a basic website!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Reading and modifying code is an essential first step in learning to
build things for the web. This practice can take you a long way while
you’re learning to build websites from scratch.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
An <em>attribute</em> in HTML provides additional information about an
HTML element. It comes in a name and value pair with the structure
<code class="code__2rdF32qjRVp7mMVBHuPwDS">name=“value”</code>. For
example, you can specify the width of an HTML element with the attribute
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width=“500”</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Links are created in HTML with something called the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute, which
stands for <strong>h</strong>yperlink <strong>ref</strong>erence. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute allows
us to specify the URL, or address on the web, that a link should take
users to. See below for an example of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute in
action.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When we set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code>
property on an anchor tag (abbreviated to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code>) we can specify
both the text that should be rendered for the user (the text within the
anchor tag) and the URL that the browser should navigate to.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
With this code, we’re assigning the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">www.codecademy.com</code> to
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute.
When a user clicks on the text of this link (Learn to code!), they will
be directed to
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="http://www.codecademy.com">www.codecademy.com</a>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code>
<div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;a</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">"www.codecademy.com"</span><span class="mtk4">&gt;</span><span class="mtk1">Learn to code!</span><span class="mtk4">&lt;/a&gt;</span></span><br></div></code></pre></pre>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Alejandra has begun to build out her business’s website. She wants to
link from her homepage to a different page that contains her resume.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To start, look in <strong>index.html</strong> for the text that says
<code class="code__2rdF32qjRVp7mMVBHuPwDS">25 years of experience</code>
— it should be near line 20. Put an anchor tag
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<a\></code>) around this
text.
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute
to this anchor tag, and give it the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">/resume.html</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This URL is called a <em>relative path</em> and it looks a little
different from the full URLs you’re used to seeing. That’s because it’s
actually a link to another page on the same website, so we can omit the
first part. Instead of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">www.jetsetter.com/resume.html</code>
we can abbreviate the link to just
<code class="code__2rdF32qjRVp7mMVBHuPwDS">/resume.html</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Open the hint if you need a reminder on how to set attributes for html
tags.
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
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
Click on the link that you just made to navigate to see Alejandra’s
resume!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Click <strong>Run</strong> one more time when you are ready to move on
to the next lesson.
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

## LANGUAGES FOR WEB DEVELOPMENT

### What is CSS?

Languages for Web Development

<span class="gamut-yj8jvy-Text e8i0p5k0" aria-hidden="true">What is
CSS?</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Using just HTML, Alejandra was able to build a website that contains all
of the content that she wants. But it doesn’t look very
impressive—Alejandra knows that a basic black and white website won’t
give her business the credibility she needs to find new customers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
That’s where CSS comes in! <em>CSS</em> is the language that provides
<em>style</em> to the content of an HTML page. This includes colors,
fonts, positioning, layout, and more!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Why do we need a separate language for content and presentation? This is
an example of the computer science principle <em>separation of
concerns</em>. Large codebases are kept maintainable when each section
has clearly differentiated problems that it is trying to solve.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Since the styling rules are described separately from the content
itself, if Alejandra adds more paragraphs, images, or other forms of
content, she can expect them to be styled the same way as her existing
content. This will save Alejandra time in the long run, especially as
her website gets more and more complex.
</p>

<p class="p__1qg33Igem5pAgn4kPMirjw">
After you’ve reviewed the diagram to compare the uses of HTML and CSS,
continue to the next exercise.
</p>

## LANGUAGES FOR WEB DEVELOPMENT

### Applying CSS

Languages for Web Development

<span class="gamut-yj8jvy-Text e8i0p5k0" aria-hidden="true">Applying
CSS</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Alejandra has learned CSS and created the desired visual rules to make
her website look sleek and polished.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Navigate to the <strong>style.css</strong> file to take a look at the
CSS code that she’s written.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this file, you will recognize many of the HTML tags that you have
been working with — and maybe a few that you haven’t seen yet! CSS
contains <em>selectors</em> that specify the HTML elements to which the
style should be applied as well as <em>visual rules</em> that specify
how that content should be displayed.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now it’s time to use the HTML link element to apply the CSS file to her
existing website. This is done with an HTML link tag. An HTML link tag
is often used to create a connection between an HTML file and the CSS
file and tells the browser to apply the CSS styles to the HTML.
</p>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
On line 6 of <strong>index.html</strong>, copy and paste the code below
to apply the CSS file to the existing HTML.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Use your knowledge of HTML attributes to figure out what this code
specifies, and check out extra information in the hint if you want to
learn more.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code>
<div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;link</span><span class="mtk1"> </span><span class="mtk7">rel</span><span class="mtk1">=</span><span class="mtk8">"stylesheet"</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">"style.css"</span><span class="mtk4">&gt;</span></span><br></div></code></pre></pre>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
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
Awesome! Alejandra’s site is looking good! Just a little CSS can make
the difference between a website that looks like a skeleton and
portfolio-ready site.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now let’s tweak the CSS just a little bit, to see how the visual rules
specified in CSS can change the way that a website is displayed.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Navigate to the <strong>style.css</strong> and scroll down to line 37
where you will see the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> selector. This
section defines the styles for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> element on the
page, which is the most prominent heading.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Just for practice, change the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> property from
<code class="code__2rdF32qjRVp7mMVBHuPwDS">white</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">black</code> and press Run to
see what changes!
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Good job changing the color of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> text!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you look at the rendered browser, you’ll notice that the heading text
is no longer readable in-front of the image.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s change the color property within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> selector back to
white.
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

## LANGUAGES FOR WEB DEVELOPMENT

### What is JavaScript?

Languages for Web Development

<span class="gamut-yj8jvy-Text e8i0p5k0" aria-hidden="true">What is
JavaScript?</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that Alejandra has her website looking polished, she’s realized that
she wants the site to be more interactive. She would like to build a
shopping cart feature that allows her users to buy travel packages
directly from her website.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To accomplish this, Alejandra is going to need to learn JavaScript. Any
website that provides more than just static information probably
utilizes JavaScript in some way. Here are some familiar examples of
website features most often built with JavaScript:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
popup ads
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
animated graphics (2D or 3D)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
interactive audio and video
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
maps and other features access the user’s geographic location
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
and much more!
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
One of the defining features of JavaScript is its ability to respond to
browser events. These events happen in real time and can be triggered by
a wide variety of user interactions, including:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the user clicking on a button
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the user pressing enter on their keyboard
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
a video file finishing loading
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the user re-sizing their window
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the user hovering over text on the webpage
</li>
</ul>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
One of the classic browser events that JavaScript can respond to is the
position of the mouse. When a user puts the mouse near an HTML element,
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">onmouseover</code> event
is fired.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Hover over the text in the browser to see how it responds to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">onmouseover</code> event.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Once you have observed the effect of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">onmouseover</code>, click the
<strong>Run</strong> button to move on to the next Checkpoint.
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
What else is happening here?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
JavaScript uses functions, which are reusable blocks of code designed to
perform a specific task.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">drawText</code> is a function
that is being run on line 2. Change the text that says
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘hello world’</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘JavaScript’</code> to pass a
different value into this function.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Check out the browser to see what changed! One of the benefits of
functions is that they are <em>reusable</em>. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">drawText</code> function
allows us to take advantage of the reusability of functions because it
can render any input text without us needing to rewrite the logic of the
function.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Confused? Don’t worry, we’ll cover functions more thoroughly in the next
exercise.
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

## LANGUAGES FOR WEB DEVELOPMENT

### JavaScript Functions

Languages for Web Development

<span class="gamut-yj8jvy-Text e8i0p5k0" aria-hidden="true">JavaScript
Functions</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the last exercise, you started to think about two key building blocks
of JavaScript: functions and events. Let’s review:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Functions allow us to write a chunk of code once that can be reused over
and over.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Events allow JavaScript to respond to user behaviors, like the user
hovering their mouse over an HTML element or resizing their window.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Events and functions combine to give JavaScript the ability to create
interactive experiences. When an event is fired, a function is executed.
This pattern is used again and again in web development to create
interactive websites.
</p>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
First, let’s take a look at the JavaScript in the
<strong>index.html</strong> file.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The JavaScript code is between the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<script\></code> tags. This
tag alerts the browser that the page contains JavaScript and separates
the JavaScript code from the HTML.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Find the JavaScript function
<code class="code__2rdF32qjRVp7mMVBHuPwDS">changeColor()</code>. This
function chooses a color from a list of colors.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
How does that happen?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
First, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getRandomColor()</code>
function generates a random series of numbers and letters to create a
new
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.mathsisfun.com/hexadecimal-decimal-colors.html">hexadecimal
color code</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It then saves the new color under the name
<code class="code__2rdF32qjRVp7mMVBHuPwDS">newColor</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code>
<div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let newColor</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">getRandomColor</span><span class="mtk1">();</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
On the next line, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> keyword
accesses the page’s background color and sets it equal to the new color.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code>
<div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">body</span><span class="mtk1">.</span><span class="mtk10">style</span><span class="mtk1">.</span><span class="mtk10">backgroundColor</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">newColor</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Click the <strong>Run</strong> button to move on to the next checkpoint
to see how we can let a user change the color!
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
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
The next step is to connect the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">changeColor()</code>
JavaScript function with an event, so that when we click the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Repaint!</code> button, it
changes the background color.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
An event is something that can happen in a browser, like clicking or
hovering with your mouse.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
HTML attributes can set events, where the <strong>name</strong> of the
attribute is the event and the <strong>value</strong> of the attribute
is the JavaScript function that we want to execute.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this case, the name of the event is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">onclick</code> and we can
invoke the function by calling
<code class="code__2rdF32qjRVp7mMVBHuPwDS">“changeColor()”</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Paste this code into the opening tag of the button element:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">onclick=“changeColor()”</code>.
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
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
Let’s test out the functionality of the code that we just added. When
you click the “Repaint!” button, the background color of the site should
be reset at random!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When you’re ready, click <strong>Run</strong> again and move on to the
next exercise.
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

## LANGUAGES FOR WEB DEVELOPMENT

### What is SQL?

Languages for Web Development

<span class="gamut-yj8jvy-Text e8i0p5k0" aria-hidden="true">What is
SQL?</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that Alejandra has built out the user-facing checkout features of
her website, she’s realized that she needs to store all of this
information somewhere! She needs her application to be able to store,
retrieve, and modify data like usernames, shipping addresses, payment
information, and more.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In order to build out these features, Alejandra needs to learn some
<em>SQL</em>, which stands for <strong>s</strong>tructured
<strong>q</strong>uery <strong>l</strong>anguage. You might be familiar
with SQL as a language that Data Analysts and Data Scientists use to
query and analyze data.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
SQL stores information in tables, which is simply a collection of
information organized into rows and columns. If you’ve worked with a
spreadsheet like Microsoft Excel or Google Sheets, you might be familiar
with working with tables. To get the information, you would write a
<em>query</em>, or a program that would retrieve data from the table.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here’s an example of a query that would select all of the columns —the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\*</code> keyword is a
shorthand for “all”— from the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">page_views</code> table:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code>
<div data-lang="codecademy-sql" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">SELECT</span><span class="mtk1"> *&nbsp;</span><span class="mtk12">FROM</span><span class="mtk1"> page_views;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Web developers and software engineers also use SQL to build apps that
can save, modify, and access data. There’s even a growing field of
<em>data engineering</em>, which is a specialized subset of software
engineers who ensure that the applications they are working with
accurately and efficiently record all of the required data.
</p>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now you try it! Add <code class="code__2rdF32qjRVp7mMVBHuPwDS">SELECT \*
FROM users;</code> to the text editor to select the entire
<code class="code__2rdF32qjRVp7mMVBHuPwDS">users</code> table from the
database.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Press run and take a look at the data that is returned. What kinds of
data is Alejandra’s app able to store and retrieve? Why is it important
for her to store this particular set of information?
</p>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
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

## LANGUAGES FOR WEB DEVELOPMENT

### Review

Languages for Web Development

<span class="gamut-yj8jvy-Text e8i0p5k0"
aria-hidden="true">Review</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Alejandra now has a fully functional web application for her small
business!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In building out the features that she needed for her business’s
application, she learned about the four languages that form the core of
the World Wide Web today:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>HTML</strong> — structures website content
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>CSS</strong> — applies styling to websites
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>JavaScript</strong> — adds interactivity to websites
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>SQL</strong> — allows your web application to store and retrieve
data
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
While these languages are each essential to web development, many of
them also have applications in other fields. For example, JavaScript was
initially just a language for interacting with HTML, but JavaScript has
expanded to be a general-purpose programming language that can be run
outside of the browser. You can now build web applications, browser
games, desktop applications, and even VR/AR experiences in JavaScript.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Learning web development has given Alejandra the skills that she needed
for her business and also opened the door for her to take on more and
more technical projects in a wide variety of fields.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Are you interested in more content about picking your first language?
Try out
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/choosing-a-programming-language-track">Choosing
Your First Language</a>!
</p>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Congratulations! You can now understand and talk about the main
languages of web development and you’ve gotten your feet wet with
reading and editing code.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you’re intrigued by Web Development, you should now have a sense of
what skills or languages you want to learn next.
</p>

## What is Programming?

<h3 id="heading-programming-is-everywhere" class="h3__3B1DSzXTW-ux1viDSStOux">
PROGRAMMING IS EVERYWHERE
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Programming is, quite literally, all around us. From the take-out we
order, to the movies we stream, code enables everyday actions in our
lives. Tech companies are no longer recognizable as just software
companies — instead, they bring food to our door, help us get a taxi,
influence outcomes in presidential elections, or act as a personal
trainer.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>When you’re walking down the street, where can you find technology
in your environment? Click on the white circles.</em>
</p>
<iframe src="https://content.codecademy.com/programs/code-foundations-path/bop-i/intro-article-programming-everywhere/index.html" height="400px" frameborder="0" class="iframe__rk2yNYIwJeUOj5J8cQJ9-">
</iframe>

<br>

<h3 id="heading-and-programming-is-for-everyone" class="h3__3B1DSzXTW-ux1viDSStOux">
…AND PROGRAMMING IS FOR EVERYONE
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For many years, only a few people have known how to code. However,
that’s starting to change. The number of people learning to code is
increasing year by year, with estimates around
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.developernation.net/developer-reports/dn22">31.1
million software developers worldwide</a>, which doesn’t even account
for the many OTHER careers that relate to programming.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here at Codecademy, our mission is to make technical knowledge
accessible and applicable. Technology plays a crucial role in our
economy — but programming is no longer just for software engineers. Any
person can benefit from learning to program — whether it’s learning HTML
to improve your marketing emails or taking a SQL course to add a dose of
analysis to your research role.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Even outside of the tech industry, learning to program is essential to
participating in the world around you: it affects the products you buy,
the legal policies you vote for, and the data you share online.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
So, let’s dig into what programming is.
</p>
<h3 id="heading-what-is-programming" class="h3__3B1DSzXTW-ux1viDSStOux">
WHAT IS PROGRAMMING?
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Put simply, programming is giving a set of instructions to a computer to
execute. If you’ve ever cooked using a recipe before, you can think of
yourself as the computer and the recipe’s author as a programmer. The
recipe author provides you with a set of instructions which you read and
then follow. The more complex the instructions, the more complex the
result!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>How good are you at giving instructions? Try and get Codey to draw a
square!</em>
</p>
<iframe src="https://content.codecademy.com/programs/code-foundations-path/bop-i/intro-article-turtle-codey/index.html" height="400px" class="iframe__rk2yNYIwJeUOj5J8cQJ9-">
</iframe>

<br>

<h3 id="heading-programming-as-communication-or-coding" class="h3__3B1DSzXTW-ux1viDSStOux">
PROGRAMMING AS COMMUNICATION, or CODING
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
“Ok, so now I know what programming is, but what’s coding? I’m here to
learn how to code. Are they the same thing?”
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
While sometimes used interchangeably, programming and coding actually
have different definitions.
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Programming</em> is the mental process of thinking up instructions
to give to a machine (like a computer).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Coding</em> is the process of transforming those ideas into a
written language that a computer can understand.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Over the past century, humans have been trying to figure out how to best
communicate with computers through different
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/blog/programming-languages/">programming
languages</a>. Programming has evolved from punch cards with rows of
numbers that a machine read, to drag-and-drop interfaces that increase
programming speed, with lots of other methods in between.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://media.giphy.com/media/1YhafU1NFtethNxJwa/giphy.gif" alt="pictures of different punchcards" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://giphy.com/gifs/punch-card-computer-1YhafU1NFtethNxJwa">via
GIPHY</a>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To this day, people are still developing programming languages, trying
to improve our programming efficiency. Others are building new languages
that improve accessibility to learning to code, like
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="http://nas.sr/%D9%82%D9%84%D8%A8/">developing
an Arabic programming language</a> or improving access for the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://wp.nyu.edu/ability/">blind
and visually impaired</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are tons of programming languages out there, each with its own
unique strengths and applications. Ultimately, the best one for you
depends on what you’re looking to achieve. Check out our
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/blog/what-programming-language-should-i-learn/">tips
for picking your first language</a> to learn more.
</p>
<h3 id="heading-programming-as-collaboration" class="h3__3B1DSzXTW-ux1viDSStOux">
PROGRAMMING AS COLLABORATION
</h3>
<blockquote class="blockquote__Bo1k0tPllp684-m2XzKRP">
<p class="p__1qg33Igem5pAgn4kPMirjw">
“The problem with programming is not that the computer isn’t logical—the
computer is terribly logical, relentlessly literal-minded.”
</p>
</blockquote>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Ellen Ullman, <em>Life in Code</em>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When we give instructions to a computer through code, we are, in our own
way, communicating with the computer. But since computers are built
differently than we are, we have to translate our instructions in a way
that computers will understand.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Computers interpret instructions in a very literal manner, so we have to
be very specific in how we program them. Think about instructing someone
to walk. If you start by telling them, “Put your foot in front of
yourself,” do they know what a foot is? Or what front means? (and now we
understand why it’s taken so long to develop bipedal robots…). In
coding, that could mean making sure that small things like punctuation
and spelling are correct. Many tears have been shed over a missing
semicolon (<code class="code__2rdF32qjRVp7mMVBHuPwDS">;</code>) a symbol
that a lot of programming languages use to denote the end of a line.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
But rather than think of this as a boss-employee relationship, it’s more
helpful to think about our relationship with computers as a
collaboration.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The computer is just one (particularly powerful) tool in a long list of
tools that humans have used to extend and augment their ability.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As mentioned before, computers are very good at certain things and well,
not so good at others. But here’s the good news: the things that
computers are good at, humans suck at, and the things that computers
suck at, humans are good at! Take a look at this handy table:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/programs/code-foundations-path/bop-i/human_computer.png" alt="table comparing human and computer abilities" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Just imagine what we can accomplish when we work together! We can make
movies with incredible special effects, have continuous 24/7 factory
production, and improve our cities and health.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://media.giphy.com/media/eyawSuxAexInC/giphy.gif" alt="picture of a robot-human" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://giphy.com/gifs/robot-human-fx2-eyawSuxAexInC">via
GIPHY</a>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>The best computer programs are the ones that enable us to make
things that we couldn’t do on our own, but leverage our creative
capacities. We may be good at drawing, but a computer is great at doing
the same task repeatedly — and quickly!</em>
</p>
<iframe src="https://content.codecademy.com/programs/code-foundations-path/bop-i/intro-article-replication/index.html" height="400px" class="iframe__rk2yNYIwJeUOj5J8cQJ9-">
</iframe>

<br>

<h3 id="heading-conclusion" class="h3__3B1DSzXTW-ux1viDSStOux">
CONCLUSION
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As programming becomes a larger part of our lives, it’s vital that
everyone has an understanding of what programming is and how it can be
used. Programming is important to our careers, but it also plays a key
role in how we participate in politics, how we buy things, and how we
stay in touch with one another.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Learning to code is an exciting journey. Whether your goal is to build a
mobile app, search a database, or program a robot, coding is a skill
that will take you far in life. Just remember — computers are tools.
While learning to program may initially be frustrating, if you choose to
stick with it, you’ll be able to make some brilliant things.
</p>

## What is Front-End?

<iframe frameborder="0" allowfullscreen="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" title="What is front-end?" width="100%" height="100%" src="https://www.youtube.com/embed/GJ8jidDdWVg?autoplay=0&amp;mute=0&amp;controls=1&amp;origin=https%3A%2F%2Fwww.codecademy.com&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;iv_load_policy=3&amp;modestbranding=1&amp;enablejsapi=1&amp;widgetid=1" id="widget2" data-gtm-yt-inspected-76="true">
</iframe>
