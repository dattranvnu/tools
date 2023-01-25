## Introduction: JavaScript Syntax, Part I

<p class="p__1qg33Igem5pAgn4kPMirjw">
The goal of this unit is to introduce you to JavaScript and get
comfortable with the basics of writing JavaScript programs.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After this unit, you will be able to:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Relate JavaScript’s role in web development
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Read and write introductory JavaScript syntax related to variables,
conditionals, functions, and scope
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Practice JavaScript syntax
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Execute JavaScript code beyond the Codecademy site
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

## JavaScript: All the Cool Kids Are Doing It

<p class="p__1qg33Igem5pAgn4kPMirjw">
When the Internet boomed in the 1990s, technology companies battled to
build the most powerful and efficient web browser on the market. This
sparked the first “browser war,” between Microsoft (Internet Explorer)
and NetScape (NetScape Navigator) to gain dominance in the usage share
of web browsers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Netscape needed a lightweight scripting language for easier programming
which ultimately made web development more accessible, unlike other
languages that required deeper training. In 1995, a NetScape employee,
Brendan Eich, was given ten days to help build the company a lightweight
scripting language. As a result, Eich built Mocha, which was later
renamed JavaScript. The moral of the story – JavaScript was never
intended to become the standard language for the web! However, as
NetScape won the browser war, the popularity of JavaScript grew. More
and more sites began using JavaScript, and those that didn’t eventually
had to as most developers used JavaScript to make websites.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
JavaScript is now an essential web technology that’s supported by major
web browsers. The language is crucial for anyone who wants to
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/catalog/subject/web-development">become
a web developer</a>. Many experts agree that JavaScript will continue to
grow as an indispensable language for web development.
</p>
<h3 id="heading-javascript-on-the-web" class="h3__3B1DSzXTW-ux1viDSStOux">
JavaScript on the Web
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
JavaScript, also called JS, is a flexible and powerful language that is
implemented consistently by various web browsers, making it the language
for web development. JavaScript, HTML, and CSS are the core components
of web technology. While HTML is responsible for structure and CSS is
responsible for style, JavaScript provides interactivity to web pages in
the browser.
</p>
<h3 id="heading-popularity-of-javascript" class="h3__3B1DSzXTW-ux1viDSStOux">
Popularity of JavaScript
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
At this point, you may be wondering: how is it that a language written
in 10 days by one guy became mass-adopted by the world wide web? In
short, JavaScript became a hit because it turned web browsers into
application platforms. Here’s how:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
JavaScript can be used in both the front-end and back-end of web
development.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
JavaScript is standardized so it’s frequently updated with new versions.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
JavaScript integrates easily with HTML and CSS.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
JavaScript allows websites to have interactivity like scroll transitions
and object movement. Modern browsers still compete to process JavaScript
the fastest for the best user experiences. Chrome,
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Usage_share_of_web_browsers#/media/File:StatCounter-browser-ww-monthly-201707-201707-map.png">the
most used Internet browser in 2017</a>, has been so successful because
of its ability to process JavaScript quickly.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
JavaScript offers a wide range of frameworks and libraries that help
developers create complex applications with low overhead. Programmers
can import libraries and frameworks in their code to augment their
application’s functionality.
</li>
</ol>
<h3 id="heading-javascript-for-servers" class="h3__3B1DSzXTW-ux1viDSStOux">
JavaScript for Servers
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the early 2000s, big platforms like Facebook and Google began using
JavaScript in their back-end server logic to process and respond to
front-end requests. JavaScript helped businesses scale since engineers
who knew JavaScript could apply those skills in a back-end context.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
JavaScript used for servers, also known as server-side JavaScript,
gained popularity because it allowed for scalability. In the server,
JavaScript can be integrated with other languages to communicate with
databases.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Node.JS, or Node, is one of the most popular versions of server-side
JavaScript. Node has been used to write large platforms for NASA, eBay
and many others. Since Javascript can execute programs out of sequential
order, Node can be used to create scalable web applications, messaging
platforms, and multiplayer games. This is why Google Cloud and Amazon
Web Service depend on Node for some of their services.
</p>
<h3 id="heading-what-else-can-javascript-do" class="h3__3B1DSzXTW-ux1viDSStOux">
What Else Can JavaScript Do?
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Beyond the web, JavaScript has a large presence amongst cross-platform
applications. We use some popular standalone desktop apps like Slack,
GitHub, Skype, and Tidal. These applications are developed with the
JavaScript framework called
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://electronjs.org/apps">Electron.js</a>.
Electron is excellent for making desktop applications that need to work
across different devices regardless of operating system.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In addition, JavaScript has the potential of expanding into other
innovative technologies such as virtual reality and gaming. JavaScript
can be used for animating, rendering and scaling. JavaScript even has
contributed to the internet of things, the technology that makes simple
objects, like your fridge, smarter. Everyday devices can become
interactive and collect data using JavaScript libraries.
</p>
<h3 id="heading-conclusion" class="h3__3B1DSzXTW-ux1viDSStOux">
Conclusion
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When diving into either programming or web development, JavaScript is an
excellent language to learn. The capabilities of JavaScript allow you to
use it in many different fields. Mastering what is known as “vanilla” or
plain JavaScript will help you to tackle more complicated frameworks and
libraries to make you a competitive developer. Take some of our
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/catalog/language/javascript">Codecademy
JavaScript courses</a> to become the JavaScript rockstar companies are
looking for!
</p>

## JavaScript Versions: ES6 and Before

<p class="p__1qg33Igem5pAgn4kPMirjw">
You might have seen the term “ES6” or “Javascript ES6” and wondered what
it actually means. Well wonder no further, because we’re going to dive
into what ES6 is and how it relates to Javascript!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
First, let’s bring in some history. JavaScript was introduced in 1995 by
the company Netscape Communications as a scripting language for web
designers and programmers to interact with web pages. The next year,
Netscape submitted JavaScript to a standards developing organization
called Ecma International to create standards for a scripting language
(a type of programming language). In 1997, Ecma International released
ECMA-262 which sets standards for the first version of a scripting
language called ECMAScript, shortened to ES.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
These new ECMAScript standards provided rules for the architecture of
JavaScript features. As new programming paradigms emerged and developers
sought new features, newer versions of ECMAScript provided a basis for
consistency between new and old JavaScript versions.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To fully distinguish the difference between JavaScript and ECMAScript:
if you want to create an app or program you can use JavaScript — if you
want to create a new scripting language you can follow the guidelines in
ECMAScript. So, when you see ES6 or JavaScript ES6, it means that that
version of JavaScript is following the specifications in the sixth
edition of ECMAScript! You might also see ES2015 instead of ES6, but
both terminologies are referring to the same 6th edition of ECMAScript
that was released in 2015. Take a look at the timeline below to see how
JavaScript has evolved over the years:
</p>

<img src="https://content.codecademy.com/courses/javascript-article-assets/javascript_timeline.svg" alt="Timeline showing the evolution of JS editions from inception to 2018" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now, you may be asking, what makes an update in 2015 still relevant
today when there are more recent updates like ES7 and ES8?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Well, despite the release of newer versions, ES6 is actually the biggest
update made to ECMAScript since the first edition released in 1997! Some
developers even refer to ES6 as “Modern JavaScript” because of all the
major additions. There were so many great features added to help
JavaScript developers that include:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
new keywords like <code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> to declare
variables,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
new function syntax using Arrow functions,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
creation of Classes,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
parameters with default values,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
promises for asynchronous actions,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
and many more!
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Up-to-date browsers now support most of the ES6 features which allow
developers to take advantage of these new additions. ES6 ultimately
allows programmers to save time and write more concise code. As with all
ES6 features, there are other underlying benefits and tradeoffs to
consider. Nonetheless, there has been a strong adoption of ES6 in the
development community. One big ES6 benefit is the ease it allows for
utilizing a popular programming paradigm, Object-Oriented Programming
(OOP). This change allowed for developers of other languages who are
used to OOP can now transition into learning and using JavaScript.
Another reason for the popularity of ES6 is correlated with the usage of
ES6 in popular frameworks like React. So, if you want to learn the
newest tools and frameworks, you will have to pick up ES6 along the way.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This being said, you shouldn’t disregard legacy code, i.e. older
versions of JavaScript. In fact, there are still many projects that are
built and maintained with legacy code! If you want the ability and
freedom to work on any sort of JavaScript project, you should
familiarize yourself with pre-ES6 and ES6 JavaScript syntax. But don’t
worry, we cover both pre-ES6 and ES6 in our JavaScript course. Check it
out to become a rockstar at JavaScript basics and learn fundamental
programming skills!
</p>

## JavaScript Versions: ES6 and Before

<p class="p__1qg33Igem5pAgn4kPMirjw">
You might have seen the term “ES6” or “Javascript ES6” and wondered what
it actually means. Well wonder no further, because we’re going to dive
into what ES6 is and how it relates to Javascript!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
First, let’s bring in some history. JavaScript was introduced in 1995 by
the company Netscape Communications as a scripting language for web
designers and programmers to interact with web pages. The next year,
Netscape submitted JavaScript to a standards developing organization
called Ecma International to create standards for a scripting language
(a type of programming language). In 1997, Ecma International released
ECMA-262 which sets standards for the first version of a scripting
language called ECMAScript, shortened to ES.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
These new ECMAScript standards provided rules for the architecture of
JavaScript features. As new programming paradigms emerged and developers
sought new features, newer versions of ECMAScript provided a basis for
consistency between new and old JavaScript versions.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To fully distinguish the difference between JavaScript and ECMAScript:
if you want to create an app or program you can use JavaScript — if you
want to create a new scripting language you can follow the guidelines in
ECMAScript. So, when you see ES6 or JavaScript ES6, it means that that
version of JavaScript is following the specifications in the sixth
edition of ECMAScript! You might also see ES2015 instead of ES6, but
both terminologies are referring to the same 6th edition of ECMAScript
that was released in 2015. Take a look at the timeline below to see how
JavaScript has evolved over the years:
</p>

<img src="https://content.codecademy.com/courses/javascript-article-assets/javascript_timeline.svg" alt="Timeline showing the evolution of JS editions from inception to 2018" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now, you may be asking, what makes an update in 2015 still relevant
today when there are more recent updates like ES7 and ES8?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Well, despite the release of newer versions, ES6 is actually the biggest
update made to ECMAScript since the first edition released in 1997! Some
developers even refer to ES6 as “Modern JavaScript” because of all the
major additions. There were so many great features added to help
JavaScript developers that include:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
new keywords like <code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> to declare
variables,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
new function syntax using Arrow functions,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
creation of Classes,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
parameters with default values,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
promises for asynchronous actions,
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
and many more!
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Up-to-date browsers now support most of the ES6 features which allow
developers to take advantage of these new additions. ES6 ultimately
allows programmers to save time and write more concise code. As with all
ES6 features, there are other underlying benefits and tradeoffs to
consider. Nonetheless, there has been a strong adoption of ES6 in the
development community. One big ES6 benefit is the ease it allows for
utilizing a popular programming paradigm, Object-Oriented Programming
(OOP). This change allowed for developers of other languages who are
used to OOP can now transition into learning and using JavaScript.
Another reason for the popularity of ES6 is correlated with the usage of
ES6 in popular frameworks like React. So, if you want to learn the
newest tools and frameworks, you will have to pick up ES6 along the way.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This being said, you shouldn’t disregard legacy code, i.e. older
versions of JavaScript. In fact, there are still many projects that are
built and maintained with legacy code! If you want the ability and
freedom to work on any sort of JavaScript project, you should
familiarize yourself with pre-ES6 and ES6 JavaScript syntax. But don’t
worry, we cover both pre-ES6 and ES6 in our JavaScript course. Check it
out to become a rockstar at JavaScript basics and learn fundamental
programming skills!
</p>

## INTRODUCTION TO JAVASCRIPT

### What is JavaScript?

<p class="p__1qg33Igem5pAgn4kPMirjw">
Last year, millions of learners from our community started with
JavaScript. Why? JavaScript is primarily known as the language of most
modern web browsers, and its early quirks gave it a bit of a bad
reputation. However, the language has continued to evolve and improve.
JavaScript is a powerful, flexible, and fast programming language now
being used for increasingly complex web development and beyond!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Since JavaScript remains at the core of web development, it’s often the
first language learned by self-taught coders eager to learn and build.
We’re excited for what you’ll be able to create with the JavaScript
foundation you gain here. JavaScript powers the dynamic behavior on most
websites, including this one.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, you will learn introductory coding concepts including
data types and built-in objects—essential knowledge for all aspiring
developers. Make sure to take notes and pace yourself. This foundation
will set you up for understanding the more complex concepts you’ll
encounter later.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Move to the next exercise when you’re ready to begin.
</p>

**Solutions**

``` html
```

## INTRODUCTION TO JAVASCRIPT

### Console

<p class="p__1qg33Igem5pAgn4kPMirjw">
The console is a panel that displays important messages, like errors,
for developers. Much of the work the computer does with our code is
invisible to us by default. If we want to see things appear on our
screen, we can print, or <em>log</em>, to our console directly.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In JavaScript, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console</code> keyword refers
to an object, a collection of data and actions, that we can use in our
code. Keywords are words that are built into the JavaScript language, so
the computer recognizes them and treats them specially.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
One action, or method, that is built into the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console</code> object is the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.log()</code> method. When we
write <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
what we put inside the parentheses will get printed, or logged, to the
console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It’s going to be very useful for us to print values to the console, so
we can see the work that we’re doing.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">5</span><span class="mtk1">); </span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This example logs <code class="code__2rdF32qjRVp7mMVBHuPwDS">5</code> to
the console. The semicolon denotes the end of the line, or statement.
Although in JavaScript your code will usually run as intended without a
semicolon, we recommend learning the habit of ending each statement with
a semicolon so you never leave one out in the few instances when they
are required.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll see later on that we can use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to print
different kinds of data.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log</code>
code in the editor to log your age to the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Run your code when you are ready to see the result.
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
On the next line, write another
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log</code> to print
out a different number representing the number of weeks you’ve been
programming.
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

## INTRODUCTION TO JAVASCRIPT

### Comments

<p class="p__1qg33Igem5pAgn4kPMirjw">
Programming is often highly collaborative. In addition, our own code can
quickly become difficult to understand when we return to it— sometimes
only an hour later! For these reasons, it’s often useful to leave notes
in our code for other developers or ourselves.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As we write JavaScript, we can write
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/comments?page_ref=catalog">comments</a>
in our code that the computer will ignore as our program runs. These
comments exist just for human readers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Comments can explain what the code is doing, leave instructions for
developers using the code, or add any other useful annotations.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are two types of code comments in JavaScript:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
A <em>single line comment</em> will comment out a single line and is
denoted with two forward slashes
<code class="code__2rdF32qjRVp7mMVBHuPwDS">//</code> preceding it.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk16">// Prints 5&nbsp;to the console</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">5</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can also use a single line comment to comment after a line of code:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">5</span><span class="mtk1">);&nbsp;&nbsp;</span><span class="mtk16">// Prints 5&nbsp;</span></span><br></div></code></pre></pre>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
A <em>multi-line comment</em> will comment out multiple lines and is
denoted with <code class="code__2rdF32qjRVp7mMVBHuPwDS">/*</code> to
begin the comment, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">*/</code> to end the comment.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk16">/*</span></span><br><span><span class="mtk16">This is all commented </span></span><br><span><span class="mtk16">console.log(10);</span></span><br><span><span class="mtk16">None of this is going to run!</span></span><br><span><span class="mtk16">console.log(99);</span></span><br><span><span class="mtk16">*/</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can also use this syntax to comment something out in the middle of a
line of code:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk16">/*IGNORED!*/</span><span class="mtk1"> </span><span class="mtk9">5</span><span class="mtk1">);&nbsp;&nbsp;</span><span class="mtk16">// Still just prints 5&nbsp;</span></span><br></div></code></pre></pre>
</li>
</ol>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s practice adding some code comments.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To the right, we’ve provided you with the beginning of the book
<em>Catch-22</em> by Joseph Heller.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
On line 1, write a single line comment that says
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Opening line</code>.
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
Single line comments are great for adding context to your code.
Multi-line comments are often best suited to prevent a block of code
from running. However, both types of comments can be used for either
purpose.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Use a multi-line comment so that the bottom 6
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statements are all commented out.
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

## INTRODUCTION TO JAVASCRIPT

### Data Types

<p class="p__1qg33Igem5pAgn4kPMirjw">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/data-types?page_ref=catalog">Data
types</a> are the classifications we give to the different kinds of data
that we use in programming. In JavaScript, there are seven fundamental
data types:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Number</em>: Any number, including numbers with decimals:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">4</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">8</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1516</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">23.42</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>String</em>: Any grouping of characters on your keyboard (letters,
numbers, spaces, symbols, etc.) surrounded by single quotes:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">’ … ’</code> or double quotes
<code class="code__2rdF32qjRVp7mMVBHuPwDS">” … “</code>, though we
prefer single quotes. Some people like to think of string as a fancy
word for text.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Boolean</em>: This data type only has two possible values— either
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> (without
quotes). It’s helpful to think of booleans as on and off switches or as
the answers to a “yes” or “no” question.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Null</em>: This data type represents the intentional absence of a
value, and is represented by the keyword
<code class="code__2rdF32qjRVp7mMVBHuPwDS">null</code> (without quotes).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Undefined</em>: This data type is denoted by the keyword
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code> (without
quotes). It also represents the absence of a value though it has a
different use than
<code class="code__2rdF32qjRVp7mMVBHuPwDS">null</code>.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code> means that a
given value does not exist.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Symbol</em>: A newer feature to the language, symbols are unique
identifiers, useful in more complex coding. No need to worry about these
for now.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<em>Object</em>: Collections of related data.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The first 6 of those types are considered <em>primitive data types</em>.
They are the most basic data types in the language. <em>Objects</em> are
more complex, and you’ll learn much more about them as you progress
through JavaScript. At first, seven types may not seem like that many,
but soon you’ll observe the world opens with possibilities once you
start leveraging each one. As you learn more about objects, you’ll be
able to create complex collections of data.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
But before we do that, let’s get comfortable with strings and numbers!
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Location of Codecademy headquarters: 575 Broadway</span><span class="mtk8">, New York City'</span><span class="mtk1">);</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">40</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we first printed a string. Our string isn’t just a
single word; it includes both capital and lowercase letters, spaces, and
punctuation.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, we printed the number 40, notice we did not use quotes.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
On line 1, log the string
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘JavaScript’</code> to the
console.
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
On line 2, log the number
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2011</code> to the console.
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
On line 3, print <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Woohoo! I
love to code! #codecademy’</code> to the console.
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
On line 4, print the number
<code class="code__2rdF32qjRVp7mMVBHuPwDS">20.49</code> to the console.
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

## INTRODUCTION TO JAVASCRIPT

### Arithmetic Operators

<p class="p__1qg33Igem5pAgn4kPMirjw">
Basic arithmetic often comes in handy when programming.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
An
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/operators?page_ref=catalog">operator</a>
is a character that performs a task in our code. JavaScript has several
built-in <em>arithmetic operators</em>, that allow us to perform
mathematical calculations on numbers. These include the following
operators and their corresponding symbols:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Add: <code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Subtract: <code class="code__2rdF32qjRVp7mMVBHuPwDS">-</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Multiply: <code class="code__2rdF32qjRVp7mMVBHuPwDS">\*</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Divide: <code class="code__2rdF32qjRVp7mMVBHuPwDS">/</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Remainder: <code class="code__2rdF32qjRVp7mMVBHuPwDS">%</code>
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The first four work how you might guess:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">3</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">4</span><span class="mtk1">); </span><span class="mtk16">// Prints 7</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">5</span><span class="mtk1"> -&nbsp;</span><span class="mtk9">1</span><span class="mtk1">); </span><span class="mtk16">// Prints 4</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">4</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">2</span><span class="mtk1">); </span><span class="mtk16">// Prints 8</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">9</span><span class="mtk1"> /&nbsp;</span><span class="mtk9">3</span><span class="mtk1">); </span><span class="mtk16">// Prints 3</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note that when we
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> the
computer will evaluate the expression inside the parentheses and print
that result to the console. If we wanted to print the characters
<code class="code__2rdF32qjRVp7mMVBHuPwDS">3 + 4</code>, we would wrap
them in quotes and print them as a string.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">11</span><span class="mtk1"> %&nbsp;</span><span class="mtk9">3</span><span class="mtk1">); </span><span class="mtk16">// Prints 2</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">12</span><span class="mtk1"> %&nbsp;</span><span class="mtk9">3</span><span class="mtk1">); </span><span class="mtk16">// Prints 0</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The remainder operator, sometimes called <em>modulo</em>, returns the
number that remains after the right-hand number divides into the
left-hand number as many times as it evenly can:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">11 % 3</code> equals 2
because 3 fits into 11 three times, leaving 2 as the remainder.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside of a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>, add
<code class="code__2rdF32qjRVp7mMVBHuPwDS">3.5</code> to your age.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This is the age you’ll be when we start sending people to live on Mars.
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
On a new line write another
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>. Inside
the parentheses, take the current year and subtract
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1969</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The answer is how many years it’s been since the 1969 moon landing.
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
Create another
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>. Inside
the parentheses divide
<code class="code__2rdF32qjRVp7mMVBHuPwDS">65</code> by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">240</code>.
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
Create one last
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>. Inside
the parentheses, multiply
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0.2708</code> by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
That’s the percent of the sun that is made up of helium. Assuming we
could stand on the sun, we’d all sound like chipmunks!
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

## INTRODUCTION TO JAVASCRIPT

### String Concatenation

<p class="p__1qg33Igem5pAgn4kPMirjw">
Operators aren’t just for numbers! When a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code> operator is used on
two strings, it appends the right string to the left string:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'hi'</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'ya'</span><span class="mtk1">); </span><span class="mtk16">// Prints 'hiya'</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'wo'</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'ah'</span><span class="mtk1">); </span><span class="mtk16">// Prints 'woah'</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'I love to '</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'code.'</span><span class="mtk1">)</span></span><br><span><span class="mtk16">// Prints 'I love to code.'</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This process of appending one string to another is called
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/strings?page_ref=catalog"><em>concatenation</em></a>.
Notice in the third example we had to make sure to include a space at
the end of the first string. The computer will join the strings exactly,
so we needed to make sure to include the space we wanted between the two
strings.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'front '</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'space'</span><span class="mtk1">); </span></span><br><span><span class="mtk16">// Prints 'front space'</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'back'</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">' space'</span><span class="mtk1">); </span></span><br><span><span class="mtk16">// Prints 'back space'</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'no'</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'space'</span><span class="mtk1">); </span></span><br><span><span class="mtk16">// Prints 'nospace'</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'middle'</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">' '</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'space'</span><span class="mtk1">); </span></span><br><span><span class="mtk16">// Prints 'middle space'</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Just like with regular math, we can combine, or chain, our operations to
get a final result:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'One'</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">', '</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'two'</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">', '</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'three!'</span><span class="mtk1">); </span></span><br><span><span class="mtk16">// Prints 'One, two, three!'</span></span><br></div></code></pre></pre>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside a <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement, concatenate the two strings
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello’</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘World’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note: You should concatenate the two strings exactly (without
introducing any additional characters).
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
We left off the space last time. Create a second
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement in which you concatenate the strings
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello’</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘World’</code>, but this time
make sure to also include a space
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">’ ’</code>) between the two
words.
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

## INTRODUCTION TO JAVASCRIPT

### Properties

<p class="p__1qg33Igem5pAgn4kPMirjw">
When you introduce a new piece of data into a JavaScript program, the
browser saves it as an instance of the data type. All data types have
access to specific properties that are passed down to each instance. For
example, every string instance has a property called
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/strings/length"><code class="code__2rdF32qjRVp7mMVBHuPwDS">length</code></a>
that stores the number of characters in that string. You can retrieve
property information by appending the string with a period and the
property name:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Hello'</span><span class="mtk1">.</span><span class="mtk10">length</span><span class="mtk1">); </span><span class="mtk16">// Prints 5</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.</code> is another
operator! We call it the <em>dot operator</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the value saved to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">length</code> property is
retrieved from the instance of the string,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello’</code>. The program
prints <code class="code__2rdF32qjRVp7mMVBHuPwDS">5</code> to the
console, because <code class="code__2rdF32qjRVp7mMVBHuPwDS">Hello</code>
has five characters in it.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.length</code>
property to log the number of characters in the following string to the
console:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk8">'Teaching the world how to code'</span></span><br></div></code></pre></pre>

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

## INTRODUCTION TO JAVASCRIPT

### Methods

<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember that
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/methods?page_ref=catalog">methods</a>
are actions we can perform. Data types have access to specific methods
that allow us to handle instances of that data type. JavaScript provides
a number of string methods.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We <em>call</em>, or use, these methods by appending an instance with:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
a period (the dot operator)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the name of the method
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
opening and closing parentheses
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
E.g. <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘example
string’.methodName()</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Does that syntax look a little familiar? When we use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> we’re
calling the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.log()</code>
method on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">console</code>
object. Let’s see
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> and some
real string methods in action!
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'hello'</span><span class="mtk1">.</span><span class="mtk10">toUpperCase</span><span class="mtk1">()); </span><span class="mtk16">// Prints 'HELLO'</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Hey'</span><span class="mtk1">.</span><span class="mtk10">startsWith</span><span class="mtk1">(</span><span class="mtk8">'H'</span><span class="mtk1">)); </span><span class="mtk16">// Prints true</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s look at each of the lines above:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
On the first line, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.toUpperCase()</code> method
is called on the string instance
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘hello’</code>. The result is
logged to the console. This method returns a string in all capital
letters: <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘HELLO’</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
On the second line, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.startsWith()</code> method
is called on the string instance
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hey’</code>. This method
also accepts the character
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘H’</code> as an input, or
<em>argument</em>, between the parentheses. Since the string
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hey’</code> does start with
the letter <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘H’</code>, the
method returns the boolean
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can find a list of built-in string methods in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/prototype">JavaScript
documentation</a>. Developers use documentation as a reference tool. It
describes JavaScript’s keywords, methods, and syntax.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.toUpperCase()</code>
method to log the string
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Codecademy’</code> to the
console in all capital letters.
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
In the second
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement in <strong>app.js</strong>, we have a string
<code class="code__2rdF32qjRVp7mMVBHuPwDS">’ Remove whitespace ‘</code>
which has spaces before and after the words
<code class="code__2rdF32qjRVp7mMVBHuPwDS">’Remove whitespace’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If we browse the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/prototype">JavaScript
string documentation</a>, we find several built-in string methods that
each accomplish a different goal. The one method that seems ideal for us
is <code class="code__2rdF32qjRVp7mMVBHuPwDS">.trim()</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Use the method to remove the whitespace at the beginning and end of the
string in the second
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement.
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

## INTRODUCTION TO JAVASCRIPT

### Built-in Objects

<p class="p__1qg33Igem5pAgn4kPMirjw">
In addition to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console</code>, there are
other
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects">objects
built into JavaScript</a>. Down the line, you’ll build your own objects,
but for now these “built-in” objects are full of useful functionality.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, if you wanted to perform more complex mathematical
operations than arithmetic, JavaScript has the built-in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math</code> object.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The great thing about objects is that they have methods! Let’s call the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.random()</code> method from
the built-in <code class="code__2rdF32qjRVp7mMVBHuPwDS">Math</code>
object:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">Math</span><span class="mtk1">.</span><span class="mtk10">random</span><span class="mtk1">()); </span><span class="mtk16">// Prints a&nbsp;random number between 0&nbsp;and 1</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we called the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.random()</code> method by
appending the object name with the dot operator, the name of the method,
and opening and closing parentheses. This method returns a random number
between 0 (inclusive) and 1 (exclusive).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To generate a random number between 0 and 50, we could multiply this
result by 50, like so:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">Math</span><span class="mtk1">.</span><span class="mtk10">random</span><span class="mtk1">() *&nbsp;</span><span class="mtk9">50</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The example above will likely evaluate to a decimal. To ensure the
answer is a whole number, we can take advantage of another useful
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math</code> method called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.floor()</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.floor()</code> takes a
decimal number, and rounds down to the nearest whole number. You can use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.floor()</code> to round
down a random number like this:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">Math</span><span class="mtk1">.</span><span class="mtk10">floor</span><span class="mtk1">(</span><span class="mtk9">Math</span><span class="mtk1">.</span><span class="mtk10">random</span><span class="mtk1">() *&nbsp;</span><span class="mtk9">50</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this case:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.random()</code>
generates a random number between 0 and 1.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
We then multiply that number by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">50</code>, so now we have a
number between 0 and 50.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Then, <code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.floor()</code>
rounds the number down to the nearest whole number.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you wanted to see the number printed to the terminal, you would still
need to use a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">Math</span><span class="mtk1">.</span><span class="mtk10">floor</span><span class="mtk1">(</span><span class="mtk9">Math</span><span class="mtk1">.</span><span class="mtk10">random</span><span class="mtk1">() *&nbsp;</span><span class="mtk9">50</span><span class="mtk1">)); </span><span class="mtk16">// Prints a&nbsp;random whole number between 0&nbsp;and 50</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To see all of the properties and methods on the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math</code> object, take a
look at
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math">the
documentation here</a>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside of a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>, create
a random number with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.random()</code>, then
multiply it by <code class="code__2rdF32qjRVp7mMVBHuPwDS">100</code>.
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
Now, use <code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.floor()</code>
to make the output a whole number.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> you
wrote in the last step, put the existing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.random() \* 100</code>
code inside the parentheses of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.floor()</code>.
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
Find a method on the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math">JavaScript
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math</code> object</a> that
returns the smallest integer greater than or equal to a decimal number.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Use this method with the number
<code class="code__2rdF32qjRVp7mMVBHuPwDS">43.8</code>. Log the answer
to the console.
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
Use the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number">JavaScript
documentation</a> to find a method on the built-in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Number</code> object that
checks if a number is an integer.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Put the number <code class="code__2rdF32qjRVp7mMVBHuPwDS">2017</code> in
the parentheses of the method and use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to print
the result.
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

## INTRODUCTION TO JAVASCRIPT

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s take one more glance at the concepts we just learned:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Data is printed, or logged, to the console, a panel that displays
messages, with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
We can write single-line comments with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">//</code> and multi-line
comments between <code class="code__2rdF32qjRVp7mMVBHuPwDS">/*</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">*/</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
There are 7 fundamental data types in JavaScript: strings, numbers,
booleans, null, undefined, symbol, and object.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Numbers are any number without quotes:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">23.8879</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Strings are characters wrapped in single or double quotes:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Sample String’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The built-in arithmetic operators include
<code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">-</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\*</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">/</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">%</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Objects, including instances of data types, can have properties, stored
information. The properties are denoted with a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.</code> after the name of
the object, for example:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello’.length</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Objects, including instances of data types, can have methods which
perform actions. Methods are called by appending the object or instance
with a period, the method name, and parentheses. For example:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘hello’.toUpperCase()</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
We can access properties and methods by using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.</code>, dot operator.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Built-in objects, including
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math</code>, are collections
of methods and properties that JavaScript provides.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here are a few more resources to add to your toolkit:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript">Codecademy
Docs: JavaScript</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/workspaces/new">Codecademy
Workspaces: JavaScript</a>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Make sure to bookmark these links so you have them at your disposal.
</p>

## VARIABLES

### Variables

<p class="p__1qg33Igem5pAgn4kPMirjw">
In programming, a <em>variable</em> is a container for a value. You can
think of variables as little containers for information that live in a
computer’s memory. Information stored in variables, such as a username,
account number, or even personalized greeting can then be found in
memory.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Variables also provide a way of labeling data with a descriptive name,
so our programs can be understood more clearly by the reader and
ourselves.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In short, variables label and store data in memory. There are only a few
things you can do with variables:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Create a variable with a descriptive name.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Store or update information stored in a variable.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Reference or “get” information stored in a variable.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It is important to distinguish that variables are not values; they
contain values and represent them with a name. Observe the diagram with
the colored boxes. Each box represents variables; the values are
represented by the content, and the name is represented with the label.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, we will cover how to use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> keywords to
create variables.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
When you’re ready to start, go to the next exercise!
</p>

**Solutions**

``` html
```

## VARIABLES

### Create a Variable: var

<p class="p__1qg33Igem5pAgn4kPMirjw">
There were a lot of changes introduced in the ES6 version of JavaScript
in 2015. One of the biggest changes was two new keywords,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code>, to create, or
<em>declare</em>, variables. Prior to the ES6, programmers could only
use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code> keyword to
declare variables.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">var myName</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Arya'</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">myName</span><span class="mtk1">);</span></span><br><span><span class="mtk16">// Output: Arya</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s consider the example above:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code>, short for
variable, is a JavaScript <em>keyword</em> that creates, or
<em>declares</em>, a new variable.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myName</code> is the
variable’s name. Capitalizing in this way is a standard convention in
JavaScript called <em>camel casing</em>. In camel casing you group words
into one, the first word is lowercase, then every word that follows will
have its first letter uppercased. (e.g. camelCaseEverything).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">=</code> is the
<em>assignment operator</em>. It assigns the value
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Arya’</code>) to the
variable (<code class="code__2rdF32qjRVp7mMVBHuPwDS">myName</code>).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Arya’</code> is the
<em>value</em> assigned
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">=</code>) to the variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myName</code>. You can also
say that the <code class="code__2rdF32qjRVp7mMVBHuPwDS">myName</code>
variable is <em>initialized</em> with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Arya’</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
After the variable is declared, the string value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Arya’</code> is printed to
the console by referencing the variable name:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log(myName)</code>.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are a few general rules for naming variables:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Variable names cannot start with numbers.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Variable names are case sensitive, so
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myName</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myname</code> would be
different variables. It is bad practice to create two variables that
have the same name using different cases.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Variable names cannot be the same as <em>keywords</em>. For a
comprehensive list of keywords check out
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#Keywords">MDN’s
keyword documentation</a>.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the next exercises, we will learn why ES6’s
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> are the
preferred variable keywords by many programmers. Because there is still
a ton of code written prior to ES6, it’s helpful to be familiar with the
pre-ES6 <code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code> keyword.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you want to learn more about
<code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code> and the quirks
associated with it, check out the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var">MDN
var documentation</a>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Declare a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">favoriteFood</code> using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code> keyword and assign
to it the string
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘pizza’</code>.
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
Declare a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">numOfSlices</code> using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code> keyword and assign
to it the number <code class="code__2rdF32qjRVp7mMVBHuPwDS">8</code>.
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
Under the <code class="code__2rdF32qjRVp7mMVBHuPwDS">numOfSlices</code>
variable, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to print
the value saved to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">favoriteFood</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
On the following line, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to print
the value saved to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">numOfSlices</code>.
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

## VARIABLES

### Create a Variable: let

<p class="p__1qg33Igem5pAgn4kPMirjw">
As mentioned in the previous exercise, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> keyword was
introduced in ES6. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> keyword signals
that the variable can be reassigned a different value. Take a look at
the example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let meal</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Enchiladas'</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">meal</span><span class="mtk1">); </span><span class="mtk16">// Output: Enchiladas</span></span><br><span><span class="mtk9">meal</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Burrito'</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">meal</span><span class="mtk1">); </span><span class="mtk16">// Output: Burrito</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Another concept that we should be aware of when using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> (and even
<code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code>) is that we can
declare a variable without assigning the variable a value. In such a
case, the variable will be automatically initialized with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let price</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">price</span><span class="mtk1">); </span><span class="mtk16">// Output: undefined</span></span><br><span><span class="mtk9">price</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">350</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">price</span><span class="mtk1">); </span><span class="mtk16">// Output: 350</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice in the example above:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If we don’t assign a value to a variable declared using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> keyword, it
automatically has a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
We can reassign the value of the variable.
</li>
</ul>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a <code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> variable
called <code class="code__2rdF32qjRVp7mMVBHuPwDS">changeMe</code> and
set it equal to the boolean
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>.
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
On the line after
<code class="code__2rdF32qjRVp7mMVBHuPwDS">changeMe</code> is declared,
set the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">changeMe</code> to be the
boolean <code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To check if <code class="code__2rdF32qjRVp7mMVBHuPwDS">changeMe</code>
was reassigned, log the value saved to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">changeMe</code> to the
console.
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

## VARIABLES

### Create a Variable: const

<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> keyword was
also introduced in ES6, and is short for the word constant. Just like
with <code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> you can store any
value in a <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code>
variable. The way you declare a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> variable and
assign a value to it follows the same structure as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code>. Take a look at
the following example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const myName</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Gilberto'</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">myName</span><span class="mtk1">); </span><span class="mtk16">// Output: Gilberto</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
However, a <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code>
variable cannot be reassigned because it is <em>constant</em>. If you
try to reassign a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> variable, you’ll
get a <code class="code__2rdF32qjRVp7mMVBHuPwDS">TypeError</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Constant variables <em>must</em> be assigned a value when declared. If
you try to declare a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> variable without
a value, you’ll get a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">SyntaxError</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you’re trying to decide between which keyword to use,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code>, think about
whether you’ll need to reassign the variable later on. If you do need to
reassign the variable use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code>, otherwise, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a constant variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">entree</code> and set it to
equal to the string
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Enchiladas’</code>.
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
Just to check that you’ve saved the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Enchiladas’</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">entree</code>, log the value
of <code class="code__2rdF32qjRVp7mMVBHuPwDS">entree</code> to the
console.
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
Great, let’s see what happens if you try to reassign a constant
variable.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Paste the following code to the bottom of your program.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">entree</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Tacos'</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This code throws the following error when you run your code:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><code class="errorBlock__2oVHQQnsjhJzzFnkMpHhy3 code__2rdF32qjRVp7mMVBHuPwDS language-error">TypeError: Assignment to constant variable.</code></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After you clear this checkpoint, if you want to see about another quirk
of <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> in action
open the hint!
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

## VARIABLES

### Mathematical Assignment Operators

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s consider how we can use variables and math operators to calculate
new values and assign them to a variable. Check out the example below:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let w</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">4</span><span class="mtk1">;</span></span><br><span><span class="mtk9">w</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">w</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">1</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">w</span><span class="mtk1">); </span><span class="mtk16">// Output: 5</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we created the variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">w</code> with the number
<code class="code__2rdF32qjRVp7mMVBHuPwDS">4</code> assigned to it. The
following line, <code class="code__2rdF32qjRVp7mMVBHuPwDS">w = w +
1</code>, increases the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">w</code> from
<code class="code__2rdF32qjRVp7mMVBHuPwDS">4</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">5</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Another way we could have reassigned
<code class="code__2rdF32qjRVp7mMVBHuPwDS">w</code> after performing
some mathematical operation on it is to use built-in <em>mathematical
assignment operators</em>. We could re-write the code above to be:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let w</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">4</span><span class="mtk1">;</span></span><br><span><span class="mtk9">w</span><span class="mtk1"> += </span><span class="mtk9">1</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">w</span><span class="mtk1">); </span><span class="mtk16">// Output: 5</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the second example, we used the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">+=</code> assignment operator
to reassign <code class="code__2rdF32qjRVp7mMVBHuPwDS">w</code>. We’re
performing the mathematical operation of the first operator
<code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code> using the number to
the right, then reassigning
<code class="code__2rdF32qjRVp7mMVBHuPwDS">w</code> to the computed
value.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We also have access to other mathematical assignment operators:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">-=</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\*=</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">/=</code> which work in a
similar fashion.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let x</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">20</span><span class="mtk1">;</span></span><br><span><span class="mtk9">x</span><span class="mtk1"> -= </span><span class="mtk9">5</span><span class="mtk1">; </span><span class="mtk16">// Can be written as x&nbsp;= x&nbsp;- 5</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">x</span><span class="mtk1">); </span><span class="mtk16">// Output: 15</span></span><br><span><span> </span></span><br><span><span class="mtk12">let y</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">50</span><span class="mtk1">;</span></span><br><span><span class="mtk9">y</span><span class="mtk1"> *= </span><span class="mtk9">2</span><span class="mtk1">; </span><span class="mtk16">// Can be written as y&nbsp;= y&nbsp;* 2</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">y</span><span class="mtk1">); </span><span class="mtk16">// Output: 100</span></span><br><span><span> </span></span><br><span><span class="mtk12">let z</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">8</span><span class="mtk1">;</span></span><br><span><span class="mtk9">z</span><span class="mtk1"> /= </span><span class="mtk9">2</span><span class="mtk1">; </span><span class="mtk16">// Can be written as z&nbsp;= z&nbsp;/ 2</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">z</span><span class="mtk1">); </span><span class="mtk16">// Output: 4</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s practice using these mathematical assignment operators!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">+=</code>
mathematical assignment operator to increase the value stored in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">levelUp</code> by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">5</code>.
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
Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">-=</code>
mathematical assignment operator to decrease the value stored in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">powerLevel</code> by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100</code>.
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
Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\*=</code>
mathematical assignment operator to multiply the value stored in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">multiplyMe</code> by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">11</code>.
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
Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">/=</code>
mathematical assignment operator to divide the value stored in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">quarterMe</code> by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">4</code>.
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

## VARIABLES

### The Increment and Decrement Operator

<p class="p__1qg33Igem5pAgn4kPMirjw">
Other mathematical assignment operators include the <em>increment
operator</em> (<code class="code__2rdF32qjRVp7mMVBHuPwDS">++</code>) and
<em>decrement operator</em>
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">–</code>).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The increment operator will increase the value of the variable by 1. The
decrement operator will decrease the value of the variable by 1. For
example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let a</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">10</span><span class="mtk1">;</span></span><br><span><span class="mtk9">a</span><span class="mtk1">++;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">a</span><span class="mtk1">); </span><span class="mtk16">// Output: 11</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let b</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">20</span><span class="mtk1">;</span></span><br><span><span class="mtk9">b</span><span class="mtk1">--;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">b</span><span class="mtk1">); </span><span class="mtk16">// Output: 19</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Just like the previous mathematical assignment operators
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">+=</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">-=</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\*=</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">/=</code>), the variable’s
value is updated <em>and</em> assigned as the new value of that
variable.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Using the increment operator, increase the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">gainedDollar</code>.
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
Using the decrement operator, decrease the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lostDollar</code>.
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

## VARIABLES

### String Concatenation with Variables

<p class="p__1qg33Igem5pAgn4kPMirjw">
In previous exercises, we assigned strings to variables. Now, let’s go
over how to connect, or concatenate, strings in variables.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code> operator can be
used to combine two string values even if those values are being stored
in variables:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let myPet</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'armadillo'</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'I own a&nbsp;pet '</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">myPet</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'.'</span><span class="mtk1">); </span></span><br><span><span class="mtk16">// Output: 'I own a&nbsp;pet armadillo.'</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we assigned the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘armadillo’</code> to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myPet</code> variable. On the
second line, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code>
operator is used to combine three strings:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘I own a pet’</code>, the
value saved to <code class="code__2rdF32qjRVp7mMVBHuPwDS">myPet</code>,
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘.’</code>. We log the
result of this concatenation to the console as:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="plaintext" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">I own a&nbsp;pet armadillo.</span></span><br></div></code></pre></pre>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">favoriteAnimal</code> and set
it equal to your favorite animal.
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
Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to
print <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘My favorite animal:
ANIMAL’</code> to the console. Use string concatenation so that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">ANIMAL</code> is replaced
with the value in your
<code class="code__2rdF32qjRVp7mMVBHuPwDS">favoriteAnimal</code>
variable.
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

## VARIABLES

### String Interpolation

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the ES6 version of JavaScript, we can insert, or
<em>interpolate</em>, variables into strings using <em>template
literals</em>. Check out the following example where a template literal
is used to log strings together:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const myPet</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'armadillo'</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">`I own a&nbsp;pet </span><span class="mtk1">${</span><span class="mtk9">myPet</span><span class="mtk1">}</span><span class="mtk8">.`</span><span class="mtk1">);</span></span><br><span><span class="mtk16">// Output: I&nbsp;own a&nbsp;pet armadillo.</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice that:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
a template literal is wrapped by backticks
<code class="code__2rdF32qjRVp7mMVBHuPwDS">`</code> (this key is usually located on the top of your keyboard, left of the <kbd>1</kbd> key).</li> <li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Inside the template literal, you’ll see a placeholder, <code class="code__2rdF32qjRVp7mMVBHuPwDS">${myPet}</code>. The value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">myPet</code> is inserted into the template literal.</li> <li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When we interpolate <code class="code__2rdF32qjRVp7mMVBHuPwDS">`I
own a pet ${myPet}.\`</code>, the output we print is the string:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘I own a pet
armadillo.’</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
One of the biggest benefits to using template literals is the
readability of the code. Using template literals, you can more easily
tell what the new string will be. You also don’t have to worry about
escaping double quotes or single quotes.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a variable called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myName</code> and assign it
your name.
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
Create a variable called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myCity</code> and assign it
your favorite city’s name.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use a single template literal to interpolate your variables into the
sentence below. Use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to print
your sentence to the console in the following format:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="plaintext" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">My name is NAME. My favorite city is CITY.</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Replace <code class="code__2rdF32qjRVp7mMVBHuPwDS">NAME</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">CITY</code> in the string
above by interpolating the values saved to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myName</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myCity</code>.
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

## VARIABLES

### typeof operator

<p class="p__1qg33Igem5pAgn4kPMirjw">
While writing code, it can be useful to keep track of the data types of
the variables in your program. If you need to check the data type of a
variable’s value, you can use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">typeof</code> operator.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">typeof</code> operator
checks the value to its right and <em>returns</em>, or passes back, a
string of the data type.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const unknown1</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'foo'</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk12">typeof</span><span class="mtk1"> </span><span class="mtk9">unknown1</span><span class="mtk1">); </span><span class="mtk16">// Output: string</span></span><br><span><span> </span></span><br><span><span class="mtk12">const unknown2</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">10</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk12">typeof</span><span class="mtk1"> </span><span class="mtk9">unknown2</span><span class="mtk1">); </span><span class="mtk16">// Output: number</span></span><br><span><span> </span></span><br><span><span class="mtk12">const unknown3</span><span class="mtk1"> =&nbsp;</span><span class="mtk5">true</span><span class="mtk1">; </span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk12">typeof</span><span class="mtk1"> </span><span class="mtk9">unknown3</span><span class="mtk1">); </span><span class="mtk16">// Output: boolean</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s break down the first example. Since the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">unknown1</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘foo’</code>, a string,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">typeof unknown1</code> will
return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘string’</code>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to
print the <code class="code__2rdF32qjRVp7mMVBHuPwDS">typeof
newVariable</code>.
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
Great, now let’s check what happens if we reassign the variable. Below
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement, reassign
<code class="code__2rdF32qjRVp7mMVBHuPwDS">newVariable</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code>.
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
Since you assigned this new value to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">newVariable</code>, it has a
new type! On the line below your reassignment, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to print
<code class="code__2rdF32qjRVp7mMVBHuPwDS">typeof newVariable</code>
again.
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

## VARIABLES

### Review Variables

<p class="p__1qg33Igem5pAgn4kPMirjw">
Nice work! This lesson introduced you to variables, a powerful concept
you will use in all your future programming endeavors.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s review what we learned:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Variables hold reusable data in a program and associate it with a name.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Variables are stored in memory.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code> keyword is
used in pre-ES6 versions of JS.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> is the preferred
way to declare a variable when it can be reassigned, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> is the preferred
way to declare a variable with a constant value.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Variables that have not been initialized store the primitive data type
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Mathematical assignment operators make it easy to calculate a new value
and assign it to the same variable.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code> operator is used
to concatenate strings including string values held in variables.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In ES6, template literals use backticks
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\`</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">${}</code> to interpolate
values into a string.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">typeof</code> keyword
returns the data type (as a string) of a value.
</li>
</ul>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
To learn more about variables take on these challenges!
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Create variables and manipulate the values.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Check what happens when you try concatenating strings using variables of
different data types.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Interpolate multiple variables into a string.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
See what happens when you use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> on
variables declared by different keywords
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">var</code>) before they’re
defined. For example:
</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">test1</span><span class="mtk1">);</span></span><br><span><span> </span></span><br><span><span class="mtk12">const test1</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'figuring out quirks'</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Find the data type of a variable’s value using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">typeof</code> keyword on a
variable.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">typeof</code> to find the
data type of the resulting value when you concatenate variables
containing two different data types.
</li>
</ul>

**Solutions**

``` html
```

## BUILDING INTERACTIVE WEBSITES

### Kelvin Weather

<p class="p__1qg33Igem5pAgn4kPMirjw">
Deep in his mountain-side meteorology lab, the mad scientist Kelvin has
mastered weather prediction.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Recently, Kelvin began publishing his weather forecasts on his website.
However there’s a problem: All of his forecasts describe the temperature
in
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Kelvin">Kelvin</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
With our knowledge of JavaScript, let’s convert Kelvin to Celsius, then
to Fahrenheit.
</p>

<img src="https://content.codecademy.com/projects/introduction-to-javascript/learn-javascript-introduction/kelvin-weather/Kelvin%20Thermometers.svg" alt="Kelvin, Celsius, and Fahrenheit thermometers" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, 283 K converts to 10 °C which converts to 50 °F.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The forecast today is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">293</code> Kelvin. To start,
create a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">kelvin</code>, and set it
equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">293</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The value saved to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">kelvin</code> will stay
constant. Choose the variable type with this in mind.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-2">2.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment above that explains this line of code.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-3">3.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Celsius is similar to Kelvin — the only difference is that Celsius is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">273</code> degrees less than
Kelvin.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s convert Kelvin to Celsius by subtracting
<code class="code__2rdF32qjRVp7mMVBHuPwDS">273</code> from the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">kelvin</code> variable. Store
the result in another variable, named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">celsius</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-4">4.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment above that explains this line of code.
</p>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-5">5.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use this equation to calculate Fahrenheit, then store the answer in a
variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fahrenheit</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Fahrenheit = Celsius \* (9/5) + 32</em>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the next step we will round the number saved to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fahrenheit</code>. Choose the
variable type that allows you to change its value.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-6">6.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment above that explains this line of code.
</p>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-7">7.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
When you convert from Celsius to Fahrenheit, you often get a decimal
number.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.floor()</code>
method from the built-in Math object to round down the Fahrenheit
temperature. Save the result to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fahrenheit</code> variable.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-8">8.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment above that explains this line of code.
</p>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-9">9.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log</code> and
string interpolation to log the temperature in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fahrenheit</code> to the
console as follows:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="plaintext" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">The temperature is TEMPERATURE degrees Fahrenheit.</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Use string interpolation to replace
<code class="code__2rdF32qjRVp7mMVBHuPwDS">TEMPERATURE</code> with the
value saved to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fahrenheit</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-10">10.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Run your program to see your results!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you want to check your work, open the hint.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-11">11.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
By using variables, your program should work for any Kelvin temperature
— just change the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">kelvin</code> and run the
program again.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
What’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code> Kelvin in
Fahrenheit?
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-12">12.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great work! Kelvin can now publish his forecasts in Celsius and
Fahrenheit.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you’d like extra practice, try this:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Convert <code class="code__2rdF32qjRVp7mMVBHuPwDS">celsius</code> to the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Newton_scale">Newton</a>
scale using the equation below
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Newton = Celsius \* (33/100)</em>
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Round down the Newton temperature using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.floor()</code> method
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log</code> and
string interpolation to log the temperature in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">newton</code> to the console
</li>
</ul>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>

**Solutions**

``` html
```

## BUILDING INTERACTIVE WEBSITES

### Dog Years

<p class="p__1qg33Igem5pAgn4kPMirjw">
Dogs mature at a faster rate than human beings. We often say a dog’s age
can be calculated in “dog years” to account for their growth compared to
a human of the same age. In some ways we could say, time moves quickly
for dogs — 8 years in a human’s life equates to 45 years in a dog’s
life. How old would you be if you were a dog?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here’s how you convert your age from “human years” to “dog years”:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The first two years of a dog’s life count as 10.5 dog years each.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Each year following equates to 4 dog years.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Before you start doing the math in your head, let a computer take care
of it! With your knowledge of math operators and variables, use
JavaScript to convert your human age into dog years.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myAge</code>, and set it
equal to your age as a number.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment that explains this line of code.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-2">2.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">earlyYears</code> and save
the value <code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code> to it.
Note, the value saved to this variable will change.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment that explains this line of code.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-3">3.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use the multiplication assignment operator to multiply the value saved
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">earlyYears</code> by 10.5
and reassign it to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">earlyYears</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-4">4.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Since we already accounted for the first two years, take the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myAge</code> variable, and
subtract 2 from it.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Set the result equal to a variable called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">laterYears</code>. We’ll be
changing this value later.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment that explains this line of code.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-5">5.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Multiply the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">laterYears</code> variable by
4 to calculate the number of dog years accounted for by your later
years. Use the multiplication assignment operator to multiply and assign
in one step.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment that explains this line of code.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-6">6.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
If you’d like to check your work at this point, print
<code class="code__2rdF32qjRVp7mMVBHuPwDS">earlyYears</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">laterYears</code> to the
console. Are the values what you expected?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Check off this task when you’re ready to move on.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-7">7.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Add <code class="code__2rdF32qjRVp7mMVBHuPwDS">earlyYears</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">laterYears</code> together,
and store that in a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myAgeInDogYears</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment that explains this line of code.
</p>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-8">8.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s use a string method next.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write your name as a string, call its built-in method
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.toLowerCase()</code>, and
store the result in a variable called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myName</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">toLowerCase</code> method
returns a string with all lowercase letters.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment that explains this line of code.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-9">9.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log</code>
statement that displays your name and age in dog years. Use string
interpolation to display the value in the following sentence:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="plaintext" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">My name is NAME. I&nbsp;am HUMAN AGE years old in human</span><span class="mtk1"> years which is DOG AGE years old in dog years.</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Replace <code class="code__2rdF32qjRVp7mMVBHuPwDS">NAME</code> with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myName</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">HUMAN AGE</code> with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myAge</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">DOG AGE</code> with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myAgeInDogYears</code> in the
sentence above.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a comment that explains this line of code.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-10">10.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great work! You can convert any human age to dog years. Try changing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myAge</code> and see what
happens.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you’d like extra practice, try writing this project without the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\*=</code> operator.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>

**Solutions**

``` html
```

## CONDITIONAL STATEMENTS

### What are Conditional Statements?

<p class="p__1qg33Igem5pAgn4kPMirjw">
In life, we make decisions based on circumstances. Think of an everyday
decision as mundane as falling asleep — if we are tired, we go to bed,
otherwise, we wake up and start our day.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
These if-else decisions can be modeled in code by creating conditional
statements. A
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/conditionals?page_ref=catalog">conditional
statement</a> checks a specific condition(s) and performs a task based
on the condition(s).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, we will explore how programs make decisions by
evaluating conditions and introduce logic into our code!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ll be covering the following concepts:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statements
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
comparison operators
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
logical operators
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
truthy vs falsy values
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
ternary operators
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> statement
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
So <em>if</em> you’re ready to learn these concepts go to the next
lesson— <em>else</em>, read over the concepts, observe the diagram, and
prepare yourself for this lesson!
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Check out the diagram to see how conditionals allow us to create
decision-making technology.
</p>

**Solutions**

``` html
```

## CONDITIONAL STATEMENTS

### If Statement

<p class="p__1qg33Igem5pAgn4kPMirjw">
We often perform a task based on a condition. For example, if the
weather is nice today, then we will go outside. If the alarm clock
rings, then we’ll shut it off. If we’re tired, then we’ll go to sleep.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In programming, we can also perform a task based on a condition using an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk5">true</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'This message will print!'</span><span class="mtk1">); </span></span><br><span><span class="mtk1">}</span></span><br><span><span class="mtk16">// Prints: This message will print!</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice in the example above, we have an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement is
composed of:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> keyword
followed by a set of parentheses
<code class="code__2rdF32qjRVp7mMVBHuPwDS">()</code> which is followed
by a <em>code block</em>, or <em>block statement</em>, indicated by a
set of curly braces
<code class="code__2rdF32qjRVp7mMVBHuPwDS">{}</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Inside the parentheses
<code class="code__2rdF32qjRVp7mMVBHuPwDS">()</code>, a condition is
provided that evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the condition evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>, the code inside
the curly braces <code class="code__2rdF32qjRVp7mMVBHuPwDS">{}</code>
runs, or <em>executes</em>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the condition evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>, the block won’t
execute.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s make an <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> keyword,
declare a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sale</code>. Assign the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> to it.
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
Now create an <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement. Provide the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement a
condition of <code class="code__2rdF32qjRVp7mMVBHuPwDS">sale</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the code block of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> the
string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Time to buy!’</code>.
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
Notice that the code inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement ran,
since <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Time to buy!’</code>
was logged to the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Below the <code class="code__2rdF32qjRVp7mMVBHuPwDS">sale</code>
variable declaration, but before the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement, reassign
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sale</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>. Run your code
and observe what happens, we’ll be changing this behavior in the next
exercise.
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

## CONDITIONAL STATEMENTS

### If…Else Statements

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous exercise, we used an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement that
checked a condition to decide whether or not to run a block of code. In
many cases, we’ll have code we want to run if our condition evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If we wanted to add some default behavior to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement, we can
add an
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/conditionals?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statement</a> to run a block of code when the condition evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>. Take a look at
the inclusion of an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk5">false</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'The code in this block will not run.'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'But the code in this block will!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk16">// Prints: But the code in this block will!</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
An <code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement must
be paired with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement, and together they are referred to as an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> statement.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Uses the <code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> keyword
following the code block of an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Has a code block that is wrapped by a set of curly braces
<code class="code__2rdF32qjRVp7mMVBHuPwDS">{}</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The code inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement code
block will execute when the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement’s
condition evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> statements
allow us to automate solutions to yes-or-no questions, also known as
<em>binary decisions</em>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement
to the existing <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement. Inside the code block of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> the
string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Time to wait for a
sale.’</code>
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

## CONDITIONAL STATEMENTS

### Comparison Operators

<p class="p__1qg33Igem5pAgn4kPMirjw">
When writing conditional statements, sometimes we need to use different
types of operators to compare values. These operators are called
<em>comparison operators</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here is a list of some handy comparison operators and their syntax:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Less than: <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Greater than: <code class="code__2rdF32qjRVp7mMVBHuPwDS">\></code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Less than or equal to:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<=</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Greater than or equal to:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\>=</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Is equal to: <code class="code__2rdF32qjRVp7mMVBHuPwDS">===</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Is not equal to: <code class="code__2rdF32qjRVp7mMVBHuPwDS">!==</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Comparison operators compare the value on the left with the value on the
right. For instance:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">10</span><span class="mtk1"> &lt; </span><span class="mtk9">12</span><span class="mtk1"> </span><span class="mtk16">// Evaluates to true</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It can be helpful to think of comparison statements as questions. When
the answer is “yes”, the statement evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>, and when the
answer is “no”, the statement evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>. The code above
would be asking: is 10 less than 12? Yes! So
<code class="code__2rdF32qjRVp7mMVBHuPwDS">10 \< 12</code> evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can also use comparison operators on different data types like
strings:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk8">'apples'</span><span class="mtk1"> === </span><span class="mtk8">'oranges'</span><span class="mtk1"> </span><span class="mtk16">// false</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we’re using the <em>identity operator</em>
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">===</code>) to check if the
string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘apples’</code> is the
same as the string
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘oranges’</code>. Since the
two strings are not the same, the comparison statement evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
All comparison statements evaluate to either
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> and are made up
of:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Two values that will be compared.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
An operator that separates the values and compares them accordingly
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">\></code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<=</code>,<code class="code__2rdF32qjRVp7mMVBHuPwDS">\>=</code>,<code class="code__2rdF32qjRVp7mMVBHuPwDS">===</code>,<code class="code__2rdF32qjRVp7mMVBHuPwDS">!==</code>).
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s practice using these comparison operators!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Using <code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code>, create a
variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hungerLevel</code> and set it
equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">7</code>.
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
Write an <code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code>
statement using a comparison operator. The condition should check if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hungerLevel</code> is greater
than <code class="code__2rdF32qjRVp7mMVBHuPwDS">7</code>. If so, the
conditional statement should log,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Time to eat!’</code>.
Otherwise, it should log <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘We
can eat later!’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After you press run, play around with the condition by tweaking the
comparison of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hungerLevel</code> by using
different operators such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<=</code>,<code class="code__2rdF32qjRVp7mMVBHuPwDS">\>=</code>,<code class="code__2rdF32qjRVp7mMVBHuPwDS">\></code>,
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<</code>.
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

## CONDITIONAL STATEMENTS

### Logical Operators

<p class="p__1qg33Igem5pAgn4kPMirjw">
Working with conditionals means that we will be using booleans,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> values. In
JavaScript, there are operators that work with boolean values known as
<em>logical operators</em>. We can use logical operators to add more
sophisticated logic to our conditionals. There are three logical
operators:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the <em>and</em> operator
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">&&</code>)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the <em>or</em> operator
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">\|\|</code>)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the <em>not</em> operator, otherwise known as the <em>bang</em> operator
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">!</code>)
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When we use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&&</code>
operator, we are checking that two things are
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">stopLight</span><span class="mtk1"> === </span><span class="mtk8">'green'</span><span class="mtk1"> &amp;&amp; </span><span class="mtk9">pedestrians</span><span class="mtk1"> === </span><span class="mtk9">0</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Go!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Stop'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&&</code>
operator, both conditions <em>must</em> evaluate to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> for the entire
condition to evaluate to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> and execute.
Otherwise, if either condition is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">&&</code> condition will
evaluate to <code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> and
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> block will
execute.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If we only care about either condition being
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>, we can use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\|\|</code> operator:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">day</span><span class="mtk1"> === </span><span class="mtk8">'Saturday'</span><span class="mtk1"> || </span><span class="mtk9">day</span><span class="mtk1"> === </span><span class="mtk8">'Sunday'</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Enjoy the weekend!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Do some work.'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\|\|</code>
operator, only one of the conditions must evaluate to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> for the overall
statement to evaluate to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>. In the code
example above, if either <code class="code__2rdF32qjRVp7mMVBHuPwDS">day
=== ‘Saturday’</code> or <code class="code__2rdF32qjRVp7mMVBHuPwDS">day
=== ‘Sunday’</code> evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>‘s condition will
evaluate to <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> and
its code block will execute. If the first condition in an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\|\|</code> statement
evaluates to <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>, the
second condition won’t even be checked. Only if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">day === ’Saturday’</code>
evaluates to <code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>
will <code class="code__2rdF32qjRVp7mMVBHuPwDS">day === ‘Sunday’</code>
be evaluated. The code in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement above
will execute only if both comparisons evaluate to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">!</code> <em>not
operator</em> reverses, or <em>negates</em>, the value of a boolean:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let excited</span><span class="mtk1"> =&nbsp;</span><span class="mtk5">true</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(!</span><span class="mtk9">excited</span><span class="mtk1">); </span><span class="mtk16">// Prints false</span></span><br><span><span> </span></span><br><span><span class="mtk12">let sleepy</span><span class="mtk1"> =&nbsp;</span><span class="mtk5">false</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(!</span><span class="mtk9">sleepy</span><span class="mtk1">); </span><span class="mtk16">// Prints true</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Essentially, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">!</code>
operator will either take a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> value and pass
back <code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>, or it will
take a <code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> value and
pass back <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Logical operators are often used in conditional statements to add
another layer of logic to our code.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>main.js</strong> there are two variables
<code class="code__2rdF32qjRVp7mMVBHuPwDS">mood</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">tirednessLevel</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s create an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> statement that
checks if <code class="code__2rdF32qjRVp7mMVBHuPwDS">mood</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘sleepy’</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">tirednessLevel</code> is
greater than <code class="code__2rdF32qjRVp7mMVBHuPwDS">8</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If both conditions evaluate to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>, then
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> the
string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘time to
sleep’</code>. Otherwise, we should
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘not bed time yet’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After you press “Run”, play around with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\|\|</code> operator and the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">!</code> operator! What
happens if you negate the value of the entire statement with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">!</code> and switch to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\|\|</code> instead of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">&&</code>?
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

## CONDITIONAL STATEMENTS

### Truthy and Falsy

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s consider how non-boolean data types, like strings or numbers, are
evaluated when checked inside a condition.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Sometimes, you’ll want to check if a variable exists and you won’t
necessarily want it to equal a specific value — you’ll only check to see
if the variable has been assigned a value.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here’s an example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let myVariable</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'I Exist!'</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">myVariable</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">myVariable</span><span class="mtk1">)</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'The variable does not exist.'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The code block in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement will run
because <code class="code__2rdF32qjRVp7mMVBHuPwDS">myVariable</code> has
a <em>truthy</em> value; even though the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">myVariable</code> is not
explicitly the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>, when used in a
boolean or conditional context, it evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> because it has
been assigned a non-falsy value.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
So which values are <em>falsy</em>— or evaluate to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> when checked as
a condition? The list of falsy values includes:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Empty strings like <code class="code__2rdF32qjRVp7mMVBHuPwDS">““</code>
or <code class="code__2rdF32qjRVp7mMVBHuPwDS">’’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">null</code> which represent
when there is no value at all
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code> which
represent when a declared variable lacks a value
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">NaN</code>, or Not a Number
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here’s an example with numbers:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let numberOfApples</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">0</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">numberOfApples</span><span class="mtk1">){</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Let us eat apples!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'No apples left!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk16">// Prints 'No apples left!'</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The condition evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> because the
value of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">numberOfApples</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>. Since
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code> is a falsy value,
the code block in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement will
run.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Change the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wordCount</code> so that it
is truthy. This value should still be a number.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After you make this change and run your code,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Great! You’ve started your
work!’</code> should log to the console.
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
Change the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">favoritePhrase</code> so that
it is still a string but falsy.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After you make this change and run your code,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘This string is definitely
empty.’</code> should log to the console.
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

## CONDITIONAL STATEMENTS

### Truthy and Falsy Assignment

<p class="p__1qg33Igem5pAgn4kPMirjw">
Truthy and falsy evaluations open a world of short-hand possibilities!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Say you have a website and want to take a user’s username to make a
personalized greeting. Sometimes, the user does not have an account,
making the <code class="code__2rdF32qjRVp7mMVBHuPwDS">username</code>
variable falsy. The code below checks if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">username</code> is defined
and assigns a default string if it is not:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let username</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">''</span><span class="mtk1">;</span></span><br><span><span class="mtk12">let defaultName</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">username</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">defaultName</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">username</span><span class="mtk1">;</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">defaultName</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Stranger'</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">defaultName</span><span class="mtk1">); </span><span class="mtk16">// Prints: Stranger</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you combine your knowledge of logical operators you can use a
short-hand for the code above. In a boolean condition, JavaScript
assigns the truthy value to a variable if you use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\|\|</code> operator in your
assignment:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let username</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">''</span><span class="mtk1">;</span></span><br><span><span class="mtk12">let defaultName</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">username</span><span class="mtk1"> || </span><span class="mtk8">'Stranger'</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">defaultName</span><span class="mtk1">); </span><span class="mtk16">// Prints: Stranger</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Because <code class="code__2rdF32qjRVp7mMVBHuPwDS">\|\|</code> or
statements check the left-hand condition first, the variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">defaultName</code> will be
assigned the actual value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">username</code> if it is
truthy, and it will be assigned the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Stranger’</code> if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">username</code> is falsy.
This concept is also referred to as <em>short-circuit evaluation</em>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s use short-circuit evaluation to assign a value to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">writingUtensil</code>. Do not
edit <code class="code__2rdF32qjRVp7mMVBHuPwDS">tool</code> yet, we’ll
return to <code class="code__2rdF32qjRVp7mMVBHuPwDS">tool</code> in the
next step.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Assign to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">writingUtensil</code> the
value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">tool</code> and if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">tool</code> is falsy, assign
a default value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘pen’</code>.
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
Notice that text <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘The pen is
mightier than the sword’</code> logged to the console. Which means the
value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">writingUtensil</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘pen’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
What if we reassign the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">tool</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘marker’</code>. Let’s see
what happens to the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">writingUtensil</code>.
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

## CONDITIONAL STATEMENTS

### Ternary Operator

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the spirit of using short-hand syntax, we can use a <em>ternary
operator</em> to simplify an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> statement.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> statement
example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let isNightTime</span><span class="mtk1"> =&nbsp;</span><span class="mtk5">true</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">isNightTime</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Turn on the lights!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Turn off the lights!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can use a <em>ternary operator</em> to perform the same
functionality:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">isNightTime</span><span class="mtk1"> ?&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Turn on the lights!'</span><span class="mtk1">) :&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Turn off the lights!'</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The condition,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">isNightTime</code>, is
provided before the <code class="code__2rdF32qjRVp7mMVBHuPwDS">?</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Two expressions follow the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">?</code> and are separated by
a colon <code class="code__2rdF32qjRVp7mMVBHuPwDS">:</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the condition evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>, the first
expression executes.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the condition evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>, the second
expression executes.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Like <code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code>
statements, ternary operators can be used for conditions which evaluate
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Refactor, or edit, the first
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> block to use a
ternary operator.
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
Refactor the second
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> block to use a
ternary operator.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Refactor the third
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> block to use a
ternary operator.
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

## CONDITIONAL STATEMENTS

### Else If Statements

<p class="p__1qg33Igem5pAgn4kPMirjw">
We can add more conditions to our
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> with an
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/conditionals?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code> statement</a>. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statement
allows for more than two possible outcomes. You can add as many
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statements as
you’d like, to make more complex conditionals!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statement
always comes after the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement and
before the <code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statement. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code>
statement also takes a condition. Let’s take a look at the syntax:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let stopLight</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'yellow'</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">stopLight</span><span class="mtk1"> === </span><span class="mtk8">'red'</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Stop!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> </span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">stopLight</span><span class="mtk1"> === </span><span class="mtk8">'yellow'</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Slow down.'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> </span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">stopLight</span><span class="mtk1"> === </span><span class="mtk8">'green'</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Go!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Caution, unknown!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statements
allow you to have multiple possible outcomes.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statements are read from top to bottom, so the first condition that
evaluates to <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> from
the top to bottom is the block that gets executed.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, since
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stopLight === ‘red’</code>
evaluates to <code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stopLight === ‘yellow’</code>
evaluates to <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>, the
code inside the first <code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code> statement is executed. The rest of the conditions are not
evaluated. If none of the conditions evaluated to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>, then the code in
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement
would have executed.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s create a program that keeps track of the way the environment
changes with the seasons. Write a conditional statement to make this
happen!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>main.js</strong> there is already an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> statement in
place. Let’s add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code> statement that checks if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">season</code> is equal to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘winter’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the code block of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statement, add
a <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> that
prints the string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘It's
winter! Everything is covered in snow.’</code>.
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
Add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code>
statement that checks if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">season</code> is equal to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘fall’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the code block of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statement you
just created, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> that
prints the string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘It's fall!
Leaves are falling!’</code>.
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
Add a final <code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code>
statement that checks if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">season</code> is equal to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘summer’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the code block of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statement you
just created, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> that
prints the string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘It's sunny
and warm because it's summer!’</code>.
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

## CONDITIONAL STATEMENTS

### The switch keyword

<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statements are
a great tool if we need to check multiple conditions. In programming, we
often find ourselves needing to check multiple values and handling each
of them differently. For example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let groceryItem</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'papaya'</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">groceryItem</span><span class="mtk1"> === </span><span class="mtk8">'tomato'</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Tomatoes are $0.49'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> </span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">groceryItem</span><span class="mtk1"> === </span><span class="mtk8">'papaya'</span><span class="mtk1">){</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Papayas are $1.29'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Invalid item'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the code above, we have a series of conditions checking for a value
that matches a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">groceryItem</code> variable.
Our code works fine, but imagine if we needed to check 100 different
values! Having to write that many
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statements
sounds like a pain!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/switch?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code>
statement</a> provides an alternative syntax that is easier to read and
write. A <code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code>
statement looks like this:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let groceryItem</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'papaya'</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk12">switch</span><span class="mtk1"> (</span><span class="mtk9">groceryItem</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">case</span><span class="mtk1"> </span><span class="mtk8">'tomato'</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Tomatoes are $0.49'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">break</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">case</span><span class="mtk1"> </span><span class="mtk8">'lime'</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Limes are $1.49'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">break</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">case</span><span class="mtk1"> </span><span class="mtk8">'papaya'</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Papayas are $1.29'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">break</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk10">default</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Invalid item'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">break</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk16">// Prints 'Papayas are $1.29'</span></span><br></div></code></pre></pre>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> keyword
initiates the statement and is followed by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">( … )</code>, which contains
the value that each
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> will compare. In
the example, the value or expression of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> statement is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">groceryItem</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Inside the block, <code class="code__2rdF32qjRVp7mMVBHuPwDS">{ …
}</code>, there are multiple
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code>s. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> keyword checks if
the expression matches the specified value that comes after it. The
value following the first
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘tomato’</code>. If the value
of <code class="code__2rdF32qjRVp7mMVBHuPwDS">groceryItem</code>
equalled <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘tomato’</code>,
that <code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code>’s
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> would
run.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">groceryItem</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘papaya’</code>, so the third
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> runs—
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Papayas are $1.29</code> is
logged to the console.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">break</code> keyword
tells the computer to exit the block and not execute any more code or
check any other cases inside the code block. Note: Without
<code class="code__2rdF32qjRVp7mMVBHuPwDS">break</code> keywords, the
first matching case will run, but so will every subsequent case
regardless of whether or not it matches—including the default. This
behavior is different from
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
conditional statements that execute only one block of code.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
At the end of each
<code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> statement,
there is a <code class="code__2rdF32qjRVp7mMVBHuPwDS">default</code>
statement. If none of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code>s are true, then
the code in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">default</code> statement will
run.
</li>
</ul>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s write a <code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code>
statement to decide what medal to award an athlete.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">athleteFinalPosition</code>
is already defined at the top of <strong>main.js</strong>. So start by
writing a <code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code>
statement with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">athleteFinalPosition</code>
as its expression.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code>
statement, add three
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code>s:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The first <code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> checks
for the value <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘first
place’</code>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the expression’s value matches the value of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> then
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> the
string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You get the gold
medal!’</code>
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The second <code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> checks
for the value <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘second
place’</code>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the expression’s value matches the value of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> then
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> the
string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You get the silver
medal!’</code>
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The third <code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> checks
for the value <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘third
place’</code>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the expression’s value matches the value of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code> then
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> the
string <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You get the bronze
medal!’</code>
</li>
</ul>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember to add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">break</code> after each
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>.
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
Now, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">default</code>
statement at the end of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> that uses
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to print
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘No medal awarded.’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If
<code class="code__2rdF32qjRVp7mMVBHuPwDS">athleteFinalPosition</code>
does not equal any value of our
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code>s, then the string
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘No medal awarded.’</code> is
logged to the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember to add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">break</code> keyword at the
end of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">default</code>
case.
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

## CONDITIONAL STATEMENTS

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
Way to go! Here are some of the major concepts for conditionals:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
An <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement checks
a condition and will execute a task if that condition evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> statements
make binary decisions and execute different code blocks based on a
provided condition.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
We can add more conditions using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statements.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Comparison operators, including
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\></code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<=</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\>=</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">===</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">!==</code> can compare two
values.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The logical and operator,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">&&</code>, or “and”, checks
if both provided expressions are truthy.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The logical operator
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\|\|</code>, or “or”, checks
if either provided expression is truthy.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The bang operator, <code class="code__2rdF32qjRVp7mMVBHuPwDS">!</code>,
switches the truthiness and falsiness of a value.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The ternary operator is shorthand to simplify concise
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if…else</code> statements.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A <code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> statement can
be used to simplify the process of writing multiple
<code class="code__2rdF32qjRVp7mMVBHuPwDS">else if</code> statements.
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">break</code> keyword
stops the remaining
<code class="code__2rdF32qjRVp7mMVBHuPwDS">case</code>s from being
checked and executed in a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> statement.
</li>
</ul>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>main.js</strong>, practice the skills you learned in this
lesson.
</p>

**Solutions**

``` html
```

## BUILDING INTERACTIVE WEBSITES

### Magic Eight Ball

<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ve learned a powerful tool in JavaScript: control flow! It’s so
powerful, in fact, that it can be used to tell someone’s fortune.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project we will build a
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Magic_8-Ball">Magic
Eight Ball</a> using control flow in JavaScript.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The user will be able to input a question, then our program will output
a random fortune.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the first line of the program, define a variable called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userName</code> that is set
to an empty string.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If the user wants, they can enter their name in between the quotation
marks.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-2">2.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Below this variable, create a ternary expression that decides what to do
if the user enters a name or not. If the user enters a name — like
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Jane’</code> — use string
interpolation to log <code class="code__2rdF32qjRVp7mMVBHuPwDS">Hello,
Jane!</code> to the console. Otherwise, simply log
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Hello!</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-3">3.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userQuestion</code>. The
value of the variable should be a string that is the question the user
wants to ask the Magic Eight Ball.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-4">4.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">userQuestion</code>,
stating what was asked. You can include the user’s name in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement, if you wish!
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-5">5.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
We need to generate a random number between 0 and 7.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Create another variable, and name it
<code class="code__2rdF32qjRVp7mMVBHuPwDS">randomNumber</code>. Set it
equal to this expression, which uses two methods
(<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor"><code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.floor()</code></a>
and
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random"><code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.random()</code></a>)
from the Math library.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">Math</span><span class="mtk1">.</span><span class="mtk10">floor</span><span class="mtk1">(</span><span class="mtk9">Math</span><span class="mtk1">.</span><span class="mtk10">random</span><span class="mtk1">() *&nbsp;</span><span class="mtk9">8</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Check the hint to learn how it works!
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-6">6.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create one more variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">eightBall</code>, and set it
equal to an empty string. We will save a value to this variable in the
next steps, depending on the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">randomNumber</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-7">7.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
We need to create a control flow that takes in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">randomNumber</code> we made
in step 5, and then assigns
<code class="code__2rdF32qjRVp7mMVBHuPwDS">eightBall</code> to a reply
that a Magic Eight Ball would return. Think about utilizing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
or <code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> statements.
Here are 8 Magic Eight Ball phrases that we’d like to save to the
variable <code class="code__2rdF32qjRVp7mMVBHuPwDS">eightBall</code>:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘It is certain’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘It is decidedly so’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Reply hazy try again’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Cannot predict now’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Do not count on it’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘My sources say no’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Outlook not so good’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Signs point to yes’</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If the <code class="code__2rdF32qjRVp7mMVBHuPwDS">randomNumber</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>, then save an answer
to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">eightBall</code>
variable; if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">randomNumber</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code>, then save the next
answer, and so on. If you’re feeling creative, make your own responses!
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-8">8.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
to print the Magic Eight Ball’s answer, the value of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">eightBall</code> variable.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-9">9.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Run your program a few times to see random results appear in the
console!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you want extra practice:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If you started with a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> statement,
convert it to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statements.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If you started with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statements, convert them to a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> statement.
</li>
</ul>

</article>

**Solutions**

``` html
```

## BUILDING INTERACTIVE WEBSITES

### Race Day

<p class="p__1qg33Igem5pAgn4kPMirjw">
Codecademy’s annual race is just around the corner! This year, we have a
lot of participants. You have been hired to write a program that will
register runners for the race and give them instructions on race day.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As a timeline, registration would look like this:
<img src="https://content.codecademy.com/projects/introduction-to-javascript/learn-javascript-control-flow/race-day/raceday-timeline.svg" alt="registration-timeline" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here’s how our registration works. There are adult runners (over 18
years of age) and youth runners (under 18 years of age). They can
register early or late. Runners are assigned a race number and start
time based on their age and registration.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Race number:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Early adults receive a race number at or above 1000.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
All others receive a number below 1000.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Start time:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Adult registrants run at 9:30 am or 11:00 am.
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Early adults run at 9:30 am.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Late adults run at 11:00 am.
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Youth registrants run at 12:30 pm (regardless of registration).
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
But we didn’t plan for runners that are exactly 18! We’ll handle that by
the end of the project.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Race numbers are assigned randomly. We’ve provided the necessary code at
the top of the file.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Check off this task after reading that line.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can read the hint if you want to learn how it works!
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-2">2.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a variable that indicates whether a runner registered early or
not.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Set it equal to a Boolean value. You’ll change this later as you test
different runner conditions.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-3">3.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a variable for the runner’s age and set it equal to a number.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll change this later as you test different runner conditions.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-4">4.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a control flow statement that checks whether the runner is an
adult AND registered early.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Add <code class="code__2rdF32qjRVp7mMVBHuPwDS">1000</code> to their
<code class="code__2rdF32qjRVp7mMVBHuPwDS">raceNumber</code> if this is
true.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-5">5.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a separate control flow statement below the first (starting with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> again). This
statement will check age and registration time to determine race time.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For runners over 18 who registered early, log a statement to the console
telling them that they will race at 9:30 am. Include their
<code class="code__2rdF32qjRVp7mMVBHuPwDS">raceNumber</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-6">6.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
“Late adults run at 11:00 am”
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Since we already checked for early adults we can write a statement like
this: <em>else if runner is over 18 AND did not register early they will
race at 11:00am</em>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write the corresponding <code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code> statement.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Within that, log a string to the console telling them that they will
race at 11:00 am. Include their
<code class="code__2rdF32qjRVp7mMVBHuPwDS">raceNumber</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-7">7.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
“Youth registrants run at 12:30 pm (regardless of registration)”
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For people who are under 18, log a statement to the console telling them
that they will race at 12:30 pm. Include their
<code class="code__2rdF32qjRVp7mMVBHuPwDS">raceNumber</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-8">8.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Enter different combinations of values for the two variables you created
and run your code several times. Verify that the correct statements are
printing to the console!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can check your work using the examples provided in the hint.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-9">9.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Don’t forget about runners exactly 18 years old!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement
that logs a statement to the console telling the runner to see the
registration desk.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>

**Solutions**

``` html
```

## FUNCTIONS

### What are Functions?

<p class="p__1qg33Igem5pAgn4kPMirjw">
When first learning how to calculate the area of a rectangle, there’s a
sequence of steps to calculate the correct answer:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Measure the width of the rectangle.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Measure the height of the rectangle.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Multiply the width and height of the rectangle.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
With practice, you can calculate the area of the rectangle without being
instructed with these three steps every time.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can calculate the area of one rectangle with the following code:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const width</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">10</span><span class="mtk1">;</span></span><br><span><span class="mtk12">const height</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">6</span><span class="mtk1">;</span></span><br><span><span class="mtk12">const area</span><span class="mtk1"> =&nbsp;&nbsp;</span><span class="mtk9">width</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">height</span><span class="mtk1">;</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">area</span><span class="mtk1">); </span><span class="mtk16">// Output: 60</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Imagine being asked to calculate the area of three different rectangles:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk16">// Area of the first rectangle</span></span><br><span><span class="mtk12">const width1</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">10</span><span class="mtk1">;</span></span><br><span><span class="mtk12">const height1</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">6</span><span class="mtk1">;</span></span><br><span><span class="mtk12">const area1</span><span class="mtk1"> =&nbsp;&nbsp;</span><span class="mtk9">width1</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">height1</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk16">// Area of the second rectangle</span></span><br><span><span class="mtk12">const width2</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">4</span><span class="mtk1">;</span></span><br><span><span class="mtk12">const height2</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">9</span><span class="mtk1">;</span></span><br><span><span class="mtk12">const area2</span><span class="mtk1"> =&nbsp;&nbsp;</span><span class="mtk9">width2</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">height2</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk16">// Area of the third rectangle</span></span><br><span><span class="mtk12">const width3</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">10</span><span class="mtk1">;</span></span><br><span><span class="mtk12">const height3</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">10</span><span class="mtk1">;</span></span><br><span><span class="mtk12">const area3</span><span class="mtk1"> =&nbsp;&nbsp;</span><span class="mtk9">width3</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">height3</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In programming, we often use code to perform a specific task multiple
times. Instead of rewriting the same code, we can group a block of code
together and associate it with one task, then we can reuse that block of
code whenever we need to perform the task again. We achieve this by
creating a <em>function</em>. A function is a reusable block of code
that groups together a sequence of statements to perform a specific
task.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, you will learn how to create and use functions, and how
they can be used to create clearer and more concise code.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at the provided GIF. It shows a function, named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">addOneSide</code>, adding an
additional side to different shape inputs. Notice how there is only one
function, represented by the box, that is used to transform individual
shapes (inputs) into new shapes (outputs).
</p>

**Solutions**

``` html
```

## FUNCTIONS

### Function Declarations

<p class="p__1qg33Igem5pAgn4kPMirjw">
In JavaScript, there are many ways to create a
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/functions?page_ref=catalog">function</a>.
One way to create a function is by using a <em>function
declaration</em>. Just like how a variable declaration binds a value to
a variable name, a function declaration binds a function to a name, or
an <em>identifier</em>. Take a look at the anatomy of a function
declaration below:
</p>

<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/declaration.svg" alt="Diagram showing the syntax of a function declaration" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
A function declaration consists of:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">function</code> keyword.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The name of the function, or its identifier, followed by parentheses.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A function body, or the block of statements required to perform a
specific task, enclosed in the function’s curly brackets,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">{ }</code>.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A function declaration is a function that is bound to an identifier, or
name. In the next exercise we’ll go over how to run the code inside the
function body.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We should also be aware of the <em>hoisting</em> feature in JavaScript
which allows access to function declarations before they’re defined.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at example of hoisting:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">greetWorld</span><span class="mtk1">(); </span><span class="mtk16">// Output: Hello, World!</span></span><br><span><span> </span></span><br><span><span class="mtk12">function greetWorld</span><span class="mtk1">() {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Hello, World!'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice how hoisting allowed
<code class="code__2rdF32qjRVp7mMVBHuPwDS">greetWorld()</code> to be
called before the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">greetWorld()</code> function
was defined! Since hoisting isn’t considered good practice, we simply
want you to be aware of this feature.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you want to read more about hoisting, check out
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Glossary/Hoisting">MDN
documentation on hoisting</a>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s create a function that prints a reminder to the console. Using a
function declaration, create a function called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getReminder()</code>.
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
In the function body of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getReminder()</code>, log the
following reminder to the console:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Water the plants.’</code>
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
Let’s create another function that prints a useful Spanish travel phrase
to the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Using a function declaration, create a function called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">greetInSpanish()</code>.
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
Add code to the function body of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">greetInSpanish()</code>:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In the function body
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> the
following Spanish phrase to the console:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Buenas tardes.’</code>
</li>
</ul>

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

## FUNCTIONS

### Calling a Function

<p class="p__1qg33Igem5pAgn4kPMirjw">
As we saw in previous exercises, a function declaration binds a function
to an identifier.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
However, a function declaration does not ask the code inside the
function body to run, it just declares the existence of the function.
The code inside a function body runs, or <em>executes</em>, only when
the function is <em>called</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/functions?page_ref=catalog">call
a function</a> in your code, you type the function name followed by
parentheses.
</p>

<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/name.svg" alt="Diagram showing the syntax of invoking a function" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
This <em>function call</em> executes the function body, or all of the
statements between the curly braces in the function declaration.
<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/function%20execution.svg " alt="Function execution diagram" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can call the same function as many times as needed.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s practice calling functions in our code.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Imagine that you manage an online store. When a customer places an
order, you send them a thank you note. Let’s create a function to
complete this task:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Define a function called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sayThanks()</code> as a
function declaration.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In the function body of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sayThanks()</code>, add code
such that the function writes the following thank you message to the
console when called: <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Thank
you for your purchase! We appreciate your business.’</code>
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
Call <code class="code__2rdF32qjRVp7mMVBHuPwDS">sayThanks()</code> to
view the thank you message in the console.
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
Functions can be called as many times as you need them.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Imagine that three customers placed an order and you wanted to send each
of them a thank you message. Update your code to call
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sayThanks()</code> three
times.
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

## FUNCTIONS

### Parameters and Arguments

<p class="p__1qg33Igem5pAgn4kPMirjw">
So far, the functions we’ve created execute a task without an input.
However, some functions can take inputs and use the inputs to perform a
task. When declaring a function, we can specify its <em>parameters</em>.
Parameters allow functions to accept input(s) and perform a task using
the input(s). We use parameters as placeholders for information that
will be passed to the function when it is called.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s observe how to specify parameters in our function declaration:
</p>

<img src="https://static-assets.codecademy.com/Courses/Learn-JavaScript/function_parameters.svg" alt="JavaScript syntax for declaring a function with parameters" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the diagram above,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">calculateArea()</code>,
computes the area of a rectangle, based on two inputs,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>. The parameters
are specified between the parenthesis as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>, and inside the
function body, they act just like regular variables.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> act as
placeholders for values that will be multiplied together.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When calling a function that has parameters, we specify the values in
the parentheses that follow the function name. The values that are
passed to the function when it is called are called <em>arguments</em>.
Arguments can be passed to the function as values or variables.
</p>

<img src="https://static-assets.codecademy.com/Courses/Learn-JavaScript/by_value.svg" alt="JavaScript syntax for invoking a function with arguments as values" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the function call above, the number
<code class="code__2rdF32qjRVp7mMVBHuPwDS">10</code> is passed as the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">6</code> is passed as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>. Notice that
the order in which arguments are passed and assigned follows the order
that the parameters are declared.
</p>

<img src="https://static-assets.codecademy.com/Courses/Learn-JavaScript/by_variable.svg" alt="JavaScript syntax for invoking a function with arguments as variables" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
The variables
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rectWidth</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rectHeight</code> are
initialized with the values for the height and width of a rectangle
before being used in the function call.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By using parameters,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">calculateArea()</code> can be
reused to compute the area of any rectangle! Functions are a powerful
tool in computer programming so let’s practice creating and calling
functions with parameters.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">sayThanks()</code>
function works well, but let’s add the customer’s name in the message.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Add a parameter called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> to the function
declaration for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sayThanks()</code>.
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
With <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> as a
parameter, it can be used as a variable in the function body of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sayThanks()</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Using <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> and string
concatenation, change the thank you message into the following:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk8">'Thank you for your purchase '</span><span class="mtk1">+ </span><span class="mtk9">name</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">'! We appreciate your business.'</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Copy and paste the above message into your code.
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
A customer named Cole just purchased something from your online store.
Call <code class="code__2rdF32qjRVp7mMVBHuPwDS">sayThanks()</code> and
pass <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Cole’</code> as an
argument to send Cole a personalized thank you message.
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

## FUNCTIONS

### Default Parameters

<p class="p__1qg33Igem5pAgn4kPMirjw">
One of the features added in ES6 is the ability to use <em>default
parameters</em>. Default parameters allow parameters to have a
predetermined value in case there is no argument passed into the
function or if the argument is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code> when called.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at the code snippet below that uses a default parameter:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">function greeting</span><span class="mtk1"> (</span><span class="mtk12">name</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'stranger'</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">`Hello, </span><span class="mtk1">${</span><span class="mtk9">name</span><span class="mtk1">}</span><span class="mtk8">!`</span><span class="mtk1">)</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk9">greeting</span><span class="mtk1">(</span><span class="mtk8">'Nick'</span><span class="mtk1">) </span><span class="mtk16">// Output: Hello, Nick!</span></span><br><span><span class="mtk9">greeting</span><span class="mtk1">() </span><span class="mtk16">// Output: Hello, stranger!</span></span><br><span><span> </span></span><br></div></code></pre></pre>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we used the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">=</code> operator to assign
the parameter <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> a
default value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘stranger’</code>. This is
useful to have in case we ever want to include a non-personalized
default greeting!
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
When the code calls
<code class="code__2rdF32qjRVp7mMVBHuPwDS">greeting(‘Nick’)</code> the
value of the argument is passed in and,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Nick’</code>, will override
the default parameter of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘stranger’</code> to log
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello, Nick!’</code> to the
console.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
When there isn’t an argument passed into
<code class="code__2rdF32qjRVp7mMVBHuPwDS">greeting()</code>, the
default value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘stranger’</code> is used,
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello, stranger!’</code>
is logged to the console.
</p>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By using a default parameter, we account for situations when an argument
isn’t passed into a function that is expecting an argument.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s practice creating functions that use default parameters.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The function
<code class="code__2rdF32qjRVp7mMVBHuPwDS">makeShoppingList()</code>
creates a shopping list based on the items that are passed to the
function as arguments.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Imagine that you always purchase milk, bread, and eggs every time you go
shopping for groceries. To make creating a grocery list easier, let’s
assign default values to the parameters in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">makeShoppingList()</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Change the parameters of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">makeShoppingList()</code>
into default parameters :
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Assign ‘milk’ as the default value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">item1</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Assign ‘bread’ as the default value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">item2</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Assign ‘eggs’ as the default value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">item3</code>.
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

**Solutions**

``` html
```

## FUNCTIONS

### Return

<p class="p__1qg33Igem5pAgn4kPMirjw">
When a function is called, the computer will run through the function’s
code and evaluate the result of calling the function. By default that
resulting value is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">function rectangleArea</span><span class="mtk1">(</span><span class="mtk12">width</span><span class="mtk1">, </span><span class="mtk12">height</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">let area</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">width</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">height</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">rectangleArea</span><span class="mtk1">(</span><span class="mtk9">5</span><span class="mtk1">, </span><span class="mtk9">7</span><span class="mtk1">)) </span><span class="mtk16">// Prints undefined</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the code example, we defined our function to calculate the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">area</code> of a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> parameter. Then
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rectangleArea()</code> is
invoked with the arguments
<code class="code__2rdF32qjRVp7mMVBHuPwDS">5</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">7</code>. But when we went to
print the results we got
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code>. Did we
write our function wrong? No! In fact, the function worked fine, and the
computer did calculate the area as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">35</code>, but we didn’t
capture it. So how can we do that? With the keyword
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code>!
</p>

<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/function%20return.svg" alt="using return keyword in a function" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
To pass back information from the function call, we use a
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/functions?page_ref=catalog">return
statement</a>. To create a return statement, we use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> keyword
followed by the value that we wish to return. Like we saw above, if the
value is omitted,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code> is returned
instead.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When a <code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code>
statement is used in a function body, the execution of the function is
stopped and the code that follows it will not be executed. Look at the
example below:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">function rectangleArea</span><span class="mtk1">(</span><span class="mtk12">width</span><span class="mtk1">, </span><span class="mtk12">height</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">width</span><span class="mtk1"> &lt; </span><span class="mtk9">0</span><span class="mtk1"> || </span><span class="mtk9">height</span><span class="mtk1"> &lt; </span><span class="mtk9">0</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">return</span><span class="mtk1"> </span><span class="mtk8">'You need positive integers to calculate area!'</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;}</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">return</span><span class="mtk1"> </span><span class="mtk9">width</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">height</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If an argument for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> is less than
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>, then
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rectangleArea()</code> will
return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You need positive
integers to calculate area!’</code>. The second return statement
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width \* height</code> will
not run.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> keyword is
powerful because it allows functions to produce an output. We can then
save the output to a variable for later use.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Imagine if we needed to order monitors for everyone in an office and
this office is conveniently arranged in a grid shape. We could use a
function to help us calculate the number of monitors needed!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Declare a function
<code class="code__2rdF32qjRVp7mMVBHuPwDS">monitorCount()</code> that
has two parameters. The first parameter is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rows</code> and the second
parameter is <code class="code__2rdF32qjRVp7mMVBHuPwDS">columns</code>.
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
Let’s compute the number of monitors by multiplying
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rows</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">columns</code> and then
returning the value.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the function body of the function you just wrote, use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> keyword to
return <code class="code__2rdF32qjRVp7mMVBHuPwDS">rows \*
columns</code>.
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
Now that the function is defined, we can compute the number of monitors
needed. Let’s say that the office has 5 rows and 4 columns.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Declare a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">numOfMonitors</code> using
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> keyword and
assign <code class="code__2rdF32qjRVp7mMVBHuPwDS">numOfMonitors</code>
the value of invoking
<code class="code__2rdF32qjRVp7mMVBHuPwDS">monitorCount()</code> with
the arguments <code class="code__2rdF32qjRVp7mMVBHuPwDS">5</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">4</code>.
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
To check that the function worked properly, log
<code class="code__2rdF32qjRVp7mMVBHuPwDS">numOfMonitors</code> to the
console.
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

## FUNCTIONS

### Helper Functions

<p class="p__1qg33Igem5pAgn4kPMirjw">
We can also use the return value of a function inside another function.
These functions being called within another function are often referred
to as <em>helper functions</em>. Since each function is carrying out a
specific task, it makes our code easier to read and debug if necessary.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If we wanted to define a function that converts the temperature from
Celsius to Fahrenheit, we could write two functions like:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">function multiplyByNineFifths</span><span class="mtk1">(</span><span class="mtk12">number</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">return</span><span class="mtk1"> </span><span class="mtk9">number</span><span class="mtk1"> *&nbsp;(</span><span class="mtk9">9</span><span class="mtk1">/</span><span class="mtk9">5</span><span class="mtk1">);</span></span><br><span><span class="mtk1">};</span></span><br><span><span> </span></span><br><span><span class="mtk12">function getFahrenheit</span><span class="mtk1">(</span><span class="mtk12">celsius</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">return</span><span class="mtk1"> </span><span class="mtk9">multiplyByNineFifths</span><span class="mtk1">(</span><span class="mtk9">celsius</span><span class="mtk1">) +&nbsp;</span><span class="mtk9">32</span><span class="mtk1">;</span></span><br><span><span class="mtk1">};</span></span><br><span><span> </span></span><br><span><span class="mtk9">getFahrenheit</span><span class="mtk1">(</span><span class="mtk9">15</span><span class="mtk1">); </span><span class="mtk16">// Returns 59</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getFahrenheit()</code> is
called and <code class="code__2rdF32qjRVp7mMVBHuPwDS">15</code> is
passed as an argument.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The code block inside of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getFahrenheit()</code> calls
<code class="code__2rdF32qjRVp7mMVBHuPwDS">multiplyByNineFifths()</code>
and passes <code class="code__2rdF32qjRVp7mMVBHuPwDS">15</code> as an
argument.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">multiplyByNineFifths()</code>
takes the argument of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">15</code> for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">number</code> parameter.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The code block inside of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">multiplyByNineFifths()</code>
function multiplies <code class="code__2rdF32qjRVp7mMVBHuPwDS">15</code>
by <code class="code__2rdF32qjRVp7mMVBHuPwDS">(9/5)</code>, which
evaluates to <code class="code__2rdF32qjRVp7mMVBHuPwDS">27</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">27</code> is returned back to
the function call in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getFahrenheit()</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getFahrenheit()</code>
continues to execute. It adds
<code class="code__2rdF32qjRVp7mMVBHuPwDS">32</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">27</code>, which evaluates to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">59</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Finally, <code class="code__2rdF32qjRVp7mMVBHuPwDS">59</code> is
returned back to the function call
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getFahrenheit(15)</code>.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can use functions to section off small bits of logic or tasks, then
use them when we need to. Writing helper functions can help take large
and difficult tasks and break them into smaller and more manageable
tasks.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous exercise, we created a function to find the number of
monitors to order for an office. Now let’s write another function that
uses the <code class="code__2rdF32qjRVp7mMVBHuPwDS">monitorCount</code>
function to figure out the price.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Below <code class="code__2rdF32qjRVp7mMVBHuPwDS">monitorCount</code>
Create a function declaration named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">costOfMonitors</code> that
has two parameters, the first parameter is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rows</code> and the second
parameter is <code class="code__2rdF32qjRVp7mMVBHuPwDS">columns</code>.
Leave the function body empty for now.
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
Time to add some code to the function body of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">costOfMonitors</code> to
calculate the total cost.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> statement
that returns the value of calling
<code class="code__2rdF32qjRVp7mMVBHuPwDS">monitorCount(rows,
columns)</code> multiplied by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">200</code>.
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
We should save the cost to a variable.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Declare a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">totalCost</code> using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> keyword. Assign
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">totalCost</code> the value
of calling
<code class="code__2rdF32qjRVp7mMVBHuPwDS">costOfMonitors()</code> with
the arguments <code class="code__2rdF32qjRVp7mMVBHuPwDS">5</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">4</code> respectively.
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
To check that the function worked properly, log
<code class="code__2rdF32qjRVp7mMVBHuPwDS">totalCost</code> to the
console.
</p>

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

## FUNCTIONS

### Function Expressions

<p class="p__1qg33Igem5pAgn4kPMirjw">
Another way to define a function is to use a <em>function
expression</em>. To define a function inside an expression, we can use
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">function</code> keyword.
In a function expression, the function name is usually omitted. A
function with no name is called an <em>anonymous function</em>. A
function expression is often stored in a variable in order to refer to
it.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Consider the following function expression:
</p>

<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/expression.svg" alt="defining a function expression" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
To declare a function expression:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Declare a variable to make the variable’s name be the name, or
identifier, of your function. Since the release of ES6, it is common
practice to use <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code>
as the keyword to declare the variable.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Assign as that variable’s value an anonymous function created by using
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">function</code> keyword
followed by a set of parentheses with possible parameters. Then a set of
curly braces that contain the function body.
</p>
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To invoke a function expression, write the name of the variable in which
the function is stored followed by parentheses enclosing any arguments
being passed into the function.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">variableName</span><span class="mtk1">(</span><span class="mtk9">argument1</span><span class="mtk1">, </span><span class="mtk9">argument2</span><span class="mtk1">)</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Unlike function declarations, function expressions are not hoisted so
they cannot be called before they are defined.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s define a new function using a function expression.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s say we have a plant that we need to water once a week on
Wednesdays. We could define a function expression to help us check the
day of the week and if the plant needs to be watered:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Create a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">plantNeedsWater</code> using
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> variable
keyword.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Assign an anonymous function that takes in a parameter of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">day</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">plantNeedsWater</code>.
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
Now we need to add some code to the function body of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">plantNeedsWater()</code>:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In the function body add an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> conditional that
checks <code class="code__2rdF32qjRVp7mMVBHuPwDS">day ===
‘Wednesday’</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the conditional is truthy, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> code block, use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> keyword to
return <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>.
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
On days that aren’t
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Wednesday’</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">plantNeedsWater()</code>
should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code> statement
after the <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statement use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> keyword to
return <code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>.
</li>
</ul>

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
Call the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">plantNeedsWater()</code> and
pass in <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Tuesday’</code> as
an argument.
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
Let’s check that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">plantNeedsWater()</code>
returned the expected value.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Log
<code class="code__2rdF32qjRVp7mMVBHuPwDS">plantNeedsWater(‘Tuesday’)</code>
to the console. If it worked correctly, you should see
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> logged to the
console.
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

## FUNCTIONS

### Arrow Functions

<p class="p__1qg33Igem5pAgn4kPMirjw">
ES6 introduced <em>arrow function syntax</em>, a shorter way to write
functions by using the special “fat arrow”
<code class="code__2rdF32qjRVp7mMVBHuPwDS">() =\></code> notation.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/arrow-functions?page_ref=catalog">Arrow
functions</a> remove the need to type out the keyword
<code class="code__2rdF32qjRVp7mMVBHuPwDS">function</code> every time
you need to create a function. Instead, you first include the parameters
inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">( )</code> and
then add an arrow <code class="code__2rdF32qjRVp7mMVBHuPwDS">=\></code>
that points to the function body surrounded in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">{ }</code> like this:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const rectangleArea</span><span class="mtk1"> =&nbsp;(</span><span class="mtk12">width</span><span class="mtk1">, </span><span class="mtk12">height</span><span class="mtk1">) =&gt; {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">let area</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">width</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">height</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">return</span><span class="mtk1"> </span><span class="mtk9">area</span><span class="mtk1">;</span></span><br><span><span class="mtk1">};</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It’s important to be familiar with the multiple ways of writing
functions because you will come across each of these when reading other
JavaScript code.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Change
<code class="code__2rdF32qjRVp7mMVBHuPwDS">plantNeedsWater()</code> to
use arrow function syntax.
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

## FUNCTIONS

### Concise Body Arrow Functions

<p class="p__1qg33Igem5pAgn4kPMirjw">
JavaScript also provides several ways to refactor
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/arrow-functions?page_ref=catalog">arrow
function</a> syntax. The most condensed form of the function is known as
<em>concise body</em>. We’ll explore a few of these techniques below:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Functions that take only a single parameter do not need that parameter
to be enclosed in parentheses. However, if a function takes zero or
multiple parameters, parentheses are required.
</p>
<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/parameters.svg" alt="showcasing how arrow functions parameters differ for different amounts of parameters" class="img__1JGFO2nlisObc3KeOSGPRp">
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
A function body composed of a single-line block does not need curly
braces. Without the curly braces, whatever that line evaluates will be
automatically returned. The contents of the block should immediately
follow the arrow <code class="code__2rdF32qjRVp7mMVBHuPwDS">=\></code>
and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> keyword
can be removed. This is referred to as <em>implicit return</em>.
</p>
</li>
</ol>

<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/return.svg" alt="comparing single line and multiline arrow functions" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">
So if we have a function:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const squareNum</span><span class="mtk1"> =&nbsp;(</span><span class="mtk12">num</span><span class="mtk1">) =&gt; {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">return</span><span class="mtk1"> </span><span class="mtk9">num</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">num</span><span class="mtk1">;</span></span><br><span><span class="mtk1">};</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can refactor the function to:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const squareNum</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">num</span><span class="mtk1"> =&gt; </span><span class="mtk9">num</span><span class="mtk1"> *&nbsp;</span><span class="mtk9">num</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice the following changes:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The parentheses around
<code class="code__2rdF32qjRVp7mMVBHuPwDS">num</code> have been removed,
since it has a single parameter.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The curly braces <code class="code__2rdF32qjRVp7mMVBHuPwDS">{ }</code>
have been removed since the function consists of a single-line block.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> keyword has
been removed since the function consists of a single-line block.
</li>
</ul>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s refactor
<code class="code__2rdF32qjRVp7mMVBHuPwDS">plantNeedsWater()</code> to
be a concise body. Notice that we’ve already converted the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statement to a ternary operator to make the code fit on one line.
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

## FUNCTIONS

### Review Functions

<p class="p__1qg33Igem5pAgn4kPMirjw">
Give yourself a pat on the back, you just navigated through functions!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, we covered some important concepts about functions:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
A <em>function</em> is a reusable block of code that groups together a
sequence of statements to perform a specific task.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
A <em>function declaration</em> :
</p>

<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/declaration.svg" alt="Diagram showing the syntax of a function declaration" class="img__1JGFO2nlisObc3KeOSGPRp">

</li>
</ul>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
A parameter is a named variable inside a function’s block which will be
assigned the value of the argument passed in when the function is
invoked:
</p>
<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/function_parameters.svg" alt="JavaScript syntax for declaring a function with parameters" class="img__1JGFO2nlisObc3KeOSGPRp">
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
To <em>call</em> a function in your code:
</p>
<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/name.svg" alt="Diagram showing the syntax of invoking a function" class="img__1JGFO2nlisObc3KeOSGPRp">
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
ES6 introduces new ways of handling arbitrary parameters through
<em>default parameters</em> which allow us to assign a default value to
a parameter in case no argument is passed into the function.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
To return a value from a function, we use a <em>return statement</em>.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
To define a function using <em>function expressions</em>:
</p>
<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/expression.svg" alt="defining a function expression" class="img__1JGFO2nlisObc3KeOSGPRp">
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
To define a function using <em>arrow function notation</em>:
</p>
<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/arrow_notation.svg" alt="" class="img__1JGFO2nlisObc3KeOSGPRp">
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Function definition can be made concise using concise arrow notation:
</p>

<img src="https://content.codecademy.com/courses/learn-javascript-functions/Diagram/return.svg" alt="comparing single line and multiline arrow functions" class="img__1JGFO2nlisObc3KeOSGPRp">

</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It’s good to be aware of the differences between function expressions,
arrow functions, and function declarations. As you program more in
JavaScript, you’ll see a wide variety of how these function types are
used.
</p>

## BUILDING INTERACTIVE WEBSITES

### Rock, Paper, or Scissors

<p class="p__1qg33Igem5pAgn4kPMirjw">
Rock paper scissors is a classic two player game. Each player chooses
either rock, paper, or scissors. The items are compared, and whichever
player chooses the more powerful item wins.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The possible outcomes are:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Rock destroys scissors.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Scissors cut paper.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Paper covers rock.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If there’s a tie, then the game ends in a draw.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Our code will break the game into four parts:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Get the user’s choice.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Get the computer’s choice.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Compare the two choices and determine a winner.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Start the program and display the results.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The user should be able to choose ‘rock’, ‘paper’, or ‘scissors’ when
the game starts.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Using <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> and arrow
function syntax, create a function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getUserChoice</code> that
takes a single parameter
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userInput</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-2">2.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Since a user can pass in a parameter, such as ‘Rock’ or ‘rock’ with
different capitalizations, begin by utilizing JavaScript’s
<code class="code__2rdF32qjRVp7mMVBHuPwDS">toLowerCase()</code> function
to make the <code class="code__2rdF32qjRVp7mMVBHuPwDS">userInput</code>
all lowercase.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can use code like this:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">userInput</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">userInput</span><span class="mtk1">.</span><span class="mtk10">toLowerCase</span><span class="mtk1">();</span></span><br></div></code></pre></pre>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-3">3.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
When getting the user’s choice, you should also check to make sure that
the user typed a valid choice: ‘rock’, ‘paper’, or ‘scissors’.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getUserChoice()</code>, write
an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statement that makes sure the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userInput</code> is either
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘rock’</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘paper’</code>, or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘scissors’</code>. If it
does, then <code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userInput</code>. If not, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log</code> to print
an error message to the console.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-4">4.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Test the function by calling it with valid and invalid input, and
printing the results to the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can delete this when you know your function works.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-5">5.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now we need to have the computer make a choice.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a new function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getComputerChoice</code> with
no parameters. Inside its block, utilize
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.random()</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.floor()</code> to get a
whole number between 0 and 2. Then, depending on the number,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> either
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘rock’</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘paper’</code>, or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘scissors’</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-6">6.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Test the function by calling it multiple times and printing the results
to the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can delete this when you know your function works.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-7">7.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now it’s time to determine a winner.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">determineWinner</code> that
takes two parameters named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userChoice</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">computerChoice</code>. This
function will compare the two choices played and then
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> if the human
player won, lost, or tied.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s deal with the tie condition first. Within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">determineWinner()</code>
function, write an <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement that checks if the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userChoice</code> parameter
equals the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">computerChoice</code>
parameter. If so,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> a string that
the game was a tie.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-8">8.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
If the game is not a tie, you’ll need to determine a winner.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Begin by writing an <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement that checks if the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userChoice</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘rock’</code>. Inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement’s block,
write another
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statement. The inner
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
should check if the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">computerChoice</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘paper’</code>. If so,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> a message that
the computer won. If not,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> a message that
the user won.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-9">9.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, write another <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement for if the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userChoice</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘paper’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside this <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">computerChoice</code> must be
either <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘scissors’</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘rock’</code>. Write logic
that will <code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> a
winner.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-10">10.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, write yet another
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement for if
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">userChoice</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘scissors’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside of this <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">computerChoice</code> must
either be <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘rock’</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘paper’</code>. Write logic
that will <code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> a
winner.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-11">11.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Don’t forget to test your function!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Check off this task when you’ve finished testing.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-12">12.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Everything is set up. Now you need to start the game and log the
results.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">playGame</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">playGame()</code>
function, create a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userChoice</code> set equal
to the result of calling
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getUserChoice()</code>,
passing in either
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘rock’</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘paper’</code>, or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘scissors’</code> as an
argument.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Create another variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">computerChoice</code>, and
set it equal to the result of calling
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getComputerChoice()</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Under both of these variables, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log</code> to print
them to the console.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-13">13.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Finally, let’s determine who won.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">playGame()</code>
function, call the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">determineWinner()</code>
function. Pass in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">userChoice</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">computerChoice</code>
variables as its parameters. Make sure to put this function call inside
of a <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement so you can see the result.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Then, to start the game, call the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">playGame()</code> function on
the last line of your program.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-14">14.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Make this game better by adding a secret cheat code. If a user types
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘bomb’</code> as their
choice, then make sure they win, no matter what.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>

**Solutions**

``` html
```

## BUILDING INTERACTIVE WEBSITES

### Sleep Debt Calculator

<p class="p__1qg33Igem5pAgn4kPMirjw">
Did you know that giraffes sleep
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Giraffe#Legs,_locomotion_and_posture
">4.6 hours a day</a>? We humans need more than that. If we don’t sleep
enough, we accumulate sleep debt. In this project we’ll calculate if
you’re getting enough sleep each week using a sleep debt calculator.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The program will determine the actual and ideal hours of sleep for each
night of the last week.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Finally, it will calculate, in hours, how far you are from your weekly
sleep goal.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The first problem to solve is determining how many hours of sleep you
got each night of the week.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can create a function that returns any given night’s number of hours
of rest. Instead of writing seven different functions (one for each day
of the week), let’s write one function with a parameter for the day.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getSleepHours</code> with a
single parameter named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">day</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-2">2.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The function should accept a day as an argument and return the number of
hours you slept that night.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For instance, if you got 8 hours of sleep on Monday night, calling
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getSleepHours(‘monday’)</code>
should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">8</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Use an <code class="code__2rdF32qjRVp7mMVBHuPwDS">if/else</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">switch</code> statement to
implement this.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-3">3.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Test the function by calling it multiple times and printing the results
to the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can remove the tests when you know your function works.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-4">4.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that you’ve written a function to get the sleep hours for each
night, we need to do three things:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Get the total sleep hours that you actually slept
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Get the ideal sleep hours that you prefer
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Calculate the sleep debt, if any.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To get the total sleep hours that you actually slept, create a new
function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getActualSleepHours</code>
that takes no parameters.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-5">5.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getActualSleepHours()</code>
function, call the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getSleepHours()</code>
function for each day of the week. Add the results together and return
the sum using an implicit
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-6">6.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
To get the ideal sleep hours that you prefer, create a function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getIdealSleepHours</code>
with no parameters.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the function, declare a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">idealHours</code> and set its
value to your ideal hours per night. Then
<code class="code__2rdF32qjRVp7mMVBHuPwDS">return</code> the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">idealHours</code> multiplied
by 7.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll want to multiply by 7 to get the total hours you prefer per week.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-7">7.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Test your two new functions by calling them and printing the results to
the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can remove the tests when you know your functions works.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-8">8.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that you can get the actual sleep hours and the ideal sleep hours,
it’s time to calculate sleep debt.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">calculateSleepDebt</code>
with no parameters.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside of its block, create a variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">actualSleepHours</code> set
equal to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getActualSleepHours()</code>
function call.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Then, create another variable named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">idealSleepHours</code>, set
equal to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getIdealSleepHours()</code>
function call.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-9">9.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that you have
<code class="code__2rdF32qjRVp7mMVBHuPwDS">actualSleepHours</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">idealSleepHours</code>, you
can write a few
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else</code>
statements to output the result to the console. The function should
fulfill this logic:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If actual sleep equals ideal sleep, log to the console that the user got
the perfect amount of sleep.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the actual sleep is greater than the ideal sleep, log to the console
that the user got more sleep than needed.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If the actual sleep is less than the ideal sleep, log to the console
that the user should get some rest.
</li>
</ul>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-10">10.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
To make this calculator more helpful, add the hours the user is over or
under their ideal sleep in each log statement in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">calculateSleepDebt()</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-11">11.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
On the last line of the program, start the program by calling the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">calculateSleepDebt()</code>
function.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-12">12.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
For extra practice, try these:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getActualSleepHours()</code>
could be implemented without calling
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getSleepHours()</code>. Use
literal numbers and the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code> operator to rewrite
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getActualSleepHours()</code>.
It should still return the total actual hours slept in the week.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Some people need to sleep longer than others. Rewrite
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getIdealSleepHours()</code>
so that you can pass it an argument, like
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getIdealSleepHours(8)</code>
where <code class="code__2rdF32qjRVp7mMVBHuPwDS">8</code> is the ideal
hours per night. Update the call to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getIdealSleepHours()</code>
in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">calculateSleepDebt()</code>
too.
</p>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To see the solutions, open the hint.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>

**Solutions**

``` html
```

## SCOPE

### Scope

<p class="p__1qg33Igem5pAgn4kPMirjw">
An important idea in programming is <em>scope</em>. Scope defines where
variables can be accessed or referenced. While some variables can be
accessed from anywhere within a program, other variables may only be
available in a specific context.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can think of scope like the view of the night sky from your window.
Everyone who lives on the planet Earth is in the global scope of the
stars. The stars are accessible <em>globally</em>. Meanwhile, if you
live in a city, you may see the city skyline or the river. The skyline
and river are only accessible <em>locally</em> in your city, but you can
still see the stars that are available globally.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Over the next few exercises, we’ll explore how scope relates to
variables and learn best practices for variable declaration.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Go to the next exercise to learn more about scope.
</p>

**Solutions**

``` html
```

## SCOPE

### Blocks and Scope

<p class="p__1qg33Igem5pAgn4kPMirjw">
Before we talk more about scope, we first need to talk about
<em>blocks</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ve seen blocks used before in functions and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statements. A block
is the code found inside a set of curly braces
<code class="code__2rdF32qjRVp7mMVBHuPwDS">{}</code>. Blocks help us
group one or more statements together and serve as an important
structural marker for our code.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A block of code could be a function, like this:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const logSkyColor</span><span class="mtk1"> =&nbsp;() =&gt; {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">let color</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'blue'</span><span class="mtk1">; </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">color</span><span class="mtk1">); </span><span class="mtk16">// blue </span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice that the function body is actually a block of code.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Observe the block in an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">dusk</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">let color</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'pink'</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">color</span><span class="mtk1">); </span><span class="mtk16">// pink</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the next few exercises, we’ll see how blocks define the scope of
variables.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
At the top of <strong>main.js</strong>, declare a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code> variable, named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">city</code> set equal to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘New York City’</code>. This
variable will exist <em>outside</em> of the block.
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
Below the <code class="code__2rdF32qjRVp7mMVBHuPwDS">city</code>
variable, write a function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logCitySkyline</code>.
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
Inside of the function body of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logCitySkyline()</code>,
write another variable using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">skyscraper</code> and set it
equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Empire State
Building’</code>.
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
Inside the function, include a return statement like this:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">return</span><span class="mtk1"> </span><span class="mtk8">'The stars over the '</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">skyscraper</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">' in '</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">city</span><span class="mtk1">;</span></span><br></div></code></pre></pre>

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
Beneath the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logCitySkyline()</code>
function, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to log
the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logCitySkyline()</code> to
the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll notice that the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logCitySkyline()</code>
function is able to access both variables without any problems. In the
next exercise we’ll consider why would it be preferable to have one
variable outside of a block and the other inside of a block.
</p>

<span aria-live="assertive">Checkpoint 6 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

**Solutions**

``` html
```

## SCOPE

### Global Scope

<p class="p__1qg33Igem5pAgn4kPMirjw">
Scope is the context in which our variables are declared. We think about
scope in relation to blocks because variables can exist either outside
of or within these blocks.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <em>global scope</em>, variables are declared outside of blocks.
These variables are called <em>global variables</em>. Because global
variables are not bound inside a block, they can be accessed by any code
in the program, including code in blocks.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s take a look at an example of global scope:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const color</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'blue'</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk12">const returnSkyColor</span><span class="mtk1"> =&nbsp;() =&gt; {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">return</span><span class="mtk1"> </span><span class="mtk9">color</span><span class="mtk1">; </span><span class="mtk16">// blue </span></span><br><span><span class="mtk1">};</span></span><br><span><span> </span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">returnSkyColor</span><span class="mtk1">()); </span><span class="mtk16">// blue</span></span><br></div></code></pre></pre>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Even though the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code>
variable is defined outside of the block, it can be accessed in the
function block, giving it global scope.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In turn, <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> can be
accessed within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">returnSkyColor</code>
function block.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s work with global variables to see how data can be accessible from
any place within a program.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
At the top of <strong>main.js</strong>, write three global variables:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Name the first variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">satellite</code> and set it
equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘The Moon’</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Name the second variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">galaxy</code> and set it
equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘The Milky
Way’</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Name the third variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stars</code> and set it equal
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘North Star’</code>.
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
Below the variables created in the previous step, write a function named
<code class="code__2rdF32qjRVp7mMVBHuPwDS">callMyNightSky</code>. Inside
the function, include a return statement like this:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">return</span><span class="mtk1"> </span><span class="mtk8">'Night Sky: '</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">satellite</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">', '</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">stars</span><span class="mtk1"> +&nbsp;</span><span class="mtk8">', and '</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">galaxy</span><span class="mtk1">;</span></span><br></div></code></pre></pre>

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
Beneath the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">callMyNightSky()</code>
function, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to log
the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">callMyNightSky()</code> to
the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll notice that the function block for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">callMyNightSky()</code> is
able to access the global variables freely since the variables are
available to all lines of code in the file.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

**Solutions**

``` html
```

## SCOPE

### Block Scope

<p class="p__1qg33Igem5pAgn4kPMirjw">
The next context we’ll cover is <em>block scope</em>. When a variable is
defined inside a block, it is only accessible to the code within the
curly braces <code class="code__2rdF32qjRVp7mMVBHuPwDS">{}</code>. We
say that variable has <em>block scope</em> because it is <em>only</em>
accessible to the lines of code within that block.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Variables that are declared with block scope are known as <em>local
variables</em> because they are only available to the code that is part
of the same block.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Block scope works like this:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const logSkyColor</span><span class="mtk1"> =&nbsp;() =&gt; {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">let color</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'blue'</span><span class="mtk1">; </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">color</span><span class="mtk1">); </span><span class="mtk16">// Prints "blue"</span></span><br><span><span class="mtk1">};</span></span><br><span><span> </span></span><br><span><span class="mtk9">logSkyColor</span><span class="mtk1">(); </span><span class="mtk16">// Prints "blue"</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">color</span><span class="mtk1">); </span><span class="mtk16">// throws a&nbsp;ReferenceError</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll notice:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
We define a function
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logSkyColor()</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Within the function, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> variable is only
available within the curly braces of the function.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If we try to log the same variable outside the function, it throws a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">ReferenceError</code>.
</li>
</ul>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>main.js</strong>, define a function
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logVisibleLightWaves()</code>.
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
Within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logVisibleLightWaves()</code>
function, using <code class="code__2rdF32qjRVp7mMVBHuPwDS">const</code>,
create a variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lightWaves</code> and set it
equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Moonlight’</code>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logVisibleLightWaves()</code>
function, beneath the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lightWaves</code> variable,
add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement that will log the value of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lightWaves</code> variable
when the function runs.
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
Call the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logVisibleLightWaves()</code>
function from outside the function.
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
Beneath the function call, log the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lightWaves</code> to the
console from outside the function.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll notice that it logs a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">ReferenceError</code> since
the variable is tied to the block scope of the function!
</p>

<span aria-live="assertive">Checkpoint 6 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

**Solutions**

``` html
```

## SCOPE

### Scope Pollution

<p class="p__1qg33Igem5pAgn4kPMirjw">
It may seem like a great idea to always make your variables accessible,
but having too many global variables can cause problems in a program.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When you declare global variables, they go to the <em>global
namespace</em>. The global namespace allows the variables to be
accessible from anywhere in the program. These variables remain there
until the program finishes which means our global namespace can fill up
really quickly.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Scope pollution</em> is when we have too many global variables that
exist in the global namespace, or when we reuse variables across
different scopes. Scope pollution makes it difficult to keep track of
our different variables and sets us up for potential accidents. For
example, globally scoped variables can collide with other variables that
are more locally scoped, causing unexpected behavior in our code.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s look at an example of scope pollution in practice so we know how
to avoid it:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let num</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">50</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk12">const logNum</span><span class="mtk1"> =&nbsp;() =&gt; {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">num</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">100</span><span class="mtk1">; </span><span class="mtk16">// Take note of this line of code</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">num</span><span class="mtk1">);</span></span><br><span><span class="mtk1">};</span></span><br><span><span> </span></span><br><span><span class="mtk9">logNum</span><span class="mtk1">(); </span><span class="mtk16">// Prints 100</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">num</span><span class="mtk1">); </span><span class="mtk16">// Prints 100</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll notice:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
We have a variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">num</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Inside the function body of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logNum()</code>, we want to
declare a new variable but forgot to use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code> keyword.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
When we call <code class="code__2rdF32qjRVp7mMVBHuPwDS">logNum()</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">num</code> gets reassigned to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The reassignment inside
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logNum()</code> affects the
global variable <code class="code__2rdF32qjRVp7mMVBHuPwDS">num</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Even though the reassignment is allowed and we won’t get an error, if we
decided to use <code class="code__2rdF32qjRVp7mMVBHuPwDS">num</code>
later, we’ll unknowingly use the new value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">num</code>.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
While it’s important to know what global scope is, it’s best practice to
not define variables in the global scope.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s see what happens if we create a variable that overwrites a global
variable.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">callMyNightSky()</code>
function, on the very first line of the function body, assign the
variable <code class="code__2rdF32qjRVp7mMVBHuPwDS">stars</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Sirius’</code> as such:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">stars</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Sirius'</span><span class="mtk1">;</span></span><br></div></code></pre></pre>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Outside the function, under the current
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement, add another
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement to log <code class="code__2rdF32qjRVp7mMVBHuPwDS">stars</code>
to the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll notice that the global variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stars</code> was reassigned
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Sirius’</code>. In other
words, we changed the value of the global
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stars</code> variable but
it’s not easy to read what exactly happened. This is bad practice in
code maintainability and could impact our program in ways we do not
intend.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

**Solutions**

``` html
```

## SCOPE

### Practice Good Scoping

<p class="p__1qg33Igem5pAgn4kPMirjw">
Given the challenges with global variables and scope pollution, we
should follow best practices for scoping our variables as tightly as
possible using block scope.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Tightly scoping your variables will greatly improve your code in several
ways:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
It will make your code more legible since the blocks will organize your
code into discrete sections.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
It makes your code more understandable since it clarifies which
variables are associated with different parts of the program rather than
having to keep track of them line after line!
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
It’s easier to maintain your code, since your code will be modular.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
It will save memory in your code because it will cease to exist after
the block finishes running.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here’s another example of how to use block scope, as defined within an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> block:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const logSkyColor</span><span class="mtk1"> =&nbsp;() =&gt; {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">const dusk</span><span class="mtk1"> =&nbsp;</span><span class="mtk5">true</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">let color</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'blue'</span><span class="mtk1">; </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">dusk</span><span class="mtk1">) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">let color</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'pink'</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">color</span><span class="mtk1">); </span><span class="mtk16">// Prints "pink"</span></span><br><span><span class="mtk1">&nbsp;&nbsp;}</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">color</span><span class="mtk1">); </span><span class="mtk16">// Prints "blue"</span></span><br><span><span class="mtk1">};</span></span><br><span><span> </span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">color</span><span class="mtk1">); </span><span class="mtk16">// throws a&nbsp;ReferenceError</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here, you’ll notice:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
We create a variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">dusk</code> inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logSkyColor()</code>
function.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
After the <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>
statement, we define a new code block with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">{}</code> braces. Here we
assign a new value to the variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> if the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement is
truthy.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Within the <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> block,
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> variable
holds the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘pink’</code>, though outside
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> block, in the
function body, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> variable holds
the value <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘blue’</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
While we use block scope, we still pollute our namespace by reusing the
same variable name twice. A better practice would be to rename the
variable inside the block.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Block scope is a powerful tool in JavaScript, since it allows us to
define variables with precision, and not pollute the global namespace.
If a variable does not need to exist outside a block— it shouldn’t!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the function body of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logVisibleLightWaves()</code>,
beneath the <code class="code__2rdF32qjRVp7mMVBHuPwDS">region</code>
variable and before the provided
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code>
statement, create an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement that
checks if the <code class="code__2rdF32qjRVp7mMVBHuPwDS">region</code>
is the <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘The Arctic’</code>.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> block,
define a new <code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code>
variable <code class="code__2rdF32qjRVp7mMVBHuPwDS">lightWaves</code>
and set it equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Northern
Lights’</code>.
</p>

<span aria-live="assertive">Checkpoint 3 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Beneath the variable in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> block, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> to log
the value of the block variable inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> block.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Run your code and notice the output. Inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> block
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log(lightWaves)</code>
logs the value <code class="code__2rdF32qjRVp7mMVBHuPwDS">Northern
Lights</code> to the console. Outside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> block, but still
within the function, the same statement logs
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Moonlight</code> to the
console.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

**Solutions**

``` html
```

## SCOPE

### Review: Scope

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, you learned about scope and how it impacts the
accessibility of different variables.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s review the following terms:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>Scope</strong> refers to where variables can be accessed
throughout the program, and is determined by where and how they are
declared.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>Blocks</strong> are statements that exist within curly braces
<code class="code__2rdF32qjRVp7mMVBHuPwDS">{}</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>Global scope</strong> refers to the context within which
variables are accessible to every part of the program.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>Global variables</strong> are variables that exist within global
scope.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>Block scope</strong> refers to the context within which
variables are accessible only within the block they are defined.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>Local variables</strong> are variables that exist within block
scope.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>Global namespace</strong> is the space in our code that contains
globally scoped information.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<strong>Scope pollution</strong> is when too many variables exist in a
namespace or variable names are reused.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As you continue your coding journey, remember to use best practices when
declaring your variables! Scoping your variables tightly will ensure
that your code has clean, organized, and modular logic.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Practice the concepts you’ve learned in the code editor!
</p>

**Solutions**

``` html
```

## BUILDING INTERACTIVE WEBSITES

### Training Days

<p class="p__1qg33Igem5pAgn4kPMirjw">
As a seasoned athlete, one of your favorite activities is running
marathons. You use a service called Training Days that sends you a
message for the event you signed up for and the days you have left to
train.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Since you also code, Training Days has asked you to help them solve a
problem: The program currently uses the wrong scope for its variables.
They know this can be troublesome as their service evolves. In this
project you will make Training Days more maintainable and less
error-prone by fixing variable scopes.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project or would like to see an experienced
developer work through it, click “<strong>Get Unstuck</strong>“ to see a
<strong>project walkthrough video</strong>.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s begin by running the <strong>trainingDays.js</strong> file. In the
console we can see that the program is broken!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Ideally, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getRandEvent()</code>
function selects an event at random. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getTrainingDays()</code>
function returns the number of days to train based on the event
selected. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logEvent()</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">logTime()</code> functions
print the athlete name, event, and number of days to the console.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
But poorly scoped variables are causing errors.
</p>

</article>

<h2 class="fit-full fcn-task-header">
Expand days scope
</h2>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-2">2.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
To avoid the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">ReferenceError</code>,
declare <code class="code__2rdF32qjRVp7mMVBHuPwDS">days</code> within
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">getTrainingDays</code>
function, before the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code> statement.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-3">3.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Run the program again: no error, but
<code class="code__2rdF32qjRVp7mMVBHuPwDS">days</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code>! New
<code class="code__2rdF32qjRVp7mMVBHuPwDS">days</code> variables are
being defined in the scope of each
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code> statement.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Delete the three <code class="code__2rdF32qjRVp7mMVBHuPwDS">let</code>’s
within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code> statements.
</p>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-4">4.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Run the program again: fixed! Now the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">if</code>/<code class="code__2rdF32qjRVp7mMVBHuPwDS">else
if</code> statements are changing the original
<code class="code__2rdF32qjRVp7mMVBHuPwDS">days</code> rather than
defining a new one.
</p>

</article>

<h2 class="fit-full fcn-task-header">
Make name global
</h2>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-5">5.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">log</code>
functions–<code class="code__2rdF32qjRVp7mMVBHuPwDS">logEvent()</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">logTime()</code>–use the
same <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> variable.
There seems to be a problem with the scoping; we can tell by the amount
of duplicate code here! In addition to variables scoped too broadly,
duplicate code can indicate that a variable may be scoped too tightly.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s avoid this repetition by adding
<code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> as the first
parameter for each function.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-6">6.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Move the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> variable
to global scope.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-7">7.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Pass <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> as the first
argument to <code class="code__2rdF32qjRVp7mMVBHuPwDS">logEvent()</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">logTime()</code>.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-8">8.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Check that the program still works! Run it and check the output.
</p>

</article>

<h2 class="fit-full fcn-task-header">
Make random local
</h2>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-9">9.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Try the functions for another competitor. Copy and paste this code at
the end of the file.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">const event2</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">getRandEvent</span><span class="mtk1">();</span></span><br><span><span class="mtk12">const days2</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">getTrainingDays</span><span class="mtk1">(</span><span class="mtk9">event2</span><span class="mtk1">);</span></span><br><span><span class="mtk12">const name2</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Warren'</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk9">logEvent</span><span class="mtk1">(</span><span class="mtk9">name2</span><span class="mtk1">, </span><span class="mtk9">event2</span><span class="mtk1">);</span></span><br><span><span class="mtk9">logTime</span><span class="mtk1">(</span><span class="mtk9">name2</span><span class="mtk1">, </span><span class="mtk9">days2</span><span class="mtk1">);</span></span><br></div></code></pre></pre>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-10">10.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Run the program. The events are assigned randomly, but Nala and Warren
are running the same events!
</p>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-11">11.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
We see that the <code class="code__2rdF32qjRVp7mMVBHuPwDS">random</code>
variable is defined in the global scope. Each time
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getRandEvent()</code> is
called, it uses the same value.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
At the top of the file, move the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">random</code> variable from
the global scope to block scope within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getRandEvent</code> function.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-12">12.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Well done! Training Days is more maintainable and less error-prone
thanks to your work. Run the program a few times to make sure the
results are randomized.
</p>

</article>

**Solutions**

``` html
```

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### Introduction

<p class="p__1qg33Igem5pAgn4kPMirjw">
You know a bunch about JavaScript syntax,
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/introduction-to-javascript/lessons/control-flow/exercises/control-flow-intro">control
flow</a>, and
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/introduction-to-javascript/lessons/functions/exercises/intro-to-functions">functions</a>!
The best way to reinforce these skills is through practice. We’ve
created a series of problems designed to use your JavaScript knowledge.
We encourage you to review relevant lessons, look things up in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference">documentation</a>,
check out the hints and solution code if you get stuck, and, most of
all, have fun!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The tasks provided are designed to be challenging. Throughout this code
challenge, we’ll be running tests to check that the functions you write
are working correctly. We’ll often provide some example code to test
your function. We encourage you to write additional code to test your
functions. To pass our tests, your function will need to work as
described in the prompt. This means your function may seem to be passing
when you run it, but it will still fail the test because it doesn’t run
as expected in every situation we’re testing behind the scenes. Take
special note of strings—strings must be <em>identical</em> to that
requested to pass!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">greetWorld()</code>. Your
function should have no parameters and return the string
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello, World!’</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Helpful Notes:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Your function can be a function expression or a function declaration.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Notice that the prompt requires your function to <em>return</em> the
string—it will not pass the test if the string is printed to the console
rather than returned.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Your code must return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello,
World!’</code> <em>exactly</em>. The test will not pass with the
following strings: <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘hello,
world!’</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello,
world!’</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello
World!’</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello
World’</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Hello,
World.’</code>, etc.
</li>
</ul>

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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### canIVote()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The most common minimum age to vote is 18. Write a function
<code class="code__2rdF32qjRVp7mMVBHuPwDS">canIVote()</code> that takes
in a number, representing the person’s age, and returns the boolean
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> if they are 18
years old or older, and the boolean
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> if they are not.
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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### agreeOrDisagree()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">agreeOrDisagree()</code>,
that takes in two strings, and returns
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You agree!’</code> if the
two strings are the same and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You disagree!’</code> if the
two strings are different.
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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### lifePhase()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lifePhase()</code>, that
takes in a person’s
<code class="code__2rdF32qjRVp7mMVBHuPwDS">age</code>, as a number, and
returns which phase of life they are in.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here are the classifications:<br> 0-3 should return
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘baby’</code><br> 4-12 should
return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘child’</code><br>
13-19 should return
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘teen’</code><br> 20-64
should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘adult’</code>
<br> 65-140 should return
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘senior citizen’</code><br>
If the number is less than 0 or greater than 140, the program should
return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘This is not a valid
age’</code>
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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### finalGrade()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">finalGrade()</code>. It
should:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
take three arguments of type number
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
find the <code class="code__2rdF32qjRVp7mMVBHuPwDS">average</code> of
those three numbers
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
return the letter grade (as a string) that the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">average</code> corresponds to
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
return ‘You have entered an invalid grade.’ if any of the three grades
are less than 0 or greater than 100
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
0-59 should return:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘F’</code><br> 60-69 should
return: <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘D’</code><br> 70-79
should return: <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘C’</code><br>
80-89 should return:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘B’</code><br> 90-100 should
return: <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘A’</code>
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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### reportingForDuty()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">reportingForDuty()</code>,
that has two string parameters,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rank</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lastName</code>, and returns
a string in the following format: ‘rank lastName reporting for duty!’
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">reportingForDuty</span><span class="mtk1">(</span><span class="mtk8">'Private'</span><span class="mtk1">, </span><span class="mtk8">'Fido'</span><span class="mtk1">) </span></span><br><span><span class="mtk16">// Should return 'Private Fido reporting for duty!</span><span class="mtk16">'</span></span><br></div></code></pre></pre>

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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### Fix The Broken Code

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
We wrote a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rollTheDice()</code>, which
is supposed to simulate two dice being rolled and totalled. It’s close
to doing what we want, but there’s something not quite right. Can you
fix our code, please?
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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### calculateWeight()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Though an object’s mass remains consistent throughout the universe,
weight is determined by the force of gravity on an object. Since
different planets have different gravity, the same object would weigh
different amounts on each of those planets! Cool, huh?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">calculateWeight()</code>. It
should:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
have two parameters:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">earthWeight</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">planet</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
expect <code class="code__2rdF32qjRVp7mMVBHuPwDS">earthWeight</code> to
be a number
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
expect <code class="code__2rdF32qjRVp7mMVBHuPwDS">planet</code> to be a
string
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
return a number representing what that Earth-weight would equate to on
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">planet</code> passed in.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Handle the following cases:<br>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Mercury’</code> weight =
<code class="code__2rdF32qjRVp7mMVBHuPwDS">earthWeight</code> \*
0.378<br> <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Venus’</code>
weight = <code class="code__2rdF32qjRVp7mMVBHuPwDS">earthWeight</code>
\* 0.907<br> <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Mars’</code>
weight = <code class="code__2rdF32qjRVp7mMVBHuPwDS">earthWeight</code>
\* 0.377<br> <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Jupiter’</code>
weight = <code class="code__2rdF32qjRVp7mMVBHuPwDS">earthWeight</code>
\* 2.36<br> <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Saturn’</code>
weight = <code class="code__2rdF32qjRVp7mMVBHuPwDS">earthWeight</code>
\* 0.916<br> For all other inputs, return
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘Invalid Planet Entry. Try:
Mercury, Venus, Mars, Jupiter, or Saturn.’</code>
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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### truthyOrFalsy()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
It can be hard to keep track of
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Glossary/Falsy">what’s
<strong>truthy</strong> or <strong>falsy</strong> in JavaScript</a>.
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">truthyOrFalsy()</code>, that
takes in any value and returns
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> if that value is
<strong>truthy</strong> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> if that value is
<strong>falsy</strong>.
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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### truthyOrFalsy()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
It can be hard to keep track of
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Glossary/Falsy">what’s
<strong>truthy</strong> or <strong>falsy</strong> in JavaScript</a>.
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">truthyOrFalsy()</code>, that
takes in any value and returns
<code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> if that value is
<strong>truthy</strong> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> if that value is
<strong>falsy</strong>.
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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### sillySentence()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">sillySentence()</code>, that
has 3 string parameters and returns the following silly sentence with
the blanks filled in by the arguments passed into the function:
</p>

<img src="https://content.codecademy.com/courses/js-fundamentals-code-challenge/sillySentence.svg" class="img__1JGFO2nlisObc3KeOSGPRp">
<br>

<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">sillySentence</span><span class="mtk1">(</span><span class="mtk8">'excited'</span><span class="mtk1">, </span><span class="mtk8">'love'</span><span class="mtk1">, </span><span class="mtk8">'functions'</span><span class="mtk1">); </span></span><br><span><span class="mtk16">// Should return 'I am so excited because I&nbsp;love c</span><span class="mtk16">oding! Time to write some more awesome functions!'</span></span><br></div></code></pre></pre>

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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### howOld()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">howOld()</code>, that has two
number parameters, <code class="code__2rdF32qjRVp7mMVBHuPwDS">age</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">year</code>, and returns
how old someone who is currently that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">age</code> was (or will be)
during that <code class="code__2rdF32qjRVp7mMVBHuPwDS">year</code>.
Handle three different cases:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
If the year is in the future, you should return a string in the
following format:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk8">'You will be [calculated age] in the year [year pa</span><span class="mtk8">ssed in]'</span></span><br></div></code></pre></pre>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
If the year is before they were born, you should return a string in the
following format:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk8">'The year [year passed in] was [calculated number </span><span class="mtk8">of years] years before you were born'</span></span><br></div></code></pre></pre>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
If the year is in the past but not before the person was born, you
should return a string in the following format:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk8">'You were [calculated age] in the year [year passe</span><span class="mtk8">d in]'</span></span><br></div></code></pre></pre>
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

**Solutions**

``` html
```

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### Fix the broken code (round 2)!

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Given the percentage of DNA shared between two people, you can
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://isogg.org/wiki/Autosomal_DNA_statistics">calculate
their likely familial relationship</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We wrote a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">whatRelation()</code>, that
has one number parameter,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">percentSharedDNA</code>, and
returns the likely relationship. We expect the number passed in to
always be an integer from 0 to 100, but for some reason it’s not
working!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Here’s how it’s supposed to calculate the relationship:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
100 should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You are
likely identical twins.’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
35-99 should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You are
likely parent and child or full siblings.’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
14-34 should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You are
likely grandparent and grandchild, aunt/uncle and niece/nephew, or half
siblings.’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
6-13 should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You are
likely 1st cousins.’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
3-5 should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You are
likely 2nd cousins.’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
1-2 should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You are
likely 3rd cousins.’</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
0 should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘You are
likely not related.’</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Unfortunately, it’s not working how we want!
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">whatRelation</span><span class="mtk1">(</span><span class="mtk9">34</span><span class="mtk1">) </span></span><br><span><span class="mtk16">// Should return 'You are likely grandparent and g</span><span class="mtk16">randchild, aunt/uncle and niece/nephew, or half si</span><span class="mtk16">blings.'</span></span><br><span><span class="mtk16">// But instead it's returning 'You are likely 1st </span><span class="mtk16">cousins.'</span></span><br><span><span> </span></span><br><span><span class="mtk9">whatRelation</span><span class="mtk1">(</span><span class="mtk9">3</span><span class="mtk1">)</span></span><br><span><span class="mtk16">// Should return 'You are likely 2nd cousins.'</span></span><br><span><span class="mtk16">// But instead it's returning 'You are likely gran</span><span class="mtk16">dparent and grandchild, aunt/uncle and niece/nephe</span><span class="mtk16">w, or half siblings.'</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Can you fix our code, please?
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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### tipCalculator()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">tipCalculator()</code>, that
has two parameters, a string representing the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">quality</code> of the service
received and a number representing the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">total</code> cost.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Return the tip, as a number, based on the following:<br> ‘bad’ should
return a 5% tip<br> ‘ok’ should return a 15% tip<br> ‘good’ should
return a 20% tip <br> ‘excellent’ should return a 30% tip<br> all other
inputs should default to 18%<br>
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">tipCalculator</span><span class="mtk1">(</span><span class="mtk8">'good'</span><span class="mtk1">, </span><span class="mtk9">100</span><span class="mtk1">) </span><span class="mtk16">// Should return 20</span></span><br></div></code></pre></pre>

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

## CODE CHALLENGES: JAVASCRIPT FUNDAMENTALS

### toEmoticon()

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">toEmoticon()</code>, that
takes in a string and returns the corresponding emoticon as a string.
Use a switch/case, and cover these cases:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘shrug’</code> should return
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘\|*{“}*\|’</code><br>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘smiley face’</code> should
return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘:)’</code><br>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘frowny face’</code> should
return<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘:(’</code><br>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘winky face’</code> should
return <code class="code__2rdF32qjRVp7mMVBHuPwDS">‘;)’</code><br>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘heart’</code> should return
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘\<3’</code><br> any other
input should return <code class="code__2rdF32qjRVp7mMVBHuPwDS">’\|\_(\*
\~ \*)\_\|’</code>
</p>

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

## JavaScript Practice: Data Types, Conditional, Functions

<p class="p__1qg33Igem5pAgn4kPMirjw">
In these exercises, you will practice creating JavaScript functions.
This is helpful if you want to improve your logical thought process and
practice creating functions with proper JavaScript syntax.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Some of these challenges are difficult! Take some time to think about
them before starting to code.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You might not get the solution correct on your first try — look at your
output, try to find where you’re going wrong, and iterate on your
solution.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Finally, if you get stuck, use our solution code! If you “Check Answer”
twice with an incorrect solution, you should see an option to get our
solution code. However, truly investigate that solution — experiment and
play with the solution code until you have a good grasp of how it is
working. Good luck!
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

## Going Off-Platform with JavaScript

<p class="p__1qg33Igem5pAgn4kPMirjw">
When you come to Codecademy to learn how to code, you’re able to run
code from the start — and that’s because we’ve taken care of the
language setup process for you! Up until now, you’ve been able to focus
on learning JavaScript syntax rather than the configurations needed to
run that language outside of our site.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
However, as you gain more experience and get more comfortable as a
developer, you’ll realize the need to branch out from using Codecademy
to run your code. In the upcoming articles, you’ll learn different
options for executing JavaScript code. You’ll see first-hand how to use
the browser to run JavaScript, how to install JavaScript onto your
computer, how to write JavaScript code, and how to execute JavaScript
without the browser at all!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Are you ready? Click next to find out more!
</p>

## Running JavaScript in the Browser Console

<p class="p__1qg33Igem5pAgn4kPMirjw">
Along with HTML and CSS, JavaScript (JS) makes up one of the core
languages in
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/catalog/subject/web-development">web
development</a>. JS code is normally added using the HTML
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<script\></code> element for
executing in web browsers, but most modern browsers also provide a
console as part of their developer tools where we can directly write and
run JS, typically for testing and debugging purposes. The console is
essentially a REPL
(<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop">Read-Evaluate-Print-Loop</a>)
that allows us to execute JS within the context of the page, such as
modifying the page’s
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/blog/what-is-dom/">DOM
(<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction">Document
Object Model</a>)</a> or logging to the console. The console itself is
also the place to view the messages that were logged by JS code, as well
as any other information that the browser had documented, including
network requests and security errors.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this article, we’ll walk through how to open the developer console
and run JS code right in your browser!
</p>
<h2 id="heading-opening-the-browser-console" class="h2__1Ly_Sza5xVS3yZl46_StcN">
Opening the browser console
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The steps to opening the console may be slightly different depending on
the browser you use as well as your computer’s operating system. But
generally, you should be able to bring up the developer tools by right
clicking and selecting
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Inspect</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Inspect Element</code>, and
then navigate to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Console</code> tab from
there. (If you are using Apple Safari, you will first need to go to your
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Preferences</code> and check
the “Show Develop menu in menu bar” option under the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Advanced</code> tab.) Below
are some alternative ways of bringing up the console:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developers.google.com/web/tools/chrome-devtools/open">Google
Chrome</a>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Mac
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<kbd>Cmd</kbd> + <kbd>Opt</kbd> + <kbd>J</kbd>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">View</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Developer</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">JavaScript Console</code>
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Windows
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Customize and control Google
Chrome</code> (3-vertical-dot icon <kbd>⋮</kbd>) \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">More tools</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Developer tools</code>, then
click <code class="code__2rdF32qjRVp7mMVBHuPwDS">Console</code> tab
</li>
</ul>
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Tools/Web_Console/Opening_the_Web_Console">Mozilla
Firefox</a>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Mac
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<kbd>Cmd</kbd> + <kbd>Opt</kbd> + <kbd>K</kbd>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Tools</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Web Developer</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Web Console</code>
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Windows
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>K</kbd>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Open menu (3-bar icon <kbd>☰</kbd>) \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Web Developer</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Web Console</code>
</li>
</ul>
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide/console">Microsoft
Edge</a>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Mac
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<kbd>Cmd</kbd> + <kbd>Opt</kbd> + <kbd>J</kbd>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Tools</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Developer</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">JavaScript Console</code>
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Windows
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Settings and more</code>
(3-dot icon <kbd>⋯</kbd>) \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">More tools</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Developer tools</code>, then
click <code class="code__2rdF32qjRVp7mMVBHuPwDS">Console</code> tab
</li>
</ul>
</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://support.apple.com/guide/safari-developer/develop-menu-dev39df999c1/mac">Apple
Safari</a>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Mac
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<kbd>Cmd</kbd> + <kbd>Opt</kbd> + <kbd>C</kbd>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Develop</code> \>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Show JavaScript
Console</code>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ll be using Google Chrome for the following examples — also, feel
free to try to follow along with the examples! When you pull up the
console, you might see some messages that have been logged by the
browser, depending on what site you’re on. If you do, feel free to run
<code class="code__2rdF32qjRVp7mMVBHuPwDS">clear()</code> first to clear
the console.
</p>
<h2 id="heading-example-1-performing-basic-arithmetic" class="h2__1Ly_Sza5xVS3yZl46_StcN">
Example #1: Performing basic arithmetic
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember that the console is a REPL, so we can run JS code, such as
arithmetic expressions, by typing it after the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\></code> prompt and hitting
<kbd>Enter</kbd>/<kbd>Return</kbd>. The expression will be evaluated,
and the return value is printed to the console on the next line
following the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<</code>
arrow:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/articles/running-js-in-the-browser/basic_arithmetic.png" alt="basic_arithmetic" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Similarly, we can use comparison operators to compare values, which will
evaluate to <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/articles/running-js-in-the-browser/expression_evaluation.png" alt="expression_evaluation" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In some newer browsers, you may notice that the console displays a
preview of the return value as you’re typing, even before you hit
<kbd>Enter</kbd>/<kbd>Return</kbd>.
</p>
<h2 id="heading-example-2-calling-and-writing-functions" class="h2__1Ly_Sza5xVS3yZl46_StcN">
Example #2: Calling and writing functions
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In addition to performing basic arithmetic, we can also execute any
other valid JS code, such as calling functions and methods. A list of
the built-in functions and objects that are available to use in the
console can be found in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects">MDN
web docs</a>. For example,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Math.sqrt()</code> returns
the square root of a number:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/articles/running-js-in-the-browser/calling_methods.png" alt="calling_methods" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/console"><code class="code__2rdF32qjRVp7mMVBHuPwDS">console</code>
object</a> can also be accessed in the web browser’s console. Most
frequently, it is used to output text and data, such as for debugging
purposes:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/articles/running-js-in-the-browser/console_logging.png" alt="console_logging" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice that two new lines appear after running the previous code, one
preceded by the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<</code>
arrow and one without. This is because
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> simply
prints the message to the console and does not return anything. Thus,
the first line we see is the logged message, and the second line that
starts with <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<</code> is the
return value, or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can also write our own functions in the console. In the example
below, we define a function called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">addTwo()</code> which logs a
message to the console, then returns the input number plus
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code>:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/articles/running-js-in-the-browser/defining_functions.png" alt="defining_functions" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Because the function declaration itself does not evaluate to any value,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">undefined</code> is returned
and printed to the console after the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<</code> arrow.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When we call the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">addTwo()</code> function,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">Evaluating…</code> is first
outputted to the console from our
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log()</code> call.
Then, the function’s return value—which is what the function call
evaluates to—will get printed after the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<</code> arrow:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/articles/running-js-in-the-browser/calling_function.png" alt="calling_function" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<h2 id="heading-example-3-interacting-with-the-pages-dom" class="h2__1Ly_Sza5xVS3yZl46_StcN">
Example #3: Interacting with the page’s DOM
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As we’ve seen so far, we can run JS in the console completely
independent of the page we have opened in the browser. But what makes
the console particularly useful is that we could also directly inspect
and modify the page’s DOM if we wanted to. Let’s look at a simple
example using a blank webpage.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To bring up a blank page, we can enter
<code class="code__2rdF32qjRVp7mMVBHuPwDS"><about:blank></code> into the
browser’s address bar. We can confirm that there is no HTML inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<body\></code> element of
the page by checking
<code class="code__2rdF32qjRVp7mMVBHuPwDS">document.body.innerHTML</code>
in the console:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/articles/running-js-in-the-browser/inspecting_body.png" alt="inspecting_body" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can also write JS code to modify the page’s DOM, such as adding a
heading element inside the body, as seen below. Once we run the
following code, the change will immediately be reflected on the page
opened in the browser:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<img src="https://content.codecademy.com/articles/running-js-in-the-browser/manipulating_body.png" alt="manipulating_body" class="img__1JGFO2nlisObc3KeOSGPRp">
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The console also recognizes
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://api.jquery.com/jquery/"><code class="code__2rdF32qjRVp7mMVBHuPwDS">$()\</code\>\</a\> as an alias for \<a target="\_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector"\>\<code class="code\_\_2rdF32qjRVp7mMVBHuPwDS"\>document.querySelector()\</code\>\</a\> to select an element. This shorthand resembles \<a target="\_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/learn-jquery"\>jQuery\</a\> syntax and helps make manipulating the DOM through the console even more efficient:\</p\> \<p class="p\_\_1qg33Igem5pAgn4kPMirjw"\>\<img src="https://content.codecademy.com/articles/running-js-in-the-browser/aliasing_dom_selector.png" alt="aliasing_dom_selector" class="img\_\_1JGFO2nlisObc3KeOSGPRp"\>\</p\> \<p class="p\_\_1qg33Igem5pAgn4kPMirjw"\>In the code above, we used the shorthand \<code class="code\_\_2rdF32qjRVp7mMVBHuPwDS"\>$()</code>
syntax to select the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<body\></code> element and
set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> property
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">“blue”</code>. This
statement returns the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">“blue”</code> to the console,
and the color change is immediately reflected on the webpage.
</p>
<h2 id="heading-conclusion" class="h2__1Ly_Sza5xVS3yZl46_StcN">
Conclusion
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As we can see, the console provides a quick and convenient way of
running any JS code in the browser, whether independent of or directly
related to the page content. If any edits are made to the page, the
changes are temporary and will be gone upon refreshing, which works
great for testing purposes when you don’t want to modify the actual
code. Combined with the other developer tools offered by browsers, we
can see how the console can quickly become an essential part of a
developer’s toolbox!
</p>

## Introduction to JavaScript Runtime Environments

<h2 id="heading-what-is-a-runtime-environment" class="h2__1Ly_Sza5xVS3yZl46_StcN">
What is a Runtime Environment?
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A <em>runtime environment</em> is where your program will be executed.
It determines what global objects your program can access and it can
also impact how it runs. This article covers the two JavaScript runtime
environments:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the runtime environment of a browser (like
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.google.com/chrome/">Chrome</a>,
or
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.mozilla.org/en-US/firefox/">Firefox</a>)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the Node runtime environment
</li>
</ol>
<h2 id="heading-a-browsers-runtime-environment" class="h2__1Ly_Sza5xVS3yZl46_StcN">
A Browser’s Runtime Environment
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The most common place where JavaScript code is executed is in a browser.
For example, using any
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/articles/visual-studio-code">text
editor</a>, you could create a file on your own computer called
<strong>my_website.html</strong> and put the following HTML code inside:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk16">&lt;!-- my_website.html --&gt;</span></span><br><span><span class="mtk4">&lt;html&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;body&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1"> My Website </span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;script&gt;</span><span class="mtk1"> window</span><span class="mtk4">.</span><span class="mtk1">alert</span><span class="mtk4">(</span><span class="mtk8">'Hello World'</span><span class="mtk4">);</span><span class="mtk1"> </span><span class="mtk4">&lt;/script&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/body&gt;</span></span><br><span><span class="mtk4">&lt;/html&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Save your file, then open your favorite browser. Most browsers will
allow you to load websites that you have created locally by going to the
menu File \> Open File \> <strong>my_website.html</strong>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Upon loading, the embedded
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<script\>\</script\></code>
will execute and the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">window.alert()</code> method
will create a pop-up box in your browser with the text
<code class="code__2rdF32qjRVp7mMVBHuPwDS">“Hello World”</code>. How is
this possible? Where did the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">window.alert()</code> method
come from and how can it control your browser?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The answer is that you are executing this code in the <em>browser’s
runtime environment</em>. The
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Window/alert"><code class="code__2rdF32qjRVp7mMVBHuPwDS">window.alert()</code></a>
method is built into this environment and any program executed in a
browser has access to this method. In fact, the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Window"><code class="code__2rdF32qjRVp7mMVBHuPwDS">window</code></a>
object provides access to a huge amount of data and functionality
relating to the open browser window beyond just
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.alert()</code>.
</p>
<blockquote class="blockquote__Bo1k0tPllp684-m2XzKRP">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Try replacing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">window.alert()</code> with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">window.prompt()</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">window.confirm()</code>
</p>
</blockquote>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Applications created for and executed in the browser are known as
<em>front-end</em> applications. For a long time, JavaScript code could
only be executed in a browser and was used exclusively for creating
front-end applications. In order to create <em>back-end</em>
applications that could run on a computer WITHOUT a browser, you would
need to use other programming languages such as Java or PHP.
</p>
<h2 id="heading-the-node-runtime-environment" class="h2__1Ly_Sza5xVS3yZl46_StcN">
The Node Runtime Environment
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In 2009, the <em>Node runtime environment</em> was created for the
purpose of executing JavaScript code without a browser, thus enabling
programmers to create <em>full-stack</em> (front-end and back-end)
applications using only the JavaScript language.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Node is an entirely different runtime environment, meaning that
browser-environment data values and functions, like
<code class="code__2rdF32qjRVp7mMVBHuPwDS">window.alert()</code>, can’t
be used. Instead, the Node runtime environment gives back-end
applications access to a variety of features unavailable in a browser,
such as access to the server’s file system, database, and network.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, suppose you created a file called
<strong>my-app.js</strong>. We can check to see the directory that this
file is located in using the Node runtime environment variable
<code class="code__2rdF32qjRVp7mMVBHuPwDS">process</code>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk16">// my-app.js</span></span><br><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">process</span><span class="mtk1">.</span><span class="mtk10">env</span><span class="mtk1">.</span><span class="mtk10">PWD</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<blockquote class="blockquote__Bo1k0tPllp684-m2XzKRP">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice that we are using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">console.log</code> now
instead of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">window.alert()</code> since
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">window</code> object
isn’t available
</p>
</blockquote>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">process</code> is an object
containing data relating to the JavaScript file being executed.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">process.env</code> is an
object containing environment variables such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">process.env.PWD</code> which
contains the current working directory (and stands for
“<strong>P</strong>rint <strong>W</strong>orking
<strong>D</strong>irectory”).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To execute the JavaScript code in this file, first make sure that you
have
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/articles/setting-up-node-locally">set
up Node on your computer</a>. Then, open up a
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/learn-the-command-line">terminal</a>
and run the following command:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="shell" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">$ node my-app.js</span></span><br><span><span class="mtk1">/path/to/working/directory</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">node</code> command tells
your computer to execute the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">my-app.js</code> file in the
Node environment. You can also use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">node</code> command without a
file argument to open up the Node
<strong>R</strong>ead-<strong>E</strong>val-<strong>P</strong>rint-<strong>L</strong>oop
(REPL):
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="shell" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">$ node</span></span><br><span><span class="mtk1">&gt; process.env.HOME</span></span><br><span><span class="mtk1">'/home/ccuser'</span></span><br></div></code></pre></pre>
<h2 id="heading-summary" class="h2__1Ly_Sza5xVS3yZl46_StcN">
Summary
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A <em>runtime environment</em> is where your program will be executed.
JavaScript code may be executed in one of two runtime environments:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
a browser’s runtime environment
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the Node runtime environment
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In each of these environments, different data values and functions are
available, and these differences help distinguish front-end applications
from back-end applications.
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Front-end JavaScript applications are executed in a browser’s runtime
environment and have access to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">window</code> object.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Back-end JavaScript applications are executed in the Node runtime
environment and have access to the file system, databases, and networks
attached to the server.
</li>
</ul>

## Setting Up Node Locally

<h3 id="heading-what-is-node" class="h3__3B1DSzXTW-ux1viDSStOux">
What is Node?
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Node.js is a JavaScript runtime, or an environment which runs JavaScript
code outside of the browser. A “runtime” converts code written in a
high-level, human-readable, programming language and compiles it down to
code the computer can execute. Node was created with the goal of
building web servers and web applications in JavaScript, but it’s a
powerful and flexible environment that can be used for building all
sorts of applications. Check out
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/content-items/7e182ef11df387e8b51708a52df36515/exercises/introduction">our
lesson on Node</a> to get to know the environment!
</p>
<h3 id="heading-installing-node" class="h3__3B1DSzXTW-ux1viDSStOux">
Installing Node
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When you’re ready, running Node on your own computer is an exciting step
towards becoming a developer. Playing on the Node REPL in your own
terminal and executing your first local JavaScript program will set you
on your way to building all sorts of exciting projects.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Before you install Node, you’ll need to make sure you have your
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/articles/command-line-setup">command
line set up</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Navigate to the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://nodejs.org/en/">Node
website</a>, and download the version of Node labeled “LTS” on the main
page. For additional download options, such as different operating
systems and versions, you can navigate to the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://nodejs.org/en/download/">Node
downloads page</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After your download is complete, open the downloaded installation
package and follow the installation instructions.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After installation, open a new terminal window. To confirm Node was
downloaded, you can run the terminal command
<code class="code__2rdF32qjRVp7mMVBHuPwDS">which node</code> which will
print the filepath to Node. You can also check which version of Node you
downloaded with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">node
-v</code> terminal command.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Note: The current LTS version of Node.js is v14.17.1. The Node
version used in the videos below is older, but the installation process
remains the same. If the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">node</code> command is not
found, try closing and reopening the terminal/Git Bash window.</em>
</p>
<h3 id="heading-mac" class="h3__3B1DSzXTW-ux1viDSStOux">
Mac
</h3>

<iframe frameborder="0" allowfullscreen="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" title="Lesson Supplement Setting up Node js on MacOS" width="100%" height="100%" src="https://www.youtube.com/embed/uDlvILzTdh0?autoplay=0&amp;mute=0&amp;controls=1&amp;origin=https%3A%2F%2Fwww.codecademy.com&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;iv_load_policy=3&amp;modestbranding=1&amp;enablejsapi=1&amp;widgetid=1" id="widget2" data-gtm-yt-inspected-76="true">
</iframe>

<h3 id="heading-windows" class="h3__3B1DSzXTW-ux1viDSStOux">
Windows
</h3>

<iframe frameborder="0" allowfullscreen="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" title="Lesson Supplement Setting up Node js on Windows" width="100%" height="100%" src="https://www.youtube.com/embed/gbtsq3ICMBM?autoplay=0&amp;mute=0&amp;controls=1&amp;origin=https%3A%2F%2Fwww.codecademy.com&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;iv_load_policy=3&amp;modestbranding=1&amp;enablejsapi=1&amp;widgetid=3" id="widget4" data-gtm-yt-inspected-76="true">
</iframe>

## Getting Started with JavaScript in VSCode

<div data-testid="markdown" class="spacing-loose__3_R8mSIQ2cspwhDGkCOXTu markdown__1eeYJ4WPKUcvX_LDDGJR12 darkTheme__2i0sjr_RjoITRh35Ld2GzM gamut-gk1onf-ArticleMarkdown e1xfx7rd0">
<h2 id="heading-use-visual-studio-code-vscode-to-execute-javascript" class="h2__1Ly_Sza5xVS3yZl46_StcN">
Use Visual Studio Code (VSCode) to Execute JavaScript
</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As you move through various lessons and paths here on Codecademy, you
may find yourself needing to create a project on your own computer and
not on the Codecademy learning environment. This can be tricky, but it’s
an exciting step that signals that you are ready to work independently.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To do this, we’ll need to use the text editor we installed above. Let’s
take a moment to try out Visual Studio Code.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Part of becoming a skillful developer is being able to work on your own
computer to create apps and programs. In this article, you’ll write
JavaScript code in VSCode and execute it to see the output.
</p>
<h3 id="heading-pre-requisites" class="h3__3B1DSzXTW-ux1viDSStOux">
Pre-requisites
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Before getting started, please make sure that you have installed the
following:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://code.visualstudio.com/">VSCode</a> -
this is the text editor we’ll be working with.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/article/setting-up-node-locally">Node</a> -
is a runtime environment that will execute our JavaScript program.
</li>
</ul>
<h3 id="heading-development-folders" class="h3__3B1DSzXTW-ux1viDSStOux">
Development Folders
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you haven’t already set up a dedicated folder for your coding
projects, now is a good time to start. It’s important to establish an
organized file system especially as the number and size of your projects
grow. The program we’re creating for this article will be small, but
again, it’s a good habit to build.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
One convention is naming this directory <strong>projects</strong>. It
will store all of your coding projects. Whenever you create a new
project, no matter how small, you should always make a new folder inside
your <strong>projects</strong> directory. You will find that single-file
projects can quickly turn into large, multi-folder projects.
</p>
<h3 id="heading-creating-our-javascript-program" class="h3__3B1DSzXTW-ux1viDSStOux">
Creating our JavaScript program
</h3>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Below are the steps you need to follow to create a “Hello, World!”
JavaScript program.
</p>
<h4 id="heading-1-make-a-new-folder-for-this-program" class="h4__1cJx3E4QhkKjfWj3jLsTFU">

1.  Make a New Folder for this Program
    </h4>
    <p class="p__1qg33Igem5pAgn4kPMirjw">
    Navigate to your <strong>projects</strong> folder using your file
    manager or the terminal. Then inside the folder, create a new folder
    called <strong>helloJavaScript</strong>. This folder will store the
    file(s) that you’ll need.
    </p>
    <h4 id="heading-2-open-visual-studio-code" class="h4__1cJx3E4QhkKjfWj3jLsTFU">

    1.  Open Visual Studio Code
        </h4>
        <h4 id="heading-3-open-your-new-projects-folder" class="h4__1cJx3E4QhkKjfWj3jLsTFU">

        1.  Open Your New Project’s Folder
            </h4>
            <p class="p__1qg33Igem5pAgn4kPMirjw">
            Click on the ‘Explorer’ icon on the left-hand menu and click
            on the button ‘Open Folder’ and choose your development
            folder. This will launch your file manager.
            </p>
            <p class="p__1qg33Igem5pAgn4kPMirjw">
            Navigate to the <strong>helloJavaScript</strong> folder and
            select Open. The folder will open in Visual Studio Code’s
            side pane. At this point, there should not be any contents
            in the folder. We’ll add a file in the next step.
            </p>
            <h4 id="heading-4-add-a-file" class="h4__1cJx3E4QhkKjfWj3jLsTFU">

            1.  Add a File.
                </h4>
                <p class="p__1qg33Igem5pAgn4kPMirjw">
                In Visual Studio Code’s Explorer pane, click on your
                development folder’s name. You’ll see four icons appear
                to the right of the folder name. Click the ‘New File’
                icon. Type in the name of what you want to name your
                file with the correct file extension. It’s good practice
                to name the file something that matches the purpose of
                that file. In this case, you should name the file
                something like, <strong>hello.js</strong>. Press Enter
                when done.
                </p>
                <h4 id="heading-5-begin-coding" class="h4__1cJx3E4QhkKjfWj3jLsTFU">

                1.  Begin coding!
                    </h4>
                    <p class="p__1qg33Igem5pAgn4kPMirjw">
                    Copy and paste the following boilerplate JavaScript
                    code (or add your own JavaScript code):
                    </p>
                    <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk8">'Hello, World!'</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
                    <p class="p__1qg33Igem5pAgn4kPMirjw">
                    Save your file often with the Auto Save feature and
                    track changes with a version control system if you
                    know how to use one. (To turn Auto Save on, click on
                    ‘File’ then ‘Auto Save’. When it’s on, you’ll see a
                    checkmark next to ‘Auto Save’.) This will decrease
                    the chances of losing unsaved work.
                    </p>
                    <p class="p__1qg33Igem5pAgn4kPMirjw">
                    If your file has the right extension
                    <strong>.js</strong> and your code has no syntax
                    errors, you should see the correct syntax
                    highlighting in VSCode!
                    </p>
                    <p class="p__1qg33Igem5pAgn4kPMirjw">
                    Here’s what your file in VSCode should look like:
                    </p>
                    <p class="p__1qg33Igem5pAgn4kPMirjw">
                    <img src="https://static-assets.codecademy.com/Courses/javascript-local/hello_js_app_screenshot.png" alt="JavaScript code of `console.log('Hello, World!');` is written in a JavaScript file in VSCode code with full syntax highlighting" class="img__1JGFO2nlisObc3KeOSGPRp">
                    </p>
                    <h4 id="heading-6-use-node-to-run-your-program" class="h4__1cJx3E4QhkKjfWj3jLsTFU">

                    1.  Use Node to Run Your Program
                        </h4>
                        <p class="p__1qg33Igem5pAgn4kPMirjw">
                        At this point, your program can be executed by
                        Node!
                        </p>
                        <p class="p__1qg33Igem5pAgn4kPMirjw">
                        You can use your terminal or VSCode’s built-in
                        terminal to run the command:
                        </p>
                        <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="plaintext" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">node hello.js</span></span><br></div></code></pre></pre>
                        <p class="p__1qg33Igem5pAgn4kPMirjw">
                        Here’s how it could look if you’re using your
                        terminal:
                        </p>
                        <p class="p__1qg33Igem5pAgn4kPMirjw">
                        <img src="https://static-assets.codecademy.com/Courses/javascript-local/terminal_execution.png" alt="screenshot of the terminal showing the folder, `helloJavaScript` with the command `node hello.js` and a print out of &quot;Hello, World!&quot;" class="img__1JGFO2nlisObc3KeOSGPRp">
                        </p>
                        <p class="p__1qg33Igem5pAgn4kPMirjw">
                        How’s how it could look like if you’re using
                        <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://code.visualstudio.com/docs/editor/integrated-terminal">VSCode’s
                        built-in terminal</a>:
                        </p>
                        <p class="p__1qg33Igem5pAgn4kPMirjw">
                        <img src="https://static-assets.codecademy.com/Courses/javascript-local/vscode_hello.png" alt="screenshot of VSCode's terminal showing the folder, `helloJavaScript` with the command `node hello.js` and a print out of &quot;Hello, World!&quot;" class="img__1JGFO2nlisObc3KeOSGPRp">
                        </p>
                        <p class="p__1qg33Igem5pAgn4kPMirjw">
                        If you’re not seeing the correct results, make
                        sure that you’re in the correct folder in your
                        terminal and that you’ve typed in the correct
                        name of your file.
                        </p>
                        <h2 id="heading-wrapping-up" class="h2__1Ly_Sza5xVS3yZl46_StcN">
                        Wrapping up
                        </h2>
                        <p class="p__1qg33Igem5pAgn4kPMirjw">
                        Congratulations, you’ve successfully used VSCode
                        to log out
                        <code class="code__2rdF32qjRVp7mMVBHuPwDS">“Hello,
                        World!”</code> the quintessential program for
                        getting started! As you develop more, you’ll be
                        able to create more robust programs and apps —
                        straight from your own computer!
                        </p>
                        </div>

## Codecademy Workspaces

<p class="p__1qg33Igem5pAgn4kPMirjw">
By now, you have the knowledge and power to create your web development
projects locally — that’s a necessary skill of a web developer!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
However, sometimes, you just need to whip up a proof of concept, or you
want to try out a code snippet, or even take on a quick code challenge.
There’s what
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/workspaces/new">Codecademy
workspaces</a> are for.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
These
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/workspaces/new">workspaces</a>
allow you to create working code that you can save and share with
others, without needing to go through all your local setup.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
So, next time you need a lightweight tool to execute code, save it, and
also have the option to share it, consider using
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/workspaces/new">workspaces</a>!
</p>

## BUILDING INTERACTIVE WEBSITES

### Challenge Project: Number Guesser

<h4 id="heading-overview" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Overview
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This project is slightly different from others you have encountered thus
far on Codecademy. Instead of a step-by-step tutorial, this project
contains a series of open-ended requirements which describe the project
you’ll be building. There are many possible ways to correctly fulfill
all of these requirements, and you should expect to use Codecademy, the
internet, and other resources when you encounter a problem that you
cannot easily solve. In order to complete this project, you should have
completed the first three sections of
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/introduction-to-javascript">Introduction
to JavaScript</a> through Learn JavaScript: Functions.
</p>
<h4 id="heading-project-goals" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Project Goals
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you’ll write JavaScript functions to power a small
guessing game. Your code will run in the browser instead of the
terminal, and you can use your browser’s console to help you test your
functions and view any syntax errors.
</p>
<h4 id="heading-project-requirements" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Project Requirements
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you’ll write four functions in
<strong>script.js</strong>. We’ve provided some additional JavaScript
code in <strong>game.js</strong> that will call your functions based on
user interactions, but you don’t need to look at
<strong>game.js</strong> and shouldn’t edit it if you want your project
to work as intended. As you complete this project, make sure that all of
your functions are named exactly as specified within these tasks so that
they can be called correctly when the game is played. In this project,
your JavaScript functions are incorporated into a website that also uses
HTML/CSS. You’ll learn more about how to do this from scratch as you
continue your JavaScript journey. Explore the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/PRO/independent-practice-projects/number-guesser/example/index.html">completed
version</a> of the project to get a sense of what you’ll be building.
</p>
<h4 id="heading-setup-instructions" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Setup Instructions
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you choose to do this project on your computer instead of Codecademy,
you can download what you’ll need by clicking the “Download” button
below. You’ll need to open and work in <strong>script.js</strong> in a
text editor, and open <strong>index.html</strong> in a browser to test
your code. If you need help setting up on your own computer, read our
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/articles/visual-studio-code">article
about setting up a text editor for web development</a>.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">generateTarget()</code>
function. This function should return a random integer between 0 and 9.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The purpose of this function is to be called at the start of each new
round in order to generate the new secret target number.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-2">2.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">compareGuesses()</code>
function. This function:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Has three parameters representing the user (human) guess, a computer
guess, and the secret target number to be guessed.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Determines which player (human or computer) wins based on which guess is
closest to the target. If both players are tied, the human user should
win.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Return <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> if the
human player wins, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code> if the computer
player wins.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The purpose of this function is to be called each round to determine
which guess is closest to the target number.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-3">3.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">updateScore()</code>
function. This function:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Has a single parameter. This parameter will be a string value
representing the winner.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Increases the score variable
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">humanScore</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">computerScore</code>) by 1
depending on the winner passed in to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">updateScore</code>. The
string passed in will be either
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘human’</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">‘computer’</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Does not need to return any value.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The purpose of this function is to be used to correctly increase the
winner’s score after each round.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-4">4.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Create an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">advanceRound()</code>
function. This function should increase the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">currentRoundNumber</code> by
1.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The purpose of this function is to be used to update the round number
after each round.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After completing
<code class="code__2rdF32qjRVp7mMVBHuPwDS">advanceRound()</code>, your
Number Guesser game should be fully operational. You should be able to
make guesses, see your or the computer score increase correctly, move to
the next round, and see the correct round displayed.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-5">5.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Test that your code is working properly by invoking your newly written
functions within <strong>script.js</strong> with sample inputs. You can
delete this code once you’re convinced that everything is working as it
should.
</p>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-6">6.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great work! If you’d like to see the solution, move to the next task. If
you’d like to extend your project on your own, you could consider the
following:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
You probably calculated the distance from the computer guess to the
target and from the human guess to the target. Move this into a separate
<code class="code__2rdF32qjRVp7mMVBHuPwDS">getAbsoluteDistance()</code>
function that takes two numbers and returns the distance, and then use
that inside your
<code class="code__2rdF32qjRVp7mMVBHuPwDS">compareGuesses()</code>
function.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Add functionality to check whether the user guess is between 0 and 9 and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">alert()</code> the user that
their number is out of range. It’s not possible to set a number outside
this range with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">=</code> buttons, but
users can do so by typing directly in the input field.
</li>
</ul>

<button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true">
<span class="children__3aFTNwOnkG0i7uCSFwvYT5">

Stuck? Get a hint

</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0">
<title>
Arrow Chevron Down Icon
</title>
<path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
</button>

</article>
<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-7">7.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great work! Visit
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/t/number-guesser-challenge-project-javascript/462394">our
forums</a> to compare your project to our sample solution code. You can
also
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/learn-git">learn
how to host your own solution on GitHub</a> so you can share it with
other learners! Your solution might look different from ours, and that’s
okay! There are multiple ways to solve these projects, and you’ll learn
more by seeing others’ code.
</p>

</article>

**Solutions**

``` html
```

## Review: JavaScript Syntax, Part I

<p class="p__1qg33Igem5pAgn4kPMirjw">
Congratulations! The goal of this unit was to introduce you to
JavaScript, the basic syntax, and the primary concepts needed to write a
JavaScript program.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Having completed this unit, you are now able to:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Relate JavaScript’s role in web development
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Read and write introductory JavaScript syntax related to variables,
conditionals, functions, and scope
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Write JavaScript syntax to create simple programs
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Execute JavaScript code beyond the Codecademy site
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you are interested in learning more about these topics, here are some
additional resources:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Video:
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://youtu.be/v2ifWcnQs6M">Douglas
Crockford on JavaScript</a>
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
