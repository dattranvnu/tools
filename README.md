---
output:
  md_document:
    variant: markdown_github
---

## Introduction: Building Interactive Websites




<div data-testid="markdown" class="spacing-loose__3_R8mSIQ2cspwhDGkCOXTu markdown__1eeYJ4WPKUcvX_LDDGJR12 darkTheme__2i0sjr_RjoITRh35Ld2GzM gamut-gk1onf-ArticleMarkdown e1xfx7rd0"><p class="p__1qg33Igem5pAgn4kPMirjw">The goal of this unit is to learn how JavaScript is used to add interactive experiences to a website. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After this unit, you will be able to:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add JavaScript to a website for interactivity</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Describe what the DOM is</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Explain what DOM Events are</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Create forms using HTML and validate them using JavaScript</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">You will put all of this knowledge into practice with an upcoming Portfolio Project. You can complete the Portfolio Project either in parallel with or after taking the prerequisite content — it’s up to you! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Whatever you’re working on, be sure to connect with the Codecademy community in the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/">forums</a>. Remember to check in with the community regularly, including for things like code review on your project work and what material you will need to accomplish your goals.</p>
</div>




## THE SCRIPT ELEMENT

### JavaScript and HTML




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Script Element</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">JavaScript and HTML</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">HTML defines the structure of a web page by using page elements as the building blocks. However, HTML by itself can not produce web page interactivity, that’s where JavaScript comes in.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Below, we see a post-it with a typical stick figure on it. We can think of this as the HTML, with the head, body, and limbs as the elements on the page:</p>
<img src="https://content.codecademy.com/courses/script/Javascript_stick_figure.png" class="img__1JGFO2nlisObc3KeOSGPRp">


<p class="p__1qg33Igem5pAgn4kPMirjw">In web development, CSS provides the style to our HTML structure. Below, the stick figure is now dressed in a nice tuxedo:</p>
<img src="https://content.codecademy.com/courses/script/Javascript_stick_figure_2.png" class="img__1JGFO2nlisObc3KeOSGPRp">


<p class="p__1qg33Igem5pAgn4kPMirjw">If HTML and CSS provide structure and style in this analogy, JavaScript provides interactivity, allowing our stick figure to move. Below, the stick figure moves, swaying up and down, thanks to JavaScript:</p>
<img src="https://content.codecademy.com/courses/script/stick_figure_v2.gif" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">Web programmers use JavaScript to make web pages dynamic and interactive. This powerful scripting language is encapsulated in its own HTML element: the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element. You can think of this <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element as the door to JavaScript for HTML. This lesson will dig deeper into what the  <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element can do for your websites and best practices on how and where to insert JavaScript in your HTML files.</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">In the diagram to the right, we display HTML as the architecture of a web page, or the house structure. The script tag serves as the door opener connecting JavaScript to the HTML file.</p>
</div></div></div>


**Solutions**


```html

```




## THE SCRIPT ELEMENT

### The <script> tag




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Script Element</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">The &lt;script&gt; tag</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element allows you to add JavaScript code inside an HTML file. Below, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element embeds valid JavaScript code:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">This is an embedded JS example</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk4">&lt;script&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">function</span><span class="mtk1"> </span><span class="mtk4">Hello()</span><span class="mtk1"> </span><span class="mtk4">{</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;alert </span><span class="mtk4">(</span><span class="mtk8">'Hello World'</span><span class="mtk4">);</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">}</span></span><br><span><span class="mtk4">&lt;/script&gt;</span></span><br></div></code></pre></pre>


<p class="p__1qg33Igem5pAgn4kPMirjw">Frankly, without the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> tag, websites would be unclickable and a bit boring.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element, like most elements in <em>HTML</em>, has an opening and closing angle bracket. The closing tag marks the end of the content inside of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element. Just like the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;style&gt;</code> tag used to <em>embed</em> CSS code, you use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> tag to <em>embed</em> valid JavaScript code.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Copy this JavaScript code and paste it between the opening and closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> tags. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">function blooming</span><span class="mtk1">() {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">var image</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">getElementById</span><span class="mtk1">(</span><span class="mtk8">'myImage'</span><span class="mtk1">);</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk12">if</span><span class="mtk1"> (</span><span class="mtk9">image</span><span class="mtk1">.</span><span class="mtk10">src</span><span class="mtk1">.</span><span class="mtk10">match</span><span class="mtk1">(</span><span class="mtk8">"normal"</span><span class="mtk1">)) {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">image</span><span class="mtk1">.</span><span class="mtk10">src</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">"flower.png"</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;} </span><span class="mtk12">else</span><span class="mtk1"> {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">image</span><span class="mtk1">.</span><span class="mtk10">src</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">"normal.png"</span><span class="mtk1">;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;}&nbsp;&nbsp;&nbsp;&nbsp;</span></span><br><span><span class="mtk1">}&nbsp;&nbsp;&nbsp;&nbsp;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then, click <strong>Run</strong> when you are finished and click on the Codecademy logo. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div></div></div>


**Solutions**


```html

```




## THE SCRIPT ELEMENT

### The src attribute




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Script Element</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">The src attribute</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Since you know how to use a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element with embedded code, let’s talk about linking code. Linking code is preferable because of a programming concept called Separation of Concerns (SoC). Instead of having messy code that is all in the same file, web developers separate their code into different files, making each “concern” easier to understand and more convenient when changes must be made. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For this exercise, instead of writing JavaScript in our HTML file, we are going to write it in its own file, and then reference this code with a <em>file path name</em>. We will do this using an attribute that may jog your memory: the <code class="code__2rdF32qjRVp7mMVBHuPwDS">src</code> attribute!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If this seems familiar, that’s because you may have been linking to external files with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;img&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;link&gt;</code> elements. The attribute is exactly the same, but now its value specifies the location of your script file.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If the file is in the same project folder, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">src</code> value will be a <em>relative path</em> name. Below is an example of providing a relative path for a JavaScript file. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;script </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">"./exampleScript.js"</span><span class="mtk4">&gt;&lt;/script&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> above would look for a file called <strong>exampleScript.js</strong> that is in the same folder/directory as our <strong>index.html</strong> file.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you must refer to JavaScript hosted externally, or in a <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Glossary/CDN">CDN</a>, you can also link to that file location. </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">src</code> attribute that points to <strong>script.js</strong>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, click on the Codecademy logo repeatedly to see random font families and font colors. The source attribute allows our HTML file to access all of this magical JavaScript with little code.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Once you have clicked the Codecademy logo several times, click <strong>Run</strong> to move on to the next exercise.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div></div></div>


**Solutions**


```html

```




## THE SCRIPT ELEMENT

### How are scripts loaded?




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Script Element</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">How are scripts loaded?</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">A quick recap: the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element allows HTML files to load and execute JavaScript. The JavaScript can either go embedded inside of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> tag or the script tag can reference an external file. Before we dive deeper, let’s take a moment to talk about how browsers parse HTML files into web pages. This informs where to include a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element inside your HTML file.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Browsers come equipped with <em>HTML parsers</em> that help browsers render the elements accordingly. Elements, including the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element, are by default, parsed in the order they appear in the HTML file. When the <em>HTML parser</em> encounters a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element, it loads the script then executes its contents before parsing the rest of the HTML. The two main points to note here are that:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <em>HTML parser</em> does NOT process the next element in the HTML file until it loads and executes the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element, thus leading to a delay in load time and resulting in a poor user experience.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Additionally, scripts are loaded sequentially, so if one script depends on another script, they should be placed in that very order inside the HTML file.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">The GIF below displays two scripts being loaded. The first script makes a <code class="code__2rdF32qjRVp7mMVBHuPwDS">Watering Can</code> appear, the second script makes a <code class="code__2rdF32qjRVp7mMVBHuPwDS">Flower</code> appear. This shows how scripts are loaded sequentially, and how they pause the <em>HTML parser</em>, which is why “Blooming” appears at the end. 
<img src="https://content.codecademy.com/courses/script/ScriptNoAttribute.gif" alt="Image showing a flower bloom" width="400" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Oops! In the code editor <strong>script2.js</strong> depends on a variable in <strong>script1.js</strong> causing an error (we actually want our text to be blue instead of pink). Switch the order of the scripts so that they load appropriately. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## THE SCRIPT ELEMENT

### Defer attribute




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Script Element</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Defer attribute</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">When the HTML parser comes across a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element, it stops to load its content. Once loaded, the JavaScript code is executed and the HTML parser proceeds to parse the next element in the file. This can result in a slow load time for your website. HTML4 introduced the defer and async attributes of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element to address the user wait-time in the website based on different scenarios. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <em>defer attribute</em> specifies scripts should be executed after the HTML file is completely parsed. When the HTML parser encounters a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">defer</code> attribute, it loads the script but defers the actual execution of the JavaScript until after it finishes parsing the rest of the elements in the HTML file.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Here is an example of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">defer</code> tag:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;script</span><span class="mtk1"> </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">"example.js"</span><span class="mtk1"> </span><span class="mtk7">defer</span><span class="mtk4">&gt;&lt;/script&gt;</span><span class="mtk1"> </span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">When is <code class="code__2rdF32qjRVp7mMVBHuPwDS">defer</code> useful?</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">When a script contains functionality that requires interaction with the DOM, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">defer</code> attribute is the way to go. This way, it ensures that the entire HTML file has been parsed before the script is executed. </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">We want the “Codecademy” to be blue, not yellow! Each script tag re-styles the Codecademy logo, but the <strong>turnYellow.js</strong> executes last, making the font color <code class="code__2rdF32qjRVp7mMVBHuPwDS">'yellow'</code>. Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">defer</code> attribute to the <strong>turnBlue.js</strong> script to make it the last script that is downloaded and executed. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## THE SCRIPT ELEMENT

### Async attribute




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Script Element</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Async attribute</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">async</code> attribute loads and executes the script asynchronously with the rest of the webpage. This means that, similar to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">defer</code> attribute, the HTML parser will continue parsing the rest of the HTML as the script is downloaded in the background. However, with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">async</code> attribute, the script will not wait until the entire page is parsed: it will execute immediately after it has been downloaded. Here is an example of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">async</code> tag:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;script</span><span class="mtk1"> </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">"example.js"</span><span class="mtk1"> </span><span class="mtk7">async</span><span class="mtk4">&gt;&lt;/script&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">When is it useful?</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><code class="code__2rdF32qjRVp7mMVBHuPwDS">async</code> is useful for scripts that are independent of other scripts in order to function accordingly. Thus, if it does not matter exactly at which point the script file is executed, asynchronous loading is the most suitable option as it optimizes web page load time. </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Currently our text is pink because in our <strong>style.css</strong> file, we have a ruleset for that. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add <code class="code__2rdF32qjRVp7mMVBHuPwDS">async</code> attribute to the <strong>turnBlue.js</strong> script to optimize load speed. Notice that once the <strong>turnBlue.js</strong> script is loaded, the text turns blue! </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## THE SCRIPT ELEMENT

### Review




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Script Element</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Review</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s review. </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><p class="p__1qg33Igem5pAgn4kPMirjw">HTML creates the skeleton of a webpage, but JavaScript introduces interactivity</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> element has an opening and closing tag. You can embed JavaScript code inbetween the opening and closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> tags. </p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><p class="p__1qg33Igem5pAgn4kPMirjw">You link to external JavaScript files with the <strong>src</strong> attribute in the opening <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;script&gt;</code> tag.</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><p class="p__1qg33Igem5pAgn4kPMirjw">By default, scripts are loaded and executed as soon as the HTML parser encounters them in the HTML file, the HTML parser waits to load the entire script before from proceeding to parse the rest of the page elements. </p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">defer</code> attribute ensures that the entire HTML file has been parsed before the script is executed. </p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">async</code> attribute will allow the <em>HTML parser</em> to continue parsing as the script is being downloaded, but will execute immediately after it has been downloaded. </p>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">The old convention was to put scripts right before the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;/body&gt;</code> tag to prevent the script from blocking the rest of the HTML content. Now, the convention is to put the script tag in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;head&gt;</code> element and to use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">defer</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">async</code> attributes.</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Congratulations on completing this lesson!</p>
</div></div></div>


**Solutions**


```html

```




## What is the DOM?




<iframe frameborder="0" allowfullscreen="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" title="What is the DOM?" width="100%" height="100%" src="https://www.youtube.com/embed/kd8zX-66FS0?autoplay=0&amp;mute=0&amp;controls=1&amp;origin=https%3A%2F%2Fwww.codecademy.com&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;iv_load_policy=3&amp;modestbranding=1&amp;enablejsapi=1&amp;widgetid=1" id="widget2" data-gtm-yt-inspected-76="true"></iframe>




## THE DOCUMENT OBJECT MODEL

### What is the DOM?




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Document Object Model</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">What is the DOM?</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The <em>Document Object Model</em>, abbreviated DOM, is a powerful tree-like structure that allows programmers to conceptualize hierarchy and access the elements on a web page. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The DOM is one of the better-named acronyms in the field of Web Development. In fact, a useful way to understand what DOM does is by breaking down the acronym but out of order:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <em>DOM</em> is a logical tree-like <strong>M</strong>odel that organizes a web page’s HTML <strong>D</strong>ocument as an <strong>O</strong>bject.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">The DOM is implemented by browsers to allow JavaScript to access, modify, and update the structure of an HTML web page in an organized way.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For this reason, we like to think of the DOM as the link between an HTML web page and scripting languages. </p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">The diagram to the right illustrates how an HTML document is modeled as a tree-like structure accessed by scripting languages like Javascript.</p>
</div></div></div>


**Solutions**


```html

```




## THE DOCUMENT OBJECT MODEL

### The DOM as a Tree Structure




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Document Object Model</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">The DOM as a Tree Structure</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Tree-like modeling is used in many fields, including evolutionary science and data analytics. Perhaps you’re already familiar with the concept of family trees: these charts represent the familial relationships amongst the descendants of a given family name.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The DOM tree follows similar logic to that of a family tree. A family tree is made up of family members and their relationships to the family name. In computer science, we would call each family member a node.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">We define a <em>node</em> as an intersecting point in a tree that contains data. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the DOM tree, the top-most node is called the <em>root node</em>, and it represents the HTML document. The descendants of the root node are the HTML tags in the document, starting with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;html&gt;</code> tag followed by the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;head&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> tags and so on.</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">The diagram to the right models the HTML document and labels the root element, which is the document.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Observe the difference in the rectangular boxes and the curved boxes. These denote a difference in the types of nodes in the DOM structure.</p>
</div></div></div>


**Solutions**


```html

```




## THE DOCUMENT OBJECT MODEL

### Parent Child Relationships in the DOM




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Document Object Model</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Parent Child Relationships in the DOM</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Following the metaphor of a family tree, let’s define some key terminology in the DOM hierarchy:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">A <em>parent node</em> is any node that is a direct ancestor of another node.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">A <em>child node</em> is a direct descendant of another node, called the parent node. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Knowing these terms will allow you to understand and discuss the DOM as a tree-like structure. In fact, you will also see this terminology used when referring to the nesting structure of HTML code. Programmers refer to elements nested inside other elements as the children elements and parent elements respectively.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add the appropriate HTML elements to the <strong>index.html</strong> file so that it reflects the tree-diagram on the far right. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Start by adding the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;title&gt;</code> element. Make sure to nest the tags correctly, so that the nodes follow the illustrated parent-child relationships.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code> element to <strong>index.html</strong> so that it reflects the DOM diagram to the right.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## THE DOCUMENT OBJECT MODEL

### Nodes and Elements in the DOM




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Document Object Model</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Nodes and Elements in the DOM</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">As mentioned, a node is the equivalent of each family member in a family tree. A node is an intersecting point in a tree that also contains data.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">There are multiple types of node objects in the DOM tree. In our diagram, the node objects with the sharp-edge rectangles are <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Element"><em>Element</em></a> nodes, while the rounded edge rectangles are <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Text"><em>Text</em></a> nodes, because they represent the text inside the HTML paragraph elements.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">When trying to modify a web page, the script will mostly interact with the DOM element nodes and occasionally text nodes.</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">In the diagram to the right, the DOM element nodes are highlighted red.  These correspond to elements in the HTML document. Move on to the next exercise when you’re ready!</p>
</div></div></div>


**Solutions**


```html

```




## THE DOCUMENT OBJECT MODEL

### Attributes of Element Node




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Document Object Model</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0"> Attributes of Element Node</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">DOM element nodes model elements in an HTML document.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Much like an element in an HTML page, the DOM allows us to access a node’s attributes, such as its <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code>, and inline <code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the diagram to the right, we have highlighted the paragraph element with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">'bio'</code> in the HTML document. If we were accessing that element node in our script, the DOM would allow us to tweak each of those attributes, or simply access them to check their value in the code.</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">After studying the diagram on the right, feel free to click on to the next exercise.</p>
</div></div></div>


**Solutions**


```html

```




## THE DOCUMENT OBJECT MODEL

### Review




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">The Document Object Model</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Review</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Congratulations on completing our introduction to the Document Object Model, or DOM, as a structure!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s review what you’ve learned so far:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The DOM is a structural model of a web page that allows for scripting languages to access that page.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The system of organization in the DOM mimics the nesting structure of an HTML document. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Elements nested within another are referred to as the children of that element. The element they are nested within is called the parent element of those elements.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The DOM also allows access to the attributes of an HTML element such as <code class="code__2rdF32qjRVp7mMVBHuPwDS">style</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code>, etc.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">With this understanding, you can begin to leverage the power of scripting languages to create, update, and maintain web pages! </p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Click next when you are ready to move on to the last exercise!</p>
</div></div></div>


**Solutions**


```html

```




## JAVASCRIPT AND THE DOM

### The Document Keyword




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">JavaScript and the DOM</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">The Document Keyword</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The <em>Document Object Model</em>, abbreviated DOM, is a powerful tree-like structure that organizes the elements on a web page and allows scripting languages to access them. This lesson will focus on some of the most useful methods and properties of the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model">DOM interface</a> in JavaScript. This interface is implemented by every modern browser.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">First things first! The <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> object in JavaScript is the door to the DOM structure. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> object allows you to access the root node of the DOM tree. Before you can access a specific element in the page, first you must access the document structure itself. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> object allows scripts to access children of the DOM as properties.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For example, if you want to access the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element from your script, you can access it as a property of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> object by using <code class="code__2rdF32qjRVp7mMVBHuPwDS">document.body</code>. This property will return the body element of that DOM. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Similarly, you could access the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;title&gt;</code> element with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.title</code> property. 
Here is a <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Document">comprehensive list</a> of all <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> properties.</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">The diagram to the right illustrates that the <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> keyword points to the root node of the Document Object Model (DOM). The <code class="code__2rdF32qjRVp7mMVBHuPwDS">document.body</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">document.head</code> properties act as though you were directly accessing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">html</code> DOM element. Click “Next” when you’re ready!</p>
</div></div></div>


**Solutions**


```html

```




## JAVASCRIPT AND THE DOM

### Tweak an Element




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">JavaScript and the DOM</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Tweak an Element</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">When using the DOM in your script to access an HTML element, whether it’s an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> element or the entire <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element, you also have access to all of that element’s properties.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">This includes the ability to modify the contents of the element as well as its attributes and properties, which can range from modifying the text inside a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element to assigning a new background color to a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;div&gt;</code>. For example, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.innerHTML</code> property allows you to access and set the contents of an element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s take a look at how we can reassign the contents of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element to the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">'The cat loves the dog'</code>:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">body</span><span class="mtk1">.</span><span class="mtk10">innerHTML</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'The cat loves the dog.'</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.innerHTML</code> property can also add any valid HTML elements. The following example replaces the contents of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element by assigning an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h2&gt;</code> element as a child inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">body</span><span class="mtk1">.</span><span class="mtk10">innerHTML</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'&lt;h2&gt;This is a&nbsp;heading&lt;/h2&gt;'</span><span class="mtk1">; </span></span><br></div></code></pre></pre>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.innerHTML</code> property to modify the content of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element to display an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> heading with the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">'This is now the heading of the body element'</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice how the previous content inside of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element has been replaced!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## JAVASCRIPT AND THE DOM

### Select and Modify Elements




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">JavaScript and the DOM</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Select and Modify Elements</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In the previous exercise, we accessed the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> keyword!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">What if we wanted to select a specific element besides the entire <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element? The DOM interface allows us to access a specific element with CSS selectors.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><em>CSS selectors</em> define the elements to which a set of CSS rules apply, but we can also use these same selectors to access DOM elements with JavaScript! Selectors can include a tag name, a class, or an ID.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.querySelector()</code> method allows us to specify a CSS selector as a string and returns the first element that matches that selector. The following code would return the first paragraph in the document.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">querySelector</span><span class="mtk1">(</span><span class="mtk8">'p'</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Along with <code class="code__2rdF32qjRVp7mMVBHuPwDS">.querySelector()</code>, JavaScript has more targeted methods that select elements based on their class, id, or tag name.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">For example, if you want to access an element directly by its <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code>, you can use the aptly named <code class="code__2rdF32qjRVp7mMVBHuPwDS">.getElementById()</code> method:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">getElementById</span><span class="mtk1">(</span><span class="mtk8">'bio'</span><span class="mtk1">).</span><span class="mtk10">innerHTML</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'The description'</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this example, we’ve selected the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">'bio'</code> and set its <code class="code__2rdF32qjRVp7mMVBHuPwDS">.innerHTML</code> to the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">'The description'</code>. Notice that the ID is passed as a string, wrapped in quotation marks (<code class="code__2rdF32qjRVp7mMVBHuPwDS">' '</code>).</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">There are also the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.getElementsByClassName()</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">.getElementsByTagName()</code> methods which return an array of elements, instead of just one element. You can use bracket notation to access individual elements of an array:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk16">// Set first element of .student class as 'Not yet</span><span class="mtk16"> registered'</span></span><br><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">getElementsByClassName</span><span class="mtk1">(</span><span class="mtk8">'student'</span><span class="mtk1">)[</span><span class="mtk9">0</span><span class="mtk1">].</span><span class="mtk10">innerHTML</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Not yet registered'</span><span class="mtk1">;</span></span><br><span><span> </span></span><br><span><span class="mtk16">// Set second &lt;li&gt; tag as 'Cedric Diggory'</span></span><br><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">getElementsByTagName</span><span class="mtk1">(</span><span class="mtk8">'li'</span><span class="mtk1">)[</span><span class="mtk9">1</span><span class="mtk1">].</span><span class="mtk10">innerHTML</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Cedric Diggory`;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the above example code, the first element with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">'student'</code> class and the second <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> element have had their inner HTML changed.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.querySelector()</code> method to select the first <code class="code__2rdF32qjRVp7mMVBHuPwDS">'h1'</code> element.
Access that element’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">.innerHTML</code> property to change the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> title to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'Most popular Harry Potter characters'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.getElementById()</code> method to access the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">'fourth'</code>. Set that element’s inner HTML to read <code class="code__2rdF32qjRVp7mMVBHuPwDS">'Professor Snape'</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.getElementsByClassName()</code> method to access the first element with the class name of <code class="code__2rdF32qjRVp7mMVBHuPwDS">'slytherin'</code>. Replace that element’s inner HTML with the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">'Salazar Slytherin'</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.getElementsByTagName()</code> method to access the first element with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> tag. Access that element’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">.innerHTML</code> to replace the content to read <code class="code__2rdF32qjRVp7mMVBHuPwDS">'Dobby'</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 5 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## JAVASCRIPT AND THE DOM

### Style an Element




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">JavaScript and the DOM</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Style an Element</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Another way to modify an element is by changing its CSS style. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.style</code> property of a DOM element provides access to the inline style of that HTML tag.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The syntax follows an <code class="code__2rdF32qjRVp7mMVBHuPwDS">element.style.property</code> format, with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">property</code> representing a CSS property. For example, the following code selects the first element with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">blue</code> and assigns blue as the <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code>:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let blueElement</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">querySelector</span><span class="mtk1">(</span><span class="mtk8">'.blue'</span><span class="mtk1">);</span></span><br><span><span class="mtk9">blueElement</span><span class="mtk1">.</span><span class="mtk10">style</span><span class="mtk1">.</span><span class="mtk10">backgroundColor</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'blue'</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Unlike CSS, the DOM <code class="code__2rdF32qjRVp7mMVBHuPwDS">.style</code> property does not implement a hyphen such as <code class="code__2rdF32qjRVp7mMVBHuPwDS">background-color</code>, but rather camel case notation, <code class="code__2rdF32qjRVp7mMVBHuPwDS">backgroundColor</code>. Check out this <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference">MDN reference page</a> to see a list of how CSS properties are converted into JavaScript. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The following <em>chaining</em> syntax would also work:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">querySelector</span><span class="mtk1">(</span><span class="mtk8">'.blue'</span><span class="mtk1">).</span><span class="mtk10">style</span><span class="mtk1">.</span><span class="mtk10">fontFamily</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'Roboto'</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Style the <code class="code__2rdF32qjRVp7mMVBHuPwDS">backgroundColor</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> element in the blog post to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'#201F2E'</code> to match the Codecademy text editor.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, change the font family of the element with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">heading</code> class to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'Roboto'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## JAVASCRIPT AND THE DOM

### Traversing the DOM




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">JavaScript and the DOM</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Traversing the DOM</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s recap the parent and children relationship in the DOM hierarchy. A <em>parent node</em> is any node that is a direct ancestor of another node. A <em>child node</em> is a direct descendant of another node, called the parent node.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">These relationships follow the nested structure of the HTML code. Elements nested within one HTML element are children of that parent element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Each element has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">.parentNode</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">.children</code> property. The <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Node/parentNode"><code class="code__2rdF32qjRVp7mMVBHuPwDS">.parentNode</code> property</a> returns the parent of the specified element in the DOM hierarchy. Note that the <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> element is the <em>root node</em> so its <code class="code__2rdF32qjRVp7mMVBHuPwDS">.parentNode</code> property will return <code class="code__2rdF32qjRVp7mMVBHuPwDS">null</code>. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.children</code> property returns an array of the specified element’s children. If the element does not have any children, it will return <code class="code__2rdF32qjRVp7mMVBHuPwDS">null</code>.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;ul</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">'groceries'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">'must-have'</span><span class="mtk4">&gt;</span><span class="mtk1">Toilet Paper</span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;</span><span class="mtk1">Apples</span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;</span><span class="mtk1">Chocolate</span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;li&gt;</span><span class="mtk1">Dumplings</span><span class="mtk4">&lt;/li&gt;</span></span><br><span><span class="mtk4">&lt;/ul&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the HTML code above, we have an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;ul&gt;</code> element with the ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">groceries</code> with four <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> elements inside. </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let parentElement</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">getElementById</span><span class="mtk1">(</span><span class="mtk8">'must-have'</span><span class="mtk1">).</span><span class="mtk10">parentNode</span><span class="mtk1">; </span><span class="mtk16">// returns &lt;ul&gt; element</span></span><br><span><span class="mtk12">let childElements</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">getElementById</span><span class="mtk1">(</span><span class="mtk8">'groceries'</span><span class="mtk1">).</span><span class="mtk10">children</span><span class="mtk1">; </span><span class="mtk16">// returns an array of &lt;li&gt; elements</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Here, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">parentElement</code> variable stores the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.parentNode</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> element with the ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">must-have</code>, which will be the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;ul&gt;</code> element with the ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">groceries</code>. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">childElements</code> variable is set to the children of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;ul&gt;</code> element with the ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">groceries</code>, which will be an array of four <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> elements. </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">First, create a variable called <code class="code__2rdF32qjRVp7mMVBHuPwDS">first</code> and set it to the first child of the document body.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then, set the inner HTML of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">first</code> element to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'BROWN BEARS ARE AWESOME!'</code>. Take a moment to note which element has been modified.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.parentNode</code> property to access the parent element of the variable <code class="code__2rdF32qjRVp7mMVBHuPwDS">first</code> and modify its <code class="code__2rdF32qjRVp7mMVBHuPwDS">.style.backgroundColor</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'beige'</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Take a moment to notice the change in the web page. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## JAVASCRIPT AND THE DOM

### Create and Insert Elements




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">JavaScript and the DOM</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0"> Create and Insert Elements</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Just as the DOM allows scripts to modify existing elements, it also allows for the creation of new ones.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement"><code class="code__2rdF32qjRVp7mMVBHuPwDS">.createElement()</code> method</a> creates a new element based on the specified tag name passed into it as an argument. However, it does not append it to the document. It creates an empty element with no inner HTML.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let paragraph</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">createElement</span><span class="mtk1">(</span><span class="mtk8">'p'</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example code above, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.createElement()</code> method takes <code class="code__2rdF32qjRVp7mMVBHuPwDS">'p'</code> as its argument which creates an empty <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element and stores it as the <code class="code__2rdF32qjRVp7mMVBHuPwDS">paragraph</code> variable.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">We can assign values to the properties of the newly created element like how we’ve done previously with existing elements.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">paragraph</span><span class="mtk1">.</span><span class="mtk10">id</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'info'</span><span class="mtk1">; </span></span><br><span><span class="mtk9">paragraph</span><span class="mtk1">.</span><span class="mtk10">innerHTML</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'The text inside the paragraph'</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Above, we use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.id</code> property to assign <code class="code__2rdF32qjRVp7mMVBHuPwDS">'info'</code> as ID and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.innerHTML</code> property to set <code class="code__2rdF32qjRVp7mMVBHuPwDS">'The text inside the paragraph'</code> as the content of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In order to create an element and add it to the web page, you must assign it to be the child of an element that already exists on the DOM, referred to as the parent element. We call this process <em>appending</em>. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.appendChild()</code> method will add a child element as the parent element’s last child node. The following code appends the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element stored in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">paragraph</code> variable to the document body.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">body</span><span class="mtk1">.</span><span class="mtk10">appendChild</span><span class="mtk1">(</span><span class="mtk9">paragraph</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.appendChild()</code> method does not replace the content inside of the parent, in this case, <code class="code__2rdF32qjRVp7mMVBHuPwDS">body</code>. Rather, it appends the new element as the last child of that parent.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Create a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;li&gt;</code> element using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.createElement()</code> method and save it in a variable called <code class="code__2rdF32qjRVp7mMVBHuPwDS">newAttraction</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">On the following line, assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">newAttraction</code> element an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">'vespa'</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">newAttraction</code> element the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">'Rent a Vespa'</code> as its inner HTML. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Lastly, append the <code class="code__2rdF32qjRVp7mMVBHuPwDS">newAttraction</code> element to the list of top attractions with the ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">italy-attractions</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 5 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## JAVASCRIPT AND THE DOM

### Remove an Element




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">JavaScript and the DOM</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Remove an Element</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In addition to modifying or creating an element from scratch, the DOM also allows for the removal of an element. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.removeChild()</code> method removes a specified child from a parent.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let paragraph</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">querySelector</span><span class="mtk1">(</span><span class="mtk8">'p'</span><span class="mtk1">);</span></span><br><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">body</span><span class="mtk1">.</span><span class="mtk10">removeChild</span><span class="mtk1">(</span><span class="mtk9">paragraph</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the above example code, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.querySelector()</code> method returns the first paragraph in the document. Then, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">paragraph</code> element is passed as an argument of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.removeChild()</code> method chained to the parent of the paragraph—<code class="code__2rdF32qjRVp7mMVBHuPwDS">document.body</code>. This removes the first paragraph from the document body.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you want to hide an element rather than completely deleting it, the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/hidden"><code class="code__2rdF32qjRVp7mMVBHuPwDS">.hidden</code> property</a> allows you to hide it by setting the property as <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code> or <code class="code__2rdF32qjRVp7mMVBHuPwDS">false</code>:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">getElementById</span><span class="mtk1">(</span><span class="mtk8">'sign'</span><span class="mtk1">).</span><span class="mtk10">hidden</span><span class="mtk1"> =&nbsp;</span><span class="mtk5">true</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code above did not remove the element with ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">'sign'</code> from the DOM but rather, hid it.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">First, save the element with the ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">vespa</code> as a variable named <code class="code__2rdF32qjRVp7mMVBHuPwDS">elementToRemove</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">elementToRemove</code> element is a child of the list of top attractions with the ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">italy-attractions</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Remove the <code class="code__2rdF32qjRVp7mMVBHuPwDS">elementToRemove</code> element from its parent.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## JAVASCRIPT AND THE DOM

### Add Click Interactivity




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">JavaScript and the DOM</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Add Click Interactivity</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">You can add interactivity to DOM elements by assigning a function to run based on an <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/Events">event</a>. Events can include anything from a click to a user mousing over an element. We will learn more about events in the upcoming <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/build-interactive-websites/lessons/dom-events">DOM Events with JavaScript</a> lesson. For now, let’s take a look at how to modify an element when a click event happens.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.onclick</code> property allows you to assign a function to run on when a click event happens on an element:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let element</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">querySelector</span><span class="mtk1">(</span><span class="mtk8">'button'</span><span class="mtk1">);</span></span><br><span><span> </span></span><br><span><span class="mtk9">element</span><span class="mtk1">.</span><span class="mtk10">onclick</span><span class="mtk1"> =&nbsp;</span><span class="mtk12">function</span><span class="mtk1">() {&nbsp;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk9">element</span><span class="mtk1">.</span><span class="mtk10">style</span><span class="mtk1">.</span><span class="mtk10">backgroundColor</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'blue'</span><span class="mtk1"> </span></span><br><span><span class="mtk1">};</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">You can also assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.onclick</code> property to a function by name:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let element</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">querySelector</span><span class="mtk1">(</span><span class="mtk8">'button'</span><span class="mtk1">);</span></span><br><span><span> </span></span><br><span><span class="mtk12">function turnBlue</span><span class="mtk1">() {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk9">element</span><span class="mtk1">.</span><span class="mtk10">style</span><span class="mtk1">.</span><span class="mtk10">backgroundColor</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'blue'</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk9">element</span><span class="mtk1">.</span><span class="mtk10">onclick</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">turnBlue</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the above example code, when the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;button&gt;</code> element detects a click event, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">backgroundColor</code> will change to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'blue'</code>.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">turnButtonRed()</code> function, add the code to modify the button stored in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">element</code> variable as follows:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.style.backgroundColor</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'red'</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.style.color</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'white'</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Modify the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.innerHTML</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'Red Button'</code></li>
</ol>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Below our <code class="code__2rdF32qjRVp7mMVBHuPwDS">turnButtonRed()</code> function definition, trigger the <code class="code__2rdF32qjRVp7mMVBHuPwDS">turnButtonRed()</code> function when the <code class="code__2rdF32qjRVp7mMVBHuPwDS">element</code> detects a click event. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## JAVASCRIPT AND THE DOM

### Review




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">JavaScript and the DOM</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Review</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson, you manipulated a webpage structure by leveraging the Document Object Model (DOM) interface in JavaScript.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s review what we learned:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> keyword grants access to the root of the DOM in JavaScript.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The DOM Interface allows you to select a specific element with CSS selectors by using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.querySelector()</code> method.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">You can access an element directly by its ID with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.getElementById()</code> method which returns a single element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">You can access an array of elements with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.getElementsByClassName()</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">.getElementsByTagName()</code> methods, then call a single element by referencing its placement in the array.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.innerHTML</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">.style</code> properties allow you to modify an element by changing its contents or style respectively.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">You can create, append, and remove elements by using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.createElement()</code>,<code class="code__2rdF32qjRVp7mMVBHuPwDS">.appendChild()</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">.removeChild()</code> methods respectively.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.onclick</code> property can add interactivity to a DOM element based on a click event.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.children</code> property returns a list of an element’s children and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.parentNode</code> property returns the element’s closest connected node in the direction towards the root.</li>
</ul>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Feel free to practice what we’ve learned in this lesson. When you are ready, click “Next” to continue!</p>
</div></div></div>


**Solutions**


```html

```




## Create Your First JavaScript Website




<iframe frameborder="0" allowfullscreen="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" title="Create your first HTML/CSS/JS project" width="100%" height="100%" src="https://www.youtube.com/embed/iwNUJU5D3aI?autoplay=0&amp;mute=0&amp;controls=1&amp;origin=https%3A%2F%2Fwww.codecademy.com&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;iv_load_policy=3&amp;modestbranding=1&amp;enablejsapi=1&amp;widgetid=1" id="widget2" data-gtm-yt-inspected-76="true"></iframe>




## DOM EVENTS WITH JAVASCRIPT

### What is an Event?




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">What is an Event?</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">When you refresh your email inbox, double tap on a post, or scroll through a newsfeed — something cool happens in your browser. These actions are known as <em>events</em>! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Events on the web are user interactions and browser manipulations that you can program to trigger functionality. Some other examples of events are:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">A mouse clicking on a button</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Webpage files loading in the browser</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">A user swiping right on an image</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">When a user does any of the above actions, they’re causing the event to be <em>fired</em> or be <em>triggered</em>. As in, “a click event fired when the button was clicked”. Being able to respond to these events makes your website interactive and therefore <em>dynamic</em>.</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Check out the recipe webpage — interact with the page and see how it responds. What events do you think are firing?</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">You’ll learn more about each event as you progress in the lesson, but here’s a quick overview:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Click the <code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code> button to increase the measurements of the ingredients.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Hover over the instructions to see the estimated cook time.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Click on highlighted ingredients in the instructions for facts about the foods in the ingredient list.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Click the bar at the bottom (footer) to change its background color.</li>
</ol>
</div></div></div>


**Solutions**


```html

```




## DOM EVENTS WITH JAVASCRIPT

### "Firing" Events




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">"Firing" Events</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">After a specific event fires on a specific element in the <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/paths/web-development/tracks/build-interactive-websites/modules/web-dev-interactive-websites/lessons/intro-dom/exercises/what-is-the-dom">document object model</a> (or DOM), an <em>event handler</em> function can be created to run as a response. In this lesson, we will learn about event handler functions that modify and update DOM elements after an event fires.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s compare the firing of events to something more familiar: a dog trained to eat when they hear the sound of a bell! (This is known as the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Classical_conditioning">Pavlovian conditioning</a>.)</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">As you can see in the diagram, the ringing of the bell is analogous to a JavaScript event <em>firing</em>. The dog is trained to anticipate the ringing of the bell and this action is analogous to creating an <em>event listener</em>. After the dog hears the bell, it’ll come over and eat its food! This response is like an <em>event handler function</em> that executes code which, in a website, could change an element’s color, text, and much more!”</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Most events in the browser take place without being noticed — the events are undetected because there is no event handler associated with the event to execute an action. Event handlers are crucial for creating interactive websites with JavaScript.</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Check out the diagram to see the event firing process of a dog trained to eat when they hear the sound of a bell.</p>
</div></div></div>


**Solutions**


```html

```




## DOM EVENTS WITH JAVASCRIPT

### Event Handler Registration




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Event Handler Registration</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">You’re doing great! Now it’s time to dive into using event handler functions to create interactivity.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> method, we can have a DOM element listen for a specific event and execute a block of code when the event is detected. The DOM element that listens for an event is called the <em>event target</em> and the block of code that runs when the event happens is called the <em>event handler</em>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s take a look at the code below:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let eventTarget</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">document</span><span class="mtk1">.</span><span class="mtk10">getElementById</span><span class="mtk1">(</span><span class="mtk8">'targetElement'</span><span class="mtk1">);</span></span><br><span><span> </span></span><br><span><span class="mtk9">eventTarget</span><span class="mtk1">.</span><span class="mtk10">addEventListener</span><span class="mtk1">(</span><span class="mtk8">'click'</span><span class="mtk1">, </span><span class="mtk12">function</span><span class="mtk1">() {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk16">// this block of code will run when click event ha</span><span class="mtk16">ppens on eventTarget element</span></span><br><span><span class="mtk1">});</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s break this down! </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">We selected our event target from the DOM using <code class="code__2rdF32qjRVp7mMVBHuPwDS">document.getElementById('targetElement')</code>. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">We used the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> method on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">eventTarget</code> DOM element.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> method takes two arguments: an event name in <em>string</em> format and an event handler function. We will learn about different values we can use as event names in a later lesson.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">In this example, we used the <code class="code__2rdF32qjRVp7mMVBHuPwDS">'click'</code> event, which fires when the user clicks on <code class="code__2rdF32qjRVp7mMVBHuPwDS">eventTarget</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The code block in the event handler function will execute when the <code class="code__2rdF32qjRVp7mMVBHuPwDS">'click'</code> event is detected.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Instead of using an anonymous function as the event handler, it’s best practice to create a named event handler function. Your code will remain organized and reusable this way, even if your code gets complex. Check out the syntax:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">function eventHandlerFunction</span><span class="mtk1">() {</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk16">// this block of code will run when click event ha</span><span class="mtk16">ppens</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk9">eventTarget</span><span class="mtk1">.</span><span class="mtk10">addEventListener</span><span class="mtk1">(</span><span class="mtk8">'click'</span><span class="mtk1">, </span><span class="mtk9">eventHandlerFunction</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The named function <code class="code__2rdF32qjRVp7mMVBHuPwDS">eventHandlerFunction</code> is passed as the second argument of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> method instead of defining an anonymous function within the method!</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Look at the browser and notice that there are two elements, one containing informational text about JavaScript and a button. When the button is clicked, there should be more text that appears. Currently, clicking the button doesn’t seem to do anything. You are going to create an event handler to fix this!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">First, create a function called <code class="code__2rdF32qjRVp7mMVBHuPwDS">showInfo()</code> which we will use as the event handler function to make the hidden element containing the additional informational text (<code class="code__2rdF32qjRVp7mMVBHuPwDS">moreInfo</code>) appear when the <code class="code__2rdF32qjRVp7mMVBHuPwDS">'click'</code> event fires.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Inside the function, create a statement that changes the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.display</code> style property of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">moreInfo</code> element to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'block'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, create an event handler for a click event using <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code>. Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">readMore</code> as the event target and <code class="code__2rdF32qjRVp7mMVBHuPwDS">showInfo</code> as the event handler function.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Run your code and fire your event once you’re done.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## DOM EVENTS WITH JAVASCRIPT

### Adding Event Handlers




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Adding Event Handlers</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">We looked at registering event handlers using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> method, but there is also another way!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Event Handlers can also be registered by setting an <code class="code__2rdF32qjRVp7mMVBHuPwDS">.onevent</code> property on a DOM element (event target). The pattern for registering a specific event is to append an element with <code class="code__2rdF32qjRVp7mMVBHuPwDS">.on</code> followed by the lowercased event type name. For instance, if we want to register a click event with this pattern, we would write: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">eventTarget</span><span class="mtk1">.</span><span class="mtk10">onclick</span><span class="mtk1"> =&nbsp;</span><span class="mtk9">eventHandlerFunction</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Here, we give the DOM element <code class="code__2rdF32qjRVp7mMVBHuPwDS">eventTarget</code> the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick"><code class="code__2rdF32qjRVp7mMVBHuPwDS">.onclick</code> property</a> and set its value as the event handler function <code class="code__2rdF32qjRVp7mMVBHuPwDS">eventHandlerFunction</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">It’s important to know that this <code class="code__2rdF32qjRVp7mMVBHuPwDS">.onevent</code> property and <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> will both register event listeners. With <code class="code__2rdF32qjRVp7mMVBHuPwDS">.onevent</code>, it allows for one event handler function to be attached to the event target. However, with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> method , we can add multiple event handler functions. In the later exercises, we’ll be using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> syntax, but we wanted to also introduce the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.onevent</code> syntax because both are widely used.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Play around with the <code class="code__2rdF32qjRVp7mMVBHuPwDS">view</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">close</code> elements to meet the Codecademy mascot, Codey. Codey is super happy you made it this far and they need your help!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Right now, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">open()</code> function makes the <code class="code__2rdF32qjRVp7mMVBHuPwDS">codey</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">close</code> elements visible by changing their <code class="code__2rdF32qjRVp7mMVBHuPwDS">.display</code> properties to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'block'</code>. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">hide()</code> function hides the same elements by assigning a <code class="code__2rdF32qjRVp7mMVBHuPwDS">'none'</code> value to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.display</code> properties.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Codey wants you to create a function named <code class="code__2rdF32qjRVp7mMVBHuPwDS">textChange()</code> that changes the text in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">view</code> element to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'Hello, World!'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, you must create a function named <code class="code__2rdF32qjRVp7mMVBHuPwDS">textReturn()</code> that changes the text of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">view</code> element variable back to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'View'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Assign <code class="code__2rdF32qjRVp7mMVBHuPwDS">textChange</code> as an event handler function to a <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event fired on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">view</code> variable and run your code.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Assign <code class="code__2rdF32qjRVp7mMVBHuPwDS">textReturn</code> as an event handler function to a <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event fired on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">close</code> variable. Then run your code and fire the events!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 5 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## DOM EVENTS WITH JAVASCRIPT

### Removing Event Handlers




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Removing Event Handlers</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.removeEventListener()</code> method is used to reverse the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> method. This method stops the event target from “listening” for an event to fire when it no longer needs to. <code class="code__2rdF32qjRVp7mMVBHuPwDS">.removeEventListener()</code> also takes two arguments:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The event type as a string</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The event handler function</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">Check out the syntax of a <code class="code__2rdF32qjRVp7mMVBHuPwDS">.removeEventListener()</code> method with a click event:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk9">eventTarget</span><span class="mtk1">.</span><span class="mtk10">removeEventListener</span><span class="mtk1">(</span><span class="mtk8">'click'</span><span class="mtk1">, </span><span class="mtk9">eventHandlerFunction</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Because there can be multiple event handler functions associated with a particular event, <code class="code__2rdF32qjRVp7mMVBHuPwDS">.removeEventListener()</code> needs both the exact event type name and the name of the event handler you want to remove. If <code class="code__2rdF32qjRVp7mMVBHuPwDS">.addEventListener()</code> was provided an anonymous function, then that event listener cannot be removed.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Check out this website that shows your daily fortune. But the website is broken! You should only be able to see your daily fortune once, but you will see that you can keep pressing the button to get a new fortune. You need to use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.removeEventListener()</code> method after a fortune is displayed.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">showFortune()</code> function, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">.removeEventListener()</code> to prevent a new fortune from being displayed when a user tries to click the <code class="code__2rdF32qjRVp7mMVBHuPwDS">button</code> element.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## DOM EVENTS WITH JAVASCRIPT

### Event Object Properties




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Event Object Properties</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">JavaScript stores events as <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Event"><code class="code__2rdF32qjRVp7mMVBHuPwDS">Event</code> objects</a> with their related data and functionalities as properties and methods. When an event is triggered, the event object can be passed as an argument to the event handler function.</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">function eventHandlerFunction</span><span class="mtk1">(</span><span class="mtk12">event</span><span class="mtk1">){</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk9">console</span><span class="mtk1">.</span><span class="mtk10">log</span><span class="mtk1">(</span><span class="mtk9">event</span><span class="mtk1">.</span><span class="mtk10">timeStamp</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk9">eventTarget</span><span class="mtk1">.</span><span class="mtk10">addEventListener</span><span class="mtk1">(</span><span class="mtk8">'click'</span><span class="mtk1">, </span><span class="mtk9">eventHandlerFunction</span><span class="mtk1">);</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, when the <code class="code__2rdF32qjRVp7mMVBHuPwDS">'click'</code> event is triggered on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">eventTarget</code>, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">eventHandlerFunction</code> receives <code class="code__2rdF32qjRVp7mMVBHuPwDS">event</code>, the Event object, which has information related to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">'click'</code> event. Then, we log the time it took for the event to be triggered since the document was loaded by accessing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.timeStamp</code> property of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">event</code> object.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">There are pre-determined properties associated with event objects. You can call these properties to see information about the event, for example:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Event/target"><code class="code__2rdF32qjRVp7mMVBHuPwDS">.target</code> property</a> to reference the element that the event is registered to.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Event/type"><code class="code__2rdF32qjRVp7mMVBHuPwDS">.type</code> property</a> to access the name of the event.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/API/Event/timeStamp"><code class="code__2rdF32qjRVp7mMVBHuPwDS">.timeStamp</code> property</a> to access the number of milliseconds that passed since the document loaded and the event was triggered.</li>
</ul>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Everyone loves a good puppy picture! Use what you’ve learned about event object properties to share this puppy photo with your friends.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">First, add a statement inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">sharePhoto()</code> function that will change the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.display</code> property of the event <code class="code__2rdF32qjRVp7mMVBHuPwDS">.target</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'none'</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Remember that the event <code class="code__2rdF32qjRVp7mMVBHuPwDS">.target</code> is a DOM element and you can access the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.display</code> property by referencing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.style</code> property first.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, add a statement to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">sharePhoto</code> function that will modify the <code class="code__2rdF32qjRVp7mMVBHuPwDS">text</code> element to state the number of milliseconds from the DOM loading to the event firing.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, to create functionality for the event object, assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">sharePhoto</code> function to a <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">share</code> element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Run your code!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## DOM EVENTS WITH JAVASCRIPT

### Event Types




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Event Types</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Beyond the <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event, there are all types of DOM events that can fire in a browser! It’s important to know <em>most</em> events in the DOM take place without being noticed because there are no event handlers connected to them.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">It’s also important to know some registered events don’t depend on user interactions to fire. For instance, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">load</code> event fires after website files completely load in the browser. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Browsers can fire many other events without a user — you can check out a list of events on the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/Events">MDN Events Reference</a> page.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Many events need user interaction with the DOM to fire. One user interaction event you’ve become familiar with is the <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event. A <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event fires when the user presses and releases a mouse button on an element in the DOM.</p>
<img alt="Click Event Image" src="https://content.codecademy.com/courses/javascript-dom-events/click-event.png" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">In the rest of this lesson, you’ll explore more user interaction event types like the mouse and keyboard events. To explore more event types, check out the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/Events">MDN Events Reference</a>.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">We made a really cool color generator to help people find different colors — try it out! Uh oh, it seems to be broken. We need you to use your new knowledge to fix the website.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Complete the <code class="code__2rdF32qjRVp7mMVBHuPwDS">colorChange()</code> function, which will be used as an event handler function, to randomly change the colors of the buttons when specific events are fired on them. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">First, add the following variable to the event handler function:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-js" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">let randomColor</span><span class="mtk1"> =&nbsp;</span><span class="mtk8">'rgb('</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">colorValue</span><span class="mtk1">() +&nbsp;</span><span class="mtk8">','</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">colorValue</span><span class="mtk1">() +&nbsp;</span><span class="mtk8">','</span><span class="mtk1"> +&nbsp;</span><span class="mtk9">colorValue</span><span class="mtk1">() +&nbsp;</span><span class="mtk8">')'</span><span class="mtk1">;</span></span><br></div></code></pre></pre>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add a statement that changes the background color of the event target and set it equal to <code class="code__2rdF32qjRVp7mMVBHuPwDS">randomColor</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">There are two elements that should change color on this web page. First, create an event handler property on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">button</code> element that fires when it’s clicked. Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">colorChange</code> as the event handler function. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then run your code and fire the <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, create an event handler property on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">mysteryButton</code> element. This property needs an event that fires when you rotate the mouse wheel or slide down on the mousepad. Use the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/Events#Mouse_Events">MDN Events Reference</a> page to find the correct event type. Assign the same <code class="code__2rdF32qjRVp7mMVBHuPwDS">colorChange</code> event handler function to the event handler property.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then run your code and fire the event.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 5 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## DOM EVENTS WITH JAVASCRIPT

### Mouse Events




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Mouse Events</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">When you use a mouse device on a website, <em>mouse events</em> fire. You’ve seen the <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">wheel</code> events, but, there are even more mouse events to explore!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">mousedown</code> event is fired when the user presses a mouse button down. This is different from a <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event because <code class="code__2rdF32qjRVp7mMVBHuPwDS">mousedown</code> doesn’t need the mouse button to be released to fire.</p>
<img alt="Mouse Down Event Image" src="https://content.codecademy.com/courses/javascript-dom-events/mousedown.png" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">mouseup</code> event is fired when the user releases the mouse button. This is different from the <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">mousedown</code> events because <code class="code__2rdF32qjRVp7mMVBHuPwDS">mouseup</code> doesn’t depend on the mouse button being pressed down to fire.</p>
<img alt="Mouse Up Event Image" src="https://content.codecademy.com/courses/javascript-dom-events/mouseup.png" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">mouseover</code> event is fired when the mouse enters the content of an element.</p>
<img alt="Mouse Over Event Image" src="https://content.codecademy.com/courses/javascript-dom-events/mouseover.png" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">mouseout</code> event is fired when the mouse leaves an element.</p>
<img src="https://content.codecademy.com/courses/javascript-dom-events/mouseout.gif" alt="Mouse Out Event Image" class="img__1JGFO2nlisObc3KeOSGPRp"></div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In this exercise, you’ll modify the list elements using mouse events. You can use the reset element that is already programmed to set the other list element back to their default styles.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">First, create a function called <code class="code__2rdF32qjRVp7mMVBHuPwDS">increaseWidth()</code> that changes the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.width</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">itemOne</code> to any size greater than <code class="code__2rdF32qjRVp7mMVBHuPwDS">'400px'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, create an event handler for <code class="code__2rdF32qjRVp7mMVBHuPwDS">itemOne</code> that will trigger the <code class="code__2rdF32qjRVp7mMVBHuPwDS">increaseWidth()</code> function when the mouse hovers on it.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, create a function called <code class="code__2rdF32qjRVp7mMVBHuPwDS">changeBackground()</code> that changes the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.backgroundColor</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">itemTwo</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">changeBackground()</code> function we just created as an event handler for <code class="code__2rdF32qjRVp7mMVBHuPwDS">itemTwo</code> that will be triggered when the mouse is released over the element!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 5 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">5.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, create a function called <code class="code__2rdF32qjRVp7mMVBHuPwDS">changeText()</code> that changes the text of <code class="code__2rdF32qjRVp7mMVBHuPwDS">itemThree</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'The mouse has left the element'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 6 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">6.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Create an event handler for <code class="code__2rdF32qjRVp7mMVBHuPwDS">itemThree</code> that will fire <code class="code__2rdF32qjRVp7mMVBHuPwDS">changeText()</code> function when the mouse leaves the element.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 7 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">7.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Finally, let’s create a function called <code class="code__2rdF32qjRVp7mMVBHuPwDS">showItem()</code> that makes the <code class="code__2rdF32qjRVp7mMVBHuPwDS">itemFive</code> element appear by changing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.display</code> style property to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'block'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 8 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">8.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, create an event handler for <code class="code__2rdF32qjRVp7mMVBHuPwDS">itemFour</code> that triggers the <code class="code__2rdF32qjRVp7mMVBHuPwDS">showItem()</code> function when the mouse is pressed down on the element.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 9 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## DOM EVENTS WITH JAVASCRIPT

### Keyboard Events




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Keyboard Events</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Other popular types of events are keyboard events! <em>keyboard events</em> are triggered by user interaction with keyboard keys in the browser.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">keydown</code> event is fired while a user presses a key down.
<img alt="Key Down Event Image" src="https://content.codecademy.com/courses/javascript-dom-events/keydown.png" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">keyup</code> event is fired while a user releases a key.
<img alt="Key Up Event Image" src="https://content.codecademy.com/courses/javascript-dom-events/keyup.png" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">keypress</code> event is fired when a user presses a key down and releases it. This is different from using <code class="code__2rdF32qjRVp7mMVBHuPwDS">keydown</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">keyup</code> events together, because those are two complete events and <code class="code__2rdF32qjRVp7mMVBHuPwDS">keypress</code> is one complete event.
<img alt="Key P ress Event Image" src="https://content.codecademy.com/courses/javascript-dom-events/keypress.png" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Keyboard events have unique properties assigned to their event objects like the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.key</code> property that stores the values of the key pressed by the user. You can program the event handler function to react to a specific key, or react to any interaction with the keyboard.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now it’s time to create a game! Program this code to dribble the ball on the platform using any key on a keyboard. When a user presses a key down, it should lift the ball up. When the user releases the key, the ball should drop.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">First, make a function named <code class="code__2rdF32qjRVp7mMVBHuPwDS">up()</code> that will raise the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.bottom</code> position of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">ball</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'250px'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, make a function named <code class="code__2rdF32qjRVp7mMVBHuPwDS">down()</code> that will lower the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.bottom</code> position of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">ball</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'50px'</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Create an event handler property that runs the <code class="code__2rdF32qjRVp7mMVBHuPwDS">up()</code> function when a <code class="code__2rdF32qjRVp7mMVBHuPwDS">keydown</code> event fires on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code> object, or anywhere on the DOM, as the event target.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Create an event handler property that runs the <code class="code__2rdF32qjRVp7mMVBHuPwDS">down()</code> function when a <code class="code__2rdF32qjRVp7mMVBHuPwDS">keyup</code> event fires on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">document</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Run your code and play around with the keyboard events to make the ball bounce on the platform. You can try keys like the space bar, letter keys, or number keys!</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 5 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## DOM EVENTS WITH JAVASCRIPT

### Review




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">DOM Events with JavaScript</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Review</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Congrats, you completed the lesson! Now you’ve learned about JavaScript events and you can leverage these events on the DOM to create interactivity with event handlers.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"> Let’s review what you’ve learned:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">You can register events to DOM elements using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">addEventListener()</code> method.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">addEventListener()</code> method takes two arguments: an event type and an event handler function.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When an event is triggered on the event target, the registered event handler function executes.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Event handler functions can also be registered as values of <code class="code__2rdF32qjRVp7mMVBHuPwDS">onevent</code> properties of their event target.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Event object properties like <code class="code__2rdF32qjRVp7mMVBHuPwDS">.target</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">.type</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">.timeStamp</code> are used to provide information about the event.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">addEventListener()</code> method can be used to add multiple event handler functions to a single event.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">removeEventListener()</code> method stops specific event handlers from “listening” for specific events firing.</li>
</ul>
</div></div></div>




## BUILDING INTERACTIVE WEBSITES

### Piano Keys




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Building Interactive Websites</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Piano Keys</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">You’re a web developer who has been hired by a music education company. This client wants you to create an interactive game to help their beginner-level piano students study. Create a piano player with DOM events in JavaScript!</p>
<img alt="Cat Playing Piano GIF" src="https://media.giphy.com/media/RccMM7hsUoW4w/giphy.gif" class="img__1JGFO2nlisObc3KeOSGPRp">

<br>

<p class="p__1qg33Igem5pAgn4kPMirjw">If you get stuck during this project, check out the <strong>project walkthrough video</strong>, which can be found by selecting “Get Unstuck” in the upper right-hand corner of this window.</p>
</div></div><div class="group__LspoGf1Fw0-ac_AUnuvRV"></div></div>




**Instructions** 


<div class="tasks__2zeiH_BHmhuJBXUlJC3X0R"><span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as complete by checking them off</span><h2 class="fit-full fcn-task-header">Create An Interactive Piano Game</h2><div><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 1" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-1-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-1">1.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">At the beginning of the code, we have variable name assignments for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">keys</code> array and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">notes</code> array. There is also a function looping through the elements of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">keys</code> array and pushing them to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">notes</code> array.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After the second comment, create a function named <code class="code__2rdF32qjRVp7mMVBHuPwDS">keyPlay</code> that changes the background color of the keys when they are pressed down. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Be sure to use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.target</code> property in the function because the target is being modified in this case.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 2" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-2-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-2">2.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, create a function named <code class="code__2rdF32qjRVp7mMVBHuPwDS">keyReturn</code> that returns the background color of the keys to their default with an empty string <code class="code__2rdF32qjRVp7mMVBHuPwDS">''</code> when the mouse is released on the element. Be sure to use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.target</code> property.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 3" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-3-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-3">3.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now that you have created two functions that change the color of the key elements, you must assign them as the values of event handler properties. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Create a named function and leave the code block blank for now. This function will be used later on to assign events to the keys, so it should take one parameter — you can call it <code class="code__2rdF32qjRVp7mMVBHuPwDS">note</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 4" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-4-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-4">4.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside the function, create an event handler that runs the <code class="code__2rdF32qjRVp7mMVBHuPwDS">keyPlay</code> as an event handler when a <code class="code__2rdF32qjRVp7mMVBHuPwDS">mousedown</code> event fires on any <code class="code__2rdF32qjRVp7mMVBHuPwDS">note</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 5" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-5-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-5">5.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside the function, create a second event handler property that runs the <code class="code__2rdF32qjRVp7mMVBHuPwDS">keyReturn</code> when a <code class="code__2rdF32qjRVp7mMVBHuPwDS">mouseup</code> event fires on any <code class="code__2rdF32qjRVp7mMVBHuPwDS">note</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 6" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-6-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-6">6.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">At the beginning of the code, we have variable name assignments for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">keys</code> array and the empty <code class="code__2rdF32qjRVp7mMVBHuPwDS">notes</code> array. There is also a function looping through the <code class="code__2rdF32qjRVp7mMVBHuPwDS">keys</code> array and pushing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">keys</code> elements to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">notes</code> array to be assigned a variable name.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Now, you must create a <code class="code__2rdF32qjRVp7mMVBHuPwDS">.forEach</code> loop that will pass the elements in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">notes</code> array through your event assignment function.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 7" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-7-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-7">7.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now, the program knows what to do when each piano key has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">mousedown</code> or <code class="code__2rdF32qjRVp7mMVBHuPwDS">mouseup</code> event fired on it. Run your code and see how it works!</p>
</div></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 8" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-8-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-8">8.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, there are variables that represent the progress buttons in the song box below that allow students to progress the piano.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextOne</code>,  <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextTwo</code>,  <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">startOver</code> change the lyrics and musical notes of the song to help the student play along. In the beginning of the song the only button the student needs is <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextOne</code>. Because of this the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.hidden</code> properties of the other buttons are assigned the value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">true</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Now you must create events on all the progress buttons. First, create an event handler property with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextOne</code> element.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 9" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-9-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-9">9.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">To begin modifying the song box, you must switch the progress buttons first.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Using an anonymous event handler function, make the following changes to the button that appears after <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextOne</code> is clicked:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Reveal the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextTwo</code> button by changing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.hidden</code> property to make the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextTwo</code> button appear.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Hide the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextOne</code> button by changing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.hidden</code> property to hide the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextOne</code> button.</li>
</ol>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 10" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-10-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-10">10.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Next, a <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event firing on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextOne</code> must change the music notes that guide the piano student through the song.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add the following changes to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextOne</code> event handler function so the musical notes change when the button is clicked.</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-five</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">D</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-six</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">C</code>.</li>
</ol>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 11" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-11-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-11">11.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Create another event handler property with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event on the button element called <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextTwo</code>. Then assign the property to the value of an anonymous event handler function.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 12" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-12-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-12">12.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Make the following changes to the button that appears when <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextTwo</code> is clicked:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Reveal the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code> button by changing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.hidden</code> property to make the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code> button appear.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Hide the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextTwo</code> button by changing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.hidden</code> property to hide the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextTwo</code> button.</li>
</ol>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 13" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-13-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-13">13.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Once the student has reached this point of the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Happy_Birthday_to_You#%22Happy_birthday_to_you%22"> Happy Birthday song </a>the lyrics changes from <code class="code__2rdF32qjRVp7mMVBHuPwDS">HAP-PY BIRTH-DAY TO YOU</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">HAP-PY BIRTH-DAY DEAR FRI-END</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Make the following changes to the lyrics in the function when the button is clicked:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">word-five</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">DEAR</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">word-six</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">FRI-</code>.</li>
</ol>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 14" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-14-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-14">14.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now you have the lyrics <code class="code__2rdF32qjRVp7mMVBHuPwDS">HAP-PY BIRTH-DAY DEAR FRI-</code>.  To finish the line, you must add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">-END</code> to the song box under the piano.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">-END</code> element is stored in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">lastLyric</code> variable.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add a statement to the event handler function for <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextTwo</code> that changes the display property of <code class="code__2rdF32qjRVp7mMVBHuPwDS">lastLyric</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'inline-block'</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 15" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-15-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-15">15.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">A <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event firing on the second button must also change the music notes to guide the piano student through the song.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add the following changes to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextTwo</code> event handler function so the musical notes change when the button is clicked:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-three</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">G</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-four</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">E</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-five</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">C</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-six</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">B</code>.</li>
</ol>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 16" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-16-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-16">16.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Create an event handler property with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">click</code> event on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code> element.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 17" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-17-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-17">17.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Using an anonymous event handler function, make the following changes to the button that appears when <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code> is clicked:</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Reveal the <code class="code__2rdF32qjRVp7mMVBHuPwDS">startOver</code> button by changing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.hidden</code> property to make the <code class="code__2rdF32qjRVp7mMVBHuPwDS">startOver</code> button appear.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Hide the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code> button by changing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.hidden</code> property to hide the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code> button.</li>
</ol>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 18" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-18-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-18">18.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Add the following changes to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code> event handler function so the lyrics change when this button is clicked.</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">word-one</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">HAP-</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">word-two</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">PY</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">word-three</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">BIRTH</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">word-four</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">DAY</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">word-five</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">TO</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">word-six</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">YOU!</code>.</li>
</ol>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 19" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-19-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-19">19.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Add the following changes to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code> event handler function so the musical notes change when the button is clicked.</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-one</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">F</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-two</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">F</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-three</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">E</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-four</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">C</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-five</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">D</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Change the content of the element with an ID of <code class="code__2rdF32qjRVp7mMVBHuPwDS">letter-note-six</code> to  <code class="code__2rdF32qjRVp7mMVBHuPwDS">C</code>.</li>
</ol>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 20" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-20-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-20">20.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now you have the lyrics<code class="code__2rdF32qjRVp7mMVBHuPwDS">HAP-PY BIRTH-DAY TO YOU! -END</code> — that couldn’t be right! To finish the line you must get rid of the “-end” in the song box.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add a statement to the event handler function for <code class="code__2rdF32qjRVp7mMVBHuPwDS">nextThree</code> that changes the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property of <code class="code__2rdF32qjRVp7mMVBHuPwDS">lastLyric</code> back to <code class="code__2rdF32qjRVp7mMVBHuPwDS">'none'</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 21" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-21-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-21">21.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Congrats, you’ve completed the Piano Player! Play around with the piano and the song box to fire all the events.</p>
</div></div></div></article></div></div>


**Solutions**


```html

```




## INTRODUCTION TO FORM VALIDATION

### Introduction




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Introduction to Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Introduction</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Modern websites require a lot of information to function as intended. Information like our usernames, passwords, “friends”, “likes”, credit card information, and shopping orders all have to be provided by users on the front-end and sent to the web applications’ servers so they can be processed. This information is used to create a personalized experience for the user. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">User information is traditionally collected using HTML <em>forms</em>. If you’ve ever entered text in a website, selected from options on a list, or checked boxes and then hit enter or pressed a button, you likely filled out and submitted an HTML form! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In order for the data submitted through forms to be useful, it’s essential that the information is valid—if you were allowed to accidentally submit your last name where your address was expected, your package would never show up!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The process of checking that the information submitted through a form adheres to expectations is called <em>form validation</em>. In this lesson, we’ll explore the different techniques for validating form inputs. </p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Take a look at the form provided. It’s a bare-bones HTML page with no validation. You can play around with it and get to know the different types of inputs on an HTML form. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Think about any of the forms you’ve submitted today—did you log into any sites? Use a search bar? Buy something online? </p>
</div></div></div>


**Solutions**


```html

```




## INTRODUCTION TO FORM VALIDATION

### Why Validate Forms?




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Introduction to Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Why Validate Forms?</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Most data, once submitted, is stored by a website or web application. It’s stored in a database on the server side. There are important reasons for us to make sure the information that will be stored in the database is accurate. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">We want operations that depend on the data to work:
Allowing a user to enter an incorrectly formatted email address, either on purpose or by accident, means that we won’t be able to contact that user later. Allowing a user to sign up for an account with a username that is already in use could cause numerous errors down the line. Making sure we collect all the data we need and checking that the data are formatted correctly can save a web application and its users a lot of trouble. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">We want to keep our site secure:
Unprotected data leaves entry points for malicious actors to hurt our application or our users. Allowing a user to submit a non-secure password means that their account will not be protected. Unprotected forms can also allow bits of code to be injected into our servers. This can potentially leave our users’ sensitive information exposed. The malicious actor could even gain control of our site or corrupt our existing data!  </p>
</div></div></div>




## INTRODUCTION TO FORM VALIDATION

### Regular Expressions




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Introduction to Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Regular Expressions</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Data submitted through forms are stored as strings. Strings are a fundamental data type in computer science representing a series of characters “strung” together. As humans, we can intuitively recognize patterns within strings, and this allows us to catch errors. Try to notice what’s wrong in the following examples:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">ABCDEF2GHIJKLMNOPQRSTUVWXYZ</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">My zip code is 9021</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The ct meowed </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt; Hello, World! &lt;/h2&gt;</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the first example, we had the letters of the alphabet presented in order but interrupted by an out of place <code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code>. In the second, we left off the 5th digit of a famous zip code. In the third, we omitted the “a” from the word cat. In the final example, we wrote some HTML with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> opening tag but an unmatching <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;/h2&gt;</code> closing tag.  If you picked up on these mistakes, it’s because your brain has been trained to expect patterns in certain types of data. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Unlike humans, who can get this training passively over time, computers have to be precisely programmed to recognize patterns. To specify patterns for the computer to recognize, we use a special language called <em>regular expressions</em> — also known as regex or regexp. A regular expression is a sequence of characters representing a pattern. We can use that pattern to match a string, match parts of a string, confirm that data is formatted acceptably, or even replace parts of strings with different characters.  </p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Try entering some patterns in the applet provided. If you enter <code class="code__2rdF32qjRVp7mMVBHuPwDS">ello</code>, you’ll notice how many of the examples include those characters. We could fully match all of the expressions with the pattern <code class="code__2rdF32qjRVp7mMVBHuPwDS">[^]*</code>. To match the first four expressions, we could use a pattern like <code class="code__2rdF32qjRVp7mMVBHuPwDS">[hH]ello[^]*</code>. The pattern <code class="code__2rdF32qjRVp7mMVBHuPwDS">[^]*\d{3}[^]*\d{3}-\d{4}</code> will match the two example phone numbers. </p>
</div></div></div>


**Solutions**


```html

```




## INTRODUCTION TO FORM VALIDATION

### Client-side Validation: HTML




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Introduction to Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Client-side Validation: HTML</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">The first technique we can use to validate form data is to prevent problematic inputs from being submitted in the first place. This is called <em>client-side validation</em>. The client is the process interacting with the server on behalf of a user—in the case of websites, the web browser is the client. The logic for validating the form is included with the code that displays the form on the user’s device. No interaction with the back-end is required to perform client-side validations. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Since form validation is so common, modern HTML provides some of these validation features built-in. For example, we can use HTML to make parts of a form <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> and others optional. We can also use HTML to set minimum and maximum values for an input or minimum or maximum lengths for a text input. We can even necessitate that the input match a particular pattern, specified by a regular expression. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If any of the rules laid out in the HTML form validation aren’t followed, the user will not be able to submit their form, and they’ll receive an error message explaining why. With these checks in place, the back-end is less likely to be sent incorrect data. HTML form validation will also benefit the user—the client provides the user immediate feedback, without having to wait for time-consuming communication with the back-end. </p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">The provided HTML form has three input fields that are <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code>. Try submitting the form without any one of them. Notice now a message appears on the form. We didn’t have to design that ourselves. It’s built into HTML. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Each input has additional requirements. </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">"name"</code> input requires a text input with a length between 3 and 100.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">"age"</code> input requires a number value between 1 and 123. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">"code"</code> input requires an input of either <code class="code__2rdF32qjRVp7mMVBHuPwDS">Codecademy</code> or <code class="code__2rdF32qjRVp7mMVBHuPwDS">codecademy</code>.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Try out the form with correct and incorrect inputs for each field. </p>
</div></div></div>


**Solutions**


```html

```




## INTRODUCTION TO FORM VALIDATION

### Client-side Validation: JavaScript




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Introduction to Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Client-side Validation: JavaScript</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Client-side validation has two main advantages. First, it’s a better experience for the user to be alerted to problematic data immediately rather than having to wait for that information to come back from the server and have to fill out the form again. Second, catching mistakes earlier in the process saves the application time and resources as well. But not all issues can be handled with the built-in HTML validations. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In order to truly customize validation or to perform more complex validations, we can incorporate JavaScript form validations. We can do this by either writing the JavaScript ourselves or by incorporating a JavaScript library. If we have unique requirements for usernames on our site, for example, we’ll have to provide these systems of validation ourselves. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If we’re creating a relatively simple website, it makes sense to code the form validation ourselves or use a simple vanilla JavaScript library—<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.npmjs.com/package/just-validate">just-validate, for example</a>. But most basic validation libraries will involve directly accessing or manipulating the DOM. This can get tricky when working with a framework that relies on a virtual DOM—like React or Vue. In those situations, it might be best to incorporate a library that works well with your specific framework. For example, the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.npmjs.com/package/formik">formik library</a> is a lightweight library that simplifies validating forms in a React app.</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Play around with the website we’ve provided. It’s a password validator with some specific requirements. This validation is done completely on the client-side using JavaScript. Specifically, it uses a library called <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://parsleyjs.org/">Parsley.js</a>.</p>
</div></div></div>


**Solutions**


```html

```




## INTRODUCTION TO FORM VALIDATION

### Back-end Validation




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Introduction to Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Back-end Validation</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">No matter how complete the front-end validation of a website or application seems, validations must also be completed on the back-end or server-side. Front-end validations are easy to bypass—a malicious user can simply turn off JavaScript on their browser, for example. There’s also the potential for middleman attacks in which data is changed after the request is submitted by a user but before it arrives at the server. As a rule, the back-end should never trust the data it receives.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">As the developer, once data is in the back-end, we have complete control over it, luckily. Back-end validation has several advantages:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">It enables us to use validation code often on machines with more computing power. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">It allows us to write validation code that a user can’t see—if malicious users can’t see exactly <em>how</em> we validate the data, it’s much more difficult for them to find ways around it. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">We can validate the information against other data the front-end doesn’t have access to—for example, we can check our database to see if a given username is already in use. </li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">There are two main ways to validate inputs on the server-side. The first takes place while the user is still inputting data into the form on the front-end. We can make asynchronous requests to the server with pieces of their data and send feedback directly to the user before they’ve submitted. This is slower than front-end validation and can be a design challenge from a user-experience perspective. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The second is once the form has been submitted. Back-end form validation is our application’s last defense against problematic data, and it’s essential to verify the validity and safety of data before adding it to a database. This is also an opportunity to “sanitize” the data: in order for our database to be useful, it’s important that all data within it is formatted consistently. This means that while we may want to be flexible about the formatting we require from a user, we likely want to transform inputs into a strict format before entering them in the database. </p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">This video illustrates the process of validating forms on the back-end.</p>
</div></div></div>


**Solutions**


```html

```




## INTRODUCTION TO FORM VALIDATION

### Back-end Validation




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Introduction to Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Back-end Validation</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">No matter how complete the front-end validation of a website or application seems, validations must also be completed on the back-end or server-side. Front-end validations are easy to bypass—a malicious user can simply turn off JavaScript on their browser, for example. There’s also the potential for middleman attacks in which data is changed after the request is submitted by a user but before it arrives at the server. As a rule, the back-end should never trust the data it receives.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">As the developer, once data is in the back-end, we have complete control over it, luckily. Back-end validation has several advantages:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">It enables us to use validation code often on machines with more computing power. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">It allows us to write validation code that a user can’t see—if malicious users can’t see exactly <em>how</em> we validate the data, it’s much more difficult for them to find ways around it. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">We can validate the information against other data the front-end doesn’t have access to—for example, we can check our database to see if a given username is already in use. </li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">There are two main ways to validate inputs on the server-side. The first takes place while the user is still inputting data into the form on the front-end. We can make asynchronous requests to the server with pieces of their data and send feedback directly to the user before they’ve submitted. This is slower than front-end validation and can be a design challenge from a user-experience perspective. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The second is once the form has been submitted. Back-end form validation is our application’s last defense against problematic data, and it’s essential to verify the validity and safety of data before adding it to a database. This is also an opportunity to “sanitize” the data: in order for our database to be useful, it’s important that all data within it is formatted consistently. This means that while we may want to be flexible about the formatting we require from a user, we likely want to transform inputs into a strict format before entering them in the database. </p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">This video illustrates the process of validating forms on the back-end.</p>
</div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Introduction to HTML Forms




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Introduction to HTML Forms</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Forms are a part of everyday life. When we use a physical form in real life, we write down information and give it to someone to process. Think of the times you’ve had to fill out information for various applications like a job, or a bank account, or dropped off a completed suggestion card — each instance is a form! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Just like a physical form, an HTML <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> element is responsible for collecting information to send somewhere else. Every time we browse the internet we come into contact with many forms and we might not even realize it. There’s a good chance that if you’re typing into a text field or providing an input, the field that you’re typing into is part of a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson, we’ll go over the structure and syntax of a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> and the many elements that populate it. </p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Look over the image, can you think of any other forms you’ve interacted with? Go to the next exercise when you’re ready. </p>
</div></div></div>


**Solutions**


```html

```




## HTML FORMS

### How a Form Works




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">How a Form Works</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">We can think of the internet as a network of computers which send and receive information. Computers need an <em>HTTP request</em> to know how to communicate. The HTTP request instructs the receiving computer how to handle the incoming information. More information can be found in our article about <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/articles/http-requests">HTTP requests</a>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/forms?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code></a> element is a great tool for collecting information, but then we need to send that information somewhere else for processing. We need to supply the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> element with both the location of where the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>‘s information goes and what HTTP request to make. Take a look at the sample <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> below: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form</span><span class="mtk1"> </span><span class="mtk7">action</span><span class="mtk1">=</span><span class="mtk8">"/example.html"</span><span class="mtk1"> </span><span class="mtk7">method</span><span class="mtk1">=</span><span class="mtk8">"POST"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the above example, we’ve created the skeleton for a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> that will send information to <strong>example.html</strong> as a POST request:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">action</code> attribute determines where the information is sent.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">method</code> attribute is assigned a HTTP verb that is included in the HTTP request. </li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Note: HTTP verbs like POST do not need to be capitalized for the request to work, but it’s done so out of convention. In the example above we could have written <code class="code__2rdF32qjRVp7mMVBHuPwDS">method="post"</code> and it would still work.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> element can also contain child elements. For instance, it would be helpful to provide a header so that users know what this <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> is about. We could also add a paragraph to provide even more detail. Let’s see an example of this in code:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form</span><span class="mtk1"> </span><span class="mtk7">action</span><span class="mtk1">=</span><span class="mtk8">"/example.html"</span><span class="mtk1"> </span><span class="mtk7">method</span><span class="mtk1">=</span><span class="mtk8">"POST"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">Creating a&nbsp;form</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">Looks like you want to learn how to create an HTML</span><span class="mtk1"> form. Well, the best way to learn is to play arou</span><span class="mtk1">nd with it.</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The example above doesn’t collect any user input, but we’ll do that in the next exercise. For now, let’s practice making the foundation of an HTML <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section&gt;</code> element, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> element under the provided comment. Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> with:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">an <code class="code__2rdF32qjRVp7mMVBHuPwDS">action</code> attribute with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"/practice.html"</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">method</code> attribute with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"POST"</code></li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Right now we have a blank <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> on a burger site, let’s add some context.  </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> element with text related to the site between the opening and closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> tags. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add some details to the form by inserting a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element below the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;h1&gt;</code> element. Write a relevant description within the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;p&gt;</code> element. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Text Input




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Text Input</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">If we want to create an input field in our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>, we’ll need the help of the <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/html/elements/input?page_ref=catalog"><code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code></a> element. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> attribute which determines how it renders on the web page and what kind of data it can accept.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The first value for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> attribute we’re going to explore is <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code>. When we create an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element with <code class="code__2rdF32qjRVp7mMVBHuPwDS">type="text"</code>, it renders a text field that users can type into. Note that the default value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> is <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code>. It’s also important that we include a <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> — without the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute, information in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> won’t be sent when the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> is submitted. We’ll explain more about submissions and the submit button in a later exercise. For now, let’s examine the following code that produces a text input field: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form</span><span class="mtk1"> </span><span class="mtk7">action</span><span class="mtk1">=</span><span class="mtk8">"/example.html"</span><span class="mtk1"> </span><span class="mtk7">method</span><span class="mtk1">=</span><span class="mtk8">"POST"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"text"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"first-text-field"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Here’s a screen shot of how the rendered form looks like on a web page for the Chrome browser (different browsers have different default rendering). When initially loaded, it will be an empty box:</p>
<img src="https://content.codecademy.com/courses/learn-html-forms/textInput%20-%20unlabeled%20blank.png" alt="rendered empty text field from input element type='text'" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;">

<p class="p__1qg33Igem5pAgn4kPMirjw">After users type into the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element, the value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute becomes what is typed into the text field. The value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute is paired with the value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute and sent as text when the form is submitted. For instance, if a user typed in “important details” in the text field created by our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element:</p>
<img src="https://content.codecademy.com/courses/learn-html-forms/textInput%20-%20unlabeled%20filled.png" alt="rendered filled text field which reads 'important details' " class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;">

<p class="p__1qg33Igem5pAgn4kPMirjw">When the form is submitted, the text: <code class="code__2rdF32qjRVp7mMVBHuPwDS">"first-text-field=important details"</code> is sent to <code class="code__2rdF32qjRVp7mMVBHuPwDS">/example.html</code> because the value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute is <code class="code__2rdF32qjRVp7mMVBHuPwDS">"first-text-field"</code> and the value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> is <code class="code__2rdF32qjRVp7mMVBHuPwDS">"important details"</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">We could also assign a default value for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute so that users have a pre-filled text field when they first see the rendered form like so:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form</span><span class="mtk1"> </span><span class="mtk7">action</span><span class="mtk1">=</span><span class="mtk8">"/example.html"</span><span class="mtk1"> </span><span class="mtk7">method</span><span class="mtk1">=</span><span class="mtk8">"POST"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"text"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"first-text-field"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"already pre-filled"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Which renders: </p>
<img src="https://content.codecademy.com/courses/learn-html-forms/textInput%20-%20unlabeled%20prefilled.png" alt="pre-filled text box due to assigned `value` attribute" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;">

<p class="p__1qg33Igem5pAgn4kPMirjw">Time to put this knowledge into practice! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s start with creating a login form for our users. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Inside the provided <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> element, add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code>.  </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw"> Even though we’re not submitting the form, let’s develop some good habits by giving the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> a <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"username"</code>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s see what happens if we add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"Davie"</code></p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Adding a Label




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Adding a Label</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In the previous exercise we created an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element but we didn’t include anything to explain what the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> is used for. For a user to properly identify an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> we use the appropriately named <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element has an opening and closing tag and displays text that is written between the opening and closing tags. To associate a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> and an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> needs an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> attribute. We then assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element with the value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>, like so: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form</span><span class="mtk1"> </span><span class="mtk7">action</span><span class="mtk1">=</span><span class="mtk8">"/example.html"</span><span class="mtk1"> </span><span class="mtk7">method</span><span class="mtk1">=</span><span class="mtk8">"POST"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"meal"</span><span class="mtk4">&gt;</span><span class="mtk1">What do you want to eat?</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;br&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"text"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"food"</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"meal"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code above renders: </p>
<img src="https://content.codecademy.com/courses/learn-html-forms/label%20-%20text%20input.png" alt="rendered form with labeled text field" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;">

<p class="p__1qg33Igem5pAgn4kPMirjw">Look, now users know what the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element is for! Another benefit for using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element is when this element is clicked, the corresponding <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> is highlighted/selected. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s see the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element in action! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element that is associated with the included <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element in <strong>index.html</strong>. (use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute!)</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then add text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Username</code> within the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After clearing this checkpoint, click on the <code class="code__2rdF32qjRVp7mMVBHuPwDS">Username</code> label in the web browser to see the corresponding <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> field selected.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Password Input




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Password Input</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Think about all those times we have to put sensitive information, like a password or PIN,  into a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>. We wouldn’t want our information to be seen by anyone peeking over our shoulder! Luckily, we have the <code class="code__2rdF32qjRVp7mMVBHuPwDS">type="password"</code> attribute for <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">An <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input type ="password"&gt;</code> element will replace input text with another character like an asterisk (*) or a dot (•). The code below provides an example of how to create a password field:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"user-password"</span><span class="mtk4">&gt;</span><span class="mtk1">Password: </span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"password"</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"user-password"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"user-password"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">After a user types into the field, it would look like:</p>
<img src="https://content.codecademy.com/courses/learn-html-forms/pwInput%20-%20labeled%20filled.png" alt="password field in a form with 6 dots showing text added to the field" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;"> 

<p class="p__1qg33Igem5pAgn4kPMirjw">Even though the password field obscures the text of the password, when the form is submitted, the value of the text is sent. In other words, if “hunter2” is typed into the password field, “user-password=hunter2” is sent along with the other information on the form. </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">To complete our login page in <strong>index.html</strong> we need a password field. Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element under the second <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element.</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> to the correct value to associate the second <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with this new <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the newly created <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"password"</code>. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"user-pw"</code>. </li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Number Input




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Number Input</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">We’ve now gone over two <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> attributes for <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> related to text. But, we might want our users to type in a number — in which case we can set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> attribute to… (you guessed it)… <code class="code__2rdF32qjRVp7mMVBHuPwDS">"number"</code>! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">By setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type="number"</code> for an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> we can restrict what users type into the input field to just numbers (and a few special characters like <code class="code__2rdF32qjRVp7mMVBHuPwDS">-</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">+</code>, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">.</code>). We can also provide a <code class="code__2rdF32qjRVp7mMVBHuPwDS">step</code> attribute which creates arrows inside the input field to increase or decrease by the value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">step</code> attribute. Below is the code needed to render an input field for numbers: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"years"</span><span class="mtk4">&gt;</span><span class="mtk1"> Years of experience: </span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"years"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"years"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"number"</span><span class="mtk1"> </span><span class="mtk7">step</span><span class="mtk1">=</span><span class="mtk8">"1"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Which renders:</p>
<img src="https://content.codecademy.com/courses/learn-html-forms/numInput%20-%20labeled%20blank%20steps.png" alt="rendered number input field with arrows to the right hand side of the field" width="100%" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;">

<p class="p__1qg33Igem5pAgn4kPMirjw">Now it’s time to apply this knowledge. </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In <strong>index.html</strong> we started a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> for users to make a custom burger. Right now we have a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> for patties that needs an associated <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Since we want users to enter a number, create an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> and set the attributes: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Associate the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> to the first <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> by assigning the correct value to <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code>. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">type="number"</code> </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">step="1"</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"amount"</code>.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw"><strong>Note</strong>: You may notice that we started adding <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section&gt;</code>s and other semantic HTML elements to help organize our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> elements. If you want to learn more about these elements, please take our <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-html/lessons/semantic-html/exercises/introduction-to-semantic-html">Semantic HTML lesson</a>. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Range Input




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Range Input</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Using an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input type="number"&gt;</code>  is great if we want to allow users to type in any number of their choosing. But, if we wanted to limit what numbers our users could type we might consider using a different <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> value. Another option we could use is setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"range"</code> which creates a slider. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To set the minimum and maximum values of the slider we assign values to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">min</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">max</code> attribute of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>. We could also control how smooth and fluid the slider works by assigning the <code class="code__2rdF32qjRVp7mMVBHuPwDS">step</code> attribute a value. Smaller <code class="code__2rdF32qjRVp7mMVBHuPwDS">step</code> values will make the slider move more fluidly, whereas larger <code class="code__2rdF32qjRVp7mMVBHuPwDS">step</code> values will make the slider move more noticeably. Take a look at the code to create a slider:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"volume"</span><span class="mtk4">&gt;</span><span class="mtk1"> Volume Control</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"volume"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"volume"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"range"</span><span class="mtk1"> </span><span class="mtk7">min</span><span class="mtk1">=</span><span class="mtk8">"0"</span><span class="mtk1"> </span><span class="mtk7">max</span><span class="mtk1">=</span><span class="mtk8">"100"</span><span class="mtk1"> </span><span class="mtk7">step</span><span class="mtk1">=</span><span class="mtk8">"1"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">The code above renders:
<img src="https://content.codecademy.com/courses/learn-html-forms/rangeInput%20-%20labeled.png" alt="rendered slider for volume control" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the example above, every time the slider moves by one, the value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>‘s <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute changes.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s give our users an option for how they want to cook their patties. We can do this by adding a slider to the existing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section&gt;</code> with <code class="code__2rdF32qjRVp7mMVBHuPwDS">class="cooked"</code>, add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element.  Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"doneness"</code>. Also, set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"range"</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Since our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> is getting long, you might have to scroll down to find the provided <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section&gt;</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">For the newly created <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> set the:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">min</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"0"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">max</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"5"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">step</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"0.5"</code>.</li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Checkbox Input




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Checkbox Input</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">So far the types of inputs we’ve allowed were all single choices. But, what if we presented multiple options to users and allow them to select any number of options? Sounds like we could use checkboxes! In a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> we would use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element and set <code class="code__2rdF32qjRVp7mMVBHuPwDS">type="checkbox"</code>. Examine the code used to create multiple checkboxes:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">Choose your pizza toppings:</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"cheese"</span><span class="mtk4">&gt;</span><span class="mtk1">Extra cheese</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"cheese"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"topping"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"checkbox"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"cheese"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;br&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"pepperoni"</span><span class="mtk4">&gt;</span><span class="mtk1">Pepperoni</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"pepperoni"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"topping"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"checkbox"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"pepperoni"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;br&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"anchovy"</span><span class="mtk4">&gt;</span><span class="mtk1">Anchovy</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"anchovy"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"topping"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"checkbox"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"anchovy"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Which renders:
<img src="https://content.codecademy.com/courses/learn-html-forms/checkboxInput%20-%20labeled.png" alt="HTML form asking user to select pizza toppings and three topping selections as checkboxes" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice in the example provided: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">there are assigned values to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute of the checkboxes. These values are not visible on the form itself, that’s why it is important that we use an associated <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> to identify the checkbox. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">each <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> has the same value for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute. Using the same <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> for each checkbox groups the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>s together. However, each <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> has a unique <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> to pair with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>. </li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Alright, time to use checkboxes in our code! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Time to add some toppings! In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section&gt;</code> with <code class="code__2rdF32qjRVp7mMVBHuPwDS">class="toppings"</code>, there are two <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>s but no associated <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> elements. Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element associated with the first <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The created <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> should have:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"lettuce"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"topping"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"checkbox"</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"lettuce"</code>. </li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element and associate it with the second <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element should have: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"tomato"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"checkbox"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"topping"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"tomato"</code>. </li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Two choices are good, but it would be better to have even more. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input type="checkbox"&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> pair. Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"topping"</code>. You’re free to decide the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> but make sure that your new <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> are associated. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Checkbox Input




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Checkbox Input</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">So far the types of inputs we’ve allowed were all single choices. But, what if we presented multiple options to users and allow them to select any number of options? Sounds like we could use checkboxes! In a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> we would use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element and set <code class="code__2rdF32qjRVp7mMVBHuPwDS">type="checkbox"</code>. Examine the code used to create multiple checkboxes:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">Choose your pizza toppings:</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"cheese"</span><span class="mtk4">&gt;</span><span class="mtk1">Extra cheese</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"cheese"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"topping"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"checkbox"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"cheese"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;br&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"pepperoni"</span><span class="mtk4">&gt;</span><span class="mtk1">Pepperoni</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"pepperoni"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"topping"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"checkbox"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"pepperoni"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;br&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"anchovy"</span><span class="mtk4">&gt;</span><span class="mtk1">Anchovy</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"anchovy"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"topping"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"checkbox"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"anchovy"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Which renders:
<img src="https://content.codecademy.com/courses/learn-html-forms/checkboxInput%20-%20labeled.png" alt="HTML form asking user to select pizza toppings and three topping selections as checkboxes" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice in the example provided: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">there are assigned values to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute of the checkboxes. These values are not visible on the form itself, that’s why it is important that we use an associated <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> to identify the checkbox. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">each <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> has the same value for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute. Using the same <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> for each checkbox groups the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>s together. However, each <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> has a unique <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> to pair with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>. </li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Alright, time to use checkboxes in our code! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Time to add some toppings! In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section&gt;</code> with <code class="code__2rdF32qjRVp7mMVBHuPwDS">class="toppings"</code>, there are two <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>s but no associated <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> elements. Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element associated with the first <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The created <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> should have:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"lettuce"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"topping"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"checkbox"</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"lettuce"</code>. </li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element and associate it with the second <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element should have: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"tomato"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"checkbox"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"topping"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"tomato"</code>. </li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Two choices are good, but it would be better to have even more. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input type="checkbox"&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> pair. Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"topping"</code>. You’re free to decide the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> but make sure that your new <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> are associated. </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 4 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Dropdown list




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Dropdown list</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Radio buttons are great if we want our users to pick one option out of a few visible options, but imagine if we have a whole list of options! This situation could quickly lead to a lot of radio buttons to keep track of. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">An alternative solution is to use a dropdown list to allow our users to choose one option from an organized list. Here’s the code to create a dropdown menu:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"lunch"</span><span class="mtk4">&gt;</span><span class="mtk1">What's for lunch?</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;select</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"lunch"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"lunch"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"pizza"</span><span class="mtk4">&gt;</span><span class="mtk1">Pizza</span><span class="mtk4">&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"curry"</span><span class="mtk4">&gt;</span><span class="mtk1">Curry</span><span class="mtk4">&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"salad"</span><span class="mtk4">&gt;</span><span class="mtk1">Salad</span><span class="mtk4">&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"ramen"</span><span class="mtk4">&gt;</span><span class="mtk1">Ramen</span><span class="mtk4">&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"tacos"</span><span class="mtk4">&gt;</span><span class="mtk1">Tacos</span><span class="mtk4">&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/select&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Which renders: 
<img src="https://content.codecademy.com/courses/learn-html-forms/dropdown%20list%20-%20concealed.png" alt="rendered dropdown list with the first option showing" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">And if we click on the field containing the first option, the list is revealed:
<img src="https://content.codecademy.com/courses/learn-html-forms/dropdown%20list%20-%20revealed.png" alt="rendered dropdown list with the all options showing" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice in the code that we’re using the element <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> to create the dropdown list. To populate the dropdown list, we add multiple <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> elements, each with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute. By default, only one of these options can be selected. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The text rendered is the text included between the opening and closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> tags. However, it is the value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute that is used in <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> submission (notice the difference in the text and <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> capitalization). When the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> is submitted, the information from this input field will be sent using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> of the chosen <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code>. For instance, if a user selected Pizza from the dropdown list, the information would be sent as <code class="code__2rdF32qjRVp7mMVBHuPwDS">"lunch=pizza"</code>. </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s now give our users a choice of buns using a dropdown list.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section&gt;</code> element with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"bun-type"</code> there is a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> that we can associate a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> element with.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"> Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> element with a name of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"bun"</code> and an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"bun"</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> element, add 3 <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code>s.</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The first <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> should have a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"sesame"</code> and display the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Sesame</code> on the webpage.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The second <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> should have a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"potato"</code> and display the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Potato</code> on the webpage. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The third <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> can be a value that you choose and display text relevant to the value (make sure it’s not empty!) </li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Datalist Input




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Datalist Input</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Even if we have an organized dropdown list, if the list has a lot of options, it could be tedious for users to scroll through the entire list to locate one option. That’s where using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> element comes in handy. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> is used with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input type="text"&gt;</code> element. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> creates a text field that users can type into and filter options from the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code>. Let’s go over a concrete example: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"city"</span><span class="mtk4">&gt;</span><span class="mtk1">Ideal city to visit?</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"text"</span><span class="mtk1"> </span><span class="mtk7">list</span><span class="mtk1">=</span><span class="mtk8">"cities"</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"city"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"city"</span><span class="mtk4">&gt;</span></span><br><span><span> </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;datalist</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"cities"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"New York City"</span><span class="mtk4">&gt;&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Tokyo"</span><span class="mtk4">&gt;&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Barcelona"</span><span class="mtk4">&gt;&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Mexico City"</span><span class="mtk4">&gt;&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Melbourne"</span><span class="mtk4">&gt;&lt;/option&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Other"</span><span class="mtk4">&gt;&lt;/option&gt;</span><span class="mtk1">&nbsp;&nbsp;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/datalist&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Notice, in the code above, we have an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> that has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">list</code> attribute. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> is associated to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> via the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>‘s <code class="code__2rdF32qjRVp7mMVBHuPwDS">list</code> attribute and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">From the code provided, the following form is rendered:
<img src="https://content.codecademy.com/courses/learn-html-forms/datalist%20-%20concealed.png" alt="input field with a label 'Ideal city to visit?'" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">And when field is selected: 
<img src="https://content.codecademy.com/courses/learn-html-forms/datalist%20-%20revealed.png" alt="clicking on the input field reveals a dropdown 
list" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">While <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> share some similarities, there are some major differences. In the associated <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element, users can type in the input field to search for a particular option. If none of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code>s match, the user can still use what they typed in. When the form is submitted, the value of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>‘s <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> of the option selected, or what the user typed in, is sent as a pair.  </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Now it’s time to make a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> of our own! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Time to add some sauce! Users might get creative with what sauce they choose to put, so let’s use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section&gt;</code> element with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"sauce-selection"</code>, we already have the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> set up. Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> element with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"sauces"</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> element, add 3 <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code>s.</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The first <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> should have a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"ketchup"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The second <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> should have a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"mayo"</code>. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The third <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> can be a value that you choose and display text relevant to the value (make sure it’s not empty!) </li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Textarea element




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Textarea element</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">An <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element with <code class="code__2rdF32qjRVp7mMVBHuPwDS">type="text"</code> creates a single row input field for users to type in information. However, there are cases where users need to write in more information, like a blog post. In such cases, instead of using an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>, we could use <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> element is used to create a bigger text field for users to write more text. We can add the attributes <code class="code__2rdF32qjRVp7mMVBHuPwDS">rows</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">cols</code> to determine the amount of rows and columns for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code>. Take a look:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"blog"</span><span class="mtk4">&gt;</span><span class="mtk1">New Blog Post: </span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;br&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;textarea</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"blog"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"blog"</span><span class="mtk1"> </span><span class="mtk7">rows</span><span class="mtk1">=</span><span class="mtk8">"5"</span><span class="mtk1"> </span><span class="mtk7">cols</span><span class="mtk1">=</span><span class="mtk8">"30"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/textarea&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the code above, an empty <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> that is 5 rows by 30 columns is rendered to the page like so:</p>
<img src="https://content.codecademy.com/courses/learn-html-forms/textarea%20-%20blank.png" alt="rendered empty textarea element" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;">

<p class="p__1qg33Igem5pAgn4kPMirjw">If we wanted an even bigger text field, we could click and drag on the bottom right corner to expand it.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">When we submit the form, the value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> is the text written inside the box. If we want to add a default value to <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> we would include it within the opening and closing tags like so:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;textarea&gt;</span><span class="mtk1">Adding default text</span><span class="mtk4">&lt;/textarea&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">This code will render a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> that contains pre-filled text: “Adding default text”.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">But don’t just take our word for it, let’s test it out! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">We covered a lot of options but users might still have other ideas. Let’s make use of a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> element to give users more freedom. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section&gt;</code> element with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">class</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"extra-info"</code>, we have provided a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element. Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> with the following attributes:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"extra"</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">rows</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"3"</code> </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">cols</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"40"</code></li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Now add some default text to the created <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code>. You may add any text you want, but it cannot be blank! </p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Submit Form




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Submit Form</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Remember, the purpose of a form is to collect information that will be submitted. That’s the role of the submit button — users click on it when they are finished with filling out information in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> and they’re ready to send it off.  Now that we’ve gone over how to create various input elements, let’s now go over how to create a submit button! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To make a submit button in a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>, we’re going to use the reliable <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element and set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"submit"</code>. For instance:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"submit"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Send"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Which renders:</p>
<img src="https://content.codecademy.com/courses/learn-html-forms/submit%20button2.png" alt="rendered submit button" class="img__1JGFO2nlisObc3KeOSGPRp" style="border: 1px solid black;"> 

<p class="p__1qg33Igem5pAgn4kPMirjw">Notice in the code snippet that the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> assigned to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> shows up as text on the submit button. If there isn’t a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> attribute, the default text, <code class="code__2rdF32qjRVp7mMVBHuPwDS">Submit</code> shows up on the button.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s now add this element to make our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>s complete! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw"> At the bottom of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> inside the element <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;section class="submission"&gt;</code>, add a submit button using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The text inside the submit button should read: <code class="code__2rdF32qjRVp7mMVBHuPwDS">Submit</code>.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## HTML FORMS

### Review




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">HTML Forms</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Review</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Nice work interacting with the extremely common and useful <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> element! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson we went over:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The purpose of a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> is to allow users to input information and send it.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>‘s <code class="code__2rdF32qjRVp7mMVBHuPwDS">action</code> attribute determines where the form’s information goes.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>‘s <code class="code__2rdF32qjRVp7mMVBHuPwDS">method</code> attribute determines how the information is sent and processed.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">To add fields for users to input information we use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element and set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> attribute to a field of our choosing:<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code> creates a single row field for text input.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"password"</code> creates a single row field that censors text input.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"number"</code> creates a single row field for number input.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"range"</code> creates a slider to select from a range of numbers. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"checkbox"</code> creates a single checkbox that can be paired with other checkboxes.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"radio"</code> creates a radio button that can be paired with other radio buttons.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code> and adding the <code class="code__2rdF32qjRVp7mMVBHuPwDS">list</code> attribute will pair the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> element if the <code class="code__2rdF32qjRVp7mMVBHuPwDS">list</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> are the same.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Setting <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"submit"</code> creates a submit button.</li>
</ul>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">A <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> element is populated with <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> elements and renders a dropdown list selection.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">A <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> element is populated with <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> elements and works with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> to search through choices.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">A <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> element is a text input field that has a customizable area.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">When a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> is submitted, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> of the fields that accept input and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> of those fields are sent as <code class="code__2rdF32qjRVp7mMVBHuPwDS">name=value</code> pairs. </li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> element in conjunction with the other elements listed above allows us to create sites that take into consideration the wants and needs of our users. Take the opportunity to take what you’ve learned, and apply it!</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">If you want to challenge yourself:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Create a form with multiple fields that accept user input.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add two separate sets of radio buttons or checkboxes.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Search how to add <em>placeholder</em> (hint hint) to an input field. A placeholder shows ups when the field has no <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code>, it disappears after the user types or selects something in the field. </li>
</ul>
</div></div></div>


**Solutions**


```html

```




## FORM VALIDATION

### Introduction to HTML Form Validation




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Introduction to HTML Form Validation</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Ever wonder how a login page actually works? Or why the combination of a username and password grants you access to a website? The answers lie in <em>validation</em>. Validation is the concept of checking user provided data against the required data.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">There are different types of validation. One type is <em>server-side validation</em>, this happens when data is sent to another machine (typically a server) for validation. An example of this type of validation is the usage of a login page. The form on the login page accepts username and password input, then sends the data to a server that checks that the pair matches up correctly. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">On the other hand, we use <em>client-side validation</em> if we want to check the data on the browser (the client). This validation occurs before data is sent to the server. Different browsers implement client-side validation differently, but it leads to the same outcome.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Shared among the different browsers are the benefits of using HTML5’s built-in client-side validation. It saves us time from having to send information to the server and wait for the server to send back confirmation or rejection of the data. This can also help us protect our server from malicious code or data from a malicious user. It also allows us to quickly give feedback to users for specific fields rather than having them fill in a form again if the data they input into the form was rejected. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In this lesson, we’ll learn how to add some validation checks to our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>s!</p>
</div></div></div>




**Instructions** 


<div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 body__3bSqqzbent-J_gmFLtFRzM"><p class="p__1qg33Igem5pAgn4kPMirjw">Press <strong>Next</strong> to get started on validations. </p>
</div></div></div>


**Solutions**


```html

```




## FORM VALIDATION

### Requiring an Input




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Requiring an Input</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Sometimes we have fields in our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>s which are not optional, i.e. there must be information provided before we can submit it. To enforce this rule, we can add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> attribute to an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Take for example:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form</span><span class="mtk1"> </span><span class="mtk7">action</span><span class="mtk1">=</span><span class="mtk8">"/example.html"</span><span class="mtk1"> </span><span class="mtk7">method</span><span class="mtk1">=</span><span class="mtk8">"POST"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"allergies"</span><span class="mtk4">&gt;</span><span class="mtk1">Do you have any dietary restrictions?</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;br&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"allergies"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"allergies"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"text"</span><span class="mtk1"> </span><span class="mtk7">required</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;br&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"submit"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Submit"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">This renders a text box, and if we try to submit the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> without filling it out we get this message:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://content.codecademy.com/courses/learn-html-forms/required%20field.png" alt="message pop up prompting user to fill in the field" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The styling of the message varies from browser to browser, the picture above depicts the message in a Chrome browser. We’ll also continue to show these messages as they appear in Chrome in later exercises. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s see how it shows up in your browser! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Currently, in the provided <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>, the user can submit it without putting any values inside the input field.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s change that by adding a <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> attribute to the existing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After you clear this checkpoint, try submitting the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> without filling out the fields.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## FORM VALIDATION

### Set a Minimum and Maximum




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Set a Minimum and Maximum</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Another built-in validation we can use is to assign a minimum or maximum value for a number field, e.g. <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input type="number"&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input type="range"&gt;</code>. To set a minimum acceptable value, we use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">min</code> attribute and assign a value. On the flip side, to set a maximum acceptable value, we assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">max</code> attribute a value. Let’s see this in code: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form</span><span class="mtk1"> </span><span class="mtk7">action</span><span class="mtk1">=</span><span class="mtk8">"/example.html"</span><span class="mtk1"> </span><span class="mtk7">method</span><span class="mtk1">=</span><span class="mtk8">"POST"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"guests"</span><span class="mtk4">&gt;</span><span class="mtk1">Enter #&nbsp;of guests:</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"guests"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"guests"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"number"</span><span class="mtk1"> </span><span class="mtk7">min</span><span class="mtk1">=</span><span class="mtk8">"1"</span><span class="mtk1"> </span><span class="mtk7">max</span><span class="mtk1">=</span><span class="mtk8">"4"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"submit"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Submit"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">If a user tries to submit an input that is less than 1 a warning will appear: 
<img src="https://content.codecademy.com/courses/learn-html-forms/min%20max%20attr.png" alt="prompt on a number field for user to input a value greater than or equal to 1" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">A similar message will appear if a user tries to input a number greater than 4. Let’s now see this action.</p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Time to enforce the rules of the guessing game.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">In the opening <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> tag, set:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">min</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"1"</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">The <code class="code__2rdF32qjRVp7mMVBHuPwDS">max</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"10"</code></li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## FORM VALIDATION

### Checking Text Length




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Checking Text Length</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In the previous exercise, we were able to use <code class="code__2rdF32qjRVp7mMVBHuPwDS">min</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">max</code> to set acceptable minimum and maximum values in a number field. But what about text fields? There are certainly cases where we wouldn’t want our users typing more than a certain number of characters (think about the character cap for messages on Twitter). We might even want to set a minimum number of characters. Conveniently, there are built-in HTML5 validations for these situations.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To set a minimum number of characters for a text field, we add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">minlength</code> attribute and a value to set a minimum value. Similarly, to set the maximum number of characters for a text field, we use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">maxlength</code> attribute and set a maximum value. Let’s take a look at these attributes in code: </p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form</span><span class="mtk1"> </span><span class="mtk7">action</span><span class="mtk1">=</span><span class="mtk8">"/example.html"</span><span class="mtk1"> </span><span class="mtk7">method</span><span class="mtk1">=</span><span class="mtk8">"POST"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"summary"</span><span class="mtk4">&gt;</span><span class="mtk1">Summarize your feelings in less than 250 character</span><span class="mtk1">s</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"summary"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"summary"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"text"</span><span class="mtk1"> </span><span class="mtk7">minlength</span><span class="mtk1">=</span><span class="mtk8">"5"</span><span class="mtk1"> </span><span class="mtk7">maxlength</span><span class="mtk1">=</span><span class="mtk8">"250"</span><span class="mtk1"> </span><span class="mtk7">required</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"submit"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Submit"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">If a user tries to submit the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> with less than the set minimum, this message appears:</p>
<p class="p__1qg33Igem5pAgn4kPMirjw"><img src="https://content.codecademy.com/courses/learn-html-forms/minlength.png" alt="prompt on a number field for user to length the input" class="img__1JGFO2nlisObc3KeOSGPRp"></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">And if a user tries to type in more than the maximum allowed number of characters, they don’t get a warning message, but they can’t type it in! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s add this validation to our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>. </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">For the login <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>, we want our users to have usernames that are at least 3 characters and at most 15. Let’s add this validation to our current  <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To  the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"username"</code>, add the following attributes and values:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">minlength</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"3"</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">maxlength</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"15"</code></li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">We also want passwords to have at least 8 characters and at most 15. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">So, in the opening <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> tag that has an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"pw"</code>, add:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">minlength</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"8"</code></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">maxlength</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"15"</code></li>
</ul>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 3 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div></div></div>


**Solutions**


```html

```




## FORM VALIDATION

### Matching a Pattern




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Matching a Pattern </span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">In addition to checking the length of a text, we could also add a validation to check how the text was provided. For cases when we want user input to follow specific guidelines, we use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">pattern</code> attribute and assign it a <em>regular expression</em>, or regex. Regular expressions are a sequence of characters that make up a search pattern. If the input matches the regex, the form can be submitted.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s say we wanted to check for a valid credit card number (a 14 to 16 digit number). We could use the regex: <code class="code__2rdF32qjRVp7mMVBHuPwDS">[0-9]{14,16}</code> which checks that the user provided only numbers and that they entered at least 14 digits and at most 16 digits. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To add this to a form:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;form</span><span class="mtk1"> </span><span class="mtk7">action</span><span class="mtk1">=</span><span class="mtk8">"/example.html"</span><span class="mtk1"> </span><span class="mtk7">method</span><span class="mtk1">=</span><span class="mtk8">"POST"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;label</span><span class="mtk1"> </span><span class="mtk7">for</span><span class="mtk1">=</span><span class="mtk8">"payment"</span><span class="mtk4">&gt;</span><span class="mtk1">Credit Card Number (no spaces):</span><span class="mtk4">&lt;/label&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;br&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">id</span><span class="mtk1">=</span><span class="mtk8">"payment"</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"payment"</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"text"</span><span class="mtk1"> </span><span class="mtk7">required</span><span class="mtk1"> </span><span class="mtk7">pattern</span><span class="mtk1">=</span><span class="mtk8">"[0-9]{14,16}"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;input</span><span class="mtk1"> </span><span class="mtk7">type</span><span class="mtk1">=</span><span class="mtk8">"submit"</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"Submit"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk4">&lt;/form&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">With the <code class="code__2rdF32qjRVp7mMVBHuPwDS">pattern</code> in place, users can’t submit the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> with a number that doesn’t follow the regex. When they try, they’ll see a validation message like so:</p>
<img src="https://content.codecademy.com/courses/learn-html-forms/pattern.png" alt="message prompting user to follow the requested format" width="100%" class="img__1JGFO2nlisObc3KeOSGPRp">

<p class="p__1qg33Igem5pAgn4kPMirjw">If you want to find out more about Regex, read more at the <a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/resources/docs/javascript/regexp?page_ref=catalog">Docs RegEx</a> entry.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To see it in practice, let’s use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">pattern</code> attribute in our HTML! </p>
</div></div></div>




**Instructions** 


<div><div aria-hidden="false"><div class="checkpoint__Mmv3yv-wu7NJCX0vgcy0h" data-testid="checkpoint-satisfied"><b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b><div class="checkpointBody__3Sn4jghNHiScLJ7-zmcXUk"><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">We might also want to limit usernames to only letters and numbers (and not special characters like ! or @).</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To add this validation,  add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">pattern</code> attribute and set it to: <code class="code__2rdF32qjRVp7mMVBHuPwDS">"[a-zA-Z0-9]+"</code> in the first <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element.</p>
</div></div></div><div class="checkpointCheckbox__vmGdbkCMW4Z7ET3KCrCJP checkboxSatisfied__1xX8YQAWCZp7OxlyblPKiC"><div class="gamut-xz9pfx-HiddenText e88fw8k0"><span aria-live="assertive">Checkpoint 2 Passed</span></div><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></div></div>


**Solutions**


```html

```




## FORM VALIDATION

### Review




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Form Validation</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Review</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Awesome job adding client-side validation to <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>s! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s quickly recap:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Client-side validations happen in the browser before information is sent to a server.  </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Adding the <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> attribute to an input related element will validate that the input field has information in it.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Assigning a value to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">min</code> attribute of a number input element will validate an acceptable minimum value. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Assigning a value to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">max</code> attribute of a number input element will validate an acceptable maximum value. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Assigning a value to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">minlength</code> attribute of a text input element will validate an acceptable minimum number of characters. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Assigning a value to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">maxlength</code> attribute of a text input element will validate an acceptable maximum number of characters. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Assigning a regex to <code class="code__2rdF32qjRVp7mMVBHuPwDS">pattern</code> matches the input to the provided regex.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">If validations on a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> do not pass, the user gets a message explaining why and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> cannot be submitted.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">These quick checks help ensure that input data is correct and safe for our servers. It also helps give users immediate feedback on what they need to fix instead of having to wait for a server to send back that information.</p>
</div></div></div>




## BUILDING INTERACTIVE WEBSITES

### Form a Story




<div class="gamut-1h3qpnn-Box ebnwbv90"><div aria-hidden="true" class="gamut-haybot-Text e8i0p5k0">Building Interactive Websites</div><span aria-hidden="true" class="gamut-yj8jvy-Text e8i0p5k0">Form a Story</span><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12"><p class="p__1qg33Igem5pAgn4kPMirjw">Forms are great for collecting information on users, like job applications or insightful surveys. However, we can also stretch our creative muscles and have a little fun with forms. For this project, we’ll use our knowledge of the HTML <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> and grab user input to put a spin on a classic story! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">The logic for parsing and inserting of user inputs is already taken care of in <strong>main.js</strong> using JavaScript . We’ve also added some styling to the page in <strong>style.css</strong>. You can find these files by click on the folder icon located at the top of the code editor and selecting the files you’re interested in. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">What you have to do is now make a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> capable of collecting the correct information so that the newly crafted story makes sense!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Note: Save your code as you follow the steps to see your progress!</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you get stuck during this project, check out the <strong>project walkthrough video</strong> which can be found in the help menu.</p>
</div></div><div class="group__LspoGf1Fw0-ac_AUnuvRV"></div></div>




**Instructions** 


<div class="tasks__2zeiH_BHmhuJBXUlJC3X0R"><span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as complete by checking them off</span><h2 class="fit-full fcn-task-header">Adding The Form</h2><div><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 1" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-1-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-1">1.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">We’ll be collecting information from our users using a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> so, first, we have to add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> under the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;hr&gt;</code> element inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;body&gt;</code> of <strong>index.html</strong>.   </p>
</div></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 2" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-2-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-2">2.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> an <code class="code__2rdF32qjRVp7mMVBHuPwDS">action</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"story.html"</code> and a <code class="code__2rdF32qjRVp7mMVBHuPwDS">method</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"GET"</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">We’ll be sending information from our form to <strong>story.html</strong> using a GET request. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 3" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-3-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-3">3.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>, create a submit button by adding an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"submit"</code>. Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"Form My Story!"</code>. Save your code to see the button rendered.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">This might seem counterintuitive, but by creating this submit button and submitting the form as you add more code, you can see how the final result of the story evolves and debug in smaller chunks. Check the hint for more debugging tips! </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article></div><h2 class="fit-full fcn-task-header">Adding Text Input</h2><div><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 4" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-4-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-4">4.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now we can populate our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> with <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> elements that allow users to type in their responses. We’ll also want to have associated <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>s with these <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> elements so users know what they’re filling in. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element and assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"animal-1"</code>. Have the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> render the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Animal:</code> on the webpage. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Write your code so that the submit button always shows up at the bottom of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>. As you add more code, the submit button should be kept at the bottom. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 5" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-5-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-5">5.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Now we can create an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> to associate our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element with.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"animal-1"</code> and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code>. Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"animal-1"</code>. Remember, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> attribute is needed for information from this <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> to be sent with the form during submission.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Speaking of submission, since we want our users to put in some value, add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> attribute to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 6" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-6-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-6">6.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">We’re going to be adding more <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>s and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>s so we should add some spacing. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Below the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element, add a line break using <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;br&gt;</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">With the first input field and working submit button, type some text into the field and submit it! Remember, in order for you to see the new code rendered on the browser, you’re going to need to save your code. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 7" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-7-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-7">7.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Our story has quite a few blanks, so we’re going to need a lot more <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>s and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>s.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"animal-2"</code> that renders <code class="code__2rdF32qjRVp7mMVBHuPwDS">Another Animal:</code> to the webpage. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Underneath the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>, create a new <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> with the attributes: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"animal-2"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;br&gt;</code> for a line break. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 8" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-8-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-8">8.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">There’s another animal in our story, so let’s add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"animal-3"</code> that renders <code class="code__2rdF32qjRVp7mMVBHuPwDS">One More Animal:</code> to the webpage. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then, add a new <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> with the attributes: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"animal-3"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Remember to add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;br&gt;</code> for a line break. </p>
</div></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 9" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-9-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-9">9.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s have our users provide an adjective.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"adj-1"</code> that renders the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Adjective (ends in -ed):</code> to the webpage. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then, add a new <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> with the attributes: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"adj-1"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add another line break.</p>
</div></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 10" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-10-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-10">10.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s get a verb.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Create a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"verb-1"</code> that renders the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Verb (ends in -ing):</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Follow the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> with the attributes: </p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"verb-1"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code></li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Also, add a line break. </p>
</div></div></div></article></div><h2 class="fit-full fcn-task-header">Other Inputs</h2><div><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 11" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-11-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-11">11.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Great, we have some <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>s set up that accept text, but we can use some <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> with different <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code>s in our <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code>.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Let’s add a field that will accept a number. First add <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"num-1"</code>that renders the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Number:</code> to the webpage. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> element, add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> that has:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx"><code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"num-1"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"number"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> attribute.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Also, add a line break.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 12" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-12-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-12">12.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">One of our blanks requires a “yes” or “no” answer— sounds like we can use some radio buttons for that.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Before we can add the radio buttons, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;span&gt;</code> element that has the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Yes or No:</code>.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 13" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-13-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-13">13.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">For radio buttons, we want to add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> before the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>  to render the radio button on the left of the text. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element with the following attributes:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"yes"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"radio"</code>. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"answer"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"yes"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> attribute.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Under the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute assigned a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"yes"</code> that renders the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Yes</code> on the webpage. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 14" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-14-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-14">14.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">We should now add a radio button that represents the “no” choice. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element that has the following attributes:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"no"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"radio"</code>. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"answer"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"no"</code>.</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Under the just added <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>, add another <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute assigned a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"no"</code> that renders the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">No</code> on the webpage. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">This time, add a line break! </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 15" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-15-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-15">15.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">The story that we’re creating this <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> for involves some sort of speed, so let’s give our users a dropdown list of speed options. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Create a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> and set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"speed"</code>. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> should render the text: <code class="code__2rdF32qjRVp7mMVBHuPwDS">Relative speed (ends in -er):</code></p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> element with an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"speed"</code>. Add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> attribute to make this field mandatory. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Insert a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;br&gt;</code> after the closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> tag. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> element will be empty for now. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 16" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-16-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-16">16.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;select&gt;</code> add a few <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code>s for users to choose from.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">One example of an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> you could include is:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"faster"</span><span class="mtk4">&gt;</span><span class="mtk1">Faster</span><span class="mtk4">&lt;/option&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add as many or as few as you’d like! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Remember to assign a <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code> and include text between the opening and closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code> tags. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 17" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-17-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-17">17.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">One of our story’s blank requires a quote. We could provide our users with a few options but also give them the choice of adding their own custom quote. To do this, we can use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> element.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">To set up the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> we need an accompanying <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Under the last <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;br&gt;</code>,  add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> with a <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"quote"</code>. Have the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> render the text <code class="code__2rdF32qjRVp7mMVBHuPwDS">Motivational Quote:</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">After the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code>, add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> with the follow attributes:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> assigned a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"quote"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">the <code class="code__2rdF32qjRVp7mMVBHuPwDS">type</code> set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">"text"</code>.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> attribute.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">a <code class="code__2rdF32qjRVp7mMVBHuPwDS">list</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"quote-choices"</code>.</li>
</ul>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 18" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-18-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-18">18.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Awesome, we should add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> now under the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;input&gt;</code> element. Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"quote-choices"</code>. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;br&gt;</code> after the closing <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> tag.</p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 19" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-19-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-19">19.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Let’s add a few <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;option&gt;</code>s with <code class="code__2rdF32qjRVp7mMVBHuPwDS">value</code>s within the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;datalist&gt;</code> element. For example:</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;option</span><span class="mtk1"> </span><span class="mtk7">value</span><span class="mtk1">=</span><span class="mtk8">"winner gets ice cream!"</span><span class="mtk4">&gt;&lt;/option&gt;</span></span><br></div></code></pre></pre>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 20" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-20-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-20">20.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Every good story has a key takeaway, so let’s finish off this <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> by having our users provide this message! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> that has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">for</code> attribute of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"message"</code>. Have the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> render <code class="code__2rdF32qjRVp7mMVBHuPwDS">Meaningful Message:</code> on the web page. </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Under the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;label&gt;</code> add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> that has an <code class="code__2rdF32qjRVp7mMVBHuPwDS">id</code> and <code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code> of <code class="code__2rdF32qjRVp7mMVBHuPwDS">"message"</code>. Make the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> a <code class="code__2rdF32qjRVp7mMVBHuPwDS">required</code> field. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> should have 8 rows and 40 columns. (Check the hint for a syntax reminder).</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Then add a line break after the <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;textarea&gt;</code> element. </p>
</div></div></div><div class="hintAccordion__9ohWFNq_viHGmKzOyh-M3"><button aria-expanded="false" class="basicBtn__2_xxdSYwVIY18Fd5pq9JgS accordionButton__3LbMIquV93ec6TYv2l6mjX yellow__2olEZaNZdnw4sc3pSwo39e" data-btn="true"><span class="children__3aFTNwOnkG0i7uCSFwvYT5"><div class="accordionHeader__10Sfx7s_OzXLjiFtCNI7ZV">Stuck? Get a hint</div></span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="expansionIcon__3EAlubPR6T3-MPaeVEwyjl gamut-sd6ku5-Svg eol2zvm0"><title>Arrow Chevron Down Icon</title><path d="M23.25 7.311L12.53 18.03a.749.749 0 01-1.06 0L.75 7.311" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg></button><div class="gamut-1j727xk-StyledAccordionBody eg6ri2w0" style="height: 0px;"></div></div></article></div><h2 class="fit-full fcn-task-header">Project Extras</h2><div><article class="fit-full fcn-task fcn-task--complete"><div class="gamut-1m02y73-FlexBox e1tc6bzh0"><div class="gamut-1efsrtw-Box ebnwbv90"><div aria-checked="true" aria-label="Task item 21" class="fcn-task__check fcn-task__check--checked centeredCheckbox__2QQhtR9gO-52xrQs_8ZEjS" data-cue="discovery-checklist" role="checkbox" tabindex="0" data-testid="task-21-checkbox"><svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0"><title>Check Icon</title><path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path></svg></div></div><div class="gamut-dtzm1a-Box ebnwbv90"><span class="fcn-task__number" data-testid="task-21">21.</span></div><div><div data-testid="markdown" class="spacing-tight__2Gp7GTqG0TykPQ18OnUOVt markdown__1eeYJ4WPKUcvX_LDDGJR12 narrativeMarkdown__1UywfcBd-60XKky6qUHIYA scrollable___DFOWZAyFa-jr7fZML66U"><p class="p__1qg33Igem5pAgn4kPMirjw">Fantastic job creating a <code class="code__2rdF32qjRVp7mMVBHuPwDS">&lt;form&gt;</code> to fill in a story! </p>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you want to challenge yourself:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add pre-selected values for each input field.</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add placeholder text that contains examples for users. </li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add some extra validations like <code class="code__2rdF32qjRVp7mMVBHuPwDS">min</code>, <code class="code__2rdF32qjRVp7mMVBHuPwDS">minlength</code>, or <code class="code__2rdF32qjRVp7mMVBHuPwDS">pattern</code> to the elements that accept user input. </li>
</ul>
</div></div></div></article></div></div>


**Solutions**


```html

```




## Review: Building Interactive Websites




<div data-testid="markdown" class="spacing-loose__3_R8mSIQ2cspwhDGkCOXTu markdown__1eeYJ4WPKUcvX_LDDGJR12 darkTheme__2i0sjr_RjoITRh35Ld2GzM gamut-gk1onf-ArticleMarkdown e1xfx7rd0"><p class="p__1qg33Igem5pAgn4kPMirjw">Congratulations! The goal of this unit was to use JavaScript to create interactive websites that will respond to input from the user.</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">Having completed this unit, you are now able to:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Add JavaScript to a website for interactivity</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Describe what the DOM is</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Explain what DOM Events are</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Create forms using HTML and validate them using JavaScript</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">If you are interested in learning more about these topics, here are some additional resources:</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Article: <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html">How To Add JavaScript to HTML
</a></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Article: <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation">MDN Guide to Client-side form validation</a></li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">Book: <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://bookshop.org/books/html-and-css-design-and-build-websites/9781118008188">HTML &amp; CSS</a>, Jon Duckett, Chapter 7 (pp. 144-174)</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">Whatever you’re working on, be sure to connect with the Codecademy community in the <a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/">forums</a>. Remember to check in with the community regularly, including for things like code review on your project work and what material you will need to accomplish your goals.</p>
</div>




