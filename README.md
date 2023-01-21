---
output:
  md_document:
    variant: markdown_github
---

# Introduction: Fundamentals of CSS

## Introduction: Fundamentals of CSS




<div data-testid="markdown" class="spacing-loose__3_R8mSIQ2cspwhDGkCOXTu markdown__1eeYJ4WPKUcvX_LDDGJR12 darkTheme__2i0sjr_RjoITRh35Ld2GzM gamut-gk1onf-ArticleMarkdown e1xfx7rd0"><p class="p__1qg33Igem5pAgn4kPMirjw">The goal of this unit is to introduce you to CSS, one of the languages essential to developing websites. You will learn how to apply styles to HTML documents using CSS.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After this unit, you will be able to:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Understand how CSS is used for web development</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Use CSS to add initial styling to your website</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Understand the Box Model in CSS</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add positioning using CSS</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Read CSS documentation</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Learning is social. Whatever you’re working on, be sure to connect with the Codecademy community in the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/">forums</a>. Remember to check in with the community regularly, including for things like asking for code reviews on your project work and providing code reviews to others in the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/c/project/1833">projects category</a>, which can help to reinforce what you’ve learned.</p>
</div>





# Learn CSS: Selectors and Visual Rules

## SETUP AND SYNTAX

### Intro to CSS




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">While <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/learn-html">HTML</a> is the fundamental structure of every web page, it can be visually unappealing on its own. Cascading Style Sheets or <em>CSS</em> is a language web developers use to style the HTML content on a web page. If you’re interested in modifying colors, font types, font sizes, images, element positioning, and more, CSS is the tool for the job!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson, you’ll learn how to set up your CSS file structure and select which HTML elements you wish to style.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Take a look at the code in <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code> and observe how it displays in the browser to the right. This is plain HTML without any styling. Let’s take a quick look at the power of CSS.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Copy and paste the following line of code onto line 5:</p>


<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;link</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">"style.css"</span><span class="mtk1"> </span><span class="mtk7">rel</span><span class="mtk1">=</span><span class="mtk8">"stylesheet"</span><span class="mtk4">&gt;</span></span><br></div></code></pre></pre> -->

```html
<link href="style.css" rel="stylesheet">
```

<p class="p__1qg33Igem5pAgn4kPMirjw">What happens when you press the Run button?</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Take some time to explore and experiment with the code in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code> file.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html
<!DOCTYPE html>
<html>
  <head>
    <link
      href="https://fonts.googleapis.com/css?family=Roboto:400,300,500,100"
      rel="stylesheet"
      type="text/css"
    />
  </head>
  <body>
    <div class="header">
      <div class="container">
        <h1>Innovation Cloud</h1>
        <p>Connect your ideas globally</p>
        <a class="btn" href="#">Learn More</a>
      </div>
    </div>

    <div class="nav">
      <div class="container">
        <ul>
          <li>Register</li>
          <li>Schedule</li>
          <li>Sponsors</li>
          <li>About</li>
          <li>Contact</li>
        </ul>
      </div>
    </div>

    <div class="main">
      <div class="container">
        <img
          src="https://content.codecademy.com/projects/innovation-cloud/cloud.svg"
          height="128"
          width="196"
        />
        <h2>The Innovation Cloud Conference</h2>
        <p>
          Connect with the best minds across a wide range of industries to share
          ideas and brainstorm new solutions to challenging problems.
        </p>
        <p>
          Hear industry leaders talk about what worked (and what didn't) so that
          you can save time on your most challenging projects.
        </p>
        <p>
          Learn about the latest research and technologies that you can use
          immediately to invent the future.
        </p>
      </div>
    </div>

    <div class="jumbotron">
      <div class="container">
        <h2>Stay Connected</h2>
        <p>Receive weekly insights from industry insiders.</p>
        <a class="btn" href="#">Join</a>
      </div>
    </div>

    <div class="footer">
      <div class="container">
        <p>&copy; Innovation Cloud Conference</p>
      </div>
    </div>
  </body>
</html>

```

```css
html, body {
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Roboto', sans-serif;
  font-weight: 100;
}

.container {
  margin: 0 auto;
  max-width: 940px; 
  padding: 0 10px;
}

.header {
  background: url(https://content.codecademy.com/projects/innovation-cloud/bg.jpg) no-repeat center center; 
  background-size: cover;
  height: 800px;
  text-align: center; 
}

.header .container {
  position: relative;
  top: 200px;
}

.header h1 {
  color: #fff;
  line-height: 100px; 
  font-size: 80px;
  margin-top: 0;
  margin-bottom: 80px;
  text-transform: uppercase; 
}

@media (min-width:850px) {
  .header h1 {
    font-size: 120px;
  }
}

.header p {
  color: #fff;
  font-weight: 500;
  letter-spacing: 8px;
  margin-bottom: 40px;
  margin-top: 0;
  text-transform: uppercase; 
}

.btn {
  color: #fff;
  background: #000;
  padding: 10px 40px;
  text-decoration: none; 
  transition: background .5s; 
}

.nav { 
  background: #000;
  height: 80px; 
  width: 100%;
}

.nav ul {
  height: 80px;
  list-style: none;
  margin: 0 auto; 
  padding: 0;
}

.nav ul li {
  color: #fff;
  display: inline-block; 
  height: 80px;
  line-height: 80px; 
  list-style: none;
  padding: 0 10px;
  transition: background .5s; 
}

.btn:hover, .nav ul li:hover {
  background: #117bff;
  cursor: pointer; 
  transition: background .5s;  
}

.main .container {
  margin: 80px auto;
}

.main img {
  float: left;
  margin: 50px 80px 50px 0;
}

.jumbotron {
  background: url(https://content.codecademy.com/projects/innovation-cloud/jumbotron_bg.jpg) center center;
  background-size: cover;
  height: 600px; 
}

.jumbotron .container {
  position: relative;
  top: 220px;
}

.jumbotron h2 {
  color: #fff;
  text-align: right; 
}

.jumbotron p {
  color: #fff; 
  text-align: right; 
}

.jumbotron .btn {
  margin: 10px 0 0;
  float: right; 
}

.footer { 
  background: #000;
  height: 80px; 
  padding-bottom: 50px;
}

.footer p { 
  color: #fff;
  font-size: 14px;  
  height: 80px; 
  line-height: 80px;
  margin: 0;  
}

@media (max-width: 500px) {
  .header h1 {
    font-size: 50px;
    line-height: 64px;
  }

  .main, .jumbotron {
    padding: 0 30px;
  }

  .main img {
    width: 100%;
  }
}
```




### CSS Anatomy




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The diagram on the right shows two different methods, or <em>syntaxes</em>, for writing CSS code. The first syntax shows CSS applies as a <em>ruleset</em>, while the second shows it written as an <em>inline style</em>. Two different methods of writing CSS may seem a bit intimidating at first, but it’s not as bad as it looks! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/css/anatomy?page_req=catalog">anatomy</a> of both methods does share common features. Notice how both syntaxes contain a <em>declaration</em>. Declarations are the core of CSS. They apply a style to the selected element. Here, the <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/paragraphs?page_req=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code></a> element has been selected in both syntaxes and will be styled to display the text in blue.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Understanding that a declaration is used to style a selected element is key to learning how to style HTML documents with CSS! The terms below explain each of the labels in the diagram on the right.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Ruleset Terms:</strong></p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Selector</em>—The beginning of the ruleset used to target the element that will be styled.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Declaration Block</em>—The code in-between (and including) the curly braces (<code class="code__2rdF32qjRVp7mMVBHuPwDS">{ }</code>) that contains the CSS declaration(s).</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Declaration</em>—The group name for a property and value pair that applies a style to the selected element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Property</em>—The first part of the declaration that signifies what visual characteristic of the element is to be modified.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Value</em>—The second part of the declaration that signifies the value of the property.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Inline Style Terms:</strong></p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Opening Tag</em>—The start of an <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements?page_req=catalog">HTML element</a>. This is the element that will be styled.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Attribute</em>—The style <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/attributes?page_req=catalog">attribute</a> is used to add CSS inline styles to an HTML element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Declaration</em>—The group name for a property and value pair that applies a style to the selected element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Property</em>—The first part of the declaration that signifies what visual characteristic of the element is to be modified.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><em>Value</em>—The second part of the declaration that signifies the value of the property.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Don’t worry about memorizing all of these—you will get acquainted with them more and more as the course progresses! Feel free to come back and use this exercise as a reference later on.</p>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Study the diagrams to become familiar with the CSS syntax and the new terms that will be used throughout the course. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Click the “Next” button when you are ready to write some code!</p>
</div></div></div>


<img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Setup-and-Syntax/CSS_Anatomy-v2-nobgfill.svg" alt="table labeling different components of CSS syntaxes" class="gamut-1h2re45-imageStyles-imageStyles e1xtjyf0">






### Inline Styles

<div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Although CSS is a different language than HTML, it’s possible to write CSS code directly within HTML code using <em>inline styles</em>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To style an HTML element, you can add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute directly to the opening tag. After you add the attribute, you can set it equal to the CSS style(s) you’d like applied to that element.</p>


<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;p</span><span class="mtk1"> </span><span class="mtk7">style</span><span class="mtk1">=</span><span class="mtk8">'color: red;'</span><span class="mtk4">&gt;</span><span class="mtk1">I'm learning to code!</span><span class="mtk4">&lt;/p&gt;</span></span><br></div></code></pre></pre> -->

```html
<p style='color: red;'>I'm learning to code!</p>

```

<p class="p__1qg33Igem5pAgn4kPMirjw">The code in the example above demonstrates how to use inline styling. The paragraph element has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute within its opening tag. Next, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute is set equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">color: red;</code>, which will set the color of the paragraph text to red within the browser. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you’d like to add <em>more</em> than one style with inline styles, simply keep adding to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute. Make sure to end the styles with a semicolon (<code class="code__2rdF32qjRVp7mMVBHuPwDS">;</code>).</p>


<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;p</span><span class="mtk1"> </span><span class="mtk7">style</span><span class="mtk1">=</span><span class="mtk8">'color: red; font-size: 20px;'</span><span class="mtk4">&gt;</span><span class="mtk1">I'm learning to code!</span><span class="mtk4">&lt;/p&gt;</span></span><br></div></code></pre></pre> -->

```html
<p style='color: red; font-size: 20px;'>I'm learning to code!</p>

```

<p class="p__1qg33Igem5pAgn4kPMirjw">It’s important to know that inline styles are a quick way of directly styling an HTML element, but are rarely used when creating websites. But you may encounter circumstances where inline styling is necessary, so understanding how it works, and recognizing it in HTML code is good knowledge to have. Soon you’ll learn the proper way to add CSS code!</p>
</div></div>




#### Instructions 

<div><div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>, use inline styling to set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> of the first paragraph (the first <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element) to <code class="code__2rdF32qjRVp7mMVBHuPwDS">green</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div></div>


#### Solutions


```html
<!DOCTYPE html>
<html>
  <head>
      
  </head>

  <body>
    <img
      src="https://content.codecademy.com/courses/freelance-1/unit-2/explorer.jpeg"
    />
    <h1 class="title">Top Vacation Spots</h1>
    <h5>By: Stacy Gray</h5>
    <h6>Published: 2 Days Ago</h6>

    <p style="color: green;">
      The world is full of fascinating places. Planning the perfect vacation
      involves packing up, leaving home, and experiencing something new.
    </p>

    <h2 class="destination">1. Florence, Italy</h2>
    <div class="description">
      A city-size shrine to the Renaissance, Florence offers frescoes,
      sculptures, churches, palaces, and other monuments from the richest
      cultural flowering the world has known. Names from its dazzling historical
      past; Dante, Michelangelo, Galileo, Machiavelliare are some of the most
      resonant of the medieval age.
      <a
        href="https://www.nationalgeographic.com/travel/destination/florence"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Museums</li>
        <li>Bike Tours</li>
        <li>Historical Monuments</li>
      </ul>
    </div>

    <h2 class="destination">2. Beijing, China</h2>
    <div class="description">
      A city in the midst of reinventing itself and continuing to build on the
      success of the 2008 Summer Olympics, Beijing is a place of frenzied
      construction. New housing, new roads, and new sports venues seem to spring
      up overnight. At the same time, the capital of the Peoples Republic of
      China remains an epicenter of tradition, with the treasures of nearly
      2,000 years as the imperial capital still on view in the famed Forbidden
      City and in the luxuriant pavilions and gardens of the Summer Palace.
      <a
        href="https://www.nationalgeographic.com/travel/destination/beijing"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Biking</li>
        <li>Historical Sites</li>
        <li>Restaurants and Dining</li>
      </ul>
    </div>

    <h2 class="destination">3. Seoul, South Korea</h2>
    <div class="description">
      The Korean capital is a city of contrasts. Fourteenth-century city gates
      squat in the shadow of 21st-century skyscrapers, while the broad Han River
      is back-dropped by granite mountains rising in the city center complete
      with alpine highways speeding around their contours and temples nestling
      among their crags. Fashionable, gadget-laden youths battle for sidewalk
      space with fortune-tellers and peddlers, while tiny neighborhoods of
      traditional cottages contrast with endless ranks of identical apartments.
      <a
        href="https://www.nationalgeographic.com/travel/destination/seoul"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Parasailing</li>
        <li>Segway Tours</li>
        <li>Spas and Resorts</li>
      </ul>
    </div>

    <h2>More Destinations</h2>
    <ul>
      <li><h4 class="destination">Jackson Hole, Wyoming</h4></li>
      <li><h4 class="destination">Cape Town, South Africa</h4></li>
      <li><h4 class="destination">La Paz, Bolivia</h4></li>
    </ul>

    <p>
      &mdash;Best of luck with your travels, and be sure to send pictures and
      stories. We'd love to hear them!
    </p>
  </body>
</html>

```






### Internal Stylesheet




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">As previously stated, inline styles are not the best way to style HTML elements. If you wanted to style, for example, multiple <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements/h1-h6?page_req=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> elements</a>, you would have to add inline styling to each element manually. In addition, you would also have to maintain the HTML code when additional <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> elements are added. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Fortunately, HTML allows you to write CSS code in its own dedicated section with a <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style"><code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code></a> element nested inside of the <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements/head?page_req=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;head&gt;</code></a> element. The CSS code inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code> element is often referred to as an <em>internal stylesheet</em>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">An internal stylesheet has certain benefits and use cases over inlines styles, but once again, it’s not best practice (we’ll get there, we promise). Understanding how to use internal stylesheets is nonetheless helpful knowledge to have.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To create an internal stylesheet, a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code> element must be placed inside of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;head&gt;</code> element.</p>


<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;head&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;style&gt;</span></span><br><span><span> </span></span><br><span><span> </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/style&gt;</span></span><br><span><span class="mtk4">&lt;/head&gt;</span></span><br></div></code></pre></pre> -->

```html
<head>
  <style>
 
 
  </style>
</head>
```

<p class="p__1qg33Igem5pAgn4kPMirjw">After adding opening and closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code> tags in the head section, you can begin writing CSS code.</p>


<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;head&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;style&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">p</span><span class="mtk1"> </span><span class="mtk4">{</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk7">color:</span><span class="mtk1"> </span><span class="mtk4">red;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk7">font-size:</span><span class="mtk1"> </span><span class="mtk14">20px</span><span class="mtk4">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">}</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/style&gt;</span></span><br><span><span class="mtk4">&lt;/head&gt;</span></span><br></div></code></pre></pre> -->

```html
<head>
  <style>
    p {
      color: red;
      font-size: 20px;
    }
  </style>
</head>
```

<p class="p__1qg33Igem5pAgn4kPMirjw">The CSS code in the example above changes the color of all paragraph text to red and also changes the size of the text to 20 pixels. Note how the syntax of the CSS code matches (for the most part) the syntax you used for inline styling. The main difference is that you can specify which elements to apply the styling.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s move the inline style that was added to the paragraph into an internal stylesheet.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Start by adding an empty <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code> element in the head of <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code> element, add a CSS ruleset targeting the paragraph (the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element). You can leave the declaration block empty for now.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, place just the declaration from the inline style into the empty declaration block in the inline stylesheet.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Finally, delete the inline style from the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice how the styling works the same in the stylesheet as it did in the inline style!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html
<!DOCTYPE html>
<html>
  <head>
      
    <style>
      p {
        color: green;
      }
    </style>
  </head>

  <body>
    <img
      src="https://content.codecademy.com/courses/freelance-1/unit-2/explorer.jpeg"
    />
    <h1 class="title">Top Vacation Spots</h1>
    <h5>By: Stacy Gray</h5>
    <h6>Published: 2 Days Ago</h6>

    <p>
      The world is full of fascinating places. Planning the perfect vacation
      involves packing up, leaving home, and experiencing something new.
    </p>

    <h2 class="destination">1. Florence, Italy</h2>
    <div class="description">
      A city-size shrine to the Renaissance, Florence offers frescoes,
      sculptures, churches, palaces, and other monuments from the richest
      cultural flowering the world has known. Names from its dazzling historical
      past; Dante, Michelangelo, Galileo, Machiavelliare are some of the most
      resonant of the medieval age.
      <a
        href="https://www.nationalgeographic.com/travel/destination/florence"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Museums</li>
        <li>Bike Tours</li>
        <li>Historical Monuments</li>
      </ul>
    </div>

    <h2 class="destination">2. Beijing, China</h2>
    <div class="description">
      A city in the midst of reinventing itself and continuing to build on the
      success of the 2008 Summer Olympics, Beijing is a place of frenzied
      construction. New housing, new roads, and new sports venues seem to spring
      up overnight. At the same time, the capital of the Peoples Republic of
      China remains an epicenter of tradition, with the treasures of nearly
      2,000 years as the imperial capital still on view in the famed Forbidden
      City and in the luxuriant pavilions and gardens of the Summer Palace.
      <a
        href="https://www.nationalgeographic.com/travel/destination/beijing"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Biking</li>
        <li>Historical Sites</li>
        <li>Restaurants and Dining</li>
      </ul>
    </div>

    <h2 class="destination">3. Seoul, South Korea</h2>
    <div class="description">
      The Korean capital is a city of contrasts. Fourteenth-century city gates
      squat in the shadow of 21st-century skyscrapers, while the broad Han River
      is back-dropped by granite mountains rising in the city center complete
      with alpine highways speeding around their contours and temples nestling
      among their crags. Fashionable, gadget-laden youths battle for sidewalk
      space with fortune-tellers and peddlers, while tiny neighborhoods of
      traditional cottages contrast with endless ranks of identical apartments.
      <a
        href="https://www.nationalgeographic.com/travel/destination/seoul"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Parasailing</li>
        <li>Segway Tours</li>
        <li>Spas and Resorts</li>
      </ul>
    </div>

    <h2>More Destinations</h2>
    <ul>
      <li><h4 class="destination">Jackson Hole, Wyoming</h4></li>
      <li><h4 class="destination">Cape Town, South Africa</h4></li>
      <li><h4 class="destination">La Paz, Bolivia</h4></li>
    </ul>

    <p>
      &mdash;Best of luck with your travels, and be sure to send pictures and
      stories. We'd love to hear them!
    </p>
  </body>
</html>

```






### External Stylesheet




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Developers avoid mixing code by storing HTML and CSS code in separate files (HTML files contain only HTML code, and CSS files contain only CSS code). </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can create an external stylesheet by using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.css</code> file name extension, like so: <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">With an external stylesheet, you can write all the CSS code needed to style a page without sacrificing the readability and maintainability of your HTML file.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Take a look at <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>. Cut the CSS code ruleset in between the opening and closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code> tags and paste it directly into the file called <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Delete the remaining <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code> element (now empty) from <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code> and press the Run button.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Hmm, the font changes didn’t take effect? Click the Next button to find out why.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html
<!DOCTYPE html>
<html>
  <head>
    <title>Vacation World</title>
  </head>

  <body>
    <img
      src="https://content.codecademy.com/courses/freelance-1/unit-2/explorer.jpeg"
    />
    <h1 class="title">Top Vacation Spots</h1>
    <h5>By: Stacy Gray</h5>
    <h6>Published: 2 Days Ago</h6>

    <p>
      The world is full of fascinating places. Planning the perfect vacation
      involves packing up, leaving home, and experiencing something new.
    </p>

    <h2 class="destination">1. Florence, Italy</h2>
    <div class="description">
      A city-size shrine to the Renaissance, Florence offers frescoes,
      sculptures, churches, palaces, and other monuments from the richest
      cultural flowering the world has known. Names from its dazzling historical
      past; Dante, Michelangelo, Galileo, Machiavelliare are some of the most
      resonant of the medieval age.
      <a
        href="https://www.nationalgeographic.com/travel/destination/florence"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Museums</li>
        <li>Bike Tours</li>
        <li>Historical Monuments</li>
      </ul>
    </div>

    <h2 class="destination">2. Beijing, China</h2>
    <div class="description">
      A city in the midst of reinventing itself and continuing to build on the
      success of the 2008 Summer Olympics, Beijing is a place of frenzied
      construction. New housing, new roads, and new sports venues seem to spring
      up overnight. At the same time, the capital of the Peoples Republic of
      China remains an epicenter of tradition, with the treasures of nearly
      2,000 years as the imperial capital still on view in the famed Forbidden
      City and in the luxuriant pavilions and gardens of the Summer Palace.
      <a
        href="https://www.nationalgeographic.com/travel/destination/beijing"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Biking</li>
        <li>Historical Sites</li>
        <li>Restaurants and Dining</li>
      </ul>
    </div>

    <h2 class="destination">3. Seoul, South Korea</h2>
    <div class="description">
      The Korean capital is a city of contrasts. Fourteenth-century city gates
      squat in the shadow of 21st-century skyscrapers, while the broad Han River
      is back-dropped by granite mountains rising in the city center complete
      with alpine highways speeding around their contours and temples nestling
      among their crags. Fashionable, gadget-laden youths battle for sidewalk
      space with fortune-tellers and peddlers, while tiny neighborhoods of
      traditional cottages contrast with endless ranks of identical apartments.
      <a
        href="https://www.nationalgeographic.com/travel/destination/seoul"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Parasailing</li>
        <li>Segway Tours</li>
        <li>Spas and Resorts</li>
      </ul>
    </div>

    <h2>More Destinations</h2>
    <ul>
      <li><h4 class="destination">Jackson Hole, Wyoming</h4></li>
      <li><h4 class="destination">Cape Town, South Africa</h4></li>
      <li><h4 class="destination">La Paz, Bolivia</h4></li>
    </ul>

    <p>
      &mdash;Best of luck with your travels, and be sure to send pictures and
      stories. We'd love to hear them!
    </p>
  </body>
</html>

```

```css
p {
  color: green;
}

```




### Linking the CSS File




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Perfect! We successfully separated structure (HTML) from styling (CSS), but the web page still looks bland. Why?</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">When HTML and CSS codes are in separate files, the files must be linked. Otherwise, the HTML file won’t be able to locate the CSS code, and the styling will not be applied.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can use the <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements/link?page_req=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;link&gt;</code></a> element to link HTML and CSS files together. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;link&gt;</code> element must be placed within the head of the HTML file. It is a self-closing tag and requires the following attributes:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> — like the anchor element, the value of this attribute must be the address, or path, to the CSS file.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">rel</code> — this attribute describes the relationship between the HTML file and the CSS file. Because you are linking to a stylesheet, the value should be set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">stylesheet</code>.</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">When linking an HTML file and a CSS file together, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;link&gt;</code> element will look like the following:</p>


<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;link</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">'https://www.codecademy.com/stylesheets/style.css'</span><span class="mtk1"> </span><span class="mtk7">rel</span><span class="mtk1">=</span><span class="mtk8">'stylesheet'</span><span class="mtk4">&gt;</span></span><br></div></code></pre></pre> -->

```html
<link href='https://www.codecademy.com/stylesheets/style.css' rel='stylesheet'>

```

<p class="p__1qg33Igem5pAgn4kPMirjw">Note that in the example above, the path to the stylesheet is a URL:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="plaintext" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">https://www.codecademy.com/stylesheets/style.css</span></span><br></div></code></pre></pre><p class="p__1qg33Igem5pAgn4kPMirjw">Specifying the path to the stylesheet using a URL is one way of linking a stylesheet. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If the CSS file is stored in the same <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Directory_(computing)">directory</a> as your HTML file, then you can specify a <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/general/file-paths?page_req=catalog">relative path</a> instead of a URL, like so:</p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;link</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">'./style.css'</span><span class="mtk1"> </span><span class="mtk7">rel</span><span class="mtk1">=</span><span class="mtk8">'stylesheet'</span><span class="mtk4">&gt;</span></span><br></div></code></pre></pre>

```html
<link href='./style.css' rel='stylesheet'>

```

<p class="p__1qg33Igem5pAgn4kPMirjw">Using a relative path is very common way of linking a stylesheet.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s link the stylesheet <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code> to the HTML file <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">First, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;link&gt;</code> element within the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;head&gt;</code> section.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;link&gt;</code> element and set it equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Take a look at the web page in the browser to the right. Do you notice any changes yet? </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Finally, add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">rel</code> attribute and set it to the correct value. Keep an eye on the first paragraph’s font—it should appear different from the destinations’ descriptions when your stylesheet is linked correctly.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html
<!DOCTYPE html>
<html>
  <head>
    <title>Vacation World</title>
    <link href="style.css" rel="stylesheet" />
  </head>

  <body>
    <img
      src="https://content.codecademy.com/courses/freelance-1/unit-2/explorer.jpeg"
    />
    <h1 class="title">Top Vacation Spots</h1>
    <h5>By: Stacy Gray</h5>
    <h6>Published: 2 Days Ago</h6>

    <p>
      The world is full of fascinating places. Planning the perfect vacation
      involves packing up, leaving home, and experiencing something new.
    </p>

    <h2 class="destination">1. Florence, Italy</h2>
    <div class="description">
      A city-size shrine to the Renaissance, Florence offers frescoes,
      sculptures, churches, palaces, and other monuments from the richest
      cultural flowering the world has known. Names from its dazzling historical
      past; Dante, Michelangelo, Galileo, Machiavelliare are some of the most
      resonant of the medieval age.
      <a
        href="https://www.nationalgeographic.com/travel/destination/florence"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Museums</li>
        <li>Bike Tours</li>
        <li>Historical Monuments</li>
      </ul>
    </div>

    <h2 class="destination">2. Beijing, China</h2>
    <div class="description">
      A city in the midst of reinventing itself and continuing to build on the
      success of the 2008 Summer Olympics, Beijing is a place of frenzied
      construction. New housing, new roads, and new sports venues seem to spring
      up overnight. At the same time, the capital of the Peoples Republic of
      China remains an epicenter of tradition, with the treasures of nearly
      2,000 years as the imperial capital still on view in the famed Forbidden
      City and in the luxuriant pavilions and gardens of the Summer Palace.
      <a
        href="https://www.nationalgeographic.com/travel/destination/beijing"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Biking</li>
        <li>Historical Sites</li>
        <li>Restaurants and Dining</li>
      </ul>
    </div>

    <h2 class="destination">3. Seoul, South Korea</h2>
    <div class="description">
      The Korean capital is a city of contrasts. Fourteenth-century city gates
      squat in the shadow of 21st-century skyscrapers, while the broad Han River
      is back-dropped by granite mountains rising in the city center complete
      with alpine highways speeding around their contours and temples nestling
      among their crags. Fashionable, gadget-laden youths battle for sidewalk
      space with fortune-tellers and peddlers, while tiny neighborhoods of
      traditional cottages contrast with endless ranks of identical apartments.
      <a
        href="https://www.nationalgeographic.com/travel/destination/seoul"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Parasailing</li>
        <li>Segway Tours</li>
        <li>Spas and Resorts</li>
      </ul>
    </div>

    <h2>More Destinations</h2>
    <ul>
      <li><h4 class="destination">Jackson Hole, Wyoming</h4></li>
      <li><h4 class="destination">Cape Town, South Africa</h4></li>
      <li><h4 class="destination">La Paz, Bolivia</h4></li>
    </ul>

    <p>
      &mdash;Best of luck with your travels, and be sure to send pictures and
      stories. We'd love to hear them!
    </p>
  </body>
</html>

```

```css
p {
  color: green;
}
```




### Review




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Great work so far! By understanding how to incorporate CSS code into your HTML file, as well as learning some of the key terms, you’re on your way to creating spectacular websites with HTML and CSS.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s review what you learned so far:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The basic anatomy of CSS syntax written for both inline styles and stylesheets.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Some commonly used CSS terms, such as <em>ruleset</em>, <em>selector</em>, and <em>declaration</em>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">CSS inline styles can be written inside the opening HTML tag using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code> attribute.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Inline styles can be used to style HTML, but it is not the best practice.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">An internal stylesheet is written using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code> element inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;head&gt;</code> element of an HTML file.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Internal stylesheets can be used to style HTML but are also not best practice.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">An external stylesheet separates CSS code from HTML, by using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.css</code> file extension.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">External stylesheets are the best approach when it comes to using HTML and CSS.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">External stylesheets are linked to HTML using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;link&gt;</code> element.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Take this knowledge to the next lesson, where you start learning how to select HTML elements to style!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Here are a few more resources to add to your toolkit:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/css">Codecademy Docs: CSS</a></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/workspaces/new">Codecademy Workspaces: CSS</a></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Make sure to bookmark these links so you have them at your disposal.</p>
</div>

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Vacation World</title>
    <link href="style.css" rel="stylesheet" />
  </head>

  <body>
    <img
      src="https://content.codecademy.com/courses/freelance-1/unit-2/explorer.jpeg"
    />
    <h1 class="title">Top Vacation Spots</h1>
    <h5>By: Stacy Gray</h5>
    <h6>Published: 2 Days Ago</h6>

    <p>
      The world is full of fascinating places. Planning the perfect vacation
      involves packing up, leaving home, and experiencing something new.
    </p>

    <h2 class="destination">1. Florence, Italy</h2>
    <div class="description">
      A city-size shrine to the Renaissance, Florence offers frescoes,
      sculptures, churches, palaces, and other monuments from the richest
      cultural flowering the world has known. Names from its dazzling historical
      past; Dante, Michelangelo, Galileo, Machiavelliare are some of the most
      resonant of the medieval age.
      <a
        href="https://www.nationalgeographic.com/travel/destination/florence"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Museums</li>
        <li>Bike Tours</li>
        <li>Historical Monuments</li>
      </ul>
    </div>

    <h2 class="destination">2. Beijing, China</h2>
    <div class="description">
      A city in the midst of reinventing itself and continuing to build on the
      success of the 2008 Summer Olympics, Beijing is a place of frenzied
      construction. New housing, new roads, and new sports venues seem to spring
      up overnight. At the same time, the capital of the Peoples Republic of
      China remains an epicenter of tradition, with the treasures of nearly
      2,000 years as the imperial capital still on view in the famed Forbidden
      City and in the luxuriant pavilions and gardens of the Summer Palace.
      <a
        href="https://www.nationalgeographic.com/travel/destination/beijing"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Biking</li>
        <li>Historical Sites</li>
        <li>Restaurants and Dining</li>
      </ul>
    </div>

    <h2 class="destination">3. Seoul, South Korea</h2>
    <div class="description">
      The Korean capital is a city of contrasts. Fourteenth-century city gates
      squat in the shadow of 21st-century skyscrapers, while the broad Han River
      is back-dropped by granite mountains rising in the city center complete
      with alpine highways speeding around their contours and temples nestling
      among their crags. Fashionable, gadget-laden youths battle for sidewalk
      space with fortune-tellers and peddlers, while tiny neighborhoods of
      traditional cottages contrast with endless ranks of identical apartments.
      <a
        href="https://www.nationalgeographic.com/travel/destination/seoul"
        target="_blank"
        >Learn More</a
      >.
      <h5>Top Attractions</h5>
      <ul>
        <li>Parasailing</li>
        <li>Segway Tours</li>
        <li>Spas and Resorts</li>
      </ul>
    </div>

    <h2>More Destinations</h2>
    <ul>
      <li><h4 class="destination">Jackson Hole, Wyoming</h4></li>
      <li><h4 class="destination">Cape Town, South Africa</h4></li>
      <li><h4 class="destination">La Paz, Bolivia</h4></li>
    </ul>

    <p>
      &mdash;Best of luck with your travels, and be sure to send pictures and
      stories. We'd love to hear them!
    </p>
  </body>
</html>

```

```css
p {
  color: green;
}

```




## SELECTORS

### Type




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Remember that <em>declarations</em> are a fundamental part of CSS because they apply a style to a selected element. But how do you decide which elements will get the style? With a <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/css/selectors?page_req=catalog"><em>selector</em></a>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">A selector is used to target the specific HTML element(s) to be styled by the declaration. One selector you may already be familiar with is the <em>type</em> selector. Just like its name suggests, the type selector matches the <em>type</em> of the element in the HTML document. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the previous lesson, you changed the color of a paragraph element.</p>

<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">green</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre> -->

```css
p {
  color: green;
}
```

<p class="p__1qg33Igem5pAgn4kPMirjw">This is an instance of using the type selector! The element type is <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code>, which comes from the HTML <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Some important notes on the type selector:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The type selector does not include the angle brackets.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Since element types are often referred to by their opening tag name, the type selector is sometimes referred to as the <em>tag name</em> or <em>element</em> selector.</li>
</ul>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Open <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code>. On line 5, add a ruleset using the type selector to target all <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> elements. Leave the declaration block (<code class="code__2rdF32qjRVp7mMVBHuPwDS">{ }</code>) empty for now.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside the curly braces of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> selector, add the declaration below:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">maroon</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Note that the content of the web page will update because we’ve already linked <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html
<!DOCTYPE html>
<html>

<head>
  <title>Vacation World</title>
  <link href='style.css' rel='stylesheet'>
</head>

<body>
  <img src='https://content.codecademy.com/courses/freelance-1/unit-2/explorer.jpeg' />
  <h1 class='title'>Top Vacation Spots</h1>
  <h5>By: Stacy Gray</h5>
  <h6>Published: 2 Days Ago</h6>

  <p>The world is full of fascinating places. Planning the perfect vacation involves packing up, leaving home, and experiencing something new.</p>

  <h2 class='destination'>1. Florence, Italy</h2>
  <div class='description'>A city-size shrine to the Renaissance, Florence offers frescoes, sculptures, churches, palaces, and other monuments from the richest cultural flowering the world has known. Names from its dazzling historical past; Dante, Michelangelo, Galileo, Machiavelliare are some of the most resonant of the medieval age. <a href='https://www.nationalgeographic.com/travel/destination/florence' target='_blank'>Learn More</a>.
    <h5>Top Attractions</h5>
    <ul>
      <li>Museums</li>
      <li>Bike Tours</li>
      <li>Historical Monuments</li>
    </ul>
  </div>

  <h2 class='destination'>2. Beijing, China</h2>
  <div class='description'>A city in the midst of reinventing itself and continuing to build on the success of the 2008 Summer Olympics, Beijing is a place of frenzied construction. New housing, new roads, and new sports venues seem to spring up overnight. At the same time, the capital of the Peoples Republic of China remains an epicenter of tradition, with the treasures of nearly 2,000 years as the imperial capital still on view in the famed Forbidden City and in the luxuriant pavilions and gardens of the Summer Palace.
    <a href='https://www.nationalgeographic.com/travel/destination/beijing' target='_blank'>Learn More</a>.
    <h5>Top Attractions</h5>
    <ul>
      <li>Biking</li>
      <li>Historical Sites</li>
      <li>Restaurants and Dining</li>
    </ul>
  </div>

  <h2 class='destination'>3. Seoul, South Korea</h2>
  <div class='description'>The Korean capital is a city of contrasts. Fourteenth-century city gates squat in the shadow of 21st-century skyscrapers, while the broad Han River is back-dropped by granite mountains rising in the city center complete with alpine highways speeding around their contours and temples nestling among their crags. Fashionable, gadget-laden youths battle for sidewalk space with fortune-tellers and peddlers, while tiny neighborhoods of traditional cottages contrast with endless ranks of identical apartments.
    <a href='https://www.nationalgeographic.com/travel/destination/seoul' target='_blank'>Learn More</a>.
    <h5>Top Attractions</h5>
    <ul>
      <li>Parasailing</li>
      <li>Segway Tours</li>
      <li>Spas and Resorts</li>
    </ul>
  </div>

  <h2> More Destinations </h2>
  <ul>
    <li><h4 class='destination'>Jackson Hole, Wyoming</h4></li>
    <li><h4 class='destination'>Cape Town, South Africa</h4></li>
    <li><h4 class='destination'>La Paz, Bolivia</h4></li>
  </ul>

  <p>&mdash;Best of luck with your travels, and be sure to send pictures and stories. We'd love to hear them!</p>


</body>

</html>
```

```css
p {
  color: green;
}

```




### Universal




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">You learned how the <em>type selector</em> selects all elements of a given type. Well, the <em>universal selector</em> selects all elements of <em>any</em> type. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Targeting all of the elements on the page has a few specific use cases, such as resetting default browser styling, or selecting all <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/t/what-are-parent-elements-and-child-elements-in-html-and-css/283224">children</a> of a parent element. Don’t worry if you don’t understand the use cases right now—we will get to them later on in our Learn CSS journey.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The universal selector uses the <code class="code__2rdF32qjRVp7mMVBHuPwDS">*</code> character in the same place where you specified the type selector in a ruleset, like so:</p>

<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span><span class="mtk9"> </span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> Verdana</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre> -->

```css
* { 
  font-family: Verdana;
}
```

<p class="p__1qg33Igem5pAgn4kPMirjw">In the code above, every text element on the page will have its font changed to <code class="code__2rdF32qjRVp7mMVBHuPwDS">Verdana</code>.  </p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">To see how the universal selector targets all elements on a page, copy the rule below and paste it on the first line of <strong>style.css</strong>.</p>

<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 1px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">red</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre> -->

```css
* {
  border: 1px solid red;
}
```

<p class="p__1qg33Igem5pAgn4kPMirjw">Then, click “Run”.  </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Since the universal selector targets all elements, every element on the page now has a red border. Not a visually pleasing look, but you can see how all of the elements have been modified.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html
<!DOCTYPE html>
<html>

<head>
  <title>Vacation World</title>
  <link href='style.css' rel='stylesheet'>
</head>

<body>
  <img src='https://content.codecademy.com/courses/freelance-1/unit-2/explorer.jpeg' />
  <h1 class='title'>Top Vacation Spots</h1>
  <h5>By: Stacy Gray</h5>
  <h6>Published: 2 Days Ago</h6>

  <p>The world is full of fascinating places. Planning the perfect vacation involves packing up, leaving home, and experiencing something new.</p>

  <h2 class='destination'>1. Florence, Italy</h2>
  <div class='description'>A city-size shrine to the Renaissance, Florence offers frescoes, sculptures, churches, palaces, and other monuments from the richest cultural flowering the world has known. Names from its dazzling historical past; Dante, Michelangelo, Galileo, Machiavelliare are some of the most resonant of the medieval age. <a href='https://www.nationalgeographic.com/travel/destination/florence' target='_blank'>Learn More</a>.
    <h5>Top Attractions</h5>
    <ul>
      <li>Museums</li>
      <li>Bike Tours</li>
      <li>Historical Monuments</li>
    </ul>
  </div>

  <h2 class='destination'>2. Beijing, China</h2>
  <div class='description'>A city in the midst of reinventing itself and continuing to build on the success of the 2008 Summer Olympics, Beijing is a place of frenzied construction. New housing, new roads, and new sports venues seem to spring up overnight. At the same time, the capital of the Peoples Republic of China remains an epicenter of tradition, with the treasures of nearly 2,000 years as the imperial capital still on view in the famed Forbidden City and in the luxuriant pavilions and gardens of the Summer Palace.
    <a href='https://www.nationalgeographic.com/travel/destination/beijing' target='_blank'>Learn More</a>.
    <h5>Top Attractions</h5>
    <ul>
      <li>Biking</li>
      <li>Historical Sites</li>
      <li>Restaurants and Dining</li>
    </ul>
  </div>

  <h2 class='destination'>3. Seoul, South Korea</h2>
  <div class='description'>The Korean capital is a city of contrasts. Fourteenth-century city gates squat in the shadow of 21st-century skyscrapers, while the broad Han River is back-dropped by granite mountains rising in the city center complete with alpine highways speeding around their contours and temples nestling among their crags. Fashionable, gadget-laden youths battle for sidewalk space with fortune-tellers and peddlers, while tiny neighborhoods of traditional cottages contrast with endless ranks of identical apartments.
    <a href='https://www.nationalgeographic.com/travel/destination/seoul' target='_blank'>Learn More</a>.
    <h5>Top Attractions</h5>
    <ul>
      <li>Parasailing</li>
      <li>Segway Tours</li>
      <li>Spas and Resorts</li>
    </ul>
  </div>

  <h2> More Destinations </h2>
  <ul>
    <li><h4 class='destination'>Jackson Hole, Wyoming</h4></li>
    <li><h4 class='destination'>Cape Town, South Africa</h4></li>
    <li><h4 class='destination'>La Paz, Bolivia</h4></li>
  </ul>

  <p>&mdash;Best of luck with your travels, and be sure to send pictures and stories. We'd love to hear them!</p>


</body>

</html>
```

```css
* {
  border: 1px solid red;
}

p {
  color: green;
}

h1 {
  color: maroon;
}
```




### Class




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">CSS is not limited to selecting elements by their type. As you know, HTML elements can also have <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-html/lessons/intro-to-html/exercises/attr-html">attributes</a>. When working with HTML and CSS a <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/classes?page_req=catalog"><em>class</em></a> attribute is one of the most common ways to select an element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For example, consider the following HTML:</p>


<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;p</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'brand'</span><span class="mtk4">&gt;</span><span class="mtk1">Sole Shoe Company</span><span class="mtk4">&lt;/p&gt;</span></span><br></div></code></pre></pre> -->

```html
<p class='brand'>Sole Shoe Company</p>

```

<p class="p__1qg33Igem5pAgn4kPMirjw">The paragraph element in the example above has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> attribute within the opening tag of the<code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> attribute is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'brand'</code>. To select this element using CSS, we can create a ruleset with a class selector of <code class="code__2rdF32qjRVp7mMVBHuPwDS">.brand</code>.</p>

<!-- <pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.brand</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span> </span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre> -->

```css
.brand {
 
}
```

<p class="p__1qg33Igem5pAgn4kPMirjw">To select an HTML element by its class using CSS, a period (<code class="code__2rdF32qjRVp7mMVBHuPwDS">.</code>) must be prepended to the class’s name. In the example above, the class is <code class="code__2rdF32qjRVp7mMVBHuPwDS">brand</code>, so the CSS selector for it is <code class="code__2rdF32qjRVp7mMVBHuPwDS">.brand</code>.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">On line 11 of <strong>index.html</strong> there is an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> element with the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Now, open <strong>style.css</strong>. On line 13, use the class selector to create a ruleset that selects that HTML element using the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside the curly braces of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.title</code> selector, add the declaration:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">teal</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">This code will change the color of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code> class to teal.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">We’ll see in a later exercise why using <code class="code__2rdF32qjRVp7mMVBHuPwDS">.title</code> overrides the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> selector.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html
<!DOCTYPE html>
<html>

<head>
  <title>Vacation World</title>
  <link href='style.css' rel='stylesheet'>
</head>

<body>
  <img src='https://content.codecademy.com/courses/freelance-1/unit-2/explorer.jpeg' />
  <h1 class='title'>Top Vacation Spots</h1>
  <h5>By: Stacy Gray</h5>
  <h6>Published: 2 Days Ago</h6>

  <p>The world is full of fascinating places. Planning the perfect vacation involves packing up, leaving home, and experiencing something new.</p>

  <h2 class='destination'>1. Florence, Italy</h2>
  <div class='description'>A city-size shrine to the Renaissance, Florence offers frescoes, sculptures, churches, palaces, and other monuments from the richest cultural flowering the world has known. Names from its dazzling historical past; Dante, Michelangelo, Galileo, Machiavelliare are some of the most resonant of the medieval age. <a href='https://www.nationalgeographic.com/travel/destination/florence' target='_blank'>Learn More</a>.
    <h5>Top Attractions</h5>
    <ul>
      <li>Museums</li>
      <li>Bike Tours</li>
      <li>Historical Monuments</li>
    </ul>
  </div>

  <h2 class='destination'>2. Beijing, China</h2>
  <div class='description'>A city in the midst of reinventing itself and continuing to build on the success of the 2008 Summer Olympics, Beijing is a place of frenzied construction. New housing, new roads, and new sports venues seem to spring up overnight. At the same time, the capital of the Peoples Republic of China remains an epicenter of tradition, with the treasures of nearly 2,000 years as the imperial capital still on view in the famed Forbidden City and in the luxuriant pavilions and gardens of the Summer Palace.
    <a href='https://www.nationalgeographic.com/travel/destination/beijing' target='_blank'>Learn More</a>.
    <h5>Top Attractions</h5>
    <ul>
      <li>Biking</li>
      <li>Historical Sites</li>
      <li>Restaurants and Dining</li>
    </ul>
  </div>

  <h2 class='destination'>3. Seoul, South Korea</h2>
  <div class='description'>The Korean capital is a city of contrasts. Fourteenth-century city gates squat in the shadow of 21st-century skyscrapers, while the broad Han River is back-dropped by granite mountains rising in the city center complete with alpine highways speeding around their contours and temples nestling among their crags. Fashionable, gadget-laden youths battle for sidewalk space with fortune-tellers and peddlers, while tiny neighborhoods of traditional cottages contrast with endless ranks of identical apartments.
    <a href='https://www.nationalgeographic.com/travel/destination/seoul' target='_blank'>Learn More</a>.
    <h5>Top Attractions</h5>
    <ul>
      <li>Parasailing</li>
      <li>Segway Tours</li>
      <li>Spas and Resorts</li>
    </ul>
  </div>

  <h2> More Destinations </h2>
  <ul>
    <li><h4 class='destination'>Jackson Hole, Wyoming</h4></li>
    <li><h4 class='destination'>Cape Town, South Africa</h4></li>
    <li><h4 class='destination'>La Paz, Bolivia</h4></li>
  </ul>

  <p>&mdash;Best of luck with your travels, and be sure to send pictures and stories. We'd love to hear them!</p>


</body>

</html>
```

```css
* {
  border: 1px solid red;
}

p {
  color: green;
}

h1 {
  color: maroon;
}

.title {
  color: teal;
}
```




### Multiple Classes




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">We can use CSS to select an HTML element’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> attribute by name. And so far, we’ve selected elements using only one class name per element. If every HTML element had a single class, all the style information for each element would require a new class.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Luckily, it’s possible to add more than one class name to an HTML element’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> attribute.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For instance, perhaps there’s a heading element that needs to be green and bold. You could write two CSS rulesets like so:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.green</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">green</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.bold</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-weight</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">bold</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then, you could include both of these classes on one HTML element like this:</p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;h1</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'green bold'</span><span class="mtk4">&gt;</span><span class="mtk1"> ... </span><span class="mtk4">&lt;/h1&gt;</span></span><br></div></code></pre></pre>

```html

```

<p class="p__1qg33Igem5pAgn4kPMirjw">We can add multiple classes to an HTML element’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> attribute by separating them with a space. This enables us to mix and match CSS classes to create many unique styles without writing a custom class for every style combination needed.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>index.html</strong>, on line 11, there is an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> element with a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">title</code>. Add a second class named <code class="code__2rdF32qjRVp7mMVBHuPwDS">uppercase</code> to this element.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, navigate to <strong>style.css</strong>, and add a ruleset using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.uppercase</code> class selector. Then, add the declaration below inside of the curly braces.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">text-transform</span><span class="mtk9">: </span><span class="mtk4">uppercase</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### ID




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Oftentimes it’s important to select a single element with CSS to give it its own unique style. If an HTML element needs to be styled uniquely, we can give it an ID using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> attribute. </p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;h1</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">'large-title'</span><span class="mtk4">&gt;</span><span class="mtk1"> ... </span><span class="mtk4">&lt;/h1&gt;</span></span><br></div></code></pre></pre>

```html

```

<p class="p__1qg33Igem5pAgn4kPMirjw">In contrast to <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> which accepts multiple values, and can be used broadly throughout an HTML document, an element’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> can only have a single value, and only be used once per page. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To select an element’s ID with CSS, we prepend the <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> name with a number sign (<code class="code__2rdF32qjRVp7mMVBHuPwDS">#</code>). For instance, if we wanted to select the HTML element in the example above, it would look like this:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">#large-title</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span> </span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> name is <code class="code__2rdF32qjRVp7mMVBHuPwDS">large-title</code>, therefore the CSS selector for it is <code class="code__2rdF32qjRVp7mMVBHuPwDS">#large-title</code>.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">On line 11 of <strong>index.html</strong>, inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> opening tag and after the class attribute, add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> with the value <code class="code__2rdF32qjRVp7mMVBHuPwDS">article-title</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Navigate to <strong>style.css</strong>. Add a ruleset using the ID selector to target the <code class="code__2rdF32qjRVp7mMVBHuPwDS">article-title</code> ID. Inside of its curly braces, write the declaration:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">font-family</span><span class="mtk9">: </span><span class="mtk4">cursive</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">You’ll see the title change to a cursive font bringing some beauty and elegance to the page! Okay, maybe not so much. But the font does change.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Attribute




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">You may remember that some HTML elements use attributes to add extra detail or functionality to the element. Some familiar attributes may be <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">src</code>, but there are <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes">many more</a>—including <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code>!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <em>attribute selector</em> can be used to target HTML elements that already contain attributes. Elements of the same type can be targeted differently by their attribute or attribute value. This alleviates the need to add new code, like the <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> or <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> attributes. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Attributes can be selected similarly to types, classes, and IDs. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">[</span><span class="mtk9">href</span><span class="mtk1">]{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">magenta</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The most basic syntax is an attribute surrounded by square brackets. In the above example: <code class="code__2rdF32qjRVp7mMVBHuPwDS">[href]</code> would target all elements with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute and set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">magenta</code>.   </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">And it can get <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors#syntax">more granular</a> from there by adding type and/or attribute values. One way is by using <code class="code__2rdF32qjRVp7mMVBHuPwDS">type[attribute*=value]</code>. In short, this code selects an element where the attribute contains any instance of the specified value. Let’s take a look at an example.</p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;img</span><span class="mtk1"> </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">'/images/seasons/cold/winter.jpg'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;img</span><span class="mtk1"> </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">'/images/seasons/warm/summer.jpg'</span><span class="mtk4">&gt;</span></span><br></div></code></pre></pre>

```html

```

<p class="p__1qg33Igem5pAgn4kPMirjw">The HTML code above renders two <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements/img?page_req=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;img&gt;</code></a> elements, each containing a <code class="code__2rdF32qjRVp7mMVBHuPwDS">src</code> attribute with a value equaling a link to an image file.  </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">img</span><span class="mtk1">[</span><span class="mtk12">src</span><span class="mtk1">*=</span><span class="mtk8">'winter'</span><span class="mtk1">]</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 50px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">img</span><span class="mtk1">[</span><span class="mtk12">src</span><span class="mtk1">*=</span><span class="mtk8">'summer'</span><span class="mtk1">]</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Now take a look at the above CSS code. The <em>attribute selector</em> is used to target each image individually. </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The first ruleset looks for an <code class="code__2rdF32qjRVp7mMVBHuPwDS">img</code> element with an attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">src</code> that contains the string <code class="code__2rdF32qjRVp7mMVBHuPwDS">'winter'</code>, and sets the <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">50px</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The second ruleset looks for an <code class="code__2rdF32qjRVp7mMVBHuPwDS">img</code> element with an attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">src</code> that contains the string <code class="code__2rdF32qjRVp7mMVBHuPwDS">'summer'</code>, and sets the <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">100px</code>.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice how no new HTML markup (like a class or id) needed to be added, and we were still able to modify the styles of each image independently. This is one advantage to using the attribute selector!</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">To use the attribute selector to select the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;a&gt;</code> element with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute value containing ‘florence’, add the following code to <strong>style.css</strong>:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">a</span><span class="mtk1">[</span><span class="mtk9">href</span><span class="mtk1">*=</span><span class="mtk8">'florence'</span><span class="mtk1">]</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">lightgreen</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice how only the “Learn More” link in the Florence, Italy paragraph changed to light green.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, in <strong>style.css</strong>, use the attribute selector to select the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;a&gt;</code> element that has an <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute value containing <code class="code__2rdF32qjRVp7mMVBHuPwDS">'beijing'</code>. Add a declaration of <code class="code__2rdF32qjRVp7mMVBHuPwDS">color: lightblue;</code> to make the link appear light blue.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Finally, use the attribute selector change the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;a&gt;</code> element that has an <code class="code__2rdF32qjRVp7mMVBHuPwDS">href</code> attribute value containing <code class="code__2rdF32qjRVp7mMVBHuPwDS">'seoul'</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">lightpink</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Pseudo-class




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">You may have observed how the appearance of certain elements can change, or be in a different state, after certain user interactions. For instance:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When you click on an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element, and a blue border is added showing that it is in <em>focus</em>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When you click on a blue <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;a&gt;</code> link to <em>visit</em> to another page, but when you return the link’s text is purple.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When you’re filling out a form and the submit button is grayed out and <em>disabled</em>. But when all of the fields have been filled out, the button has color showing that it’s <em>active</em>.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">These are all examples of pseudo-class selectors in action! In fact, <code class="code__2rdF32qjRVp7mMVBHuPwDS">:focus</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">:visited</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">:disabled</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">:active</code> are all pseudo-classes. Factors such as user interaction, site navigation, and position in the document tree can all give elements a different state with pseudo-class.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">A pseudo-class can be attached to any selector. It is always written as a colon <code class="code__2rdF32qjRVp7mMVBHuPwDS">:</code> followed by a name. For example <code class="code__2rdF32qjRVp7mMVBHuPwDS">p:hover</code>. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9">:</span><span class="mtk4">hover</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">lime</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the above code, whenever the mouse hovers over a paragraph element, that paragraph will have a lime-colored background.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add a ruleset to the end of <strong>style.css</strong> that selects the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;a&gt;</code> elements on the page. Leave the declaration block empty for now.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">:hover</code> pseudo-class to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code> selector you just created.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Lastly, set the text color to dark orange by adding the following CSS declaration inside the declaration block:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">darkorange</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Now when you hover the mouse over the “Learn More” text, the font color changes to dark orange! Neato.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Classes and IDs




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">CSS can select HTML elements by their type, class, and ID. CSS classes and IDs have different purposes, which can affect which one you use to style HTML elements.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">CSS classes are meant to be reused over many elements. By writing CSS classes, you can style elements in a variety of ways by mixing classes.
For instance, imagine a page with two headlines. One headline needs to be bold and blue, and the other needs to be bold and green. Instead of writing separate CSS rules for each headline that repeat each other’s code, it’s better to write a <code class="code__2rdF32qjRVp7mMVBHuPwDS">.bold</code> CSS rule, a <code class="code__2rdF32qjRVp7mMVBHuPwDS">.green</code> CSS rule, and a <code class="code__2rdF32qjRVp7mMVBHuPwDS">.blue</code> CSS rule. Then you can give one headline the <code class="code__2rdF32qjRVp7mMVBHuPwDS">bold green</code> classes, and the other the <code class="code__2rdF32qjRVp7mMVBHuPwDS">bold blue</code> classes.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">While classes are meant to be used many times, an ID is meant to style only one element. As you’ll learn in the next exercise, IDs override the styles of types and classes. Since IDs override these styles, they should be used sparingly and only on elements that need to always appear the same.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">To demonstrate using classes on multiple elements, let’s give a few elements the same style.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>index.html</strong>, there are four <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h2&gt;</code> elements. Give each of them a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">heading-background</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, let’s give a unique style to a single element using ID.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">On line 13 of <strong>index.html</strong>, there’s an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h6&gt;</code> element that displays the time the article on the page was published. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add an id attribute to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h6&gt;</code>, and give it a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">publish-time</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Then, in <strong>style.css</strong>, create a ruleset targeting the new <code class="code__2rdF32qjRVp7mMVBHuPwDS">heading-background</code> class, and give it a declaration of:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">background-color</span><span class="mtk9">: </span><span class="mtk4">aqua</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">After you press Run, notice how all of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h2&gt;</code> elements now have the same style. This <code class="code__2rdF32qjRVp7mMVBHuPwDS">heading-background</code> class can continue to be applied to any element you wish to bestow that amazing style onto.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Finally, in <strong>style.css</strong>, create another ruleset using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">publish-time</code> ID selector. Add the declaration:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">gray</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Since ID’s are single-use, this element now has a unique ID that can’t be used again in this document!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Specificity




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Specificity is the order by which the browser decides which CSS styles will be displayed. A best practice in CSS is to style elements while using the lowest degree of specificity so that if an element needs a new style, it is easy to override.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">IDs are the most specific selector in CSS, followed by classes, and finally, type. For example, consider the following HTML and CSS:</p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;h1</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'headline'</span><span class="mtk4">&gt;</span><span class="mtk1">Breaking News</span><span class="mtk4">&lt;/h1&gt;</span></span><br></div></code></pre></pre>

```html

```

<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">red</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.headline</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">firebrick</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example code above, the color of the heading would be set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">firebrick</code>, as the class selector is more specific than the type selector. If an ID attribute (and selector) were added to the code above, the styles within the ID selector’s body would override all other styles for the heading.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Over time, as files grow with code, many elements may have IDs, which can make CSS difficult to edit since a new, more specific style must be created to change the style of an element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To make styles easy to edit, it’s best to style with a type selector, if possible. If not, add a class selector. If that is not specific enough, then consider using an ID selector.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">To compare type, class, and ID specificity, let’s add a class and ID to an existing element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">On line 12 of <strong>index.html</strong>, there is an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h5&gt;</code> element with the author’s name. Give the element a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">author-class</code> and an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">author-id</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The element now has 3 ways of selecting it, by type, class, and ID. Add the 3 following rulesets to the bottom of <strong>style.css</strong> utilizing each of the selectors:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h5</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">yellow</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.author-class</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">pink</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk1">#author-id</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">cornflowerblue</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Each of these rules selects the same element in a different way. Which style will win the “specificity war”? Click “Run” to find out! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Because ID is the most specific selector, the element will change to cornflower blue. You may have noticed the other <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h5&gt;</code> elements changed to yellow. This is because the most specific (and only) selector they have is their type.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Chaining




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">When writing CSS rules, it’s possible to require an HTML element to have two or more CSS selectors at the same time.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">This is done by combining multiple selectors, which we will refer to as chaining. For instance, if there was a <code class="code__2rdF32qjRVp7mMVBHuPwDS">special</code> class for <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> elements, the CSS would look like below:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk7">.special</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span> </span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code above would select only the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> elements with a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">special</code>. If a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element also had a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">special</code>, the rule in the example would not style the paragraph. </p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s use chaining to select only the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h2&gt;</code> elements with destinations, and add a style to them.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, write a CSS selector for <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h2&gt;</code> elements with a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">.destination</code>. Inside the selector’s curly braces, add this declaration:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">font-family</span><span class="mtk9">: </span><span class="mtk4">Tahoma</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">This will change the font of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h2</code> elements that also have the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">destination</code>. The last <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h2&gt;</code> element (“More Destinations”) will remain unchanged.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Descendant Combinator




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In addition to chaining selectors to select elements, CSS also supports selecting elements that are nested within other HTML elements, also known as <em>descendants</em>. For instance, consider the following HTML:</p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;ul</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'main-list'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;</span><span class="mtk1"> ... </span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;</span><span class="mtk1"> ... </span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;</span><span class="mtk1"> ... </span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk4">&lt;/ul&gt;</span></span><br></div></code></pre></pre>

```html

```

<p class="p__1qg33Igem5pAgn4kPMirjw">The nested <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> elements are descendants of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;ul&gt;</code> element and can be selected with the <em>descendant combinator</em> like so:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.main-list</span><span class="mtk9"> </span><span class="mtk4">li</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span> </span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, <code class="code__2rdF32qjRVp7mMVBHuPwDS">.main-list</code> selects the element with the<code class="code__2rdF32qjRVp7mMVBHuPwDS">.main-list</code> class (the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;ul&gt;</code> element). The descendant <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code>‘s are selected by adding <code class="code__2rdF32qjRVp7mMVBHuPwDS">li</code> to the selector, separated by a space. This results in <code class="code__2rdF32qjRVp7mMVBHuPwDS">.main-list li</code> as the final selector. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Selecting elements in this way can make our selectors even more specific by making sure they appear in the context we expect.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>index.html</strong>, each destination has a paragraph with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">description</code> class below it. Nested within each description paragraph, is an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h5&gt;</code> element with the text “Top Attractions”. They’re a little hard to read since they turned yellow. Let’s fix that!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Navigate to <strong>style.css</strong>. Add a ruleset that uses the descendant combinator to target only the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h5&gt;</code> descendants of elements with the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">.description</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside the curly braces of the selector, add a declaration of:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">blueviolet</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Chaining and Specificity




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In the last exercise, instead of selecting all <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h5&gt;</code> elements, you selected only the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h5&gt;</code> elements nested inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.description</code> elements. This CSS selector was more specific than writing only <code class="code__2rdF32qjRVp7mMVBHuPwDS">h5</code>. Adding more than one tag, class, or ID to a CSS selector increases the specificity of the CSS selector.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For instance, consider the following CSS:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.main</span><span class="mtk9"> </span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">red</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Both of these CSS rules define what a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element should look like. Since <code class="code__2rdF32qjRVp7mMVBHuPwDS">.main p</code> has a class and a <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> type as its selector, only the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> elements inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.main</code> element will appear <code class="code__2rdF32qjRVp7mMVBHuPwDS">red</code>. This occurs despite there being another more general rule that states <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> elements should be <code class="code__2rdF32qjRVp7mMVBHuPwDS">blue</code>.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">To show how specificity increases with additional selectors, let’s create another ruleset with the descendant combinator and then compare it to a ruleset without. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, write a ruleset using the descendant combinator to select the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h4&gt;</code> elements nested in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> elements. Inside of the curly braces, write:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">gold</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Click Run and then scroll down the page to see the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h4&gt;</code> elements under “More Destinations” appear gold.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, create a ruleset targeting elements with just the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h4</code> type, and add a declaration of: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">dodgerblue</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Will the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h4&gt;</code> elements turn blue? Click “Run” to find out.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The elements stay gold because there is a more specific selector for <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h4&gt;</code> elements you wrote in the last step. Because of the more specific CSS selector (<code class="code__2rdF32qjRVp7mMVBHuPwDS">li h4</code>), the more general selector of <code class="code__2rdF32qjRVp7mMVBHuPwDS">h4</code> will not take hold.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Multiple Selectors




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In order to make CSS more concise, it’s possible to add CSS styles to multiple CSS selectors all at once. This prevents writing repetitive code.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For instance, the following code has repetitive style attributes:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> Georgia</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.menu</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> Georgia</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Instead of writing <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family: Georgia</code> twice for two selectors, we can separate the selectors by a comma to apply the same style to both, like this:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk1">,</span><span class="mtk9"> </span></span><br><span><span class="mtk7">.menu</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> Georgia</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">By separating the CSS selectors with a comma, both the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> elements and the elements with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">menu</code> class will receive the <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family: Georgia</code> styling.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, write selectors for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h5&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> elements so they will both be styled with the same CSS rule. Apply this style declaration:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">font-family</span><span class="mtk9">: </span><span class="mtk4">monospace</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice that both the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h5&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> element’s fonts will change, without writing the same CSS declaration twice.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Review




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Throughout this lesson, you learned how to select HTML elements with CSS and apply styles to them. Let’s review what you learned:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">CSS can select HTML elements by type, class, ID, and attribute.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">All elements can be selected using the universal selector.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">An element can have different states using the pseudo-class selector.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Multiple CSS classes can be applied to one HTML element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Classes can be reusable, while IDs can only be used once.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">IDs are more specific than classes, and classes are more specific than type. That means IDs will override any styles from a class, and classes will override any styles from a type selector.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Multiple selectors can be chained together to select an element. This raises the specificity but can be necessary.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Nested elements can be selected by separating selectors with a space.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Multiple unrelated selectors can receive the same styles by separating the selector names with commas.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Great work this lesson. With this knowledge, you’ll be able to use CSS to change the look and feel of websites to make them look great!</p>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Take some time to take in the beauty of the site you just created, and feel free to continue when you’re ready!</p>
</div></div></div>


#### Solutions


```html

```







## VISUAL RULES

### Introduction To Visual Rules




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The purpose of CSS is to add style to web page, and each element on the page can have many style properties. Some of the basic properties relate to the size, style, and color of the element. In this lesson, you’ll learn some fundamental CSS visual rules that you can use to start styling web page elements! </p>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Explore the code to the right. Think about how it relates to the web page on the right side of the browser. </p>
</div></div></div>


#### Solutions


```html

```






### Font Family




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">If you’ve ever used word processing software, like Microsoft Word or Google Docs, chances are that you probably also used a feature that allowed you to change the font you were typing in. Font refers to the technical term <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Typeface">typeface</a>, or <em>font family</em>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To change the typeface of text on your web page, you can use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> Garamond</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the font family for all main heading elements has been set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">Garamond</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">When setting typefaces on a web page, keep the following points in mind:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The font specified must be installed on the user’s computer or downloaded with the site. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="http://www.cssfontstack.com/">Web safe fonts</a> are a group of fonts supported across most browsers and operating systems.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Unless you are using web safe fonts, the font you choose may not appear the same between all browsers and operating systems.  </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When the name of a typeface consists of more than one word, it’s a best practice to enclose the typeface’s name in quotes, like so:</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-family</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">'Courier New'</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">You’ll take a deeper look into typography in a later lesson!</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside <strong>style.css</strong>, set the font family of the main heading (<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code>) and subheading (<code class="code__2rdF32qjRVp7mMVBHuPwDS">h2</code>) to <code class="code__2rdF32qjRVp7mMVBHuPwDS">Georgia</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Note that certain font changes may be hard to recognize at first. Feel free to remove and add the declaration a few times until you notice the change!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, add a style rule that sets the font family of the paragraph (<code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code>) to <code class="code__2rdF32qjRVp7mMVBHuPwDS">Helvetica</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Font Size




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Changing the typeface isn’t the only way to customize the text. Oftentimes, different sections of a web page are highlighted by modifying the <em>font size</em>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To change the size of text on your web page, you can use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-size</code> property.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-size</span><span class="mtk1">:</span><span class="mtk9"> 18px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-size</code> of all paragraphs was set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">18px</code>. <code class="code__2rdF32qjRVp7mMVBHuPwDS">px</code> means pixels, which is one way to measure font size.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-size</code> of paragraph (<code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code>) elements to 18 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Font Weight




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In CSS, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> property controls how bold or thin text appears.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-weight</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">bold</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, all paragraphs on the web page would appear bolded.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> property has another value: <code class="code__2rdF32qjRVp7mMVBHuPwDS">normal</code>. Why does it exist?</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If we wanted <em>all</em> text on a web page to appear bolded, we could select all text elements and change their font weight to <code class="code__2rdF32qjRVp7mMVBHuPwDS">bold</code>. If a certain section of text was required to appear normal, however, we could set the font weight of that particular element to <code class="code__2rdF32qjRVp7mMVBHuPwDS">normal</code>, essentially shutting off bold for that element.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, set the font weight of paragraph (<code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code>) elements to <code class="code__2rdF32qjRVp7mMVBHuPwDS">bold</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Text Align




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">No matter how much styling is applied to text (typeface, size, weight, etc.), the text always appears on the left side of the container in which it resides.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To align text we can use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">text-align</code> property. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">text-align</code> property will align text to the element that holds it, otherwise known as its <em>parent</em>.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">text-align</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">right</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">text-align</code> property can be set to one of the following commonly used values:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">left</code> — aligns text to the left side of its parent element, which in this case is the browser.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> — centers text inside of its parent element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">right</code> — aligns text to the right side of its parent element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">justify</code>— spaces out text in order to align with the right and left side of the parent element.</li>
</ul>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">text-align</code> property of the main heading (<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code>) so that it appears in the center.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Color and Background Color




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Before discussing the specifics of color, it’s important to make two distinctions about color. Color can affect the following design aspects:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Foreground color</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Background color</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Foreground color is the color that an element appears in. For example, when a heading is styled to appear green, the <em>foreground color</em> of the heading has been styled. Conversely, when a heading is styled so that its background appears yellow, the  <em>background color</em> of the heading has been styled.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In CSS, these two design aspects can be styled with the following two properties:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code>: this property styles an element’s foreground color</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code>: this property styles an element’s background color</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">red</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the text of the heading will appear in red, and the background of the heading will appear blue.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Take a look at the caption on the image at the bottom of the page. In <strong>style.css</strong>, set the background color in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.caption</code> selector to <code class="code__2rdF32qjRVp7mMVBHuPwDS">white</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Then, in the same ruleset, set the color of the text to <code class="code__2rdF32qjRVp7mMVBHuPwDS">black</code>. That should make the text a bit easier to read!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Opacity




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Opacity is the measure of how transparent an element is. It’s measured from 0 to 1, with 1 representing 100%, or fully visible and opaque, and 0 representing 0%, or fully invisible.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Opacity can be used to make elements fade into others for a nice overlay effect. To adjust the opacity of an element, the syntax looks like this:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.overlay</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">opacity</span><span class="mtk1">:</span><span class="mtk9"> 0.5</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.overlay</code> element would be 50% visible, letting whatever is positioned behind it show through.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s give the caption on the image some transparency! In <strong>style.css</strong>, set <code class="code__2rdF32qjRVp7mMVBHuPwDS">.caption</code> to have <code class="code__2rdF32qjRVp7mMVBHuPwDS">0.75</code> opacity.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Background Image




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">CSS has the ability to change the background of an element. One option is to make the background of an element an image. This is done through the CSS property <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-image</code>. Its syntax looks like this:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.main-banner</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-image</span><span class="mtk1">:</span><span class="mtk9"> url</span><span class="mtk1">(</span><span class="mtk8">'https://www.example.com/image.jpg'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-image</code> property will set the element’s background to display an image.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The value provided to <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-image</code> is a <code class="code__2rdF32qjRVp7mMVBHuPwDS">url</code>. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">url</code> should be a URL to an image. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">url</code> can be a file within your project, or it can be a link to an external site. To link to an image inside an existing project, you must provide a <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files">relative file path</a>. If there was an image folder in the project, with an image named <code class="code__2rdF32qjRVp7mMVBHuPwDS">mountains.jpg</code>, the relative file path would look like below:</li>
</ol>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.main-banner</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-image</span><span class="mtk1">:</span><span class="mtk9"> url</span><span class="mtk1">(</span><span class="mtk8">'images/mountains.jpg'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, change the background image of the element with the<code class="code__2rdF32qjRVp7mMVBHuPwDS">.image</code> class. The image is stored in the following URL: <code class="code__2rdF32qjRVp7mMVBHuPwDS">https://content.codecademy.com/courses/freelance-1/unit-2/soccer.jpeg</code></p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Important




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw"><code class="code__2rdF32qjRVp7mMVBHuPwDS">!important</code> can be applied to specific declarations, instead of full rules. It will override <em>any</em> style no matter how specific it is. As a result, it should almost never be used. Once <code class="code__2rdF32qjRVp7mMVBHuPwDS">!important</code> is used, it is very hard to override.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The syntax of <code class="code__2rdF32qjRVp7mMVBHuPwDS">!important</code> in CSS looks like this:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk9"> </span><span class="mtk1">!important;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.main</span><span class="mtk9"> </span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">red</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Since <code class="code__2rdF32qjRVp7mMVBHuPwDS">!important</code> is used on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> selector’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> attribute, all <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> elements will appear <code class="code__2rdF32qjRVp7mMVBHuPwDS">blue</code>, even though there is a more specific <code class="code__2rdF32qjRVp7mMVBHuPwDS">.main p</code> selector that sets the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">red</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">One justification for using <code class="code__2rdF32qjRVp7mMVBHuPwDS">!important</code> is when working with multiple stylesheets. For example, if we are using the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://getbootstrap.com/">Bootstrap</a> CSS framework and want to override the styles for one specific HTML element, we can use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">!important</code> property.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Imagine <code class="code__2rdF32qjRVp7mMVBHuPwDS">style-library.css</code> is a stylesheet that is full of good styles! But, you don’t like how it is turning the color of <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> yellow.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In <code class="code__2rdF32qjRVp7mMVBHuPwDS">style.css</code>, add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">!important</code> rule to the color style of inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> ruleset to change the color back to <code class="code__2rdF32qjRVp7mMVBHuPwDS">#FFF</code> (white).</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Review Visual Rules




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Incredible work! You used CSS to alter text and images on a website. Throughout this lesson, you learned concepts including:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property defines the typeface of an element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">font-size</code> controls the size of text displayed.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> defines how thin or thick text is displayed.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">text-align</code> property places text in the left, right, or center of its parent container.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Text can have two different color attributes: <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code>. <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> defines the color of the text, while <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code> defines the color behind the text.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">CSS can make an element transparent with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">opacity</code> property.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">CSS can also set the background of an element to an image with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-image</code> property.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">!important</code> flag will override any style, however it should almost never be used, as it is extremely difficult to override.</li>
</ul>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Feel free to experiment with the code and see what other changes you can make! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you want to see how to incorporate CSS visual rules in a project, watch the video below and follow along with one of our experts:</p>
<div class="youtubeVideoWrapper__1XGg4ywjdSdfygJkAy3bB2" data-testid="yt-iframe" style="padding-bottom: 66.67%;"><iframe width="300" height="200" src="https://www.youtube.com/embed/InA5Ff7mxrc?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen="" class="iframe__rk2yNYIwJeUOj5J8cQJ9-"></iframe></div></div></div></div>


#### Solutions


```html

```








## Documentation: CSS

<div class="gamut-1qd5muv-FlexBox-ExternalResourceContainer e1xk5veq0"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank" class="noUnderline__3auQH9YTaYeT71hkb5qMQq" tabindex="0"><h2 class="gamut-3zfb2u-Anchor-AnchorBase e14vpv2g1">MDN<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="gamut-1nszhsc-Svg eol2zvm0"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M23.251 7.498V.748h-6.75m6.75 0l-15 15m3-10.5h-9a1.5 1.5 0 00-1.5 1.5v15a1.5 1.5 0 001.5 1.5h15a1.5 1.5 0 001.5-1.5v-9"></path></svg></h2></a><div class="gamut-dnk8cz-ExternalResourceMarkdown e1xk5veq1"><p class="p__1qg33Igem5pAgn4kPMirjw">The provided link goes directly to the go-to documentation for CSS (Cascading Style Sheets). This is helpful if you would like a comprehensive resource for understanding the key concepts of CSS and understanding how to debug common CSS problems.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Instead of trying to remember it all, use the documentation as a readily available resource for syntax or implementation help!</p>
</div></div>



<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Incredible work! You used CSS to alter text and images on a website. Throughout this lesson, you learned concepts including:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property defines the typeface of an element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">font-size</code> controls the size of text displayed.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> defines how thin or thick text is displayed.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">text-align</code> property places text in the left, right, or center of its parent container.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Text can have two different color attributes: <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code>. <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> defines the color of the text, while <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code> defines the color behind the text.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">CSS can make an element transparent with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">opacity</code> property.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">CSS can also set the background of an element to an image with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-image</code> property.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">!important</code> flag will override any style, however it should almost never be used, as it is extremely difficult to override.</li>
</ul>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Feel free to experiment with the code and see what other changes you can make! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you want to see how to incorporate CSS visual rules in a project, watch the video below and follow along with one of our experts:</p>
<div class="youtubeVideoWrapper__1XGg4ywjdSdfygJkAy3bB2" data-testid="yt-iframe" style="padding-bottom: 66.67%;"><iframe width="300" height="200" src="https://www.youtube.com/embed/InA5Ff7mxrc?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen="" class="iframe__rk2yNYIwJeUOj5J8cQJ9-"></iframe></div></div></div></div>


#### Solutions


```html

```






## Healthy Recipes




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Using CSS selectors, you’ll give a recipe website some new style!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you get stuck during this project or would like to see an experienced developer work through it, click “<strong>Get Unstuck</strong>“ to see a <strong>project walkthrough video</strong>.</p>
</div>




#### Instructions 


<div class="tasks__2zeiH_BHmhuJBXUlJC3X0R"><span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as complete by checking them off</span><div><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 1" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-1-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-1">1.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Before you begin, take a look at the site’s structure in <strong>index.html</strong>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Start by making the image at the top of the page a little smaller. Navigate to <strong>style.css</strong> and write a CSS selector for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">img</code> tag.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Within its curly braces, write:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">height</span><span class="mtk9">: 150</span><span class="mtk4">px</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Try experimenting with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">150</code> number and observing the results.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 2" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-2-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-2">2.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">The font size of the recipe description should be larger. In <strong>style.css</strong>, write a CSS selector for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.description</code> class.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Within its curly braces, add the following CSS:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">font-size</span><span class="mtk9">: 20</span><span class="mtk4">px</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 3" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-3-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-3">3.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, let’s style the cooking time. The element on line 15 of <strong>index.html</strong> has an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">cook-time</code>. Navigate to <strong>style.css</strong> and add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">cook-time</code> ID selector.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Inside of its curly braces, write:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">font-weight</span><span class="mtk9">: </span><span class="mtk4">bold</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 4" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-4-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-4">4.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, let’s change the bullet points of the ingredient list to squares instead of circles. Start by writing a selector for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">li</code> elements inside of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.ingredients</code> element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then, write this inside of its curly braces:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">list-style</span><span class="mtk9">: </span><span class="mtk4">square</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 5" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-5-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-5">5.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Next let’s make the time for each preparation step appear gray. In <strong>style.css</strong>, write a selector for <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> elements that also have a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">.time</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then, inside of this selector’s curly braces, write:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">gray</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 6" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-6-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-6">6.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">At the bottom of the page, there’s a link to the full recipe. Let’s make the link a different color. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice that in <strong>index.html</strong>, on line 42, there is a <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> element with a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">citation</code>, then an <code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code> element inside of it with a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">external-link</code>. Navigate to <strong>style.css</strong> and write a selector using <code class="code__2rdF32qjRVp7mMVBHuPwDS">external-link</code> class.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then, add this code inside of the selector’s curly braces:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">color</span><span class="mtk9">: </span><span class="mtk4">SeaGreen</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 7" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-7-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-7">7.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Finally, let’s make the font Helvetica instead of the default Times New Roman. Instead of writing multiple selectors to apply the <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> property, write a selector that applies a <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> attribute to all text at once.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The selector should target the  <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">h2</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">li</code> elements.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To change their font, include this line of code inside the curly braces:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">font-family</span><span class="mtk9">: </span><span class="mtk4">Helvetica</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article></div></div>


#### Solutions


```html

```






## Olivia Woodruff Portfolio




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In this project, you’ll use your knowledge of CSS visual rules to create rule sets and improve the appearance of a photography portfolio site!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you get stuck during this project or would like to see an experienced developer work through it, click “<strong>Get Unstuck</strong>“ to see a <strong>project walkthrough video</strong>.</p>
</div>




#### Instructions 


<div class="tasks__2zeiH_BHmhuJBXUlJC3X0R"><span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as complete by checking them off</span><div><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 1" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-1-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-1">1.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Look over <strong>index.html</strong> to review the different HTML elements you have to work with, then navigate to <strong>style.css</strong>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Start by making the header section stand out a bit more. Select the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.header</code> element, and make its background color <code class="code__2rdF32qjRVp7mMVBHuPwDS">CornflowerBlue</code> by using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code> property.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 2" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-2-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-2">2.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now change how the text is aligned in the top <code class="code__2rdF32qjRVp7mMVBHuPwDS">.header</code> section.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In your <code class="code__2rdF32qjRVp7mMVBHuPwDS">.header</code> rule set, align the text in the center using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">text-align</code> property.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 3" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-3-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-3">3.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, use CSS to make the paragraph below Olivia’s name have a larger text size.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, select the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.about-me</code> element, and set its <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-size</code> property to <code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 4" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-4-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-4">4.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.about-me</code> paragraph looks a little dark against the light blue background, maybe it would look nice if it blended more with the background.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Within the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.about-me</code> selector, use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">opacity</code> property to make it 50% transparent.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 5" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-5-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-5">5.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">In the Projects section, make the section titles bold.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Select the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.title</code> elements, and add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> property to make their text bold.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 6" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-6-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-6">6.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Change the main title color so that it matches the background color more nicely. Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> for <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> elements to <code class="code__2rdF32qjRVp7mMVBHuPwDS">Azure</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 7" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-7-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-7">7.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Instead of the page being in the default Times font, change the font of the entire page.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Select the <code class="code__2rdF32qjRVp7mMVBHuPwDS">body</code> element and make the <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-family</code> of the page <code class="code__2rdF32qjRVp7mMVBHuPwDS">Georgia</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 8" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-8-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-8">8.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Finally, let’s make the background of the page more interesting.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Within the <code class="code__2rdF32qjRVp7mMVBHuPwDS">body</code> selector, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-image</code> property to this URL: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="plaintext" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">https://content.codecademy.com/courses/learn-css-s</span><span class="mtk1">electors-visual-rules/hypnotize_bg.png</span></span><br></div></code></pre></pre></div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 9" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-9-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-9">9.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Great work! Feel free to keep coding and edit the visual rules to personalize the site’s appearance!</p>
</div></div></div></article></div></div>


#### Solutions


```html

```





# Learn CSS: The Box Model

## THE BOX MODEL

### Introduction to the Box Model




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Browsers load HTML elements with default position values. This often leads to an unexpected and unwanted user experience while limiting the views you can create. In this lesson, you will learn about the <em>box model</em>, an important concept to understand how elements are positioned and displayed on a website.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you have used HTML and CSS, you have unknowingly seen aspects of the box model. For example, if you have set the background color of an element, you may have noticed that the color was applied not only to the area directly behind the element but also to the area to the right of the element. Also, if you have aligned text, you know it is aligned relative to something. What is that something? </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">All elements on a web page are interpreted by the browser as “living” inside of a box. This is what is meant by the box model.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For example, when you change the background color of an element, you change the background color of its entire box. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson, you’ll learn about the following aspects of the box model:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The dimensions of an element’s box.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The borders of an element’s box.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The paddings of an element’s box.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The margins of an element’s box.</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s begin!</p>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Take some time to explore the code to the right. See if you can figure out how these following CSS properties impact how an element is displayed:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">border</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow</code></li>
</ul>
</div></div></div>


#### Solutions


```html

```






### The Box Model




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The box model comprises the set of properties that define parts of an element that take up space on a web page. The model includes the content area’s size (<em>width</em> and <em>height</em>) and the element’s <em>padding</em>, <em>border</em>, and <em>margin</em>. The properties include: </p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>: The width and height of the content area.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code>: The amount of space between the content area and the border.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">border</code>: The thickness and style of the border surrounding the content area and padding.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin</code>: The amount of space between the border and the outside edge of the element.</li>
</ol>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Take a look at the image on the right—a visual representation of the box model.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can open <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/diagram-boxmodel.svg">the box model image</a> in a new tab to reference it as you move through the lesson.</p>
</div></div></div>


#### Solutions


```html

```






### Height and Width




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">An element’s content has two dimensions: a height and a width. By default, the dimensions of an HTML box are set to hold the raw contents of the box.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The CSS <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> properties can be used to modify these default dimensions.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 80px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 240px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this example, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> of paragraph elements are set to 80 pixels and 240 pixels, respectively — the <code class="code__2rdF32qjRVp7mMVBHuPwDS">px</code> in the code above stands for <em>pixels</em>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Pixels allow you to set the exact size of an element’s box (width and height). When the width and height of an element are set in pixels, it will be the same size on all devices — an element that fills a laptop screen will overflow a mobile screen.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add a height of 700 pixels to <code class="code__2rdF32qjRVp7mMVBHuPwDS">#banner</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Set <code class="code__2rdF32qjRVp7mMVBHuPwDS">.pull-quote</code> width to 350 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#banner .content h1</code> width to 400 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Borders




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">A <em>border</em> is a line that surrounds an element, like a frame around a painting. Borders can be set with a specific <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code>:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code>—The thickness of the border. A border’s thickness can be set in pixels or with one of the following keywords: <code class="code__2rdF32qjRVp7mMVBHuPwDS">thin</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">medium</code>, or <code class="code__2rdF32qjRVp7mMVBHuPwDS">thick</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code>—The design of the border. Web browsers can render any of <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-style#Values">10 different styles</a>. Some of these styles include: <code class="code__2rdF32qjRVp7mMVBHuPwDS">none</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">dotted</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">solid</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code>—The color of the border. Web browsers can render colors using a few different formats, including <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value">140 built-in color keywords</a>.</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 3px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">coral</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the border has a width of 3 pixels, a style of <code class="code__2rdF32qjRVp7mMVBHuPwDS">solid</code>, and a color of <code class="code__2rdF32qjRVp7mMVBHuPwDS">coral</code>. All three properties are set in one line of code. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The default border is <code class="code__2rdF32qjRVp7mMVBHuPwDS">medium none color</code>, where <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> is the current color of the element. If <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code>, or <code class="code__2rdF32qjRVp7mMVBHuPwDS">color</code> are not set in the CSS file, the web browser assigns the default value for that property.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk7">.content-header</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 80px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 240px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">coral</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this example, the border style is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">solid</code> and the color is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">coral</code>. The width is not set, so it defaults to <code class="code__2rdF32qjRVp7mMVBHuPwDS">medium</code>.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add a dotted red border with 1-pixel thickness to all <code class="code__2rdF32qjRVp7mMVBHuPwDS">h2</code> headings.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add a solid, white border, with a 3 pixel width, to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#banner .content h1</code> rule.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Border Radius




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Ever since we revealed the borders of boxes, you may have noticed that the borders highlight the true shape of an element’s box: square. Thanks to CSS, a border doesn’t have to be square.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can modify the corners of an element’s border box with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">border-radius</code> property.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">div</span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 3px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-radius</span><span class="mtk1">:</span><span class="mtk9"> 5px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code in the example above will set <em>all four corners</em> of the border to a radius of 5 pixels (i.e. the same curvature that a circle with a radius of 5 pixels would have).</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can create a border that is a perfect circle by first creating an element with the same width and height, and then setting the radius equal to half the width of the box, which is 50%.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">div</span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 60px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 60px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 3px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border-radius</span><span class="mtk1">:</span><span class="mtk9"> 50%</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code in the example above creates a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code> that is a perfect circle.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, set the border radius of <code class="code__2rdF32qjRVp7mMVBHuPwDS">#banner .content h1</code> to 15 pixels.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Additionally, try experimenting with other border-radius values and running your code to see the result!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Padding




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The space between the contents of a box and the borders of a box is known as <em>padding</em>. Padding is like the space between a picture and the frame surrounding it. In CSS, you can modify this space with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code> property.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk7">.content-header</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 3px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">coral</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 10px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code in this example puts 10 pixels of space between the content of the paragraph (the text) and the borders, on all four sides.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code> property is often used to expand the background color and make the content look less cramped. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you want to be more specific about the amount of padding on each side of a box’s content, you can use the following properties:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding-top</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding-right</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding-bottom</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding-left</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Each property affects the padding on only one side of the box’s content, giving you more flexibility in customization.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk7">.content-header</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 3px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">fuchsia</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding-bottom</span><span class="mtk1">:</span><span class="mtk9"> 10px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, only the bottom side of the paragraph’s content will have a <code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code> of 10 pixels.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In a single line, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.navigation li</code> elements to have 20 pixels of padding. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Click “Run” and observe the changes.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Look at the red boxes at the bottom of the web page. Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.share a</code> elements to have 14 pixels of padding in <strong>style.css</strong> and run your code. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Observe how the red boxes at the bottom of the page changed. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Set the top and bottom padding of <code class="code__2rdF32qjRVp7mMVBHuPwDS">h2</code> elements to 20 pixels and set the left and right padding of <code class="code__2rdF32qjRVp7mMVBHuPwDS">h2</code> elements to 30 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Padding Shorthand




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Another implementation of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code> property lets you specify exactly how much padding there should be on each side of the content in a single declaration. A declaration that uses multiple properties as values is known as a <em>shorthand property</em>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Padding shorthand lets you specify all of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code> properties as values on a single line:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding-top</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding-right</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding-bottom</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding-left</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can specify these properties in a few different ways:</p>
<h6 id="heading-4-values">4 Values</h6>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk7">.content-header</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 6px 11px 4px 9px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the four values <code class="code__2rdF32qjRVp7mMVBHuPwDS">6px 11px 4px 9px</code> correspond to the amount of padding on each side, in a clockwise rotation. In order, it specifies the padding-top value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">6px</code>), the padding-right value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">11px</code>), the padding-bottom value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">4px</code>), and the padding-left value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">9px</code>) of the content. </p>
<h6 id="heading-3-values">3 Values</h6>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk7">.content-header</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 5px 10px 20px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">If the left and right sides of the content can be equal, the padding shorthand property allows for 3 values to be specified.
The first value sets the padding-top value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">5px</code>), the second value sets the padding-left and padding-right values (<code class="code__2rdF32qjRVp7mMVBHuPwDS">10px</code>), and the third value sets the padding-bottom value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code>).</p>
<h6 id="heading-2-values">2 Values</h6>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk7">.content-header</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 5px 10px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">And finally, if the top and bottom sides can be equal, and the left and right sides can be equal, you can specify 2 values. The first value sets the padding-top and padding-bottom values (<code class="code__2rdF32qjRVp7mMVBHuPwDS">5px</code>), and the second value sets the padding-left and padding-right values (<code class="code__2rdF32qjRVp7mMVBHuPwDS">10px</code>).</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Change the individual padding declarations on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h2</code> selector ruleset to use padding shorthand with 2 values.  Keep the padding for the top and bottom at 20 pixels and the value for the left and right padding at 30 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Using two values for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code> property, set the padding of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> element to 10 pixels on the top and bottom and 20 pixels on the left and right.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Margin




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">So far you’ve learned about the following components of the box model: content, borders, and padding. The fourth and final component of the box model is <em>margin</em>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Margin refers to the space directly outside of the box. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">margin</code> property is used to specify the size of this space. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 1px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">aquamarine</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin</span><span class="mtk1">:</span><span class="mtk9"> 20px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code in the example above will place 20 pixels of space on the outside of the paragraph’s box on all four sides. This means that other HTML elements on the page cannot come within 20 pixels of the paragraph’s border.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you want to be even more specific about the amount of margin on each side of a box, you can use the following properties:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-top</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-right</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-bottom</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-left</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Each property affects the margin on only one side of the box, providing more flexibility in customization.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 3px </span><span class="mtk5">solid</span><span class="mtk9"> DarkSlateGrey</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin-right</span><span class="mtk1">:</span><span class="mtk9"> 15px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, only the right side of the paragraph’s box will have a margin of 15 pixels. It’s common to see margin values used for a specific side of an element.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Set the top margin of <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> elements to 60 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Look at the three red boxes at the bottom of the web page. These elements are anchor elements of class <code class="code__2rdF32qjRVp7mMVBHuPwDS">.share</code>. Set these <code class="code__2rdF32qjRVp7mMVBHuPwDS">.share a</code> elements to have a margin of 10 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Margin Shorthand




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">What if you don’t want equal margins on all four sides of the box and don’t have time to separate properties for each side? You’re in luck! Margin can be written as a shorthand property as well. The shorthand syntax for margins is the same as padding, so if you’re feeling comfortable with that, skip to the instructions. Otherwise, read on to learn how to use margin shorthand!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Similar to padding shorthand, <em>margin shorthand</em> lets you specify all of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">margin</code> properties as values on a single line:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-top</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-right</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-bottom</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-left</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can specify these properties in a few different ways:</p>
<h6 id="heading-4-values">4 Values</h6>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin</span><span class="mtk1">:</span><span class="mtk9"> 6px 10px 5px 12px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the four values <code class="code__2rdF32qjRVp7mMVBHuPwDS">6px 10px 5px 12px</code> correspond to the thickness of the margin on each side, in a clockwise rotation. In order, it specifies the margin-top value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">6px</code>), the margin-right value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">10px</code>), the margin-bottom value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">5px</code>), and the margin-left value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">12px</code>) of the content. </p>
<h6 id="heading-3-values">3 Values</h6>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin</span><span class="mtk1">:</span><span class="mtk9"> 5px 12px 4px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">If the left and right sides of the content can be equal, the margin shorthand property allows for 3 values to be specified. The first value sets the margin-top value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">5px</code>), the second value sets the margin-left and margin-right values (<code class="code__2rdF32qjRVp7mMVBHuPwDS">12px</code>), and the third value sets the margin-bottom value (<code class="code__2rdF32qjRVp7mMVBHuPwDS">4px</code>).</p>
<h6 id="heading-2-values">2 Values</h6>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin</span><span class="mtk1">:</span><span class="mtk9"> 20px 10px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">And finally, if the top and bottom sides can be equal, and the left and right sides can be equal, you can specify 2 values. The first value sets the margin-top and margin-bottom values (<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code>), and the second value sets the margin-left and margin-right values (<code class="code__2rdF32qjRVp7mMVBHuPwDS">10px</code>).</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Using two values, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h2</code> top and bottom margins to 30 pixels and the left and right margins to 20 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Auto




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">margin</code> property also lets you center content. However, you must follow a few syntax requirements. Take a look at the following example:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">div</span><span class="mtk7">.headline</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 400px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin</span><span class="mtk1">:</span><span class="mtk9"> 0&nbsp;</span><span class="mtk5">auto</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, <code class="code__2rdF32qjRVp7mMVBHuPwDS">margin: 0 auto;</code> will center the divs in their containing elements. The 0 sets the top and bottom margins to 0 pixels. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">auto</code> value instructs the browser to adjust the left and right margins until the element is centered within its containing element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In order to center an element, a width must be set for that element. Otherwise, the width of the div will be automatically set to the full width of its containing element, like the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code>, for example. It’s not possible to center an element that takes up the full width of the page, since the width of the page can change due to display and/or browser window size.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the width of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code> is set to 400 pixels, which is less than the width of most screens. This will cause the div to center within a containing element that is greater than 400 pixels wide.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Set the width of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.pull-quote</code> class elements to 350 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In one line, set the vertical (top and bottom) margins of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.pull-quote</code> class to <code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code> and the horizontal (left and right) margins to <code class="code__2rdF32qjRVp7mMVBHuPwDS">auto</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Set the vertical margins of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#main</code> element to <code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>, and the horizontal margins to <code class="code__2rdF32qjRVp7mMVBHuPwDS">auto</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Margin Collapse




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">As you have seen, padding is space added inside an element’s border, while margin is space added outside an element’s border. One additional difference is that top and bottom margins, also called vertical margins, <em>collapse</em>, while top and bottom padding does not.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Horizontal margins (left and right), like padding, are always displayed and added together. For example, if two divs with ids <code class="code__2rdF32qjRVp7mMVBHuPwDS">#div-one</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">#div-two</code>, are next to each other, they will be as far apart as the sum of their adjacent margins. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">#img-one</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin-right</span><span class="mtk1">:</span><span class="mtk9"> 20px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk1">#img-two</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin-left</span><span class="mtk1">:</span><span class="mtk9"> 20px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this example, the space between the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#img-one</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">#img-two</code> borders is 40 pixels. The right margin of <code class="code__2rdF32qjRVp7mMVBHuPwDS">#img-one</code> (<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code>) and the left margin of <code class="code__2rdF32qjRVp7mMVBHuPwDS">#img-two</code> (<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code>) add to make a total margin of 40 pixels.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Unlike horizontal margins, vertical margins do not add. Instead, the larger of the two vertical margins sets the distance between adjacent elements.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">#img-one</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin-bottom</span><span class="mtk1">:</span><span class="mtk9"> 30px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk1">#img-two</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin-top</span><span class="mtk1">:</span><span class="mtk9"> 20px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this example, the vertical margin between the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#img-one</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">#img-two</code> elements is 30 pixels. Although the sum of the margins is 50 pixels, the margin collapses so the spacing is only dependent on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#img-one</code> bottom margin.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">It may be helpful to think of collapsing vertical margins as a short person trying to push a taller person. The tall person has longer arms and can easily push the short person, while the person with short arms cannot reach the person with long arms.</p>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Study the graphic display to the right. Elements A and B have 20 pixels of horizontal margin, the sum of each element’s margin. Elements A and C have 30 pixels of vertical margin — the top margin of element C. </p>
</div></div></div>


#### Solutions


```html

```






### Minimum and Maximum Height and Width




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Because a web page can be viewed through displays of differing screen size, the content on the web page can suffer from those changes in size. To avoid this problem, CSS offers two properties that can limit how narrow or how wide an element’s box can be sized to:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code>—this property ensures a minimum width of an element’s box.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code>—this property ensures a maximum width of an element’s box.</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">min-width</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">max-width</span><span class="mtk1">:</span><span class="mtk9"> 600px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the width of all paragraphs will not shrink below 300 pixels, nor will the width exceed 600 pixels.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Content, like text, can become difficult to read when a browser window is narrowed or expanded. These two properties ensure that content is legible by limiting the minimum and maximum widths of an element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can also limit the minimum and maximum <em>height</em> of an element:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">min-height</code> — this property ensures a minimum height for an element’s box.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code> — this property ensures a maximum height of an element’s box.</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">min-height</span><span class="mtk1">:</span><span class="mtk9"> 150px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">max-height</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the height of all paragraphs will not shrink below 150 pixels and the height will not exceed 300 pixels.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">What will happen to the contents of an element’s box if the <code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code> property is set too low? It’s possible for the content to spill outside of the box, resulting in content that is not legible. You’ll learn how to work around this issue in the next exercise.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, set the minimum width of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> element to 200 pixels.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After you’ve done this successfully, resize the browser and notice how the paragraph’s box will no longer shrink below 200 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, set the maximum width of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> element to 800 pixels. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After you’ve done this successfully, resize the browser and notice how the paragraph’s box will no longer expand beyond 800 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, set the minimum height of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> element to 200 pixels.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After you’ve done this successfully, resize the browser and notice how the height of paragraph’s box will no longer shrink below 200 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, set the maximum height of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">p</code> element to 300 pixels.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After you’ve done this successfully, resize the browser and notice how the height of paragraph’s box will no longer expand beyond 300 pixels. You should see your text overflowing. In the next exercise, we will fix that!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Overflow




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">All of the components of the box model comprise an element’s size. For example, an image that has the following dimensions is 364 pixels wide and 244 pixels tall.</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">300 pixels wide</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">200 pixels tall</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">10  pixels padding on the left and right</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">10  pixels padding on the top and bottom</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">2 pixels border on the left and right</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">2 pixels border on the top and bottom</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">20 pixels margin on the left and right</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">10 pixels margin on the top and bottom  </li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">The total dimensions (364px by 244px) are calculated by adding all of the vertical dimensions together and all of the horizontal dimensions together. Sometimes, these components result in an element that is larger than the parent’s containing area. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">How can we ensure that we can view all of an element that is larger than its parent’s containing area? </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow</code> property controls what happens to content that spills, or overflows, outside its box. The most commonly used values are:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">hidden</code>—when set to this value, any content that overflows will be hidden from view. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">scroll</code>—when set to this value, a scrollbar will be added to the element’s box so that the rest of the content can be viewed by scrolling.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">visible</code>—when set to this value, the overflow content will be displayed outside of the containing element. Note, this is the default value.</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">overflow</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">scroll</span><span class="mtk1">;</span><span class="mtk9"> </span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, if any of the paragraph content overflows (perhaps a user resizes their browser window), a scrollbar will appear so that users can view the rest of the content.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The overflow property is set on a parent element to instruct a web browser on how to render child elements. For example, if a div’s overflow property is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">scroll</code>, all children of this div will display overflowing content with a scroll bar. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For a more in-depth look at <code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow</code>, including additional properties like <code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow-x</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow-y</code> that separate out the horizontal and vertical values, head over to the MDN <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow">documentation</a>.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In order to see the impact of <code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow: scroll</code>, first change the height of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#main</code> element to 1000 pixels.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Set the overflow of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#main</code> element to scroll.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">When you scroll down, a second scroll bar should appear over the paragraph section. You may have to expand the browser component in order to see this behavior clearly.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Resetting Defaults




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">All major web browsers have a default stylesheet they use in the absence of an external stylesheet. These default stylesheets are known as <em>user agent stylesheets</em>. In this case, the term <em><a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/User_agent">user agent</a></em> is a technical term for the browser.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">User agent stylesheets often have default CSS rules that set default values for padding and margin. This affects how the browser displays HTML elements, which can make it difficult for a developer to design or style a web page.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Many developers choose to reset these default values so that they can truly work with a clean slate.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin</span><span class="mtk1">:</span><span class="mtk9"> 0</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 0</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code in the example above resets the default margin and padding values of all HTML elements. It is often the first CSS rule in an external stylesheet. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Note that both properties are set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>. When these properties are set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>, they do not require a unit of measurement. </p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, reset the default margin and padding values for the body. What happens to the web page in the browser?</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Visibility




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Elements can be hidden from view with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">visibility</code> property.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">visibility</code> property can be set to one of the following values:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">hidden</code> — hides an element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">visible</code> — displays an element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">collapse</code> — collapses an element.</li>
</ul>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;ul&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;</span><span class="mtk1">Explore</span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;</span><span class="mtk1">Connect</span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"future"</span><span class="mtk4">&gt;</span><span class="mtk1">Donate</span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk4">&lt;/ul&gt;</span></span><br></div></code></pre></pre>

```html

```

<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.future</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">visibility</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">hidden</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the list item with a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">future</code> will be hidden from view in the browser. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Keep in mind, however, that users can still view the contents of the list item (e.g., <code class="code__2rdF32qjRVp7mMVBHuPwDS">Donate</code>) by viewing the source code in their browser. Furthermore, the web page will <em>only</em> hide the contents of the element. It will still leave an empty space where the element is intended to display.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Note:</strong> What’s the difference between <code class="code__2rdF32qjRVp7mMVBHuPwDS">display: none</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">visibility: hidden</code>? An element with <code class="code__2rdF32qjRVp7mMVBHuPwDS">display: none</code> will be completely removed from the web page. An element with <code class="code__2rdF32qjRVp7mMVBHuPwDS">visibility: hidden</code>, however, will not be visible on the web page, but the space reserved for it will. </p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Take a look at the list items in <strong>index.html</strong>. Notice that the list item <code class="code__2rdF32qjRVp7mMVBHuPwDS">Donate</code> has a class of <code class="code__2rdF32qjRVp7mMVBHuPwDS">donate</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add a class selector ruleset for <code class="code__2rdF32qjRVp7mMVBHuPwDS">donate</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the visibility to <code class="code__2rdF32qjRVp7mMVBHuPwDS">hidden</code>.</li>
</ol>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Review




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson, we covered the four properties of the box model: height and width, padding, borders, and margins. Understanding the box model is an important step towards learning more advanced HTML and CSS topics. Let’s take a minute to review what you learned:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The box model comprises a set of properties used to create space around and between HTML elements.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The height and width of a content area can be set in pixels or percentages.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Borders surround the content area and padding of an element. The color, style, and thickness of a border can be set with CSS properties.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Padding is the space between the content area and the border. It can be set in pixels or percent.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Margin is the amount of spacing outside of an element’s border. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Horizontal margins add, so the total space between the borders of adjacent elements is equal to the sum of the right margin of one element and the left margin of the adjacent element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Vertical margins collapse, so the space between vertically adjacent elements is equal to the larger margin.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin: 0 auto</code> horizontally centers an element inside of its parent content area, if it has a width.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow</code> property can be set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">hide</code>, or <code class="code__2rdF32qjRVp7mMVBHuPwDS">scroll</code>, and dictates how HTML will render content that overflows its parent’s content area.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">visibility</code> property can hide or show elements.</li>
</ul>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Make some adjustments to the code in the code editor. See if you can improve the appearance of the page by changing the following properties:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">border</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">margin</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow</code></li>
</ul>
</div></div></div>


#### Solutions


```html

```





## CHANGING THE BOX MODEL

### Why Change the Box Model?




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The last lesson focused on the most important aspects of the box model: box dimensions, borders, padding, and margin. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The box model, however, has an awkward limitation regarding box dimensions. This limitation is best illustrated with an example.</p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">Hello World</span><span class="mtk4">&lt;/h1&gt;</span></span><br></div></code></pre></pre>

```html

```

<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 1px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">black</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 10px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, a heading element’s box has solid, black, 1 pixel thick borders. The height of the box is 200 pixels, while the width of the box is 300 pixels. A padding of 10 pixels has also been set on all four sides of the box’s content.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Unfortunately, under the current box model, the border thickness and the padding will affect the dimensions of the box.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The 10 pixels of padding increases the height of the box to 220 pixels and the width to 320 pixels. Next, the 1-pixel thick border increases the height to 222 pixels and the width to 322 pixels. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Under this box model, the border thickness and padding are added to the overall dimensions of the box. This makes it difficult to accurately size a box. Over time, this can also make all of a web page’s content difficult to position and manage.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this brief lesson, you’ll learn how to use a different technique that avoids this problem altogether.</p>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">We’ll be using the app provided to demonstrate how to work with the box model. Click “Next” to continue. </p>
</div></div></div>


#### Solutions


```html

```






### Box Model: Content-Box




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Many properties in CSS have a default value and don’t have to be explicitly set in the stylesheet. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For example, the default <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code> of text is <code class="code__2rdF32qjRVp7mMVBHuPwDS">normal</code>, but this property-value pair is not typically specified in a stylesheet. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The same can be said about the box model that browsers assume. In CSS, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">box-sizing</code> property controls the type of box model the browser should use when interpreting a web page. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The default value of this property is <code class="code__2rdF32qjRVp7mMVBHuPwDS">content-box</code>. This is the same box model that is affected by border thickness and padding.</p>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Study the diagram to the right. It illustrates the default box model used by the browser, <code class="code__2rdF32qjRVp7mMVBHuPwDS">content-box</code>. When you’re done, continue to the next exercise.</p>
</div></div></div>


#### Solutions


```html

```






### Box Model: Border-Box




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Fortunately, we can reset the entire box model and specify a new one: <code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code>. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">box-sizing</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">border-box</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code in the example above resets the box model to <code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code> for all HTML elements. This new box model avoids the dimensional issues that exist in the former box model you learned about.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this box model, the height and width of the box will remain fixed. The border thickness and padding will be included inside of the box, which means the overall dimensions of the box do not change.</p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">Hello World</span><span class="mtk4">&lt;/h1&gt;</span></span><br></div></code></pre></pre>

```html

```

<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">box-sizing</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">border-box</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">border</span><span class="mtk1">:</span><span class="mtk9"> 1px </span><span class="mtk5">solid</span><span class="mtk9"> </span><span class="mtk12">black</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">padding</span><span class="mtk1">:</span><span class="mtk9"> 10px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the height of the box would remain at 200 pixels and the width would remain at 300 pixels. The border thickness and padding would remain entirely <em>inside</em> of the box.</p>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Study the diagram to the right. It illustrates the new box model, <code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code>. Pay attention to how the total width (<code class="code__2rdF32qjRVp7mMVBHuPwDS">200px</code>) and the padding affect the inner width of the element. </p>
</div></div></div>


#### Solutions


```html

```






### The New Box Model




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now that you know about the new box model, let’s actually implement it in the browser. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">*</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">box-sizing</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">border-box</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">It’s that simple! In the example above, the universal selector (<code class="code__2rdF32qjRVp7mMVBHuPwDS">*</code>) targets all elements on the web page and sets their box model to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code> model.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, change the box model for all elements on the web page to the new box model.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">You probably didn’t see a difference in the web page to the right - that’s ok! The new box model simply makes sure that the dimensions of elements remains the same regardless of border width and padding.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div></div></div>


#### Solutions


```html

```






### Review: Changing the Box Model




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson, you learned about an important limitation of the default box model: box dimensions are affected by border thickness and padding.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s review what you learned:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">In the default box model, box dimensions are affected by border thickness and padding.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">box-sizing</code> property controls the box model used by the browser.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The default value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">box-sizing</code> property is <code class="code__2rdF32qjRVp7mMVBHuPwDS">content-box</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The value for the new box model is <code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code>. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">border-box</code> model is not affected by border thickness or padding.</li>
</ol>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Take some time to experiment with your new knowledge of the box model in <strong>style.css</strong>. When you’re done, proceed to the next unit.</p>
</div></div></div>


#### Solutions


```html

```







## The Box Model in DevTools




<div data-testid="markdown" class="spacing-loose__3_R8mSIQ2cspwhDGkCOXTu markdown__1eeYJ4WPKUcvX_LDDGJR12 darkTheme__2i0sjr_RjoITRh35Ld2GzM gamut-gk1onf-ArticleMarkdown e1xfx7rd0"><h2 id="heading-introduction" class="h2__1Ly_Sza5xVS3yZl46_StcN">Introduction</h2>
<p class="p__1qg33Igem5pAgn4kPMirjw">All HTML elements are boxes made up of four components: a content container, padding, border, and margin. In our <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-css/lessons/box-model-intro/exercises/box-model-intro">Box Model lesson</a> we introduce these four properties and use them to position elements on a website. If you have not taken this lesson, we recommend you do so now, before continuing.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this article, we will introduce how Google Chrome’s DevTools can be used to view the box around each element on a web page.</p>
<h4 id="heading-1-view-box-model-dimensions-with-devtools" class="h4__1cJx3E4QhkKjfWj3jLsTFU">1. View Box Model Dimensions with DevTools</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can use Google Chrome’s DevTools to view the box around every element on a web page. There are a few different ways to open DevTools, depending on your platform:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Mac</strong></p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><kbd>command</kbd> + <kbd>option</kbd> + i</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">View &gt; Developer &gt; Developer Tools </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Chrome 3 dot menu ⋮ &gt; More Tools &gt; Developer Tools</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Windows</strong></p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><kbd>control</kbd> + <kbd>shift</kbd> + i</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><kbd>F12</kbd></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Chrome 3 dot menu ⋮ &gt; More Tools &gt; Developer Tools</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Use whichever method works best for you. When you have the DevTools open, navigate to the <strong>Elements</strong> tab.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://content.codecademy.com/courses/freelance-1/unit-4/img-elements.jpg" alt="Elements Tab" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this tab you can view all of the elements on the current page. From this view, you can select the element of interest, which will open a new column on the right side of DevTools. Select the tab labeled <strong>Computed</strong> on the top of the rightmost column.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Box-Model-in-DevTools/DevToolsTabs.png" alt="Computed Tab" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The selected element’s box should appear at the top of the pane. Hovering over each property of the box will cause the property to be highlighted in the web page.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you know the element you want to inspect, going through all of the steps listed above is unnecessary. Instead, you can right click the element you want to observe and select the Inspect button. This will display DevTools on the right side of the browser with the element selected in the Elements tab. To view the element’s box, you can select the Computed tab.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you’d like some more info or a refresher on how to use Google Dev Tools, take a look at <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://youtu.be/VuQ4pF_hfag">this video</a>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Exercise I: View a Website’s Box Model Dimensions</strong></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Complete the following steps within the current web browser view.</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">In a new tab navigate to the Codecademy <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Codecademy">Wikipedia</a> page.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Right click (or <code class="code__2rdF32qjRVp7mMVBHuPwDS">Ctrl</code> and click simultaneously) the Contents navigation box displayed in the image below:</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://content.codecademy.com/courses/freelance-1/unit-4/img-inspect.jpg" alt="Dropdown image" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Select <strong>Inspect</strong>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Select the Computed tab at the top of the rightmost column.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Hover over the different properties of the logo’s box. The corresponding space on the web page should be highlighted when you do this.</li>
</ol>
<h4 id="heading-2-modify-box-dimensions" class="h4__1cJx3E4QhkKjfWj3jLsTFU">2. Modify Box Dimensions</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">Now that you know how to view the box of an element we’ll modify the box’s values with DevTools.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To modify the values of the box double click the property value, assign it a new number, and press enter. You can also adjust the value incrementally by double clicking the value and using the up or down arrow keys.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://content.codecademy.com/courses/freelance-1/unit-4/img-boxmodel.jpg" alt="Selecting Values" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the image above, the border on each side is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code> and the padding is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">7</code>. These values can be changed by double clicking the values in the box and assigning them new numbers, or using the up or down arrow keys on your keyboard.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Note:</strong> If you inspect an element and find that the border is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">-</code>, adding a numerical value will not make a border appear. The border color, style, and width must be set in the CSS document in order to see the border.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Exercise II: Modify a Website’s Box Model Dimensions</strong></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Pick up where you left off in Exercise 1. </p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Double click the top padding of the element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Use the up and down arrows to adjust the element’s padding. Observe how the appearance changes on the web page.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the left margin to 200. Observe how the element’s appearance changes.</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Remember</strong> the changes you make in DevTools are not saved. If you are using DevTools to make adjustments to a personal project, make sure to adjust values in the HTML and CSS documents.</p>
</div>







## The Box Model in DevTools




<iframe frameborder="0" allowfullscreen="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" title="The Box Model in Chrome DevTools" width="100%" height="100%" src="https://www.youtube.com/embed/uQi8TK-GDO4?autoplay=0&amp;mute=0&amp;controls=1&amp;origin=https%3A%2F%2Fwww.codecademy.com&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;iv_load_policy=3&amp;modestbranding=1&amp;enablejsapi=1&amp;widgetid=1" id="widget2" data-gtm-yt-inspected-76="true"></iframe>







## The Box Model: Davie's Burgers




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In this project, you will follow step-by-step instructions to fix a fictional restaurant’s website. All of the HTML and most of the CSS is intact, but the box model properties have yet to be set. You’ll use knowledge of <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">border</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">margin</code> to complete this project.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The website’s existing <strong>index.html</strong> and <strong>style.css</strong> files are displayed in the text editor to the right. As you work, use both to see which elements you are selecting and styling. Most of the elements that you’ll need to add styles for already have rule sets in <strong>style.css</strong> to which you can add additional declarations. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you get stuck during this project or would like to see an experienced developer work through it, click “<strong>Get Unstuck</strong>“ to see a <strong>project walkthrough video</strong>.</p>
</div>




#### Instructions 


<div class="tasks__2zeiH_BHmhuJBXUlJC3X0R"><span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as complete by checking them off</span><div><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 1" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-1-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-1">1.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">You’ll go through Davie’s Burger’s menu item roughly from top to bottom. Let’s begin with styling the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;nav&gt;</code> element containing the logo and navigation elements.</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the width of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">img</code> to 180 pixels.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Center the <code class="code__2rdF32qjRVp7mMVBHuPwDS">img</code> horizontally using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">margin</code> property.</li>
</ul>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 2" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-2-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-2">2.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Set margin of <code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> elements inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nav</code> to 10 pixels on the top and bottom, and 0 pixels on the left and right.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 3" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-3-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-3">3.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now set some rules for the element with the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">content</code>. This element is a container for all the elements not included in <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;nav&gt;</code>.</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the height to 500 pixels.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Create 10-pixel vertical margins and automatic horizontal margins.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set <code class="code__2rdF32qjRVp7mMVBHuPwDS">.body</code> elements inside <code class="code__2rdF32qjRVp7mMVBHuPwDS">.content</code> to have no vertical margin and automatic horizontal margins so that it is centered.</li>
</ul>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 4" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-4-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-4">4.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">With a 500-pixel height for <code class="code__2rdF32qjRVp7mMVBHuPwDS">.content</code>, some elements will overflow out of its box if the browser window is made too small. </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Make <code class="code__2rdF32qjRVp7mMVBHuPwDS">.content</code> scrollable with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow</code> property.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Resize the browser window so it is very skinny and notice that this section is now scrollable.</li>
</ul>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 5" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-5-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-5">5.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now it’s time to tackle the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.header</code> and its <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> text: ‘BBQ BACON BURGER’.</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the height of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.header</code> class to 320 pixels.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Create a 20-pixel padding for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> element inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.header</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set vertical margins to 0 pixels and the horizontal margins to be determined automatically for the same <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> element.</li>
</ul>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 6" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-6-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-6">6.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now add some box-model formatting to the ‘ORDER NOW’ <code class="code__2rdF32qjRVp7mMVBHuPwDS">.button</code> element. As you make each change, make sure to scroll down if necessary to view the effect on the button.</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the width to 200 pixels.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the padding to 20 pixels.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the vertical margins to 40 pixels and the horizontal margins to automatic.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Give the button a 1-pixel, solid, blue border.</li>
</ul>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 7" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-7-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-7">7.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Finally, style the nutrition facts section at the bottom. In the element selected with <code class="code__2rdF32qjRVp7mMVBHuPwDS">ul.nutrition</code>:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the padding of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">ul.nutrition</code> element to 20 pixels.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the width of <code class="code__2rdF32qjRVp7mMVBHuPwDS">li</code> elements within the <code class="code__2rdF32qjRVp7mMVBHuPwDS">ul.nutrition</code> to 200 pixels.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set a 10-pixel vertical padding and 20-pixel horizontal padding to the same elements.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add a 3-pixel bottom margin to the same elements.</li>
</ul>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 8" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-8-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-8">8.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Good job—this menu item is looking great, and the layout and spacing is much more readable. If you’d like, you can continue refining the design or add your own spin!</p>
</div></div></div></article></div></div>


#### Solutions


```html

```






## DISPLAY AND POSITIONING

### Flow of HTML




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">A browser will render the elements of an HTML document that has no CSS from left to right, top to bottom, in the same order as they exist in the document. This is called the <em>flow</em> of elements in HTML.  </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In addition to the properties that it provides to style HTML elements, CSS includes properties that change how a browser <em>positions</em> elements.  These properties specify where an element is located on a page, if the element can share lines with other elements, and other related attributes. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson, you will learn five properties for adjusting the position of HTML elements in the browser: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">clear</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Each of these properties will allow us to position and view elements on a web page. They can be used in conjunction with any other styling properties you may know.</p>
</div>






### Position




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Take a look at the <em>block-level</em> elements in the image below:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Display-Position/Position-updated.png" alt="Diagram of block-level elements" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Block-level elements like these boxes create a <em>block</em> the full width of their parent elements, and they prevent other elements from appearing in the same horizontal space.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice the block-level elements in the image above take up their own line of space and therefore don’t overlap each other. In the browser to the right, you can see block-level elements also consistently appear on the left side of the browser. This is the default <em>position</em> for block-level elements.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The default position of an element can be changed by setting its <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> property. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> property can take one of five values:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">static</code> - the default value (it does not need to be specified)</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">relative</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">absolute</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">fixed</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">sticky</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the next few exercises, you’ll learn about the values in the list above. For now, it’s important to understand that if you favor the default position of an HTML element, you don’t need to set its <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> property.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, add a declaration to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.question</code> ruleset that sets the position to static.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice that setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">static</code> does nothing. That’s because <code class="code__2rdF32qjRVp7mMVBHuPwDS">static</code> simply refers to the default behavior.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Position: Relative




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">One way to modify the default position of an element is by setting its <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> property to <code class="code__2rdF32qjRVp7mMVBHuPwDS">relative</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">This value allows you to position an element <em>relative</em> to its default static position on the web page. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.green-box</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">green</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">relative</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Although the code in the example above instructs the browser to expect a relative positioning of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.green-box</code> element, it does not specify where the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.green-box</code> element should be positioned on the page. This is done by accompanying the <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> declaration with one or more of the following <em>offset properties</em> that will move the element away from its default static position:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">top</code> - moves the element down from the top.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">bottom</code> - moves the element up from the bottom.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">left</code> - moves the element away from the left side (to the right).</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">right</code> - moves the element away from the right side (to the left).</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can specify values in pixels, ems, or percentages, among others, to dial in exactly how far you need the element to move. It’s also important to note that offset properties will not work if the element’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> property is the default <code class="code__2rdF32qjRVp7mMVBHuPwDS">static</code>.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.green-box</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">green</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">relative</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">top</span><span class="mtk1">:</span><span class="mtk9"> 50px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">left</span><span class="mtk1">:</span><span class="mtk9"> 120px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the element of <code class="code__2rdF32qjRVp7mMVBHuPwDS">green-box</code> class will be moved down 50 pixels, and to the right 120 pixels, from its default static position. The image below displays the new position of the box.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Display-Position/Relative.png" alt="Diagram of an element with relative position" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Offsetting the relative element will not affect the positioning of other elements. </p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.question</code> ruleset, change the <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> property to <code class="code__2rdF32qjRVp7mMVBHuPwDS">relative</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, in <strong>style.css</strong>, offset <code class="code__2rdF32qjRVp7mMVBHuPwDS">.question</code> 40 pixels from the top.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Position: Absolute




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Another way of modifying the position of an element is by setting its position to <code class="code__2rdF32qjRVp7mMVBHuPwDS">absolute</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">When an element’s position is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">absolute</code>, all other elements on the page will ignore the element and act like it is not present on the page. The element will be positioned relative to its closest positioned parent element, while offset properties can be used to determine the final position from there. Take a look at the image below:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Display-Position/position-absolute.png" alt="Diagram of an element with absolute position, as described in the following paragraph" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The “This website is in progress. Please come back later!” text is displaced from its static position at the top left corner of its parent container. It has offset property declarations of <code class="code__2rdF32qjRVp7mMVBHuPwDS">top: 300px;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">right: 0px;</code>, positioning it 300 pixels down, and 0 pixels from the right side of the page.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> inside of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">header</code> ruleset to <code class="code__2rdF32qjRVp7mMVBHuPwDS">absolute</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice how it’s now removed from the normal flow of the document, and covering the welcome section.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">When you changed the position to absolute, you may have noticed that the header shrunk horizontally.  We’ll learn why in a later exercise.  For now, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> property of the header to <code class="code__2rdF32qjRVp7mMVBHuPwDS">100%</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Position: Fixed




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">When an element’s position is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">absolute</code>, as in the last exercise, the element will scroll with the rest of the document when a user scrolls.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">We can <em>fix</em> an element to a specific position on the page (regardless of user scrolling) by setting its position to <code class="code__2rdF32qjRVp7mMVBHuPwDS">fixed</code>, and accompanying it with the familiar offset properties <code class="code__2rdF32qjRVp7mMVBHuPwDS">top</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">bottom</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">left</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">right</code>.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.title</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">fixed</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">top</span><span class="mtk1">:</span><span class="mtk9"> 0px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">left</span><span class="mtk1">:</span><span class="mtk9"> 0px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.title</code> element will remain fixed to its position no matter where the user scrolls on the page, like in the image below:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Display-Position/Fixed.gif" alt="Diagram of position fixed" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">This technique is often used for navigation bars on a web page.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, change the <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> property inside of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">header</code> rule to <code class="code__2rdF32qjRVp7mMVBHuPwDS">fixed</code>. Scroll up and down the web page. What do you notice?</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Notice that part of the “Welcome” section is now covered up by the header. That’s because when we changed the position of the header to fixed, we removed it from the flow of the html document. Let’s fix that. Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.welcome</code> element to <code class="code__2rdF32qjRVp7mMVBHuPwDS">relative</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Offset the “Welcome” section by 200 pixels from the top. Everything might not be displaying correctly just yet; we’ll fix it in a later exercise.  </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Position: Sticky




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Since <code class="code__2rdF32qjRVp7mMVBHuPwDS">static</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">relative</code> positioned elements stay in the normal flow of the document, when a user scrolls the page (or parent element) these elements will scroll too. And since <code class="code__2rdF32qjRVp7mMVBHuPwDS">fixed</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">absolute</code> positioned elements are removed from the document flow, when a user scrolls, these elements will stay at their specified offset position. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">sticky</code> value is another position value that keeps an element in the document flow as the user scrolls, but <em>sticks</em> to a specified position as the page is scrolled further. This is done by using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">sticky</code> value along with the familiar offset properties, as well as one new one. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.box-bottom</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">darkgreen</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> sticky</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">top</span><span class="mtk1">:</span><span class="mtk9"> 240px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.box-bottom</code> <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code> will remain in its relative position, and scroll as usual. When it reaches 240 pixels from the top, it will stick to that position until it reaches the bottom of its parent container where it will “unstick” and rejoin the flow of the document.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Display-Position/Sticky.gif" alt="Diagram of an element with sticky position" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside <strong>style.css</strong>, change the position of the elements with the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">question</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">sticky</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Z-Index




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">When boxes on a web page have a combination of different positions, the boxes (and therefore, their content) can overlap with each other, making the content difficult to read or consume.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.blue-box</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.green-box</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">green</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">relative</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">top</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">-</span><span class="mtk9">170px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">left</span><span class="mtk1">:</span><span class="mtk9"> 170px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.green-box</code> element overlaps on top of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.blue-box</code> element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> property controls how far back or how far forward an element should appear on the web page when elements overlap. This can be thought of as the <em>depth</em> of elements, with deeper elements appearing behind shallower elements.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> property accepts integer values. Depending on their values, the integers instruct the browser on the order in which elements should be layered on the web page.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.blue-box</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">blue</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">relative</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">z-index</span><span class="mtk1">:</span><span class="mtk9"> 1</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.green-box</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">green</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">relative</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">top</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">-</span><span class="mtk9">170px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">left</span><span class="mtk1">:</span><span class="mtk9"> 170px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, we set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.blue-box</code> position to <code class="code__2rdF32qjRVp7mMVBHuPwDS">relative</code> and the z-index to 1. We changed position to <code class="code__2rdF32qjRVp7mMVBHuPwDS">relative</code>, because the <code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> property does <em>not</em> work on static elements. The z-index of <code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code> moves the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.blue-box</code> element forward, because the <code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> value has not been explicitly specified for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.green-box</code> element, which means it has a default <code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> value of 0. Take a look at the example image below:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Display-Position/Z-index.png" alt="Diagram of z-index" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>style.css</strong>, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">header</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">10</code>. Notice how the header is no longer covered by other elements when you scroll! </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Inline Display




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Every HTML element has a default <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> value that dictates if it can share horizontal space with other elements. Some elements fill the entire browser from left to right regardless of the size of their content. Other elements only take up as much horizontal space as their content requires and can be directly next to other elements.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson, we’ll cover three values for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property: <code class="code__2rdF32qjRVp7mMVBHuPwDS">inline</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">block</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-block</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The default <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> for some elements, such as <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;em&gt;</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;strong&gt;</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;a&gt;</code>, is called <em>inline</em>. Inline elements have a box that wraps tightly around their content, only taking up the amount of space necessary to display their content and not requiring a new line after each element. The height and width of these elements cannot be specified in the CSS document. For example, the text of an anchor tag (<code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;a&gt;</code>) will, by default, be displayed on the same line as the surrounding text, and it will only be as wide as necessary to contain its content. <code class="code__2rdF32qjRVp7mMVBHuPwDS">inline</code> elements cannot be altered in size with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> or <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> CSS properties.</p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">To learn more about </span><span class="mtk4">&lt;em&gt;</span><span class="mtk1">inline</span><span class="mtk4">&lt;/em&gt;</span><span class="mtk1"> elements, read </span><span class="mtk4">&lt;a</span><span class="mtk1"> </span><span class="mtk7">href</span><span class="mtk1">=</span><span class="mtk8">"#"</span><span class="mtk4">&gt;</span><span class="mtk1">MDN documentation</span><span class="mtk4">&lt;/a&gt;</span><span class="mtk1">.&nbsp;&nbsp;&nbsp;</span></span><br></div></code></pre></pre>

```html

```

<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;em&gt;</code> element is <code class="code__2rdF32qjRVp7mMVBHuPwDS">inline</code>, because it displays its content on the same line as the content surrounding it, including the anchor tag. This example will display:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To learn more about <em>inline</em> elements, read <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements">MDN documentation</a>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The CSS <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property provides the ability to make any element an inline element. This includes elements that are not inline by default such as paragraphs, divs, and headings.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">inline</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The CSS in the example above will change the display of all <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> elements to <code class="code__2rdF32qjRVp7mMVBHuPwDS">inline</code>. The browser will render <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> elements on the same line as other inline elements immediately before or after them (if there are any).</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>index.html</strong>, add opening and closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;strong&gt;&lt;/strong&gt;</code> tags around the word “Welcome”. Notice that the element does not move. That’s because <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;strong&gt;</code> elements are inline, so they can share lines with other elements. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Display: Block




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Some elements are not displayed in the same line as the content around them. These are called <em>block-level</em> elements. These elements fill the entire width of the page by default, but their <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> property can also be set. Unless otherwise specified, they are the height necessary to accommodate their content. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Elements that are block-level by default include all levels of heading elements (<code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> through <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h6&gt;</code>), <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;footer&gt;</code>.  For a complete list of block level elements, visit <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements">the MDN documentation</a>.  </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">strong</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">block</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, all <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;strong&gt;</code> elements will be displayed on their own line, with no content directly on either side of them even though their contents may not fill the width of most computer screens.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>index.html</strong>, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;footer&gt;</code> element at the bottom of the document, right above the closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;/body&gt;</code> tag.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Nothing changed! That’s because the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;footer&gt;</code> element is empty.  Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h3&gt;</code> element inside of the footer that says “Thanks for taking our survey!” </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">To improve the appearance of the web page, set the height of the footer to 100 pixels in <strong>style.css</strong>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Display: Inline-Block




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The third value for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property is <code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-block</code>. Inline-block display combines features of both inline and block elements. Inline-block elements can appear next to each other and we can specify their dimensions using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> properties. Images are the best example of default inline-block elements.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For example, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code>s below will be displayed on the same line and with the specified dimensions:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Display-Position/display-inline-block.png" alt="inline block example" class="img__1JGFO2nlisObc3KeOSGPRp"> </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s take a look at the code:</p>


<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"rectangle"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">I’m a&nbsp;rectangle!</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"rectangle"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">So am I!</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"rectangle"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">Me three!</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>

```html

```

<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.rectangle</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">inline-block</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">There are three rectangular divs that each contain a paragraph of text. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.rectangle</code> <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code>s will all appear inline (provided there is enough space from left to right) with a width of 200 pixels and height of 300 pixels, even though the text inside of them may not require 200 pixels by 300 pixels of space.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s fix the display of the list elements in the menu at the top of the page.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property of <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> elements to <code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-block</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Set the width of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">li</code> elements to 80 pixels. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, we can reduce the top offset of the “Welcome” section. Set it to 50 pixels. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property of <code class="code__2rdF32qjRVp7mMVBHuPwDS">.answer</code> elements to <code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-block</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Float




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">So far, you’ve learned how to specify the exact position of an element using offset properties. If you’re simply interested in moving an element as far left or as far right as possible in the container, you can use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code> property. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code> property is commonly used for wrapping text around an image. Note, however, that moving elements left or right for layout purposes is better suited for tools like CSS grid and flexbox, which you’ll learn about later on.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code> property is often set using one of the values below:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">left</code> - moves, or floats, elements as far left as possible.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">right</code> - moves elements as far right as possible.</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.green-section</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 50%</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 150px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.orange-section</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-color</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">orange</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 50%</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">float</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">right</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, we float the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.orange-section</code> element to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">right</code>. This works for static and relative positioned elements. See the result of the code below:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://static-assets.codecademy.com/Courses/Learn-CSS/Display-Position/Float.png" alt="Diagrm of an element floating on the right" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Floated elements must have a width specified, as in the example above. Otherwise, the element will assume the full width of its containing element, and changing the float value will not yield any visible results.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add a declaration to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.answer</code> ruleset that sets the <code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code> property to <code class="code__2rdF32qjRVp7mMVBHuPwDS">left</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Clear




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code> property can also be used to float multiple elements at once. However, when multiple floated elements have different heights, it can affect their layout on the page. Specifically, elements can “bump” into each other and not allow other elements to properly move to the left or right.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">clear</code> property specifies how elements should behave when they bump into each other on the page. It can take on one of the following values:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">left</code>—the left side of the element will not touch any other element within the same containing element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">right</code>—the right side of the element will not touch any other element within the same containing element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">both</code>—neither side of the element will touch any other element within the same containing element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">none</code>—the element can touch either side.</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">div</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">float</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">left</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">div</span><span class="mtk7">.special</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">clear</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">left</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, all <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code>s on the page are floated to the left side. The element with class <code class="code__2rdF32qjRVp7mMVBHuPwDS">special</code> did not move all the way to the left because a taller <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code> blocked its positioning. By setting its <code class="code__2rdF32qjRVp7mMVBHuPwDS">clear</code> property to <code class="code__2rdF32qjRVp7mMVBHuPwDS">left</code>, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">special</code> <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code> will be moved all the way to the left side of the page.</p>
</div>




#### Instructions 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Take a look at the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.answer</code> divs on the web page. They have been floated to the left, but the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.question</code> divs are touching the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.answer</code> divs on the right, let’s fix this.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.question</code> selector, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">clear</code> property to <code class="code__2rdF32qjRVp7mMVBHuPwDS">left</code>. Notice how the questions moved.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">On second thought, this layout is not looking so good. Remove the <code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code> property from <code class="code__2rdF32qjRVp7mMVBHuPwDS">.answer</code> selector ruleset.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


#### Solutions


```html

```






### Review: Layout




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Great job! In this lesson, you learned how to control the positioning of elements on a web page.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s review what you’ve learned so far:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> property allows you to specify the position of an element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">relative</code>, an element’s position is relative to its default position on the page.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">absolute</code>, an element’s position is relative to its closest positioned parent element. It can be pinned to any part of the web page, but the element will still move with the rest of the document when the page is scrolled.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">fixed</code>, an element’s position can be pinned to any part of the web page. The element will remain in view no matter what.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">sticky</code>, an element can stick to a defined offset position when the user scrolls its parent container.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> of an element specifies how far back or how far forward an element appears on the page when it overlaps other elements.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property allows you to control how an element flows vertically and horizontally in a document.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">inline</code> elements take up as little space as possible, and they cannot have manually adjusted <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> or <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">block</code> elements take up the width of their container and can have manually adjusted <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>s.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-block</code> elements can have set <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>, but they can also appear next to each other and do not take up their entire container width.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code> property can move elements as far left or as far right as possible on a web page.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">You can clear an element’s left or right side (or both) using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">clear</code> property.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">When combined with an understanding of the box model, positioning can create visually appealing web pages. So far, we’ve focused on adding content in the form of text to a web page. In the next unit, you’ll learn how to add and manipulate images to a web page.</p>
</div>




#### Instructions 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Take some time to experiment with your new knowledge of positioning in <strong>style.css</strong>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">When you’re done, proceed to the next unit.</p>
</div></div></div>


#### Solutions


```html

```







## Broadway




<div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In this project, you will use properties such as <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> to improve the layout of the landing page for a fictional design firm, Broadway Design.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The site has some style rules to begin with. You will improve the layout and positioning of the navigation menu at the top of the page and the three supporting sections (Design, Develop, Deploy) below the image.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you get stuck during this project or would like to see an experienced developer work through it, click “<strong>Get Unstuck</strong>“ to see a <strong>project walkthrough video</strong>.</p>
</div>




#### Instructions 


<div class="tasks__2zeiH_BHmhuJBXUlJC3X0R"><span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as complete by checking them off</span><div><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 1" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-1-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-1">1.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;header&gt;</code> currently scrolls with the rest of the document.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Set its <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> property so that it stays stuck to the top of the window when the document is scrolled.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 2" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-2-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-2">2.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;header&gt;</code> has shrunk!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Change the width of the same element so that it stretches across its entire parent element. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 3" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-3-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-3">3.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">List items (<code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code>) inside of the navigation section (<code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;nav&gt;</code>) are currently displayed as a list.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Set their <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property so that they can appear next to each other horizontally (but so that you still set their <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> in the next task).</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 4" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-4-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-4">4.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Set the width of the same elements to 80 pixels. </p>
</div></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 5" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-5-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-5">5.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">After changing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;header&gt;</code> element to <code class="code__2rdF32qjRVp7mMVBHuPwDS">fixed</code>, the contents of the entire site after it shifted upwards.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">position</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;main&gt;</code> so that we can position it relatively.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 6" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-6-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-6">6.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;header&gt;</code> has disappeared behind the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;main&gt;</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> to make the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;header&gt;</code> visible. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 7" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-7-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-7">7.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now the navigation bar looks good, but it is blocking the title at the top of the page. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Offset <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;main&gt;</code> by 80 pixels from the top.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 8" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-8-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-8">8.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, fix up the supporting element style below the image.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add a declaration to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.supporting .col</code> rule set so that these elements can appear horizontally next to each other but have defined <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 9" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-9-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-9">9.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Inspect the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.supporting .col</code> elements—they don’t seem to be flowing horizontally yet because they have no set <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code>. Set the width and height of <code class="code__2rdF32qjRVp7mMVBHuPwDS">.supporting .col</code> elements to 200 pixels. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 10" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-10-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-10">10.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Great work, the Broadway Design site looks much better! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you want to continue coding, challenge yourself to make the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;footer&gt;</code> element also fixed to the bottom of the page regardless of scrolling.</p>
</div></div></div></article></div></div>


#### Solutions


```html

```







## Review: Fundamentals of CSS


### Review: Fundamentals of CSS

<div data-testid="markdown" class="spacing-loose__3_R8mSIQ2cspwhDGkCOXTu markdown__1eeYJ4WPKUcvX_LDDGJR12 darkTheme__2i0sjr_RjoITRh35Ld2GzM gamut-gk1onf-ArticleMarkdown e1xfx7rd0"><p class="p__1qg33Igem5pAgn4kPMirjw">Congratulations! The goal of this unit was to get an introduction to CSS, one of the languages essential to developing websites. You learned how to apply styles to HTML documents using CSS.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Having completed this unit, you are now able to:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Understand how CSS is used for web development</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Use CSS to add initial styling to your website</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Understand the Box Model in CSS</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add positioning using CSS</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Read CSS documentation</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you are interested in learning more about these topics, here are some additional resources:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Book: <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://bookshop.org/books/html-and-css-design-and-build-websites/9781118008188">HTML &amp; CSS</a>, Jon Duckett, Chapters 10 (pp. 226-244), 13 (pp. 300-328), and 15 (pp. 358-404)</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Learning is social. Whatever you’re working on, be sure to connect with the Codecademy community in the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/">forums</a>. Remember to check in with the community regularly, including for things like asking for code reviews on your project work and providing code reviews to others in the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/c/project/1833">projects category</a>, which can help to reinforce what you’ve learned.</p>
</div>



