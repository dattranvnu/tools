## Introduction: Making a Website Responsive

<p class="p__1qg33Igem5pAgn4kPMirjw">
The goal of this unit is to utilize responsive web design practices. You
will learn how to create websites that can be viewed on a variety of
devices and use different layouts and positioning.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
After this unit, you will be able to:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Understand responsive web design
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Use CSS Grid and Flexbox for layout, positioning, and responsiveness
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Use media queries
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You will put all of this knowledge into practice with an upcoming
Challenge Project. You can complete the Challenge Project either in
parallel with or after taking the prerequisite content—it’s up to you!
</p>
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

## GRIDS AND SPACING

### Introduction

<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Grids</em> are made up of intersecting horizontal and vertical
lines. For instance, if you look at a city map, you’ll notice streets
crossing paths and forming a clear structure to the city’s layout. This
is because a lot of them were designed and built using a grid system.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As a designer, <em>grid systems</em> help you organize your designs and
provide a series of guidelines to properly align elements on a page.
Using this visual layout system can help easily define the space needed
between elements, while creating content that guides the user on how to
navigate the web page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Grids can also promote consistency, allowing you to build repeated
patterns to carry throughout your designs. Through the use of
repetition, the learning curve of using your website can be
significantly reduced allowing users to clearly navigate and consume the
content.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s explore the different parts of a grid system and discuss how it
can help enhance your designs with consistency, alignment, and spacing.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
To the right is an example website that uses a grid system. Notice how
the different pieces of content are laid out on the page and how the
design makes use of columns and rows.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Move on to the next exercise when you’re ready!
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Grid Types

<p class="p__1qg33Igem5pAgn4kPMirjw">
Various types of grids exist and are used within all types of visual
design. With the creation of the printing press, bookmakers developed a
manuscript-style grid, or a <em>block grid</em>, to bring structure to
text on pages. Within news design, the <em>column grid</em> allowed
publishers to break the page apart into sections to emphasize different
pieces of content.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Similar to news design, the most common type of grid a web designer will
use is the column grid. The column grid breaks up a page into vertical
units that span the width of the content, and this grid structure can
dictate how elements are laid out with precision and elegance.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s continue to explore the anatomy of a grid and what it comprises.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Examine the diagram in the right view. Note how the columns span the web
page evenly on the horizontal axis. By using a column-based layout, it
allows designers to evenly space content horizontally while seeing how
their layouts stack vertically.
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Grid Anatomy

<p class="p__1qg33Igem5pAgn4kPMirjw">
When designing a website, the grid comprises three major components:
columns, gutters, and margins.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Columns are defined as the vertical sections that span the width of a
page. In web design, it’s common to see layouts consisting of 12 or 16
columns, while other may only feature three columns. Defining the number
of columns depends on what’s appropriate for your design, device, and or
screen viewing size.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, a gutter is the negative space between each column. Gutters help
in ensuring the columns don’t run together, which would negate the
purpose of using a column-based grid.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Margins appear on the left and right sides of the column-based grid.
These ensure the content of your designs doesn’t match up to the edges
of the browser window.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It’s important to note, margins may vary depending on the width of the
grid, browser window, or device. For larger displays, margins may be
very noticeable while on smaller screens, they may have the same width
as a gutter.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Examine the diagram to the right. Note the three major components we
reviewed in this exercise. Notice how the columns have a gap of space
between each column as well as how the grid doesn’t bump up against the
side of the web page.
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Grid Columns

<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Columns</em> are the vertical containers that span the width of the
page. They can be dependent on each other, meaning they are used to
organize related content such as a continuation of a paragraph. They can
also be independent of each other, meaning they are used for organizing
the layout of unrelated content such as a sidebar. This allows for the
flexibility of organizing information.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Within a grid, content can span multiple columns. What this means is
that a website does not need to maintain the same column layout
throughout. For example, a section of a website with a 12 column grid
can have content that spans 4 columns, three times.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As the designer, you have the option to maintain this layout throughout
the website. Or you can choose to use various layouts, including having
the content span the whole width of the grid, half the grid or only a
small portion of the grid.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
While we will talk about this in more detail in just a few exercises,
columns are separated by gutters. This design term is referred to as the
space or gap between two columns. No content can spill into the gutter
unless it is using the next column.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Columns can also be used to push, or offset content. Say you want to
only display content on the right 4 columns of a page while using a 12
column grid. To do this, you can easily offset the content by 8 columns
so the content is pushed to those right 4 columns.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the diagram to the right, notice how the content of the web page
spans a specific set of columns but doesn’t overflow into the gutter?
This is what makes grids so great for design. They allow you to quickly
create web designs that snap together in an efficient and systematic
way.
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Grid Rows

<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Rows</em> are the horizontal lines on a grid. Think of rows as
invisible boxes that group content together by height. Rows are commonly
used in web designs to group content together and re-order other content
to allow for more whitespace.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, let’s say you have a set of items that all span the same
amount of columns and you want them to align across the page without
being disrupted by other elements. One way to achieve this outcome is to
wrap the content in a row component. This will force any content, not
inside of the row, to be pushed away.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Again, remember that a row can be used to force content away from an
area that has remaining columns not used. What does this mean? Great
question.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s say our design uses a 12 column grid and we want one element to
span seven columns. That means we still have five unfilled columns to
either the left or the right side. Naturally, any new content added to
our document will try and fill this unused space. However, by placing a
row element around our component that spans 7 columns we can force any
new content to start beneath our component and leave the remaining 5
columns empty.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Check out the diagram to the right. Notice how the row wraps around the
different components like a box.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Also, note how it forces content that is not within the box below it.
For instance, in the first row, the logo, the gutter, and the navigation
bar span the entirety of the first row. Therefore, the next element must
go in the second row.
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Grid Gutters

<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Gutters</em> make up the negative space between columns. This design
element helps to provide a natural break between elements aligned
horizontally, while also helping to break rows of content vertically.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note, there will always be one less gutter than the total number of
columns. For example, if you are designing on a 12 column grid, then you
will only have 11 gutters, one for every gap that separates each column.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
While there is no set standard for a gutter width, it’s best practice to
select a size that visually separates horizontal columns but is
significantly thinner than the width of a column. The same can be said
for vertical gutters.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Moreover, vertical and horizontal gutters do not need to match in size
for a given grid layout. This is because you as a designer may want more
vertical spacing than horizontal spacing when separating elements on a
page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember, if the gutter space is too tight, it can be hard to visually
tell where one element ends and another starts. On the other hand, if
the gutter space is too large, the design can be hard to follow.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the diagram to the right, notice the gutters between each column. The
gutter size can vary from project to project but should provide enough
space to keep the design feeling natural and allow the user to visually
see the separation of content on the page.
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Responsive Grid

<p class="p__1qg33Igem5pAgn4kPMirjw">
When designing web content, a designer needs to take into account the
different screen-sizes a user might encounter and how that will affect a
website’s layout. Many websites utilize <em>responsive design</em>, a
set of techniques that allow a website’s content to shift based on the
device or screen size. Because of these changes, responsive design
requires a different number of total columns based on screen size, in
order to accommodate content and keep it from being squished.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Consider your mobile, tablet and desktop devices. Now, think about their
viewable areas. All are substantially different in size. Thus, it’s
common practice in web design to create responsive grid sizes. On a
large or desktop device you may start with a 12 column grid, but on a
small or mobile device, you adjust the 12 column grid to a 4 column
grid.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As a designer, responsive grid design enables you to maximize the
content on the screen, ensuring a more accessible experience for users.
Additionally, your design elements will have sufficient space to breathe
and content can naturally flow across the page.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Check out the diagrams to the right. Notice how we have adjusted the
total number of columns based on the viewport size. By adjusting the
columns as the viewport becomes smaller, we can rearrange content to
better fit the viewing size.
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Whitespace

<p class="p__1qg33Igem5pAgn4kPMirjw">
Space is an important aspect of creating balanced and harmonious layouts
in web design. As a designer, it’s important to understand how space can
enhance as well as hurt your designs.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<em>Whitespace</em>, or negative space, refers to the emptiness between
elements, whether that’s in the gutter of the columns, or additional
padding around a block of text. As a designer, don’t be afraid of using
space to enhance the usability of your site and prioritize the content.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s explore some examples of good whitespace. If you look at the
examples in the workspace, you will notice that the website on the left
embraces whitespace on its landing page. It focuses the user’s attention
solely on the primary action, which is searching for content. In this
case, the whitespace is white in color as well. However, whitespace
isn’t always going to be white.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example on the right, you’ll notice that too much whitespace can
negatively impact the flow of your site. By including too much spacing
in between elements, it can cause issues for users trying to navigate
seamlessly through the content.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Whitespace is broken up into passive and active, which we’ll explore in
the next two exercises!
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice how the two web pages utilize whitespace, and which one does it
more effectively.
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Passive Whitespace

<p class="p__1qg33Igem5pAgn4kPMirjw">
The first type of whitespace we will discuss is called <em>passive
whitespace</em> or <em>micro whitespace</em>. Used to improve the
aesthetics of the layout without guiding the user through a specific
reading, flow, or content order; passive whitespace is sometimes
referred to as the unconsidered space. The most frequent use of passive
whitespace comes within text elements.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Different font families have varying amounts of passive whitespace and
you can control aspects of them within your design by altering CSS
properties such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">line-height</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">margin</code> when setting
type.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By adjusting the space between your lines of text, you can improve the
design’s overall legibility and balance.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If a site’s text is too tight or lacks sufficient margin below headings
and paragraphs, it can be hard for users to consume the content.
However, if the site’s text is too spaced out, it can make it just as
hard to read.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Finding a healthy balance between text that lacks sufficient spacing and
text that has too much is an important task for designers.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the diagram to the right, notice the difference in space between the
two paragraphs. The text on the left has very little line-height or
spacing between lines of text. However, the example on the right has a
large amount of line-height.
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Active Whitespace

<p class="p__1qg33Igem5pAgn4kPMirjw">
Unlike passive whitespace, which occurs more naturally, <em>active
whitespace</em> is intentional. Also called <em>macro whitespace</em>,
active whitespace refers to enhancing the overall page structure through
space to emphasize content or guide users from one point to the next.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By adding active whitespace to a site’s design, we can spread our
different sections out. This technique helps guide the user through the
page’s content more effectively, allowing users to consume and absorb
content more easily.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Active whitespace comes in many forms. But traditionally, it is achieved
by adding space between a site’s elements. For instance, adding space to
an article’s sidebar helps to visually separate the content from the
page’s main content.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Additionally, this type of whitespace allows readers to quickly
understand what they should be focusing on versus what is just
supplementary details.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the diagram to the left, notice how the example on the left is very
tight. There is not a lot of space that separates the various sections
of the page. This type of layout makes it hard for users to find the
information that they’re looking for. However, the image on the right
has plenty of active whitespace built in. This design allows users to
find natural breakpoints in the page and identify what information
belongs together and what does not.
</p>

**Solutions**

``` html
```

## GRIDS AND SPACING

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
Congratulations! You should have an understanding of grid structure, the
components that make up a grid, and how to use them to properly space
elements within your design.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember, the reasons we design using grids are:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Promote consistency within our designs
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Properly align elements on our page
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Provide ample spacing between content
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember a grid is made up of:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Columns
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Gutters
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Margins
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Spacing is incredibly important within a design to ensure:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Elements have ample room to breathe
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Denote emphasis on certain parts of a page
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Promote harmonious patterns and rhythms within your designs
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Following these guidelines will allow you to create elegant and usable
sites!
</p>

## FLEXBOX

### What is Flexbox?

<p class="p__1qg33Igem5pAgn4kPMirjw">
CSS provides many tools and properties that you can use to position
elements on a webpage. Codecademy’s lessons on the box model and CSS
display introduce a couple of these techniques.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, you will learn about Flexible Box Layout or
<em>flexbox</em>, a tool that greatly simplifies how to position
elements.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are two important components to a flexbox layout: <em>flex
containers</em> and <em>flex items</em>. A flex container is an element
on a page that contains flex items. All direct child elements of a flex
container are flex items. This distinction is important because some of
the properties you will learn in this lesson apply to flex containers
while others apply to flex items.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To designate an element as a flex container, set the element’s
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-flex</code>. Once an
item is a flex container, there are several properties we can use to
specify how its children behave. In this lesson we will cover these
properties:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-flow</code>
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Flexbox is an elegant tool that makes it easy to address positioning
issues that may have been difficult before. Let’s get started!
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the browser to the right, scroll down until you see the phrase “Our
Expertise” in the div with the yellow background. Stretch and shrink the
browser and observe how the elements change position to fit in the width
of the page.
</p>

**Solutions**

``` html
```

## FLEXBOX

### display: flex

<p class="p__1qg33Igem5pAgn4kPMirjw">
Any element can be a flex container. Flex containers are helpful tools
for creating websites that respond to changes in screen sizes. Child
elements of flex containers will change size and location in response to
the size and position of their parent container.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For an element to become a flex container, its
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property must
be set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">div</span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, all divs with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">container</code> are flex
containers. If they have children, the children are flex items. A div
with the declaration <code class="code__2rdF32qjRVp7mMVBHuPwDS">display:
flex;</code> will remain block level — no other elements will appear on
the same line as it.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
However, it will change the behavior of its child elements. Child
elements will not begin on new lines. In the exercises that follow, we
will cover how the flex
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property
impacts the positioning of child elements.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> with id
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property with
a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>.
Compare the two divs in the browser.
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

## FLEXBOX

### inline-flex

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous exercise, you might have observed that when we gave a
div — a block level element — the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> that it remained
a block level element. What if we want multiple flex containers to
display inline with each other?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If we didn’t want div elements to be block-level elements, we would use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display: inline</code>.
Flexbox, however, provides the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-flex</code> value for
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property,
which allows us to create flex containers that are also inline elements.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">I’m inside of a&nbsp;flex container!</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">A flex container’s children are flex items!</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">I’m also a&nbsp;flex item!</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;p&gt;</span><span class="mtk1">Me too!</span><span class="mtk4">&lt;/p&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">inline-flex</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, there are two container divs. Without a width,
each div would stretch the entire width of the page. The paragraphs
within each div would also display on top of each other because
paragraphs are block-level elements.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When we change the value of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-flex</code>, the divs
will display inline with each other if the page is wide enough. As we
progress through this lesson, we will cover in more detail how flex
items are displayed.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice that in the example above, the size of the flex container is set.
Currently, the size of the parent container will override the size of
its child elements. If the parent element is too small, the flex items
will shrink to accommodate the parent container’s size. We’ll explain
why in a later exercise.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'child'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">1</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'child'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">2</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.child</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">inline-flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 150px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">auto</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.child</code> divs will take
up more width (300 pixels) than the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">container</code> div allows
(200 pixels). The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.child</code> divs will
shrink to accommodate the container’s size. In later exercises, we will
explore several ways to handle this.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-flex</code>.
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

## FLEXBOX

### justify-content

<p class="p__1qg33Igem5pAgn4kPMirjw">
In previous exercises, when we changed the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> value of
parent containers to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-flex</code>, all of
the child elements (flex items) moved toward the upper left corner of
the parent container. This is the default behavior of flex containers
and their children. We can specify how flex items spread out from left
to right, along the <em>main axis</em>. We will learn more about axes in
a later exercise.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To position the items from left to right, we use a property called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">justify-content</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">flex-end</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we set the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-end</code>. This will
cause all of the flex items to shift to the right side of the flex
container.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Below are five commonly used values for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-start</code> — all items
will be positioned in order, starting from the left of the parent
container, with no extra space between or before them.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-end</code> — all items
will be positioned in order, with the last item starting on the right
side of the parent container, with no extra space between or after them.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> — all items
will be positioned in order, in the center of the parent container with
no extra space before, between, or after them.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code> — items
will be positioned with equal space before and after each item,
resulting in double the space between elements.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-between</code> — items
will be positioned with equal space between them, but no extra space
before the first or after the last elements.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the definitions above, “no extra space” means that margins and
borders will be respected, but no more space (than is specified in the
style rule for the particular element) will be added between elements.
The size of each individual flex item is not changed by this property.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element with the id
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flexstart</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-start</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You won’t see any changes since
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-start</code> is the
default value;
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
Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element with the id
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flexend</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-end</code>.
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
Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element with the id
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>.
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
Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element with the id
<code class="code__2rdF32qjRVp7mMVBHuPwDS">spacearound</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Stretch and shrink the browser window to compare and contrast how the
elements in each div behave.
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
Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element with the id
<code class="code__2rdF32qjRVp7mMVBHuPwDS">spacebetween</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-between</code>.
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

## FLEXBOX

### align-items

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous exercise, you learned how to justify the content of a
flex container from left to right across the page. It is also possible
to align flex items vertically within the container. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
makes it possible to space flex items vertically.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">align-items</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">baseline</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
is set to <code class="code__2rdF32qjRVp7mMVBHuPwDS">baseline</code>.
This means that the baseline of the content of each item will be
aligned.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Below are five commonly used values for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-start</code> — all
elements will be positioned at the top of the parent container.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-end</code> — all
elements will be positioned at the bottom of the parent container.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> — the center of
all elements will be positioned halfway between the top and bottom of
the parent container.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">baseline</code> — the bottom
of the content of all items will be aligned with each other.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stretch</code> — if possible,
the items will stretch from top to bottom of the container (this is the
default value; elements with a specified height will not stretch;
elements with a minimum height or no height specified will stretch).
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
These five values tell the elements how to behave along the <em>cross
axis</em> of the parent container. In these examples, the cross axis
stretches from top to bottom of the container. We’ll learn more about
this in a future exercise.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You might be unfamiliar with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-height</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code> properties,
but you have used
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> before.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-height</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> are
properties that ensure an element is at least a certain size or at most
a certain size. You’ll see how these become useful as you move
throughout this lesson.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now you’re going to see each of the five values above in action!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element with id
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flexstart</code> an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
with the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-start</code>.
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
Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element with id
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flexend</code> an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
with the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-end</code>.
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
Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element with id <code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>
an <code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code>
property with the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>.
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
Assign the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>
element with id
<code class="code__2rdF32qjRVp7mMVBHuPwDS">baseline</code> an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
with the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">baseline</code>. How does the
behavior of these elements differ from those in other divs?
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
Take a look at the elements under “Stretch” at the bottom of the page.
Now, in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.left</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.center</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.right</code> ruleset, change
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> property to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-height</code> and observe
what happens to these elements.
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

## FLEXBOX

### flex-grow

<p class="p__1qg33Igem5pAgn4kPMirjw">
In Exercise 3, we learned that all flex items shrink proportionally when
the flex container is too small. However, if the parent container is
larger than necessary then the flex items will not stretch by default.
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> property
allows us to specify if items should grow to fill a container and also
which items should grow proportionally more or less than others.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'side'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">I’m on the side of the flex container!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'center'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">I'm in the center of the flex container!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'side'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">I'm on the other side of the flex container!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.side</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-grow</span><span class="mtk1">:</span><span class="mtk9"> 1</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.center</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-grow</span><span class="mtk1">:</span><span class="mtk9"> 2</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code> div has a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>, so its three
child divs will be positioned next to each other. If there is additional
space in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code> div (in
this case, if it is wider than 300 pixels), the flex items will grow to
fill it. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">.center</code>
div will stretch twice as much as the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.side</code> divs. For
example, if there were 60 additional pixels of space, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> div would
absorb 30 pixels and the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">side</code> divs would absorb
15 pixels each.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If a <code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> is set
for an element, it will not grow larger than that even if there is more
space for it to absorb.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
All of the previous properties we have learned are declared on flex
containers, or the parent elements. This property —
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> — is the
first we have learned that is declared on flex items.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Assign <code class="code__2rdF32qjRVp7mMVBHuPwDS">.top.side</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.top.center</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code>. Stretch and shrink
the browser.
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
Assign <code class="code__2rdF32qjRVp7mMVBHuPwDS">.middle.center</code>
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code>. Stretch and shrink
the browser again.
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
Assign <code class="code__2rdF32qjRVp7mMVBHuPwDS">.bottom.side</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.bottom.center</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code>. Shrink and stretch
the browser again. Compare the differences in behavior of all three
sections.
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

## FLEXBOX

### flex-shrink

<p class="p__1qg33Igem5pAgn4kPMirjw">
Just as the <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>
property proportionally stretches flex items, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> property
can be used to specify which elements will shrink and in what
proportions.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You may have noticed in earlier exercises that flex items shrank when
the flex container was too small, even though we had not declared the
property. This is because the default value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code>. However, flex items
do not grow unless the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> property is
declared because the default value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'side'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">I'm on the side of the flex container!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'center'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">I'm in the center of the flex container!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'side'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">I'm on the other side of the flex container!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.side</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-shrink</span><span class="mtk1">:</span><span class="mtk9"> 1</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.center</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-shrink</span><span class="mtk1">:</span><span class="mtk9"> 2</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.center</code> div will
shrink twice as much as the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.side</code> divs if the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code> div is too
small to fit the elements within it. If the content is 60 pixels too
large for the flex container that surrounds it, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.center</code> div will
shrink by 30 pixels and the outer divs will shrink by 15 pixels each.
Margins are unaffected by
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Keep in mind, minimum and maximum widths will take precedence over
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>. As with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> will only
be employed if the parent container is too small or the browser is
adjusted.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Assign <code class="code__2rdF32qjRVp7mMVBHuPwDS">.top.side</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Stretch and shrink the browser. Because the default value for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code>, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.top.center</code> div will
shrink but not as much as the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.side</code> divs.
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
Assign <code class="code__2rdF32qjRVp7mMVBHuPwDS">.middle.side</code> a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Stretch and shrink the browser. How do the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.middle</code> divs resize
differently than the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.top</code> divs?
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
Assign the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.bottom.center</code> div a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Shrink and stretch the browser again. How do the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.bottom</code> divs resize
differently than the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.top</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.middle</code> divs?
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

## FLEXBOX

### flex-basis

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous two exercises, the dimensions of the divs were
determined by heights and widths set with CSS. Another way of specifying
the width of a flex item is with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> property.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> allows us
to specify the width of an item before it stretches or shrinks.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'side'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">Left side!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'center'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">Center!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'side'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">Right side!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.side</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-grow</span><span class="mtk1">:</span><span class="mtk9"> 1</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-basis</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.center</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-grow</span><span class="mtk1">:</span><span class="mtk9"> 2</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-basis</span><span class="mtk1">:</span><span class="mtk9"> 150px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.side</code> divs will be 100
pixels wide and the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.center</code> div will be
150 pixels wide if the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code> div has
just the right amount of space (350 pixels, plus a little extra for
margins and borders). If the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code> div is
larger, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.center</code>
div will absorb twice as much space as the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.side</code> divs.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The same would hold true if we assigned
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> values to
the divs above as well.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grow.side</code> ruleset,
add a flex-basis of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">60px</code>.
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
In the same rule, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> value of
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
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.grow.center</code>
rule, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">3</code>.
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
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.shrink.side</code>
rule, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">300px</code>.
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
In the same rule, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> property
with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">3</code>.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">6.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.shrink.center</code>
rule, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> property
with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code>.
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
In the same rule, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> property
with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">150px</code>.
Now stretch and shrink the browser.
</p>

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

## FLEXBOX

### flex

<p class="p__1qg33Igem5pAgn4kPMirjw">
The shorthand <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>
property provides a convenient way for specifying how elements stretch
and shrink, while simplifying the CSS required. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> property allows
you to declare
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> all in one
line.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> <em>property</em>
is different from the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> <em>value</em>
used for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
property.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.big</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-grow</span><span class="mtk1">:</span><span class="mtk9"> 2</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-shrink</span><span class="mtk1">:</span><span class="mtk9"> 1</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-basis</span><span class="mtk1">:</span><span class="mtk9"> 150px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.small</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-grow</span><span class="mtk1">:</span><span class="mtk9"> 1</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-shrink</span><span class="mtk1">:</span><span class="mtk9"> 2</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-basis</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, all elements with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">big</code> will grow twice as
much as elements with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">small</code>. Keep in mind,
this doesn’t mean <code class="code__2rdF32qjRVp7mMVBHuPwDS">big</code>
items will be twice as big as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">small</code> items, they’ll
just take up more of the extra space.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The CSS below declares these three properties in one line.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.big</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex</span><span class="mtk1">:</span><span class="mtk9"> 2&nbsp;1 150px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.small</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex</span><span class="mtk1">:</span><span class="mtk9"> 1&nbsp;2 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> property to
declare the values for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> (in that
order) all in one line.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.big</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">:</span><span class="mtk9"> 2&nbsp;1</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> property to
declare <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>, but not
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.small</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex</span><span class="mtk1">:</span><span class="mtk9"> 1&nbsp;20px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> property to
declare <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code>. Note that
there is no way to set only
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> using 2
values.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The browser to the right has two flex containers, each with three flex
items. In <strong>style.css</strong>, examine the values for each of
these items. Notice that the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> values are
set for the blue divs.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Stretch the browser window to increase its width. Observe that once the
top outer <code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code>s reach
100 pixels wide, they begin to grow faster than the top center
<code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code>. Also notice that
once the bottom center
<code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code> reaches 100 pixels
wide, it begins to grow faster than the outer
<code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code>s.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now, shrink the browser window and notice that once the top center
<code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code> reaches 50 pixels
wide it begins to shrink faster than the outer
<code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code>s and when the
bottom outer <code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code>s
reach 75 pixels, they begin to shrink faster than the center
<code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <code class="code__2rdF32qjRVp7mMVBHuPwDS">#top .side</code>, all
three values for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> are
assigned individually. Refactor them to be declared in one line using
the shorthand <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>
property.
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
In <code class="code__2rdF32qjRVp7mMVBHuPwDS">#top .center</code>, all
three values for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> are
assigned individually. Refactor them to be declared in one line.
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
In <code class="code__2rdF32qjRVp7mMVBHuPwDS">#bottom .side</code>, all
three values for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> are
assigned individually. Refactor them to be declared in one line.
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
In <code class="code__2rdF32qjRVp7mMVBHuPwDS">#bottom .center</code>,
all three values for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> are
assigned individually. Refactor them to be declared in one line.
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

## FLEXBOX

### flex-wrap

<p class="p__1qg33Igem5pAgn4kPMirjw">
Sometimes, we don’t want our content to shrink to fit its container.
Instead, we might want flex items to move to the next line when
necessary. This can be declared with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> property.
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> property
can accept three values:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap</code> — child elements
of a flex container that don’t fit into a row will move down to the next
line
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap-reverse</code> — the
same functionality as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap</code>, but the order of
rows within a flex container is reversed (for example, in a 2-row
flexbox, the first row from a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap</code> container will
become the second in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap-reverse</code> and the
second row from the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap</code> container will
become the first in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap-reverse</code>)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">nowrap</code> — prevents
items from wrapping; this is the default value and is only necessary to
override a wrap value set by a different CSS rule.
</li>
</ol>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'item'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">We're going to wrap!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'item'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">We're going to wrap!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'item'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">We're going to wrap!</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">inline-flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-wrap</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">wrap</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 250px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, three flex items are contained by a parent flex
container. The flex container is only 250 pixels wide so the three 100
pixel wide flex items cannot fit inline. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap: wrap;</code>
setting causes the third, overflowing item to appear on a new line,
below the other two items.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> property is
declared on flex <em>containers</em>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#wrap</code> ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> property
with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap</code>.
Shrink and stretch the browser.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#nowrap</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> property
with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">nowrap</code>. Shrink and
stretch the browser.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#reverse</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> property
with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap-reverse</code>. Shrink
and stretch the browser.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code>. Stretch
and shrink the browser. What’s different this time?
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

## FLEXBOX

### align-content

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that elements can wrap to the next line, we might have multiple rows
of flex items within the same container. In a previous exercise, we used
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code>
property to space flex items from the top to the bottom of a flex
container. <code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code>
is for aligning elements within a single row. If a flex container has
multiple rows of content, we can use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code> to space
the rows from top to bottom.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Below are some of the more commonly used
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code> values:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-start</code> — all rows
of elements will be positioned at the top of the parent container with
no extra space between.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-end</code> — all rows of
elements will be positioned at the bottom of the parent container with
no extra space between.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> — all rows of
elements will be positioned at the center of the parent element with no
extra space between.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-between</code> — all
rows of elements will be spaced evenly from the top to the bottom of the
container with no space above the first or below the last.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code> — all
rows of elements will be spaced evenly from the top to the bottom of the
container with the same amount of space at the top and bottom and
between each element.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stretch</code> — if a minimum
height or no height is specified, the rows of elements will stretch to
fill the parent container from top to bottom (default value).
</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'child'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">1</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'child'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">2</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'child'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">3</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'child'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">4</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 400px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 400px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-wrap</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">wrap</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">align-content</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">space-around</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.child</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 150px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 150px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, there are four flex items inside of a flex
container. The flex items are set to be 150 pixels wide each, but the
parent container is only 400 pixels wide. This means that no more than
two elements can be displayed inline. The other two elements will wrap
to the next line and there will be two rows of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">div</code>s inside of the
flex container. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code> property
is set to the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code>, which
means the two rows of divs will be evenly spaced from top to bottom of
the parent container with equal space before the first row and after the
second, with double space between the rows.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Below, we will see each of the properties in action!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code> property
is declared on flex containers.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#flexstart</code> ruleset,
add an <code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-start</code> to position
the rows of elements at the top of the parent container.
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
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#flexend</code> ruleset, add
an <code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-end</code> to position
the rows of elements at the bottom of the parent container.
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
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#center</code> ruleset, add
an <code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> to position the
rows of elements at the center of the parent container.
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
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#between</code> ruleset, add
an <code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-between</code> to space
out all of the rows of elements evenly with equal space between each
row.
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
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#around</code> ruleset, add
an <code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code> to space
out all of the rows of elements evenly with equal space around each row.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">6.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.left, .center,
.right</code> ruleset, change the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> property to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-height</code>. What
happens to the flex items in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#stretch</code> container?
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

**Solutions**

``` html
```

## FLEXBOX

### flex-direction

<p class="p__1qg33Igem5pAgn4kPMirjw">
Up to this point, we’ve only covered flex items that stretch and shrink
horizontally and wrap vertically. As previously stated, flex containers
have two axes: a <em>main axis</em> and a <em>cross axis</em>. By
default, the main axis is horizontal and the cross axis is vertical.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The main axis is used to position flex items with the following
properties:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The cross axis is used to position flex items with the following
properties:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The main axis and cross axis are interchangeable. We can switch them
using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property. If we add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property and give it a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column</code>, the flex items
will be ordered vertically, not horizontally.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'item'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">1</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'item'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">2</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'item'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">3</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'item'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">4</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"item"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;h1&gt;</span><span class="mtk1">5</span><span class="mtk4">&lt;/h1&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-direction</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">column</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 1000px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the five divs will be positioned in a vertical
column. All of these divs could fit in one horizontal row. However, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column</code> value tells the
browser to stack the divs one on top of the other. As explained above,
properties like
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code> will
not behave the way they did in previous examples.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property can accept four values:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row</code> — elements will be
positioned from left to right across the parent element starting from
the top left corner (default).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row-reverse</code> — elements
will be positioned from right to left across the parent element starting
from the top right corner.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column</code> — elements will
be positioned from top to bottom of the parent element starting from the
top left corner.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column-reverse</code> —
elements will be positioned from the bottom to the top of the parent
element starting from the bottom left corner.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Below, we’ll investigate how these work.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property is declared on flex containers.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#row</code> ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row</code>.
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
Inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#row-reverse</code> ruleset,
add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row-reverse</code>.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#column</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column</code>.
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
Inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#column-reverse</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column-reverse</code>.
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
Change the <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>
property of <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
elements to be
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code>. Remember
to stretch and shrink the browser after each checkpoint so you can see
the effects.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">6.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, add an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code>.
</p>

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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">8.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.box</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> property
with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">1</code>. In
which direction do the elements grow?
</p>

<span aria-live="assertive">Checkpoint 9 Passed</span>

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

## FLEXBOX

### flex-flow

<p class="p__1qg33Igem5pAgn4kPMirjw">
Like the shorthand
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> property, the
shorthand <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-flow</code>
property is used to declare both the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
properties in one line.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-wrap</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">wrap</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-direction</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">column</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we take two lines to accomplish what can be done
with one.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-flow</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">column</span><span class="mtk9"> </span><span class="mtk5">wrap</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the first value in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-flow</code> declaration
is a <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
value and the second is a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> value. All
values for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> are
accepted.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-flow</code> property is
declared on flex containers.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#row-reverse</code>
ruleset, set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-flow</code> property to
have a direction of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row-reverse</code> and to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap</code> elements. You
should be able to accomplish this in one line.
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
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">#column</code>
ruleset, set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-flow</code> property to
give elements a direction of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column</code> and to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap</code> elements. You
should be able to accomplish this in one line.
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

## FLEXBOX

### Nested Flexboxes

<p class="p__1qg33Igem5pAgn4kPMirjw">
So far, we’ve had multiple flex containers on the same page to explore
flex item positioning. It is also possible to position flex containers
inside of one another.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'container'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'left'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;img</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'small'</span><span class="mtk1"> </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">'#'</span><span class="mtk4">/&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;img</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'small'</span><span class="mtk1"> </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">'#'</span><span class="mtk4">/&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;img</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'small'</span><span class="mtk1"> </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">'#'</span><span class="mtk1"> </span><span class="mtk4">/&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'right'</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;img</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">'large'</span><span class="mtk1"> </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">'#'</span><span class="mtk1"> </span><span class="mtk4">/&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">justify-content</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">center</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">align-items</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">center</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.left</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">inline-flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex</span><span class="mtk1">:</span><span class="mtk9"> 2&nbsp;1 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex-direction</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">column</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.right</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">inline-flex</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">flex</span><span class="mtk1">:</span><span class="mtk9"> 1&nbsp;2 400px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">align-items</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">center</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.small</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">auto</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.large</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 600px</span><span class="mtk1">;</span><span class="mtk9"> </span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">auto</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, a div with three smaller images will display from
top to bottom on the left of the page
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">.left</code>). There is also
a div with one large image that will display on the right side of the
page (<code class="code__2rdF32qjRVp7mMVBHuPwDS">.right</code>). The
left div has a smaller
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> but
stretches to fill more extra space; the right div has a larger
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> but
stretches to fill less extra space. Both divs are flex items
<em>and</em> flex containers. The items have properties that dictate how
they will be positioned in the parent container and how their flex item
children will be positioned in them.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ll use the same formatting above to layout the simple page to the
right.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.main</code>
ruleset, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.main</code>
ruleset, add an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.main</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code>.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column</code>.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">6.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>.
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
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, add an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>.
</p>

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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">8.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Repeat steps 4, 6, and 7 for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.child</code> ruleset.
</p>

<span aria-live="assertive">Checkpoint 9 Passed</span>

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

## FLEXBOX

### Review: Flexbox

<p class="p__1qg33Igem5pAgn4kPMirjw">
You should be proud of yourself! You have learned the most important
properties of flexbox. Flexbox is an art and a science; you can use it
to make laying out multiple elements a piece of cake. You know
everything necessary to begin using it in your own projects.
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display: flex</code> changes
an element to a block-level container with flex items inside of it.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display: inline-flex</code>
allows multiple flex containers to appear inline with each other.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code> is
used to space items along the main axis.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> is used to
space items along the cross axis.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> is used to
specify how much space (and in what proportions) flex items absorb along
the main axis.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code> is used to
specify how much flex items shrink and in what proportions along the
main axis.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> is used to
specify the initial size of an element styled with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> and/or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code> is used to
specify <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-basis</code> in one
declaration.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> specifies
that elements should shift along the cross axis if the flex container is
not large enough.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code> is used
to space rows along the cross axis.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code> is used
to specify the main and cross axes.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-flow</code> is used to
specify <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code> in one
declaration.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Flex containers can be nested inside of each other by declaring
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display: flex</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display: inline-flex</code>
for children of flex containers.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s apply a few of the properties you’ve learned to arrange one
section of the web page in the browser to the right!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
All of the images are inside of three column divs and the three column
divs are all inside of one large div called
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.cards</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.cards</code>
ruleset, add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
property with a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Now, inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.cards</code>
ruleset, set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> property to
have a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">wrap</code>.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.cards</code>
ruleset, set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property to have a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code>.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.col</code> ruleset,
set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
property to have a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-flex</code>.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">5.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.col</code> ruleset,
set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property to have a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column</code>.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">6.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.col</code> ruleset,
set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property to have a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-between</code>.
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

## WEB DEVELOPMENT FOUNDATIONS

### Flexbox: To-Do App

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you will follow step-by-step instructions to fix a
to-do web app. All of the HTML and most of the CSS is intact, however, a
few Flexbox values are missing.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In order to complete this project, you must know how to set an element’s
Flexbox properties.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We recommend that you review our Flexbox Lesson before beginning.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The website’s existing <strong>index.html</strong> and
<strong>style.css</strong> files are displayed in the text editor to the
right. Good luck!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you get stuck during this project, check out the <strong>project
walkthrough video</strong> which can be found in the help menu.
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
Start off by turning some of the elements into flex and inline-flex
containers.
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Turn elements with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">container</code> and elements
with the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">square</code>
into flex containers.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Turn elements with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">week</code> and elements with
the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">reminders</code>
into inline-flex containers.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To do this, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property with
a value of either <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex</code>
or <code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-flex</code>.
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
The elements inside the new inline-flex containers should grow to fill
the container. This is accomplished using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> property:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Elements with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">week</code> will get a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> property
with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">3</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Elements with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">reminders</code> will get a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code> property
with a value of <code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code>.
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

<span class="fcn-task__number" data-testid="task-3">3.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
We want the flex items with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">week</code> to be ordered
vertically, instead of horizontally.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.week</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-direction</code>
property with the value that orders the items in a column.
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
The items with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row</code> should move to the
next line when the container gets too small.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.row</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-wrap</code> property
with the value that moves items to the next row, while keeping their
order intact.
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
The items with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row</code> also need some
space:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.row</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with the value that adds space around each item.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Furthermore, the items with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">square</code> need to be
centered:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.square</code>
ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property with the value that centers the items in the container.
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
Lastly, the elements with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row</code> and elements with
the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">square</code> need
to be aligned vertically:
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the rulesets for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.row</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.square</code>, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
with the value that centers the items inside the container.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You did it! Great work. Now resize the browser to see your flex
properties in action!
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

## WEB DEVELOPMENT FOUNDATIONS

### Off-Platform Project: Tea Cozy

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you will create a fictional tea shop website on your
own computer.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We will provide a <em>design spec</em> and image assets to help you
along the way. A design spec is an image of a web page outlined with all
of its CSS properties and values. These are usually created by a
designer as a source of instructions for a web developer. This project
assumes that you will be able to reproduce the basic HTML and CSS with
little guidance.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The images and design spec you need to complete the project are listed
below.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Images:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/img-tea-cozy-logo.png">Logo</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/img-bedford-bizarre.jpg">Bedford
Bizarre</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/img-berryblitz.jpg">Berry
Blitz</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/img-donut.jpg">Donut</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/img-locations-background.jpg">Locations</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/img-mission-background.jpg">Background</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/img-myrtle-ave.jpg">Myrtle
Ave</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/img-spiced-rum.jpg">Spiced
Rum</a>
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Design Spec:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Click
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-4/img-tea-cozy-redline.jpg">here</a>
to access the design spec.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Good luck!
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
This project is intended to be completed on your own computer. The
resources above will help you get to the final outcome. There’s no
single, correct way to complete this project, so experiment and have
fun!
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

## GRID ESSENTIALS

### Introduction to Grids

<p class="p__1qg33Igem5pAgn4kPMirjw">
Using CSS, you can elegantly lay out elements on a web page. There is no
simple answer for how best to do this — depending on what content you
are trying to display, multiple different techniques can work well. The
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-css/lessons/box-model-intro/exercises/box-model-intro">Box
Model</a> and
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-css/lessons/css-display-positioning/exercises/html-flow">Display
and Positioning</a> explain some possible ways to style layout.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, we introduce a powerful tool called <em>CSS Grid</em>.
The <em>grid</em> can be used to layout entire web pages. Whereas
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-css/lessons/learn-flexbox-l/exercises/flexbox">Flexbox</a>
is mostly useful for positioning items in a one-dimensional layout, CSS
grid is most useful for two-dimensional layouts, providing many tools
for aligning and moving elements across both rows and columns.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By the end of this lesson, you will understand how to use these
properties to create grid layouts:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-area</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row-gap</code> /
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column-gap</code> /
<code class="code__2rdF32qjRVp7mMVBHuPwDS">gap</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> /
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code> /
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
That’s a lot to learn. But by the end, you’ll be a master at grid
positioning. Let’s start learning!
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
When you’re ready to dive into CSS Grid, move on to the next exercise.
</p>

**Solutions**

``` html
```

## GRID ESSENTIALS

### Creating a Grid

<p class="p__1qg33Igem5pAgn4kPMirjw">
To set up a grid, you need to have both a <em>grid container</em> and
<em>grid items</em>. The grid container will be a parent element that
contains grid items as children and applies overarching styling and
positioning to them.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To turn an HTML element into a grid container, you must set the
element’s <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
property to one of two values:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid</code> — for a
block-level grid.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">inline-grid</code> — for an
inline grid.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Then, you can assign other properties to lay out the grid to suit your
needs.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
To start, look at <strong>index.html</strong> to see all seven items in
the grid. The grid container is of class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Back in <strong>style.css</strong>, in the ruleset for elements that
have the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid</code>,
set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
property to <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Right now, we haven’t specified the number of rows or columns in our
grid, so every item is sitting on a new row. We’ll learn how to
structure grid rows and columns in the next couple of exercises.
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

## GRID ESSENTIALS

### Creating Columns

<p class="p__1qg33Igem5pAgn4kPMirjw">
By default, grids contain only one column. If you were to start adding
items, each item would be put on a new row; that’s not much of a grid!
To change this, we need to explicitly define the number of rows and
columns in our grid.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can define the columns of our grid by using the CSS property
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>.
Below is an example of this property in action:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 500px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> 100px 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This property creates two changes. First, it defines the number of
columns in the grid; in this case, there are two. Second, it sets the
width of each column. The first column will be 100 pixels wide and the
second column will be 200 pixels wide.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can also define the size of our columns as a percentage of the entire
grid’s width.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 1000px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> 20% 50%</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this example, the grid is 1000 pixels wide. Therefore, the first
column will be 200 pixels wide because it is set to be 20% of the grid’s
width. The second column will be 500 pixels wide.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can also mix and match these two units. In the example below, there
are three columns of width 20 pixels, 40 percent, and 60 pixels:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> 20px 40% 60px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice that in this example, the total width of our columns (120 pixels)
exceeds the width of the grid (100 pixels). This might make our grid
cover other elements on the page! In a later exercise, we will discuss
how to avoid overflow.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code> ruleset, use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
property to create three columns. Set the first column to be
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100px</code> wide, the second
to be <code class="code__2rdF32qjRVp7mMVBHuPwDS">50%</code> of the grid,
and the third to be
<code class="code__2rdF32qjRVp7mMVBHuPwDS">200px</code> wide.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice that this causes our grid items to go outside the boundaries of
the grid. We’ll learn how to fix this soon!
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

## GRID ESSENTIALS

### Creating Rows

<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ve learned how to define the number of columns in our grid
explicitly. To specify the number and size of the rows, we are going to
use the property
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This property is almost identical to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>.
Take a look at the code below to see both properties in action.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 1000px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 500px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> 100px 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-rows</span><span class="mtk1">:</span><span class="mtk9"> 10% 20% 600px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This grid has two columns and three rows.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
defines the number of rows and sets each row’s height. In this example,
the first row is 50 pixels tall (10% of 500), the second row is 100
pixels tall (20% of 500), and the third row is 600 pixels tall.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When using percentages in these two properties, remember that rows are
defined as a percentage of the grid’s height, and columns are defined as
a percentage of its width.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
By default, the rows are sized to fit evenly inside the grid. Let’s
manually change the size of our rows.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code> ruleset, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code> to
set the first row to be
<code class="code__2rdF32qjRVp7mMVBHuPwDS">40%</code> of the grid’s
height. Set the second row to be
<code class="code__2rdF32qjRVp7mMVBHuPwDS">50%</code> of the grid’s
height. And set the third row to be
<code class="code__2rdF32qjRVp7mMVBHuPwDS">50px</code>.
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

## GRID ESSENTIALS

### Grid Template

<p class="p__1qg33Igem5pAgn4kPMirjw">
The shorthand property,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template</code>, can
replace the previous two CSS properties. Both
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
are nowhere to be found in the following code!
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 1000px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 500px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template</span><span class="mtk1">:</span><span class="mtk9"> 200px 300px </span><span class="mtk1">/</span><span class="mtk9"> 20% 10% 70%</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template</code>, the
values before the slash will determine the size of each row. The values
after the slash determine the size of each column. In this example,
we’ve made two rows and three columns of varying sizes.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The same rules from before apply; when using percentages to set rows,
each row will be a percentage of the grid’s total height. Columns are
still a percentage of the total width.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Refactor the grid template rows and columns code inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code> ruleset using
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template</code>
property. Keep the rows and columns looking the same without using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
properties!
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

## GRID ESSENTIALS

### Fraction

<p class="p__1qg33Igem5pAgn4kPMirjw">
You may already be familiar with several types of responsive units such
as percentages (<code class="code__2rdF32qjRVp7mMVBHuPwDS">%</code>),
<code class="code__2rdF32qjRVp7mMVBHuPwDS">em</code>s and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rem</code>s. CSS Grid
introduced a new relative sizing unit —
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code>, like fraction.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code> unit,
we can define the size of columns and rows as a fraction of the grid’s
length and width. This unit was specifically created for use in CSS
Grid. Using <code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code> makes
it easier to prevent grid items from overflowing the boundaries of the
grid. Consider the code below:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 1000px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 400px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template</span><span class="mtk1">:</span><span class="mtk9"> 2fr 1fr 1fr </span><span class="mtk1">/</span><span class="mtk9"> 1fr 3fr 1fr</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this example, the grid will have three rows and three columns. The
rows are splitting up the available 400 pixels of height into four
parts. The first row gets two of those parts, the second row gets one,
and the third row gets one. Therefore the first row is 200 pixels tall,
and the second and third rows are 100 pixels tall.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Each column’s width is a fraction of the available space. In this case,
the available space is split into five parts. The first column gets
one-fifth of the space, the second column gets three-fifths, and the
last column gets one-fifth. Since the total width is 1000 pixels, this
means that the columns will have widths of 200 pixels, 600 pixels, and
200 pixels respectively.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It is possible to use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code> with other units as
well. When this happens, each
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code> represents a
fraction of the <em>available</em> space.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> 1fr 60px 1fr</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this example, 60 pixels are taken up by the second column. Therefore
the first and third columns have 40 available to split between them.
Since each gets one fraction of the total, they both end up being 20
pixels wide.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Change your rows so that each row will take up the exact same fraction
of the available space.
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
Change the grid so the middle column is still 50% of the grid, but the
first column takes up three fourths of the remaining space and the last
column takes up one fourth.
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

## GRID ESSENTIALS

### Repeat

<p class="p__1qg33Igem5pAgn4kPMirjw">
The properties that define the number of rows and columns in a grid can
take a function as a value.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">repeat()</code> is one of
these functions. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">repeat()</code> function was
created specifically for CSS Grid.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">repeat(</span><span class="mtk9">3</span><span class="mtk1">,</span><span class="mtk9"> 100px</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The repeat function will duplicate the specifications for rows or
columns a given number of times. In the example above, using the repeat
function will make the grid have three columns that are each 100 pixels
wide. It is the same as writing:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">grid-template-columns</span><span class="mtk9">: 100</span><span class="mtk4">px</span><span class="mtk9"> 100</span><span class="mtk4">px</span><span class="mtk9"> 100</span><span class="mtk4">px</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Repeat is particularly useful with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code>. For example,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">repeat(5, 1fr)</code> would
split your table into five equal rows or columns.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Finally, the second parameter of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">repeat()</code> can have
multiple values.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">grid-template-columns</span><span class="mtk9">: </span><span class="mtk4">repeat</span><span class="mtk9">(2</span><span class="mtk1">,</span><span class="mtk9"> 20</span><span class="mtk4">px</span><span class="mtk9"> 50</span><span class="mtk4">px</span><span class="mtk9">)</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This code will create four columns where the first and third columns
will be 20 pixels wide and the second and fourth will be 50 pixels wide.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Refactor the sizing of the rows to use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">repeat()</code> function.
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

## GRID ESSENTIALS

### minmax

<p class="p__1qg33Igem5pAgn4kPMirjw">
So far, all of the grids that we have worked with have been a fixed
size. The grid in our example has been 400 pixels wide and 500 pixels
tall. But sometimes you might want a grid to resize based on the size of
your web browser.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In these situations, you might want to prevent a row or column from
getting too big or too small. For example, if you have a 100-pixel wide
image in your grid, you probably don’t want its column to get thinner
than 100 pixels! The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">minmax()</code> function can
help us solve this problem.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> 100px </span><span class="mtk1">minmax(</span><span class="mtk9">100px</span><span class="mtk1">,</span><span class="mtk9"> 500px</span><span class="mtk1">)</span><span class="mtk9"> 100px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this example, the first and third columns will always be 100 pixels
wide, no matter the size of the grid. The second column, however, will
vary in size as the overall grid resizes. The second column will always
be between 100 and 500 pixels wide.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
To see <code class="code__2rdF32qjRVp7mMVBHuPwDS">minmax()</code> in
action, we need to first make the grid have a variable width. Delete the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> declaration from
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you resize your browser, you will see the grid change size with the
window.
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
Using <code class="code__2rdF32qjRVp7mMVBHuPwDS">minmax()</code>, change
the second column to be between 50 pixels and 300 pixels.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Try resizing your browser window. What happens to the other columns when
the second column reaches the 300 pixel limit?
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

## GRID ESSENTIALS

### Grid Gap

<p class="p__1qg33Igem5pAgn4kPMirjw">
In all of our grids so far, there hasn’t been any space between the
items in our grid. The CSS properties
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row-gap</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column-gap</code> will put
blank space between every row and column in the grid.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 320px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">repeat(</span><span class="mtk9">3</span><span class="mtk1">,</span><span class="mtk9"> 1fr</span><span class="mtk1">);</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">column-gap</span><span class="mtk1">:</span><span class="mtk9"> 10px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It is important to note that grid gap properties do not add space at the
beginning or end of the grid. In the example code, our grid will have
three columns with two ten-pixel gaps between them.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s quickly calculate how wide these columns are. Remember that using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code> considers all of
the <em>available</em> space. The grid is 320 pixels wide and 20 of
those pixels are taken up by the two grid gaps. Therefore each column
takes a piece of the 300 available pixels. Each column gets
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1fr</code>, so the columns
are evenly divided into thirds (or 100 pixels each).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Finally, there is a shorthand CSS property,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">gap</code>, that can set the
row and column gap at the same time.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.grid</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 320px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">repeat(</span><span class="mtk9">3</span><span class="mtk1">,</span><span class="mtk9"> 1fr</span><span class="mtk1">);</span></span><br><span><span class="mtk9">&nbsp;&nbsp;gap: 20px 10px;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The example above will set the distance between rows to 20 pixels and
the distance between columns to 10 pixels. Unlike other CSS grid
properties, this shorthand does not take a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">/</code> between values! If
only one value is given, it will set the column gap and the row gap to
that value.
</p>
<blockquote class="blockquote__Bo1k0tPllp684-m2XzKRP">
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note</strong>: You might have seen
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-gap</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-gap</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-gap</code> in other
code, but these properties are now deprecated.
</p>
</blockquote>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">row-gap</code> to create
a gap of <code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code> between
the rows of your grid.
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
Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">column-gap</code> to
create a gap of <code class="code__2rdF32qjRVp7mMVBHuPwDS">5px</code>
between the column of your grid.
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
Comment out the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row-gap</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column-gap</code>
declarations. Refactor the two properties into a shorthand
<code class="code__2rdF32qjRVp7mMVBHuPwDS">gap</code> property.
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

## GRID ESSENTIALS

### Grid Items

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, we have learned how to define a grid container. When
explicitly defining a grid, you have to declare the quantity of rows and
columns and their respective sizes.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In all of our examples, the items placed in the grid have always taken
up exactly one square. This does not always need to be the case; we can
drastically change the look of our grid by making grid items take up
more than one row and one column. You can see this in the diagram to the
right. Items A, B, C, and E span more than one row!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the following exercises, you will learn CSS properties that will
affect the size of the <em>grid items</em> and where they are displayed
on the page. By manipulating both the parent and the child elements, we
can create beautiful layouts with ease.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s start exploring grid items!
</p>

## GRID ESSENTIALS

### Multiple Row Items

<p class="p__1qg33Igem5pAgn4kPMirjw">
Using the CSS properties
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code>, we can
make single grid items take up multiple rows. Remember, we are no longer
applying CSS to the outer grid container; we’re adding CSS to the
elements sitting inside the grid!
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-row-start</span><span class="mtk1">:</span><span class="mtk9"> 1</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-row-end</span><span class="mtk1">:</span><span class="mtk9"> 3</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this example, the HTML element of class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">item</code> will take up two
rows in the grid, rows 1 and 2. The values that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code> accept
are <em>grid lines</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Row grid lines and column grid lines start at 1 and end at a value that
is 1 greater than the number of rows or columns the grid has. For
example, if a grid has 5 rows, the grid row lines range from 1 to 6. If
a grid has 8 rows, the grid row lines range from 1 to 9.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The value for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> should
be the row at which you want the grid item to begin. The value for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code> should be
one greater than the row at which you want the grid item to end. An
element that covers rows 2, 3, and 4 should have these declarations:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start: 2</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end: 5</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It is possible for the value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> to be
greater than that of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code>. Both
properties can also each have negative values. Consult the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-start">documentation</a>
to learn more about how to use these features.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at the CSS rule for the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid</code>. Think about what
the grid would look like if it were completely filled. Let’s make this
first item take up the fifth and sixth rows of the grid.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code> ruleset, set
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> so the
item begins in the fifth row.
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
Set <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code> so
the item occupies the fifth and sixth rows.
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

## GRID ESSENTIALS

### Grid Row

<p class="p__1qg33Igem5pAgn4kPMirjw">
We can use the property
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row</code> as shorthand
for <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code>. The
following two code blocks will produce the same output:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-row-start</span><span class="mtk1">:</span><span class="mtk9"> 4</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-row-end</span><span class="mtk1">:</span><span class="mtk9"> 6</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-row</span><span class="mtk1">:</span><span class="mtk9"> 4&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 6</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This code should look similar to the way
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template</code> is
shorthand for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>.
In this case, the starting row goes before the “/“ and the ending row
goes after it. Again, the ending row is exclusive; this grid item will
occupy rows four and five.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When an item spans multiple rows or columns using these properties, it
will also include the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">gap</code> if any exists. For
example, if an item spans two rows of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> 100 pixels and
there is a ten-pixel
<code class="code__2rdF32qjRVp7mMVBHuPwDS">gap</code>, then the item
will have a total height of 210 pixels.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Refactor your code from the last exercise. Replace
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code> with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row</code>. Make sure
the item still takes up rows five and six.
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

## GRID ESSENTIALS

### Grid Column

<p class="p__1qg33Igem5pAgn4kPMirjw">
The previous three properties also exist for columns.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column</code> work
identically to the row properties. These properties allow a grid item to
span multiple columns.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When using these properties, we can use the keyword
<code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> to start or end a
column or row, relative to its other end. Look at how
<code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> is used in the
code below:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-column</span><span class="mtk1">:</span><span class="mtk9"> 4&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> span 2</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This is telling the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">item</code> element to begin
in column four and take up two columns of space. So
<code class="code__2rdF32qjRVp7mMVBHuPwDS">item</code> would occupy
columns four and five. It produces the same result as the following code
blocks:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-column</span><span class="mtk1">:</span><span class="mtk9"> 4&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 6</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-column-start</span><span class="mtk1">:</span><span class="mtk9"> 4</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-column-end</span><span class="mtk1">:</span><span class="mtk9"> span 2</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-column-start</span><span class="mtk1">:</span><span class="mtk9"> span 2</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-column-end</span><span class="mtk1">:</span><span class="mtk9"> 6</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> is a useful
keyword, because it avoids off-by-one errors (miscalculating the ending
grid line) you might make when determining the ending grid line of an
element. If you know where you want your grid item to start and how long
it should be, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code>!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s add another item to our grid. Navigate to
<strong>index.html</strong> and uncomment the B div.
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
Let’s make box <code class="code__2rdF32qjRVp7mMVBHuPwDS">b</code> take
up a few rows. Go back to <strong>style.css</strong>, in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.b</code> ruleset, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row</code> with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> to make the item
take up rows two through four.
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
Next, make box <code class="code__2rdF32qjRVp7mMVBHuPwDS">b</code> take
up six columns. In <strong>style.css</strong>, in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.b</code> ruleset, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column</code> to set its
starting column to <code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code>.
Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> to make the
item take up six columns.
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
Now let’s go back to the box
<code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code> ruleset. Refactor
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code>
declarations into a shorthand
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column</code>
declaration. The grid item should still start in the first column and
span 2 columns using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> keyword.
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

## GRID ESSENTIALS

### Grid Area

<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ve already been able to use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column</code> as
shorthand for properties like
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code>. We can
refactor even more using the property
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code>. This
property will set the starting and ending positions for both the rows
and columns of an item.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.item</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-area</span><span class="mtk1">:</span><span class="mtk9"> 2&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 3&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 4&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> span 5</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> takes four
values separated by slashes. The order is important! This is how
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> will
interpret those values.
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code>
</li>
</ol>

<br>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the above example, the item will start on row
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code> and end on row
<code class="code__2rdF32qjRVp7mMVBHuPwDS">4</code>, though the 4th row
is not actually included, only rows
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">3</code>! The item will then
start on column <code class="code__2rdF32qjRVp7mMVBHuPwDS">3</code> and
instead of setting a number for which column to end on, we want this
item to <code class="code__2rdF32qjRVp7mMVBHuPwDS">span 5</code> columns
— this means the item will include columns
<code class="code__2rdF32qjRVp7mMVBHuPwDS">3</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">4</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">5</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">6</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">7</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Using <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> is an
easy way to place items exactly where you want them in a grid.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>index.html</strong> uncomment the C
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> on line 10.
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
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.c</code> ruleset, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> to make the
element start at row six and column eight. Then have it take up three
rows and one column. Use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> for both ending
values.
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
Let’s refactor the code for the other two items in the grid. Start with
item <code class="code__2rdF32qjRVp7mMVBHuPwDS">b</code>. Replace
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column</code> with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code>. Make sure
the item still takes up the same amount of space.
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
Lastly, refactor item
<code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code>. Replace
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column</code> with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code>. Again, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> to set the end of
the rows and columns.
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

## GRID ESSENTIALS

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
At this point, we’ve covered a great deal of different ways to
manipulate the grid and the items inside it to create interesting
layouts.
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
defines the number and sizes of the columns of the grid
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
defines the number and sizes of the rows of the grid
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template</code> is a
shorthand for defining both
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
in one line
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row-gap</code> puts blank
space between the rows of the grid
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column-gap</code> puts blank
space between the columns of the grid
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">gap</code> is a shorthand for
defining both <code class="code__2rdF32qjRVp7mMVBHuPwDS">row-gap</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">column-gap</code> in one
line
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code> makes
elements span certain rows of the grid
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code> makes
elements span certain columns of the grid
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> is a
shorthand for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code>, all
in one line
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You have seen how to set up and fill in a grid and you now have one more
CSS positioning technique to add to your toolkit! Let’s do some practice
to solidify these skills.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s start by making this bunch of divs into a grid. In
<strong>style.css</strong>, in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code> ruleset, add a
declaration that uses the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property along
with the value necessary to make the element a CSS grid.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Structure the grid to have four columns — the first two each taking up
25% of the total width, the third column taking up two-thirds of the
remaining space, and the last column taking up the last third of the
remaining space.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">3.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Give the grid two rows, both
<code class="code__2rdF32qjRVp7mMVBHuPwDS">200px</code> in size.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Put a <code class="code__2rdF32qjRVp7mMVBHuPwDS">10px</code> gap in
between the rows of the grid and a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">15px</code> gap in between
the columns of the grid.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">5.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Using the <code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code>
keyword, make the box with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code> take up the first
two columns of the grid.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">6.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Without using <code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code>,
make the box with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code> take up the first
two rows of the grid.
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

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">7.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great! Now, feel free to play around with refactoring to see how short
you can make your <strong>style.css</strong> file while not changing the
layout we’ve created. When you’re ready, move on to the next lesson. In
the next lesson, you will learn some advanced techniques to further
style your CSS grids.
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

## ADVANCED CSS GRID

### Introduction

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous lesson, you learned all the foundational properties
necessary to create a two-dimensional grid-based layout for your web
pages! In this lesson, you’ll learn the following additional properties
that you can use to harness the power of CSS Grid Layout:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-areas</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-self</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-self</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-rows</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-columns</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-flow</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You will also learn about the <em>explicit</em> and <em>implicit</em>
grids and <em>grid axes</em>.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Examine the code in the browser to the right. Expand the browser by
clicking the diagonal arrow to the right of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">localhost:8000</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You’ll be updating this fictional recipe site as you move throughout
this lesson! Continue to the next exercise when you’re ready.
</p>

**Solutions**

``` html
```

## ADVANCED CSS GRID

### Grid Template Areas

<p class="p__1qg33Igem5pAgn4kPMirjw">
The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-areas</code>
property allows you to name sections of your web page to use as values
in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-start</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-row-end</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code>,<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code>,
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code>
properties. This property is declared on grid containers.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"container"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;header&gt;</span><span class="mtk1">Welcome!</span><span class="mtk4">&lt;/header&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;nav&gt;</span><span class="mtk1">Links!</span><span class="mtk4">&lt;/nav&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;section</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"info"</span><span class="mtk4">&gt;</span><span class="mtk1">Info!</span><span class="mtk4">&lt;/section&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;section</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"services"</span><span class="mtk4">&gt;</span><span class="mtk1">Services!</span><span class="mtk4">&lt;/section&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;footer&gt;</span><span class="mtk1">Contact us!</span><span class="mtk4">&lt;/footer&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">max-width</span><span class="mtk1">:</span><span class="mtk9"> 900px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">relative</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">margin</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">auto</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-areas</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">"head head"</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">"nav nav"</span><span class="mtk9"> </span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">"info services"</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">"footer footer"</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-rows</span><span class="mtk1">:</span><span class="mtk9"> 300px 120px 800px 120px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> 1fr 3fr</span><span class="mtk1">;</span><span class="mtk9"> </span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">header</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-area</span><span class="mtk1">:</span><span class="mtk9"> head</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span><span class="mtk9"> </span></span><br><span><span> </span></span><br><span><span class="mtk4">nav</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-area</span><span class="mtk1">:</span><span class="mtk9"> nav</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span><span class="mtk9"> </span></span><br><span><span> </span></span><br><span><span class="mtk7">.info</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-area</span><span class="mtk1">:</span><span class="mtk9"> info</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span><span class="mtk9"> </span></span><br><span><span> </span></span><br><span><span class="mtk7">.services</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-area</span><span class="mtk1">:</span><span class="mtk9"> services</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">footer</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-area</span><span class="mtk1">:</span><span class="mtk9"> footer</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span><span class="mtk9"> </span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You may want to expand this section of the website to view the code
above more clearly.
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In the example above, the HTML creates a web page with five distinct
parts.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-areas</code>
declaration creates a 2-column, 4-row layout.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
declaration specifies the height of each of the four rows from top to
bottom: 300 pixels, 120 pixels, 800 pixels, and 120 pixels.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
declaration uses the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code> value to cause the
left column to use one fourth of the available space on the page and the
right column to use three-fourths of the available space on the page.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In each ruleset below
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>, we use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> property to
tell that section to cover the portion of the page specified. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">header</code> element spans
the first row and both columns. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">nav</code> element spans the
second row and both columns. The element with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.info</code> spans the third
row and left column. The element with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.services</code> spans the
third row and right column. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">footer</code> element spans
the bottom row and both columns.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
That’s it! An entire page laid out in 40 lines of code.
</li>
</ol>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
You can see what you’ll be building in this exercise
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/learn-css-grid/lesson-ii/grid-template-areas/index.html">here</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-areas</code>
property to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code> ruleset.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Its value should create a 2-column, 4-row layout with these areas:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
header (spans two columns in the first row)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
nav (spans two columns in the second row)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
left (spans one column on the left in the third row)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
right (spans one column on the right in the third row)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
footer (spans two columns in the fourth row)
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
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">header</code> ruleset, set
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> property
to have a value of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">header</code>.
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
Follow the same pattern for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">nav</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.left</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.right</code>, and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">footer</code> rulesets in
<strong>style.css</strong>.
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
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
property to make the first column 200 pixels wide and the second column
400 pixels wide.
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
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code>
ruleset, use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
property to make the rows 150 pixels, 200 pixels, 600 pixels, and 200
pixels tall.
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

## ADVANCED CSS GRID

### Overlapping Elements

<p class="p__1qg33Igem5pAgn4kPMirjw">
Another powerful feature of CSS Grid Layout is the ability to easily
overlap elements.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When overlapping elements, it is generally easiest to use the
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-css/lessons/advanced-css-grid/exercises/grid-area"><code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code></a>
property with grid row names. Remember that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> will set the
starting and ending positions for both the rows and columns of an item.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"container"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"info"</span><span class="mtk4">&gt;</span><span class="mtk1">Info!</span><span class="mtk4">&lt;/div&gt;</span><span class="mtk1"> </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;img</span><span class="mtk1"> </span><span class="mtk7">src</span><span class="mtk1">=</span><span class="mtk8">"#"</span><span class="mtk1"> </span><span class="mtk4">/&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"services"</span><span class="mtk4">&gt;</span><span class="mtk1">Services!</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">repeat(</span><span class="mtk9">8</span><span class="mtk1">,</span><span class="mtk9"> 200px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">/</span><span class="mtk9"> </span><span class="mtk1">repeat(</span><span class="mtk9">6</span><span class="mtk1">,</span><span class="mtk9"> 100px</span><span class="mtk1">);</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.info</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-area</span><span class="mtk1">:</span><span class="mtk9"> 1&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 1&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 9&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 4</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.services</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-area</span><span class="mtk1">:</span><span class="mtk9"> 1&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 4&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 9&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 7</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">img</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-area</span><span class="mtk1">:</span><span class="mtk9"> 2&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 3&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 5&nbsp;</span><span class="mtk1">/</span><span class="mtk9"> 5</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">z-index</span><span class="mtk1">:</span><span class="mtk9"> 5</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, there is a grid container with eight rows and six
columns. There are three grid items within the container — a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">info</code>, a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> with the class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">services</code>, and an
image.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">info</code> section
covers all eight rows and the first three columns. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">services</code> section
covers all eight rows and the last three columns.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The image spans the 2nd, 3rd, and 4th rows and the 3rd and 4th columns.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The z-index property tells the browser to render the image element on
top of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">services</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">info</code> sections so
that it is visible.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.left</code> ruleset, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> property and
set its value to <code class="code__2rdF32qjRVp7mMVBHuPwDS">4 / 1 / 9 /
5</code>. This sets the Left element to take up rows 4 through 8, and
columns 1 through 4.
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
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.right</code> ruleset, add
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> property
and set its value to <code class="code__2rdF32qjRVp7mMVBHuPwDS">4 / 5 /
9 / 7</code>. This sets the Right element to take up rows 4 through 8,
and columns 5 and 6.
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
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.overlap</code> ruleset, add
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code>
property.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Set its value so that the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">overlap</code> element spans
the 6th and 7th rows and the 4th and 5th columns.
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
Notice that the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">overlap</code> element is
covered by the <code class="code__2rdF32qjRVp7mMVBHuPwDS">right</code>
element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Set the <code class="code__2rdF32qjRVp7mMVBHuPwDS">z-index</code> of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">overlap</code> element to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">5</code>.
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
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">footer</code> ruleset, add
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-area</code> property
and set its value to <code class="code__2rdF32qjRVp7mMVBHuPwDS">9 / 1 /
13 / 7</code>.
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

## ADVANCED CSS GRID

### Justify Items

<p class="p__1qg33Igem5pAgn4kPMirjw">
We have referred to “two-dimensional grid-based layout” several times
throughout this course.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are two axes in a grid layout — the <em>column</em> (or block)
axis and the <em>row</em> (or inline) axis.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The column axis stretches from top to bottom across the web page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The row axis stretches from left to right across the web page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the following four exercises, we will learn and use properties that
rely on an understanding of grid axes.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code> is a
property that positions grid items along the inline, or row, axis. This
means that it positions items from left to right across the web page.
This property is declared on grid containers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code> accepts
these values:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">start</code> — aligns grid
items to the left side of the grid area
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">end</code> — aligns grid
items to the right side of the grid area
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> — aligns grid
items to the center of the grid area
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stretch</code> — stretches
all items to fill the grid area
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are several other values that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code> accepts,
which you can read about on the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Justifying_Items_on_the_Inline_or_Row_Axis">Mozilla
Developer Network</a>. The definitions for these values can also be
found in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/justify-items#Values">documentation</a>.
It is important to note that the page with the definitions includes some
values that are not accepted in CSS Grid layout.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;main&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card"</span><span class="mtk4">&gt;</span><span class="mtk1">Card 1</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card"</span><span class="mtk4">&gt;</span><span class="mtk1">Card 2</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card"</span><span class="mtk4">&gt;</span><span class="mtk1">Card 3</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/main&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">main</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">repeat(</span><span class="mtk9">3</span><span class="mtk1">,</span><span class="mtk9"> 400px</span><span class="mtk1">);</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">justify-items</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">center</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code> to
adjust the positioning of some elements on this web page.
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
There is a grid container with three columns that are each 400 pixels
wide.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The container has three grid items that do not have a specified width.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Without setting the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code>
property, these elements will span the width of the column they are in
(400 pixels).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
By setting the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code> property
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card</code>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s will be
centered inside of their columns. They will only be as wide as necessary
to contain their content (the words Card 1, etc).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If we specify a width for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card</code> elements, they
will not stretch the width of their column.
</li>
</ol>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Look in <strong>style.css</strong>. Each column inside of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<main\></code> element is
250 pixels. The recipes stretch to take up the entire 250 pixels.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.recipe</code>
ruleset, add the <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code>
property and set its value to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">200px</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
What changes?
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
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">main</code> ruleset,
add a <code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code>
property with the value
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The elements won’t be completely centered just yet. Depending on your
browser size, you may not notice much of a move at all. We’ll learn why
in the following exercise!
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

## ADVANCED CSS GRID

### Justify Content

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous exercise, we learned how to position elements within
their columns. In this exercise, we will learn how to position a grid
within its parent element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code> to
position the entire grid along the row axis. This property is declared
on grid containers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It accepts these values:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">start</code> — aligns the
grid to the left side of the grid container
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">end</code> — aligns the grid
to the right side of the grid container
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> — centers the
grid horizontally in the grid container
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stretch</code> — stretches
the grid items to increase the size of the grid to expand horizontally
across the container
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code> —
includes an equal amount of space on each side of a grid element,
resulting in double the amount of space between elements as there is
before the first and after the last element
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-between</code> —
includes an equal amount of space between grid items and no space at
either end
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-evenly</code> — places
an even amount of space between grid items and at either end
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are several other values that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
accepts, which you can read about on the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Aligning_the_grid_tracks_on_the_block_or_column_axis">Mozilla
Developer Network</a>. The definitions for these values can also be
found in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content#Values">documentation</a>.
It is important to note that the page with the definitions includes some
values that are not accepted in CSS Grid layout.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;main&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"left"</span><span class="mtk4">&gt;</span><span class="mtk1">Left</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"right"</span><span class="mtk4">&gt;</span><span class="mtk1">Right</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/main&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">main</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 1000px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-columns</span><span class="mtk1">:</span><span class="mtk9"> 300px 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-areas</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">"left right"</span><span class="mtk1">;</span><span class="mtk9"> </span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">justify-content</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">center</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In the example above, the grid container is 1000 pixels wide, but we
only specified two columns that are 300 pixels each. This will leave 400
pixels of unused space in the grid container.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content:
center;</code> positions the columns in the center of the grid, leaving
200 pixels on the right and 200 pixels on the left of the grid.
</li>
</ol>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Expand the web browser to the right. The two columns of recipe cards are
off-center.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">main</code> ruleset, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
property and set its value to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now, all of the elements should be perfectly centered on the page! Feel
free to try some of the other values to see how they position the grid.
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

## ADVANCED CSS GRID

### Align Items

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous two exercises, we learned how to position grid items and
grid columns from left to right across the page. Now we’ll learn how to
position grid items from top to bottom!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> is a
property that positions grid items along the block, or column axis. This
means that it positions items from top to bottom. This property is
declared on grid containers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> accepts
these values:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">start</code> — aligns grid
items to the top side of the grid area
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">end</code> — aligns grid
items to the bottom side of the grid area
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> — aligns grid
items to the center of the grid area
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stretch</code> — stretches
all items to fill the grid area
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are several other values that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> accepts,
which you can read about on the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Aligning_items_on_the_block_or_column_Axis">Mozilla
Developer Network</a>. The definitions for these values can also be
found in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/align-items#values">documentation</a>.
It is important to note that the page with the definitions includes some
values that are not accepted in CSS Grid layout.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;main&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card"</span><span class="mtk4">&gt;</span><span class="mtk1">Card 1</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card"</span><span class="mtk4">&gt;</span><span class="mtk1">Card 2</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card"</span><span class="mtk4">&gt;</span><span class="mtk1">Card 3</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/main&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">main</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-rows</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">repeat(</span><span class="mtk9">3</span><span class="mtk1">,</span><span class="mtk9"> 400px</span><span class="mtk1">);</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">align-items</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">center</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> to adjust
the positioning of some elements on this web page.
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
There is a grid container with three rows that are 400 pixels tall.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The container has three grid items that do not have a specified width.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Without setting the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property,
these elements will span the height of the row they are in (400 pixels).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
By setting the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> property
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card</code>
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s will be
centered vertically inside of their rows. They will only be as tall as
necessary to contain their content (the words Card 1, etc).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
If we specify a height for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card</code> elements, they
will not stretch the height of their row even if
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items: stretch;</code>
is set.
</li>
</ol>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Notice that each row of recipe cards stretches to the height of the row
(450 pixels), even if it doesn’t have enough text to fill the space.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">main</code> ruleset, we’ve
added some <code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code>
properties with different values. Uncomment each line to see what
position the grid items take.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The final declaration
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items: stretch</code>
is what we’ll be sticking with!
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

## ADVANCED CSS GRID

### Align Content

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the previous exercise, we positioned grid items within their rows.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
positions the rows along the column axis, or from top to bottom, and is
declared on grid containers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It accepts these positional values:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">start</code> — aligns the
grid to the top of the grid container
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">end</code> — aligns the grid
to the bottom of the grid container
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> — centers the
grid vertically in the grid container
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stretch</code> — stretches
the grid items to increase the size of the grid to expand vertically
across the container
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-around</code> —
includes an equal amount of space on each side of a grid element,
resulting in double the amount of space between elements as there is
before the first and after the last element
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-between</code> —
includes an equal amount of space between grid items and no space at
either end
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">space-evenly</code> — places
an even amount of space between grid items and at either end
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
There are several other values that
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code> accepts,
which you can read about on the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Aligning_the_grid_tracks_on_the_block_or_column_axis">Mozilla
Developer Network</a>. The definitions for these values can also be
found in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/align-content#Values">documentation</a>.
It is important to note that the page with the definitions includes some
values that are not accepted in CSS Grid layout.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;main&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"top"</span><span class="mtk4">&gt;</span><span class="mtk1">Top</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"bottom"</span><span class="mtk4">&gt;</span><span class="mtk1">Bottom</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/main&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">main</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 600px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-rows</span><span class="mtk1">:</span><span class="mtk9"> 200px 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-template-areas</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk8">"top"</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">"bottom"</span><span class="mtk1">;</span><span class="mtk9"> </span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">align-content</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">center</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
In the example above, the grid container is 600 pixels tall, but we only
specified two rows that are 200 pixels each. This will leave 200 pixels
of unused space in the grid container.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content: center;</code>
positions the rows in the center of the grid, leaving 100 pixels at the
top and 100 pixels at the bottom of the grid.
</li>
</ol>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">main</code> ruleset, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> property and
set its value to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1600px</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Scroll all the way to the bottom of the web page. Notice the empty space
at the bottom?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This is because the rows are each 450 pixels tall (for a total of 1350
pixels), but the container is 1600 pixels.
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
To center the content on the page, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code> property
to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">main</code> ruleset
and set its value to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Feel free to play around with some other values to see how the grid
container can positioned!
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

## ADVANCED CSS GRID

### Justify Self and Align Self

<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> properties
specify how all grid items contained within a single container will
position themselves along the row and column axes, respectively.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-self</code> specifies
how an individual element should position itself with respect to the row
axis. This property will override
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code> for any
item on which it is declared.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-self</code> specifies
how an individual element should position itself with respect to the
column axis. This property will override
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> for any
item on which it is declared.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
These properties are declared on grid items. They both accept these four
properties: 
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">start</code> — positions grid
items on the left side/top of the grid area
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">end</code> — positions grid
items on the right side/bottom of the grid area
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">center</code> — positions
grid items on the center of the grid area
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">stretch</code> — positions
grid items to fill the grid area (default)
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-self</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-self</code> accept
the same values as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code>. You can
read about these values on the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Aligning_the_grid_tracks_on_the_block_or_column_axis">Mozilla
Developer Network</a>. The definitions for these values can also be
found in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/align-self#Values">documentation</a>.
It is important to note that the page with the definitions includes some
values that are not accepted in CSS Grid layout.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.a</code> ruleset, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-self</code> property
and set its value to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">end</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
What changes?
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
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.c</code> ruleset, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-self</code> property
and set its value to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">start</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
What changes?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The web page is looking a little uneven. We’ll get rid of both
declarations in the next exercise.
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

## ADVANCED CSS GRID

### Implicit vs. Explicit Grid

<p class="p__1qg33Igem5pAgn4kPMirjw">
So far, we have been explicitly defining the dimensions and quantities
of our grid elements using various properties. This works well in many
cases, such as a landing page for a business that will display a
specific amount of information at all times.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
However, there are instances in which we don’t know how much information
we’re going to display. For example, consider online shopping. Often,
these web pages include the option at the bottom of the search results
to display a certain quantity of results or to display ALL results on a
single page. When displaying all results, the web developer can’t know
in advance how many elements will be in the search results each time.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
What happens if the developer has specified a 3-column, 5-row grid (for
a total of 15 items), but the search results return 30?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Something called the <em>implicit</em> grid takes over. The implicit
grid is an algorithm built into the specification for CSS Grid that
determines default behavior for the placement of elements when there are
more than fit into the grid specified by the CSS.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The default behavior of the implicit grid is as follows: items fill up
rows first, adding new rows as necessary. New grid rows will only be
tall enough to contain the content within them. In the next exercise,
you’ll learn how to change this default behavior.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Move on to the next exercise when you’re ready!
</p>

**Solutions**

``` html
```

## ADVANCED CSS GRID

### Grid Auto Rows and Grid Auto Columns

<p class="p__1qg33Igem5pAgn4kPMirjw">
CSS Grid provides two properties to specify the size of grid tracks
added implicitly:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-rows</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-columns</code>.
These properties are declared on grid containers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-rows</code>
specifies the height of implicitly added grid rows.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-columns</code>
specifies the width of implicitly added grid columns.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-rows</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-columns</code>
accept the same values as their explicit counterparts,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
pixels (<code class="code__2rdF32qjRVp7mMVBHuPwDS">px</code>)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
percentages (<code class="code__2rdF32qjRVp7mMVBHuPwDS">%</code>)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
fractions (<code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code>)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">repeat()</code> function
</li>
</ul>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;body&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div&gt;</span><span class="mtk1">Part 1</span><span class="mtk4">&lt;/div&gt;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div&gt;</span><span class="mtk1">Part 2</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div&gt;</span><span class="mtk1">Part 3</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div&gt;</span><span class="mtk1">Part 4</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;div&gt;</span><span class="mtk1">Part 5</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/body&gt;</span></span><br></div></code></pre></pre>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">body</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">grid</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk1">repeat(</span><span class="mtk9">2</span><span class="mtk1">,</span><span class="mtk9"> 100px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">/</span><span class="mtk9"> </span><span class="mtk1">repeat(</span><span class="mtk9">2</span><span class="mtk1">,</span><span class="mtk9"> 150px</span><span class="mtk1">);</span><span class="mtk9"> </span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">grid-auto-rows</span><span class="mtk1">:</span><span class="mtk9"> 50px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, there are 5
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s. However, in
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">body</code> ruleset, we
only specify a 2-row, 2-column grid — four grid cells.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The fifth <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> will
be added to an implicit row that will be 50 pixels tall.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If we did not specify
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-rows</code>, the
rows would be auto-adjusted to the height of the content of the grid
items.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, delete the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height: 1600px;</code>
declaration from the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">main</code> ruleset .
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
In <strong>index.html</strong>, copy and paste the last two recipe cards
to add two more recipe cards to the bottom of the page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Examine the height of the two new cards. What do you notice?
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
To make additional cards the same height, in <strong>style.css</strong>,
inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">main</code>
ruleset, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-rows</code>
property. Set the height of the implicitly defined rows to 500 pixels.
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

## ADVANCED CSS GRID

### Grid Auto Flow

<p class="p__1qg33Igem5pAgn4kPMirjw">
In addition to setting the dimensions of implicitly-added rows and
columns, we can specify the order in which they are rendered.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-flow</code>
specifies whether new elements should be added to rows or columns, and
is declared on grid containers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-flow</code> accepts
these values:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">row</code> — specifies the
new elements should fill rows from left to right and create new rows
when there are too many elements (default)
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column</code> — specifies the
new elements should fill columns from top to bottom and create new
columns when there are too many elements
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">dense</code> — this keyword
invokes an algorithm that attempts to fill holes earlier in the grid
layout if smaller elements are added
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can pair <code class="code__2rdF32qjRVp7mMVBHuPwDS">row</code> or
<code class="code__2rdF32qjRVp7mMVBHuPwDS">column</code> with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">dense</code>, like this:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-flow: row
dense;</code>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">main</code> ruleset , add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-flow</code>
property and set its value to create columns when more elements are
added.
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

## ADVANCED CSS GRID

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great work! You have learned many new properties to use when creating a
layout using CSS Grid! Let’s review:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-areas</code>
specifies grid named grid areas
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
grid layouts are two-dimensional: they have a row, or inline, axis and a
column, or block, axis.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-items</code>
specifies how individual elements should spread across the row axis
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-content</code>
specifies how groups of elements should spread across the row axis
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">justify-self</code> specifies
how a single element should position itself with respect to the row axis
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-items</code> specifies
how individual elements should spread across the column axis
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code>
specifies how groups of elements should spread across the column axis
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-self</code> specifies
how a single element should position itself with respect to the column
axis
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-rows</code>
specifies the height of rows added implicitly to the grid
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-columns</code>
specifies the width of columns added implicitly to the grid
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-flow</code>
specifies in which direction implicit elements should be created
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This is a great time to experiment with the code in the code editor and
try any of the properties you want to practice more! When you’re ready,
move on!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
This is a great time to experiment with the code in the text editor to
visualize any of the properties covered in this lesson! Move on when
you’re ready.
</p>

**Solutions**

``` html
```

## WEB DEVELOPMENT FOUNDATIONS

### PupSpa

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s practice what we’ve just learned about CSS Grid through building a
classic, grid-based, responsive web page. Your friend has just opened a
doggie daycare and grooming services shop, PupSpa. They would like a
simple web page to let customers know about their services.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We currently have an HTML document styled with CSS, but every
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> appears in its
own row. Let’s add some CSS grid properties to make parts of the site
appear more cohesive. Some of the properties we’ll be using include:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">gap</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We’ll also cover a couple of the shorthand properties of these as well,
so let’s get started!
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
First, let’s take a look at our <strong>index.html</strong> file. As you
can see, we have several
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s that contain
the content of our website.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Find the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> with
the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid</code> — this
is our container grid and the properties applied to it will determine
the structure for the content inside.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, locate the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s that share
the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">box</code> and the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s that share
the class <code class="code__2rdF32qjRVp7mMVBHuPwDS">testimonial</code>.
Their positioning will change the most when the new grid properties are
added.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can check this step off when you feel like you’re ready to proceed!
</p>

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
Now let’s look at our CSS. We have provided the initial styling. Now it
is up to you to add the necessary CSS grid properties to make sure the
content is properly laid out on the page. The first step will be to
initialize the grid, and then we’re going to specify the number and size
of our rows and columns.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code> ruleset, set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid</code>.
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
Next, to specify the number and size of the rows, inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code> ruleset, use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
property with a value of:
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100px 8fr 5fr 4fr 5fr
80px</code>. What changes do you see?
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
Still inside of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code> ruleset, set
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
to six equal sections using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">fr</code> measurement.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When you run your code, don’t panic! The CSS is just trying to organize
our content based off of our instructions. In a later section, we’ll go
over how to style our
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s so they take
up the necessary column widths.
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
The code you added in the last two steps can be refactored into one
shorthand
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template</code>
property.
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
First, add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template</code> property
to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code> ruleset.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, cut the values from the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-templates-columns</code>
properties, and paste them as values for the new
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template</code>
property.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Then, delete the old
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-templates-columns</code>
declarations.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Finally, the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-templates-columns</code>
value can be refactored even further. Use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">repeat()</code> function to
refactor the 6 <code class="code__2rdF32qjRVp7mMVBHuPwDS">1fr</code>
values.
</p>
</li>
</ol>

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
Now, let’s fix that broken page layout. The content in the following
rulesets needs to extend across all six columns:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">header</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.banner</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.about</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">footer</code>
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Add the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code>
properties to these rulesets, with values that start the content at the
the first column and end it at the sixth column.
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
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-start</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column-end</code>
properties can also be written as a shorthand property. Using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column</code> property
and the <code class="code__2rdF32qjRVp7mMVBHuPwDS">span</code> keyword,
make:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.address</code> span the
first 2 columns
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.hours</code> span the 3rd
and 4th columns
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.call-us</code> span the 5th
and 6th columns
</li>
</ol>

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
In the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.one</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.two</code> rulesets, use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-column</code> again to
have each <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> span
three columns.
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
Let’s give our content some wiggle room. Return to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.grid</code> ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">gap</code> property, and set
its value to 20 pixels. Notice which parts of the page have changed.
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
Lastly, the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code>
elements inside of the grid boxes aren’t centered. There are some fun
ways to deal with this using some advanced CSS grid properties that
you’ll soon learn about. In the meantime, one way we can take care of it
with knowledge we already have is to make each of the boxes its own
grid! Since each <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code>
element has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">margin:
auto</code> declaration, they will be centered inside grid container.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To turn the boxes with the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<p\></code> elements into
grids, use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code>
properties in the below rulesets to turn them into grids:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">header</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.about</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.box</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.testimonial</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">footer</code>
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

## WEB DEVELOPMENT FOUNDATIONS

### CSS Grid: Task Board

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you will create a board of to-do items organized into
columns. All of the HTML and most of the CSS have been written for you,
but the grid property declarations have yet to be added.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In order to complete this project, you must know how to lay out the
structure of a grid’s rows and columns and place items within that grid
using CSS.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We recommend that you review our
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-intermediate-css/lessons/css-grid-essentials/exercises/introduction-to-grids">CSS
Grid Essentials</a> lesson before beginning.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The premade <strong>index.html</strong> and <strong>style.css</strong>
files are displayed for you. Click
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/learn-css-grid/project-ii/index.html">this
link</a> to see the completed project in another tab. Have fun!
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
We will be focusing on laying out the container
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> and the two
card-column <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s
within it. Here’s an abbreviated version of those
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s in
<strong>index.html</strong>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"container"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card-column future-projects"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card-column active-projects"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Right now, the task board looks pretty cluttered. In
<strong>style.css</strong>, let’s make the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">container</code> a grid
container so that we can start to arrange these tasks better.
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
That didn’t have any immediate effect, but it allows us to apply grid
properties to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">container</code> div. Let’s
start by giving the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code> ruleset
three equally sized columns by using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
property.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note that only 2 of columns will be filled with content at this point.
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
Now, let’s add a gap of 20 pixels in between the columns.
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
Inside of each card column, there are 5 rows of task cards. We want them
to be arranged neatly within the columns as well, so let’s make each
card column a grid container.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card-column</code> ruleset,
add a declaration that sets the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid</code>.
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
Each card column has a heading above the 5 task cards. We want the
heading to take up
<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code> and each task
card to take up <code class="code__2rdF32qjRVp7mMVBHuPwDS">100px</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card-column</code> ruleset,
set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
property to have 1
<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code> row and 5
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100px</code> rows. Use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">repeat</code> function to
make your code clean.
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
In order to have the task cards spaced evenly in each card, inside
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card-column</code>, use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code> property
to set an even amount of vertical space around each card.
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
Now we want to add another card column for Completed Projects to keep
track of all of the tasks we’ve already done. Let’s add a third card
column that’s like the other two. We already have our
<code class="code__2rdF32qjRVp7mMVBHuPwDS">container</code> set to have
space for three columns, so you just need to add the HTML.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>index.html</strong>, uncomment the code for the third card
column.
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
We expect to complete a lot of projects, but we don’t know how many.
Since those projects will be added as task cards to the Completed
Projects column, it will be helpful to use implicit grid properties
instead of the explicit properties we have been using so far. We know
the first row with the heading should be explicitly
<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code>, just as the
other heading rows are. Every additional row, if it exists, should be
implicitly set.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside <code class="code__2rdF32qjRVp7mMVBHuPwDS">.card-column</code>,
use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-rows</code>
property to implicitly set rows to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100px</code>.
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
Good job! Now, feel free to play around with the layout of this site,
using the other CSS properties you’ve learned. Once you’re satisfied
with your work, press the Next Button to move on.
</p>

</article>

**Solutions**

``` html
```

## WEB DEVELOPMENT FOUNDATIONS

### CSS Grid: Task Board

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you will create a board of to-do items organized into
columns. All of the HTML and most of the CSS have been written for you,
but the grid property declarations have yet to be added.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In order to complete this project, you must know how to lay out the
structure of a grid’s rows and columns and place items within that grid
using CSS.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We recommend that you review our
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/courses/learn-intermediate-css/lessons/css-grid-essentials/exercises/introduction-to-grids">CSS
Grid Essentials</a> lesson before beginning.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The premade <strong>index.html</strong> and <strong>style.css</strong>
files are displayed for you. Click
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/learn-css-grid/project-ii/index.html">this
link</a> to see the completed project in another tab. Have fun!
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
We will be focusing on laying out the container
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> and the two
card-column <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s
within it. Here’s an abbreviated version of those
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code>s in
<strong>index.html</strong>:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"container"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card-column future-projects"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;div</span><span class="mtk1"> </span><span class="mtk7">class</span><span class="mtk1">=</span><span class="mtk8">"card-column active-projects"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;/div&gt;</span></span><br><span><span class="mtk4">&lt;/div&gt;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Right now, the task board looks pretty cluttered. In
<strong>style.css</strong>, let’s make the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<div\></code> with class
<code class="code__2rdF32qjRVp7mMVBHuPwDS">container</code> a grid
container so that we can start to arrange these tasks better.
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
That didn’t have any immediate effect, but it allows us to apply grid
properties to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">container</code> div. Let’s
start by giving the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code> ruleset
three equally sized columns by using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-columns</code>
property.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note that only 2 of columns will be filled with content at this point.
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
Now, let’s add a gap of 20 pixels in between the columns.
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
Inside of each card column, there are 5 rows of task cards. We want them
to be arranged neatly within the columns as well, so let’s make each
card column a grid container.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card-column</code> ruleset,
add a declaration that sets the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid</code>.
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
Each card column has a heading above the 5 task cards. We want the
heading to take up
<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code> and each task
card to take up <code class="code__2rdF32qjRVp7mMVBHuPwDS">100px</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card-column</code> ruleset,
set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-template-rows</code>
property to have 1
<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code> row and 5
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100px</code> rows. Use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">repeat</code> function to
make your code clean.
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
In order to have the task cards spaced evenly in each card, inside
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.card-column</code>, use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">align-content</code> property
to set an even amount of vertical space around each card.
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
Now we want to add another card column for Completed Projects to keep
track of all of the tasks we’ve already done. Let’s add a third card
column that’s like the other two. We already have our
<code class="code__2rdF32qjRVp7mMVBHuPwDS">container</code> set to have
space for three columns, so you just need to add the HTML.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>index.html</strong>, uncomment the code for the third card
column.
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
We expect to complete a lot of projects, but we don’t know how many.
Since those projects will be added as task cards to the Completed
Projects column, it will be helpful to use implicit grid properties
instead of the explicit properties we have been using so far. We know
the first row with the heading should be explicitly
<code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code>, just as the
other heading rows are. Every additional row, if it exists, should be
implicitly set.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside <code class="code__2rdF32qjRVp7mMVBHuPwDS">.card-column</code>,
use the <code class="code__2rdF32qjRVp7mMVBHuPwDS">grid-auto-rows</code>
property to implicitly set rows to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100px</code>.
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
Good job! Now, feel free to play around with the layout of this site,
using the other CSS properties you’ve learned. Once you’re satisfied
with your work, press the Next Button to move on.
</p>

</article>

**Solutions**

``` html
```

## SIZING ELEMENTS

### Em

<p class="p__1qg33Igem5pAgn4kPMirjw">
Incorporating relative sizing starts by using units other than pixels.
One unit of measurement you can use in CSS to create relatively-sized
content is the <em>em</em>, written as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">em</code> in CSS.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Historically, the em represented the width of a capital letter M in the
typeface and size being used. That is no longer the case.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Today, the em represents the font-size of the current element or the
default base font-size set by the browser if none is given. For example,
if the base font of a browser is 16 pixels (which is normally the
default size of text in a browser), then 1 em is equal to 16 pixels. 2
ems would equal 32 pixels, and so on.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s take a look at two examples that show how em can be used in CSS.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.heading</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-size</span><span class="mtk1">:</span><span class="mtk9"> 2em</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, no base font has been specified, therefore the
font size of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">heading</code> element will
be set relative to the default font size of the browser. Assuming the
default font size is 16 pixels, then the font size of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">heading</code> element will
be 32 pixels.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.splash-section</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-size</span><span class="mtk1">:</span><span class="mtk9"> 18px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.splash-section</span><span class="mtk9"> </span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-size</span><span class="mtk1">:</span><span class="mtk9"> 1.5em</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The example above shows how to use ems without relying on the default
font size of the browser. Instead, a base font size
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">18px</code>) is defined for
all text within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">splash-section</code>
element. The second CSS rule will set the font size of all
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> elements inside of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">splash-section</code>
relative to the base font of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">splash-section</code> (18
pixels). The resulting font size of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> elements will be 27
pixels.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, set the font size in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#banner h1</code> (“Bana’s
Travel Blog”) to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1.5em</code>.
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
Set the font size in <code class="code__2rdF32qjRVp7mMVBHuPwDS">.post
h2</code> (“Saturday Market”) to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1.75em</code>.
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
Set the font size in <code class="code__2rdF32qjRVp7mMVBHuPwDS">.post
h3</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">1.25em</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Set the font size in the footer (“© Bana’s Travel Blog”) to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0.75em</code>.
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

## SIZING ELEMENTS

### Rem

<p class="p__1qg33Igem5pAgn4kPMirjw">
The second relative unit of measurement in CSS is the <em>rem</em>,
coded as <code class="code__2rdF32qjRVp7mMVBHuPwDS">rem</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Rem stands for <em>root em</em>. It acts similar to em, but instead of
checking parent elements to size font, it checks the <em>root
element</em>. The root element is the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<html\></code> tag.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Most browsers set the font size of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<html\></code> to 16 pixels,
so by default rem measurements will be compared to that value. To set a
different font size for the root element, you can add a CSS rule.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">html</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-size</span><span class="mtk1">:</span><span class="mtk9"> 20px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk4">h1</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">font-size</span><span class="mtk1">:</span><span class="mtk9"> 2rem</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the font size of the root element,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<html\></code>, is set to 20
pixels. All subsequent rem measurements will now be compared to that
value and the size of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> elements in the
example will be 40 pixels.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
One advantage of using rems is that all elements are compared to the
same font size value, making it easy to predict how large or small font
will appear. If you are interested in sizing elements consistently
across an entire website, the rem measurement is the best unit for the
job. If you’re interested in sizing elements in comparison to other
elements nearby, then the em unit would be better suited for the job.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, add a new rule on line 3 that sets the
font size of the root element to 16 pixels.
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
Let’s update the font sizes you set in the previous exercise to use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rem</code> instead of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">em</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
First, change the font size in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#banner h1</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">3.75rem</code>.
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
Set the font size in <code class="code__2rdF32qjRVp7mMVBHuPwDS">.post
h2</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">1.875rem</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Set the font size in <code class="code__2rdF32qjRVp7mMVBHuPwDS">.post
h3</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">1.125rem</code>.
</p>

<span aria-live="assertive">Checkpoint 5 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">5.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Set the font size of the footer to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1.125rem</code>.
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

## SIZING ELEMENTS

### Percentages: Height & Width

<p class="p__1qg33Igem5pAgn4kPMirjw">
To size non-text HTML elements relative to their parent elements on the
page you can use <em>percentages</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Percentages are often used to size box-model values, like width and
height, padding, border, and margins. They can also be used to set
positioning properties (top, bottom, left, right).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To start, let’s size the height and width of an element using
percentages.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.main</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 500px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.main</span><span class="mtk9"> </span><span class="mtk7">.subsection</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 50%</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 50%</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.main</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.subsection</code> each
represent divs. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.subsection</code> div is
nested within the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.main</code> div. Note that
the dimensions of the parent div
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">.main</code>) have been set
to a height of 300 pixels and a width of 500 pixels.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When percentages are used, elements are sized relative to the dimensions
of their parent element (also known as a container). Therefore, the
dimensions of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.subsection</code> div will
be 150 pixels tall and 250 pixels wide. Be careful, a child element’s
dimensions may be set erroneously if the dimensions of its parent
element aren’t set first.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> Because the box model includes padding, borders,
and margins, setting an element’s
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100%</code> may cause content
to overflow its parent container. While tempting,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100%</code> should only be
used when content will not have padding, border, or margin.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Currently, the blog takes up the full width of the body. Let’s modify
this so that it doesn’t extend to fill the full width.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, set the width in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#blog</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">86%</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This will responsively set the entire blog’s container to 86% of the
full width of the body.
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
Great! Resize the browser’s width again. Notice that the blog’s text
becomes illegible at smaller widths.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To fix this, set the width in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#blog .post</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">52%</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This will ensure that the text fills only 52% of its container’s
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">#blog</code>) width. Resize
the browser now and notice how the text remains legible.
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
Now set the width in <code class="code__2rdF32qjRVp7mMVBHuPwDS">.post
.image-container</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100%</code>. This will make
sure the image’s container is always the full width of the blog post
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">.post</code>).
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
Scroll to the bottom of the web page. Notice that there are two images.
We’d like to display these images next to each other on the page, with
equal width.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Set the width in <code class="code__2rdF32qjRVp7mMVBHuPwDS">.images
.image-container</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">50%</code>. This will give
each image in <code class="code__2rdF32qjRVp7mMVBHuPwDS">.images</code>
equal width.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Don’t worry if the images still look distorted at the moment. You’ll
improve their appearance in a later exercise.
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

## SIZING ELEMENTS

### Percentages: Padding & Margin

<p class="p__1qg33Igem5pAgn4kPMirjw">
Percentages can also be used to set the padding and margin of elements.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When height and width are set using percentages, you learned that the
dimensions of child elements are calculated based on the dimensions of
the parent element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When percentages are used to set padding and margin, however, they are
calculated based only on the <em>width</em> of the parent element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, when a property like
<code class="code__2rdF32qjRVp7mMVBHuPwDS">margin-left</code> is set
using a percentage (say
<code class="code__2rdF32qjRVp7mMVBHuPwDS">50%</code>), the element will
be moved halfway to the right in the parent container (as opposed to the
child element receiving a margin half of its parent’s margin).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Vertical padding and margin are also calculated based on the width of
the parent. Why? Consider the following scenario:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A container div is defined, but its height is not set (meaning it’s
flat).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The container then has a child element added within. The child element
<em>does</em> have a set height. This causes the height of its parent
container to stretch to that height.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The child element requires a change, and its height is modified. This
causes the parent container’s height to also stretch to the new height.
This cycle occurs endlessly whenever the child element’s height is
changed!
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the scenario above, an unset height (the parent’s) results in a
constantly changing height due to changes to the child element. This is
why vertical padding and margin are based on the width of the parent,
and not the height.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> When using relative sizing, ems and rems should
be used to size text and dimensions on the page related to text size
(i.e. padding around text). This creates a consistent layout based on
text size. Otherwise, percentages should be used.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s size the height of the banner relative to the root element’s font
size.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#banner</code> ruleset, add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code> property and
assign it to <code class="code__2rdF32qjRVp7mMVBHuPwDS">46rem</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> The root element’s font size is 16 pixels,
meaning that <code class="code__2rdF32qjRVp7mMVBHuPwDS">46rem</code>
will result in a height of 736 pixels.
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
Set the top margin in <code class="code__2rdF32qjRVp7mMVBHuPwDS">#blog
.post</code> to <code class="code__2rdF32qjRVp7mMVBHuPwDS">12.5%</code>.
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
Set the bottom margin in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">#blog .post</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">7.5%</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Set the bottom margin in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.images</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">20%</code>.
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

## SIZING ELEMENTS

### Width: Minimum & Maximum

<p class="p__1qg33Igem5pAgn4kPMirjw">
Although relative measurements provide consistent layouts across devices
of different screen sizes, elements on a website can lose their
integrity when they become too small or large. You can limit how wide an
element becomes with the following properties:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code> — ensures a
minimum width for an element.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> — ensures a
maximum width for an element.
</li>
</ol>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">min-width</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">max-width</span><span class="mtk1">:</span><span class="mtk9"> 600px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, when the browser is resized, the width of
paragraph elements will not fall below 300 pixels, nor will their width
exceed 600 pixels.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When a browser window is narrowed or widened, text can become either
very compressed or very spread out, making it difficult to read. These
two properties ensure that content is legible by limiting the minimum
and maximum widths.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note</strong>: The unit of pixels is used to ensure hard limits
on the dimensions of the element(s).
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Resize the browser to the right. Notice that the text on the web page
can become difficult to read. Let’s limit the text’s width to keep it
legible.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, create a CSS rule that sets the minimum
width of all paragraphs to 200 pixels and run your code.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now, resize your browser (make it narrower) and notice that the text no
longer compresses as much as it did before.
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

## SIZING ELEMENTS

### Height: Minimum & Maximum

<p class="p__1qg33Igem5pAgn4kPMirjw">
You can also limit the minimum and maximum <em>height</em> of an
element.
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-height</code> — ensures a
minimum height for an element’s box.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code> — ensures a
maximum height for an element’s box.
</li>
</ol>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">p</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">min-height</span><span class="mtk1">:</span><span class="mtk9"> 150px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">max-height</span><span class="mtk1">:</span><span class="mtk9"> 300px</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the height of all paragraphs will not shrink below
150 pixels and the height will not exceed 300 pixels.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
What will happen to the contents of an element if the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code> property is
set too low for that element? It’s possible that content will overflow
outside of the element, resulting in content that is not legible.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Again, resize your browser (stretch it out). Notice that the paragraph’s
text can become overly spread out (i.e. a small height). Let’s limit the
height to keep the text legible.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, set the minimum height of all paragraphs
to 200 pixels.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Resize your browser once more and notice that the text no longer spreads
out as much as it did before.
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

## SIZING ELEMENTS

### Scaling Images and Videos

<p class="p__1qg33Igem5pAgn4kPMirjw">
Many websites contain a variety of different media, like images and
videos. When a website contains such media, it’s important to make sure
that it is scaled proportionally so that users can correctly view it.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 50%</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> 200px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">overflow</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">hidden</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.container</span><span class="mtk9"> </span><span class="mtk4">img</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">max-width</span><span class="mtk1">:</span><span class="mtk9"> 100%</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">height</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">auto</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">display</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">block</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.container</code> represents
a container div. It is set to a width of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">50%</code> (half of the
browser’s width, in this example) and a height of 200 pixels. Setting
<code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hidden</code> ensures that
any content with dimensions larger than the container will be hidden
from view.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The second CSS rule ensures that images scale with the width of the
container. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">height</code>
property is set to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">auto</code>, meaning an
image’s height will <em>automatically</em> scale proportionally with the
width. Finally, the last line will display images as block level
elements (rather than inline-block, their default state). This will
prevent images from attempting to align with other content on the page
(like text), which can add unintended margin to the images.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
It’s worth memorizing the entire example above. It represents a <em>very
common</em> design pattern used to scale images and videos
proportionally.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
<strong>Note:</strong> The example above scales the width of an image
(or video) to the width of a container. If the image is larger than the
container, the vertical portion of the image will overflow and will not
display. To swap this behavior, you can set
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">100%</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">auto</code> (essentially
swapping the values). This will scale the <em>height</em> of the image
with the height of the container instead. If the image is larger than
the container, the horizontal portion of the image will overflow and not
display.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at the images on the web page. Notice that they currently
display incorrectly (too large). Let’s fix that.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
First, in <strong>style.css</strong>, set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">overflow</code> property in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.image-container</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">hidden</code>. Run your code.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Take a look at the images once more. At this point, the images partially
display. In reality, what we’ve done is constrain them to the dimensions
of their container
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">.image-container</code>).
Any part of the image that overflows out of the container will be hidden
from view. This will set us up to scale them proportionally.
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
Resize the width of the browser back and forth. Notice that the images
expand and contract to show more (or less) of the image. Instead, let’s
display the full image at all times.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, set the maximum width in
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.image-container img</code>
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">100%</code>. This will
ensure the full image is always displayed.
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
Great work! Take a look at the images on the web page again — they have
been greatly improved!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Next, we’ll want to make sure the images automatically remain in
proportion when the browser is resized.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In <code class="code__2rdF32qjRVp7mMVBHuPwDS">.image-container
img</code>, set the height to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">auto</code>.
</p>

<span aria-live="assertive">Checkpoint 4 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">4.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Finally, within the same CSS rule, set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">block</code>. This will
instruct the images to behave as block-level elements and facilitate
scaling (as opposed to their default inline behavior).
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

## SIZING ELEMENTS

### Scaling Background Images

<p class="p__1qg33Igem5pAgn4kPMirjw">
Background images of HTML elements can also be scaled responsively using
CSS properties.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">body</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-image</span><span class="mtk1">:</span><span class="mtk9"> url</span><span class="mtk1">(</span><span class="mtk8">'#'</span><span class="mtk1">);</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-repeat</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">no-repeat</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-position</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">center</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">background-size</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk5">cover</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, the first CSS declaration sets the background
image (<code class="code__2rdF32qjRVp7mMVBHuPwDS">\#</code> is a
placeholder for an image URL in this example). The second declaration
instructs the CSS compiler to not repeat the image (by default, images
will repeat). The third declaration centers the image within the
element.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The final declaration, however, is the focus of the example above. It’s
what scales the background image. The image will <em>cover</em> the
entire background of the element, all while keeping the image in
proportion. If the dimensions of the image exceed the dimensions of the
container then only a portion of the image will display.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In <strong>style.css</strong>, set the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">background-size</code>
property in <code class="code__2rdF32qjRVp7mMVBHuPwDS">#banner</code> to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">cover</code>.
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

## SIZING ELEMENTS

### Review: Relative Measurements

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great work! You learned how to size elements on a website relative to
other elements on the page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s review what you learned:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Content on a website can be sized relative to other elements on the page
using <em>relative measurements</em>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The unit of <code class="code__2rdF32qjRVp7mMVBHuPwDS">em</code> sizes
font relative to the font size of a parent element.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The unit of <code class="code__2rdF32qjRVp7mMVBHuPwDS">rem</code> sizes
font relative to the font size of a root element. That root element is
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<html\></code> element.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Percentages are commonly used to size box-model features, like the
width, height, padding, or margin of an element.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
When percentages are used to size width and height, child elements will
be sized relative to the dimensions of their parent (remember that
parent dimensions must first be set).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Percentages can be used to set padding and margin. Horizontal and
vertical padding and margin are set relative to the width of a parent
element.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The minimum and maximum width of elements can be set using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The minimum and maximum height of elements can be set using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-height</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
When the height of an image or video is set, then its width can be set
to <code class="code__2rdF32qjRVp7mMVBHuPwDS">auto</code> so that the
media scales proportionally. Reversing these two properties and values
will also achieve the same result.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A background image of an HTML element will scale proportionally when its
<code class="code__2rdF32qjRVp7mMVBHuPwDS">background-size</code>
property is set to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">cover</code>.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Relative units of measurement are a first step towards incorporating
responsive design in a website. When combined with more advanced
responsive techniques, you can create a seamless user experience
regardless of a device’s screen size.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Take some time to experiment with your new knowledge of relative
measurements in <strong>style.css</strong>. When you’re done, proceed to
the next unit.
</p>

**Solutions**

``` html
```

## MEDIA QUERIES

### Responsive Web Design

<p class="p__1qg33Igem5pAgn4kPMirjw">
When someone visits a website, it’s possible they are viewing it on a
phone, tablet, computer, or even a TV monitor. Because screen sizes can
vary greatly across different devices, it’s important for websites to
resize and reorganize their content to best fit screens of all sizes.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
When a website doesn’t respond to different screen sizes, the website
may look odd or become indecipherable on certain devices. This usually
occurs on smaller screens, like phones. When a website responds to the
size of the screen it’s viewed on, it’s called a <em>responsive</em>
website.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Because websites can be displayed on thousands of different screen
sizes, they must be able to respond to a change in screen size and adapt
the content so that users can access it.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s take a look at a website that does not respond to different screen
sizes.
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
First, visit
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-5/globe-book-store/index.html">this
site</a>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Then resize the width of your browser to simulate a smaller screen size.
Note how the content on the web page does not shrink as you resize the
browser’s width.
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In contrast, let’s take a look at a responsive website.
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
First, visit
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-5/globe-book-store/index-responsive.html">this
site</a>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Again, resize the width of your browser and note how the content on the
web page resizes and reorganizes itself.
</li>
</ol>

**Solutions**

``` html
```

## MEDIA QUERIES

### Viewport Meta Tag

<p class="p__1qg33Igem5pAgn4kPMirjw">
Thus far, we have been learning about creating responsive web designs
with CSS. However, in order for us to enable this responsive CSS to
work, we need to get familiar with the HTML viewport meta tag!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s start with the <em>viewport</em>, which is the total viewable area
for a user; this area varies depending on device. The viewport is
smaller on a mobile device and larger on a desktop.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Based on the size of the viewport, the <em>meta tag</em>
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<meta\></code>) is used to
instruct the browser on how to render the webpage’s scale and
dimensions. For instance, say if a web page is 960px and the device is
320px wide. Adding the viewport meta tag will squish the content down
until it is 320px — there is no need for the user to zoom out and view
the whole page!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside the <code class="code__2rdF32qjRVp7mMVBHuPwDS">\<head\></code>
element, we will find where the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<meta\></code> tag syntax is
implemented:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-html" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk16">&lt;!DOCTYPE html&gt;</span><span class="mtk1"> </span></span><br><span><span class="mtk4">&lt;html</span><span class="mtk1"> </span><span class="mtk7">lang</span><span class="mtk1">=</span><span class="mtk8">"en"</span><span class="mtk4">&gt;</span><span class="mtk1"> </span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;head&gt;</span><span class="mtk1"> </span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;...</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">&lt;meta</span><span class="mtk1"> </span><span class="mtk7">name</span><span class="mtk1">=</span><span class="mtk8">"viewport"</span><span class="mtk1"> </span><span class="mtk7">content</span><span class="mtk1">=</span><span class="mtk8">"width=device-width, initial-scale=1"</span><span class="mtk4">&gt;</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;...</span></span><br><span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk4">&lt;/head&gt;</span><span class="mtk1"> </span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We can break down the added
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<meta\></code> tag into the
following essential components:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">name=“viewport”</code>
attribute: tells the browser to display the web page at the same width
as its screen
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">content</code> attribute:
defines the values for the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<meta\></code> tag,
including <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">initial-scale</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">width=device-width</code>
key-value pair: controls the size of the viewport in which it sets the
width of the viewport to equal the width of the device
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">initial-scale=1</code>
key-value pair: sets the initial zoom level (Read more about scale at
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag#viewport_basics">MDN’s
viewport documentation</a>)
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The viewport meta tag allows our web pages to be responsive and adapt a
site’s contents to the users’ screen size. We’ll explore more on
actually implementing this responsiveness in the later exercises, but
for now, we need to first include the meta tag in our HTML file!
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
At the top of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">index.html</code>, create a
viewport meta tag. Be sure to include the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">name</code>,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">content</code> properties,
and other appropriate values.
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

## MEDIA QUERIES

### Media Queries

<p class="p__1qg33Igem5pAgn4kPMirjw">
CSS uses <em>media queries</em> to adapt a website’s content to
different screen sizes. With media queries, CSS can detect the size of
the current screen and apply different CSS styles depending on the width
of the screen.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">@media</span><span class="mtk9"> only </span><span class="mtk7">screen</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">max-width</span><span class="mtk1">:</span><span class="mtk9"> 480px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;body </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk10">font-size</span><span class="mtk1">:</span><span class="mtk9"> 12px</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk1">}</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The example above demonstrates how a media query is applied. The media
query defines a rule for screens smaller than 480 pixels (approximately
the width of many smartphones in
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Page_orientation">landscape</a>
orientation).
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s break this example down into its parts:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">@media</code> — This keyword
begins a media query rule and instructs the CSS compiler on how to parse
the rest of the rule.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">only screen</code> —
Indicates what types of devices should use this rule. In early attempts
to target different devices, CSS incorporated different media types
(screen, print, handheld). The rationale was that by knowing the media
type, the proper CSS rules could be applied. However, “handheld” and
“screen” devices began to occupy a much wider range of sizes and having
only one CSS rule per media device was not sufficient.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">screen</code> is the media
type always used for displaying content, no matter the type of device.
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">only</code> keyword is
added to indicate that this rule only applies to one media type
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">screen</code>).
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<code class="code__2rdF32qjRVp7mMVBHuPwDS">and (max-width :
480px)</code> — This part of the rule is called a <em>media
feature</em>, and instructs the CSS compiler to apply the CSS styles to
devices with a width of 480 pixels or smaller. Media features are the
conditions that must be met in order to render the CSS within a media
query.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
CSS rules are nested inside of the media query’s curly braces. The rules
will be applied when the media query is met. In the example above, the
text in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">body</code>
element is set to a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-size</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">12px</code> when the user’s
screen is less than 480px.
</li>
</ol>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
At the bottom of <strong>style.css</strong>, write a media query for a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">480px</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This will allow us to shrink the width of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.page-title</code> element on
smaller screens.
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
When the screen is less than
<code class="code__2rdF32qjRVp7mMVBHuPwDS">480px</code> wide, give the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.page-title</code> class a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">270px</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This will make the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.page-title</code> element
appear more clearly on small screens. Test your code by resizing the
browser.
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

## MEDIA QUERIES

### Range

<p class="p__1qg33Igem5pAgn4kPMirjw">
Specific screen sizes can be targeted by setting multiple width and
height media features.
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-height</code> are used to
set the minimum width and minimum height, respectively. Conversely,
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-height</code> set the
maximum width and maximum height, respectively.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By using multiple widths and heights, a range can be set for a media
query.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">@media</span><span class="mtk9"> only </span><span class="mtk7">screen</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">min-width</span><span class="mtk1">:</span><span class="mtk9"> 320px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">max-width</span><span class="mtk1">:</span><span class="mtk9"> 480px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk16">/* ruleset for 320px -&nbsp;480px */</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The example above would apply its CSS rules only when the screen size is
between 320 pixels and 480 pixels. Notice the use of a second
<code class="code__2rdF32qjRVp7mMVBHuPwDS">and</code> keyword after the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code> media
feature. This allows us to chain two requirements together.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The example above can be written using two separate rules as well:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">@media</span><span class="mtk9"> only </span><span class="mtk7">screen</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">min-width</span><span class="mtk1">:</span><span class="mtk9"> 320px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">{</span><span class="mtk9"> </span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk16">/* ruleset for &gt;= 320px */</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span> </span></span><br><span><span class="mtk12">@media</span><span class="mtk9"> only </span><span class="mtk7">screen</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">min-width</span><span class="mtk1">:</span><span class="mtk9"> 480px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">{</span><span class="mtk9"> </span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk16">/* ruleset for &gt;= 480px */</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The first media query in the example above will apply CSS rules when the
size of the screen meets or exceeds 320 pixels. The second media query
will then apply CSS rules when the size of the screen meets or exceeds
480 pixels, meaning that it can override CSS rules present in the first
media query or apply additional CSS rules that are not already present
in the first.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Both examples above are valid, and it is likely that you will see both
patterns used when reading another developer’s code.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Let’s make the gallery images appear larger when the screen size is
small to medium size.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write one <code class="code__2rdF32qjRVp7mMVBHuPwDS">@media</code> query
for screen sizes with a range between
<code class="code__2rdF32qjRVp7mMVBHuPwDS">320px</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">480px</code>. Use
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> to define
the range.
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
Inside the media query, select the thumbnails within the gallery with
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.gallery-item
.thumbnail</code> and give them a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">95%</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You should notice that the gallery images appear wider when the screen
size is between 320 and 480 pixels wide.
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

## MEDIA QUERIES

### Dots Per Inch (DPI)

<p class="p__1qg33Igem5pAgn4kPMirjw">
Another media feature we can target is screen resolution. Many times we
will want to supply higher quality media (images, video, etc.) only to
users with screens that can support high resolution media. Targeting
screen resolution also helps users avoid downloading high resolution
(large file size) images that their screen may not be able to properly
display.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To target by resolution, we can use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-resolution</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-resolution</code> media
features. These media features accept a resolution value in either dots
per inch (dpi) or dots per centimeter (dpc). Learn more about resolution
measurements
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://en.wikipedia.org/wiki/Dots_per_inch">here</a>.
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">@media</span><span class="mtk9"> only </span><span class="mtk7">screen</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">min-resolution</span><span class="mtk1">:</span><span class="mtk9"> 300dpi</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk16">/* CSS for high resolution screens */</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The media query in the example above targets high resolution screens by
making sure the screen resolution is at least 300 dots per inch. If the
screen resolution query is met, then we can use CSS to display high
resolution images and other media.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a media query to make the logo higher quality if the visitor is
looking at the Amazing Space website on a high resolution display.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A high resolution display may have a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-resolution</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">150dpi</code>.
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
Inside of the media query, add this CSS property to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.logo</code> class:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">background-image</span><span class="mtk9">: </span><span class="mtk4">url(</span><span class="mtk8">"../img/spaceship@2x.png"</span><span class="mtk1">)</span><span class="mtk9">;</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This code will exchange the existing logo with a higher resolution logo.
To make the difference obvious, the higher resolution spaceship logo has
blue wings.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you are accessing Codecademy on a screen with a resolution greater
than 150dpi, you will observe the spaceship change. If not, you can
re-write the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-resolution</code> media
feature to a lower value to observe the change.
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

## MEDIA QUERIES

### And Operator

<p class="p__1qg33Igem5pAgn4kPMirjw">
In previous exercises, we chained multiple media features of the same
type in one media query by using the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">and</code> operator. It
allowed us to create a range by using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> in the same
media query.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">and</code> operator can
be used to require multiple media features. Therefore, we can use the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">and</code> operator to
require both a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">480px</code> <em>and</em> to
have a <code class="code__2rdF32qjRVp7mMVBHuPwDS">min-resolution</code>
of <code class="code__2rdF32qjRVp7mMVBHuPwDS">300dpi</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">@media</span><span class="mtk9"> only </span><span class="mtk7">screen</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">max-width</span><span class="mtk1">:</span><span class="mtk9"> 480px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">min-resolution</span><span class="mtk1">:</span><span class="mtk9"> 300dpi</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk16">/* CSS ruleset */</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By placing the <code class="code__2rdF32qjRVp7mMVBHuPwDS">and</code>
operator between the two media features, the browser will require both
media features to be true before it renders the CSS within the media
query. The <code class="code__2rdF32qjRVp7mMVBHuPwDS">and</code>
operator can be used to chain as many media features as necessary.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The website’s text needs to be larger for users who have small, low
resolution screens.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a media query that applies when the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-resolution</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">150dpi</code> and the screen
has a <code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">480px</code>.
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
Inside the media query, make the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-size</code> of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.page-description</code>
element <code class="code__2rdF32qjRVp7mMVBHuPwDS">20px</code>.
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

## MEDIA QUERIES

### Comma Separated List

<p class="p__1qg33Igem5pAgn4kPMirjw">
If only one of multiple media features in a media query must be met,
media features can be separated in a comma separated list.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, if we needed to apply a style when only one of the below is
true:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The screen is more than 480 pixels wide
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The screen is in landscape mode
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
We could write:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">@media</span><span class="mtk9"> only </span><span class="mtk7">screen</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">min-width</span><span class="mtk1">:</span><span class="mtk9"> 480px</span><span class="mtk1">),</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">orientation</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">landscape</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk16">/* CSS ruleset */</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the example above, we used a comma
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">,</code>) to separate
multiple rules. The example above requires only one of the media
features to be true for its CSS to apply.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Note that the second media feature is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">orientation</code>. The
<code class="code__2rdF32qjRVp7mMVBHuPwDS">orientation</code> media
feature detects if the page has more width than height. If a page is
wider, it’s considered
<code class="code__2rdF32qjRVp7mMVBHuPwDS">landscape</code>, and if a
page is taller, it’s considered
<code class="code__2rdF32qjRVp7mMVBHuPwDS">portrait</code>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Navigate to the media query where you targeted screens with a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">320px</code> and a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">480px</code>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that you have located this media query, let’s also make the logo and
text appear vertical if the screen is in portrait orientation. To do
this, add an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">orientation</code> media
feature after inserting a comma
(<code class="code__2rdF32qjRVp7mMVBHuPwDS">,</code>) to separate the
rules. This new media feature should check if the screen’s
<code class="code__2rdF32qjRVp7mMVBHuPwDS">orientation</code> is
<code class="code__2rdF32qjRVp7mMVBHuPwDS">portrait</code>.
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

## MEDIA QUERIES

### Breakpoints

<p class="p__1qg33Igem5pAgn4kPMirjw">
We know how to use media queries to apply CSS rules based on screen size
and resolution, but how do we determine what queries to set?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The points at which media queries are set are called
<em>breakpoints</em>. Breakpoints are the screen sizes at which your web
page does not appear properly. For example, if we want to target tablets
that are in landscape orientation, we can create the following
breakpoint:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk12">@media</span><span class="mtk9"> only </span><span class="mtk7">screen</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">min-width</span><span class="mtk1">:</span><span class="mtk9"> 768px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">max-width</span><span class="mtk1">:</span><span class="mtk9"> 1024px</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk12">and</span><span class="mtk9"> </span><span class="mtk1">(</span><span class="mtk10">orientation</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk12">landscape</span><span class="mtk1">)</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk16">/* CSS ruleset */</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
The example above creates a screen size range the size of a tablet in
landscape mode and also identifies the orientation.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
However, setting breakpoints for every device imaginable would be
incredibly difficult because there are many devices of differing shapes
and sizes. In addition, new devices are released with new screen sizes
every year.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Rather than set breakpoints based on specific devices, the best practice
is to resize your browser to view where the website naturally breaks
based on its content. The dimensions at which the layout breaks or looks
odd become your media query breakpoints. Within those breakpoints, we
can adjust the CSS to make the page resize and reorganize.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
By observing the dimensions at which a website naturally breaks, you can
set media query breakpoints that create the best possible user
experience on a project by project basis, rather than forcing every
project to fit a certain screen size. Different projects have different
needs, and creating a responsive design should be no different.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Check out
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/unit-5/screen-sizes.png">this</a>
list of breakpoints by device widths. Use it as a reference of screen
widths to test your website to make certain it looks great across a
variety of devices.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
The last breakpoint we’d like to account for is a tablet in landscape
orientation. The Amazing Space website should change its format to show
the gallery pictures on the right, while having the logo and the
description on the left.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a media query that meets the following requirements:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The screen has a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">min-width</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">768px</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The screen has a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">max-width</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">1024px</code>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The screen has an
<code class="code__2rdF32qjRVp7mMVBHuPwDS">orientation</code> of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">landscape</code>
</li>
</ul>

<span aria-live="assertive">Checkpoint 2 Passed</span>

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">2.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside of the media query, include this CSS:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk7">.page-title</span><span class="mtk1">,</span><span class="mtk9"> </span><span class="mtk7">.page-description</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;</span><span class="mtk10">float</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">left</span><span class="mtk1">;</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk10">width</span><span class="mtk1">:</span><span class="mtk9"> 20em</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br><span><span> </span></span><br><span><span class="mtk7">.page-description</span><span class="mtk9"> </span><span class="mtk1">{</span></span><br><span><span class="mtk9">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk10">text-align</span><span class="mtk1">:</span><span class="mtk9"> </span><span class="mtk10">left</span><span class="mtk1">;</span></span><br><span><span class="mtk1">}</span></span><br></div></code></pre></pre>
<p class="p__1qg33Igem5pAgn4kPMirjw">
This CSS will make the page title and description float to the left of
the gallery images. Resize the browser to observe these changes at
various screen widths.
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

## MEDIA QUERIES

### Review: Media Queries

<p class="p__1qg33Igem5pAgn4kPMirjw">
Incredible work! You learned how to change the way a website appears on
different screens with media queries and breakpoints
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Throughout this lesson, you learned:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
When a website responds to the size of the screen it’s viewed on, it’s
called a <em>responsive</em> website.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
You can write <em>media queries</em> to help with different screen
sizes.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Adding the viewport
<code class="code__2rdF32qjRVp7mMVBHuPwDS">\<meta\></code> tag to our
code allows us to control the width and scaling of the viewport so that
it’s sized and scaled correctly on all devices.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Media queries require <em>media features</em>. Media features are the
conditions that must be met to render the CSS within a media query.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Media features can detect many aspects of a user’s browser, including
the screen’s width, height, resolution, orientation, and more.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The <code class="code__2rdF32qjRVp7mMVBHuPwDS">and</code> operator
requires multiple media features to be true at once.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A comma separated list of media features only requires one media feature
to be true for the code within to be applied.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
The best practice for identifying where media queries should be set is
by resizing the browser to determine where the content naturally breaks.
Natural breakpoints are found by resizing the browser.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
With your knowledge of media queries and CSS, you can make websites that
look great on any device, from a small phone to a huge television. By
making your websites responsive, you’ll make it possible for any of your
users to have a great experience.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Click ‘Up Next’ to continue.
</p>

**Solutions**

``` html
```

## Simulate Different Screen Sizes with Device Mode in Chrome DevTools

<p class="p__1qg33Igem5pAgn4kPMirjw">
→
<strong><a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.chrome.com/docs/devtools/device-mode">Simulate
Different Screen Sizes with Device Mode in Chrome DevTools</a></strong>
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this article, you will learn how to simulate different screen sizes
with device mode in Chrome DevTools in order to approximate how your
page looks and performs on different devices. This is helpful if you
want to ensure that the components of your page would be readable on
mobile devices. There’s also value in seeing how your website would load
on a device with a weak or non-existent connection to the network. After
you finish reading the article, return to this page and complete the
following assessments.
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

## WEB DEVELOPMENT FOUNDATIONS

### Tsunami Coffee

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use your knowledge of relative units and responsive web design to help
Tsunami Coffee make their website come to life.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Throughout this project, you’ll edit the existing Tsunami Coffee website
code so that the website appears correctly on varying screen sizes. In
addition, you’ll contribute styles that will make this website more
visually appealing.
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
The website needs a background image in the main section at the top of
the page.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Navigate to <strong>style.css</strong> and add the following image to
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.main</code> class as a
cover-sized background image:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="shell" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk1">https://content.codecademy.com/courses/freelance-1</span><span class="mtk1">/unit-5/tsunami-coffee/images/bg-photo.png</span></span><br></div></code></pre></pre>

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
The navigation items at the top of the page need more padding.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Add a padding of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0.75rem</code> to the top and
bottom, and <code class="code__2rdF32qjRVp7mMVBHuPwDS">1.25rem</code> to
the left and right of the navigation’’s list items.
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
The coffee beans image under the main banner in the supporting section
is too large.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Inside of the <code class="code__2rdF32qjRVp7mMVBHuPwDS">.supporting
img</code> selector, set the height and width dimensions to 10 percent.
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
The coffee beans image looks better now, but the text to the right of it
needs to be spaced out further from the image.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Set the right margin of the image to 5 percent.
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
The font size of the rating should be increased within the rating
section.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Use <code class="code__2rdF32qjRVp7mMVBHuPwDS">rem</code> units to make
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> text equivalent
to 40 pixels. This can be calculated based on the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">html</code> element’s font
size.
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
The map image near the bottom of the page should span the page’s width,
instead of overflowing.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Add a width of 100 percent to the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.location img</code> CSS
rule.
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
Now the page looks better on large screens. When the page is resized to
a smaller width, the page needs to resize and reorganize its elements
using media queries.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a media query that targets the screen when its width is under 960
pixels and smaller.
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
When the page is resized to a width less than 960 pixels, note that the
navigation bar has empty space above it. Within the media query you
wrote in the last step, set the top padding of the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.main</code> class to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code>.
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
Resize the browser from large to small. Notice that the coffee beans
image in the supporting section causes the supporting paragraph to
become too thin.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a media query for screens under 700 pixels.
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
Inside the media query, make the image disappear by ensuring that the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">.supporting img</code>
selector displays nothing.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can make an element disappear using the following property and
value:
</p>
<pre class="pre__3_SOs7YT7NaHjnNunEArSM"><pre><code><div data-lang="codecademy-css" class="gamut-1oq8wcb-ColorizedContainer e1hgti5c0"><span><span class="mtk4">display</span><span class="mtk9">: </span><span class="mtk4">none</span><span class="mtk9">;</span></span><br></div></code></pre></pre>

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
Continue to resize the width of the browser until the website is the
size of a small screen.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Write a media query that targets a screen width less than 470 pixels.
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
Inside the media query for small screens, you’’ll need to apply a
variety of styles.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
First, make the rating’s
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code> font size the
equivalent of 32 pixels using
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rem</code> units.
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
The images in the gallery are too small for small screens.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Select the images in the gallery and style them so that they fill the
width of the screen.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Then set their margin to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">0</code> so they span across
the entire page.
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
The footer’s text is not formatted correctly on small screen sizes.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Hide the <code class="code__2rdF32qjRVp7mMVBHuPwDS">nav</code> inside
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">footer</code> to appear
better on small screens.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Then, resize the screen from small to large and watch your website
change its appearance to best fit the screen size. You just built a
responsive website!
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

## DOCUMENTATION AND RESEARCH

### Overview

<p class="p__1qg33Igem5pAgn4kPMirjw">
Building websites requires technical knowledge of multiple languages and
frameworks. You may wonder, “How is it possible for developers to know
everything there is to know about every language?” The answer is,
thankfully, they don’t. One of the most essential skills of being a
developer is knowing how to investigate solutions to problems you have
not yet learned how to solve.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this lesson, you will learn how to look up new ways to use
previously-learned CSS properties and discover entirely new CSS
properties.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
On the right side of the screen is the portfolio site that you will
develop into
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/capstone-1-documentation/mocks.jpg">the
final product</a>. We suggest you keep this mock open in a separate tab
for reference throughout the lesson.
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Take some time to read the code in the code editor (some of which may be
unfamiliar). Notice the differences between our current site and the
final mock.
</p>

**Solutions**

``` html
```

## DOCUMENTATION AND RESEARCH

### Documentation

<p class="p__1qg33Igem5pAgn4kPMirjw">
Every well-developed language or framework has a place where you can
look up all of its features. This library of information is called a
language’s <em>documentation</em>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
You can find the documentation for CSS at
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/">Mozilla
Developer Network</a>. In addition to CSS, The Mozilla Developer Network
(referred to as MDN) contains the complete documentation for HTML,
JavaScript, and many other essential tools of web development.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To see the documentation for a specific CSS property, navigate to the
MDN website and search for that property in the search bar at the top of
the page. Then, click on the link for that property. For example, search
for the <code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code>
property. The list of results might appear intimidating, but you should
quickly see a link starting with the description “The font-weight css
property…”. This is the link we want.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Once you land on a property’s documentation page you can read all of the
information about it. For example,
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight"><code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code></a>
starts with a description of the property. The “Values” section lists
all of the possible values for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-weight</code>. There are
some values you already know, such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">normal</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">bold</code>, but there are
also new values, such as
<code class="code__2rdF32qjRVp7mMVBHuPwDS">lighter</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">bolder</code>.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
As you can see in the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/capstone-1-documentation/mocks.jpg">mock</a>,
on smaller screen sizes we want to hide our
<code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code>. Look up the
documentation for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> on
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/">MDN</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In the “Grouped values” section, find a value that will turn off the
display of an element. Add a
<code class="code__2rdF32qjRVp7mMVBHuPwDS">display</code> property with
that value to the <code class="code__2rdF32qjRVp7mMVBHuPwDS">h1</code>
rule in the <code class="code__2rdF32qjRVp7mMVBHuPwDS">@media</code>
query at the bottom of <strong>style.css</strong>.
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
The <strong>style.css</strong> file includes a property you might not
know — <code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code>. Read the
documentation for
<code class="code__2rdF32qjRVp7mMVBHuPwDS">float</code> to see what the
property does and what values it can accept.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Update the <code class="code__2rdF32qjRVp7mMVBHuPwDS">ul</code> rule to
push the <code class="code__2rdF32qjRVp7mMVBHuPwDS">ul</code> to the
right side of the navigation bar.
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

## DOCUMENTATION AND RESEARCH

### Google

<p class="p__1qg33Igem5pAgn4kPMirjw">
Documentation is an essential tool to learn about properties. However,
what if you don’t even know what property you need?
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In situations like this, it might come as no surprise that using
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://google.com/">Google</a>
is a great way to read other developers’ solutions to problems. Googling
the problem you’re trying to solve and the language you’re using will
yield many useful answers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
For example, if you want to know how to change the size of text, you
could google “how to change text size using CSS.” After doing this, you
will receive multiple links to information about the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">font-size</code> property.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/capstone-1-documentation/mocks.jpg">mock</a>,
we can see that the <code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code>
elements should have a light shadow beneath them. Use Google to find out
which CSS property allows you to add a shadow beneath text. Once you’ve
found the property, set its value to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">2px 2px 0 #bbbbbb</code> in
the <code class="code__2rdF32qjRVp7mMVBHuPwDS">a</code> rule (try to
figure out what this value will do by reading the documentation for the
property).
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

## DOCUMENTATION AND RESEARCH

### Stack Overflow

<p class="p__1qg33Igem5pAgn4kPMirjw">
While using Google in the previous exercise, you may have noticed a lot
of links to a site called
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://stackoverflow.com/"><em>Stack
Overflow</em></a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Stack Overflow is a useful resource where developers ask and answer
questions. You should use it to find answers to your questions, and
learn from experienced developers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Reading all of the top-voted answers to a Stack Overflow question can
give you multiple solutions to try as well as an understanding of why
one solution might be better than another. Additionally, if you can’t
find a question, you can even ask it yourself and receive answers.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
To search for a question on Stack Overflow, type your question and
programming language into the search bar and find the question threads
that seem relevant.
</p>

**Instructions**

<b class="checkpointNumber__P9kFWzdu5a6M0jcG_LgjT">1.</b>

<p class="p__1qg33Igem5pAgn4kPMirjw">
In the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/capstone-1-documentation/mocks.jpg">mock</a>,
you can see that the buttons have rounded edges. Use
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="http://stackoverflow.com/">Stack
Overflow</a> to search how to make buttons round using CSS. Once you’ve
found the property, set its value in the
<code class="code__2rdF32qjRVp7mMVBHuPwDS">li</code> rule to
<code class="code__2rdF32qjRVp7mMVBHuPwDS">5px</code>.
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

## DOCUMENTATION AND RESEARCH

### Review

<p class="p__1qg33Igem5pAgn4kPMirjw">
Awesome! With just a few simple searches and some research you completed
the header for your portfolio site. Reading documentation and searching
Google and Stack Overflow make it easy to solve development problems,
even if you haven’t previously encountered the right tool for the job.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In summary:
</p>
<ol class="ol__1XI8Ausmo9cwwog3NvDzWF">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Documentation is an easy way to view all of the information about a
language or framework. The
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://developer.mozilla.org/en-US/"><em>Mozilla
Development Network</em></a> is the source of documentation for HTML,
CSS, and JavaScript.
</p>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<p class="p__1qg33Igem5pAgn4kPMirjw">
Investigating a new language feature is as easy as typing the problem
and the language into
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://google.com/">Google</a>
or
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://stackoverflow.com/">Stack
Overflow</a>.
</p>
</li>
</ol>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Now that you know how to find any feature and read its documentation,
the sky’s the limit on what you can do. Feel free to browse MDN and
Stack Overflow to find new features and try incorporating them into your
header to make it look even better. Great job!
</p>

**Instructions**

<p class="p__1qg33Igem5pAgn4kPMirjw">
Use MDN, Google, and Stack Overflow to explore new HTML and CSS
features, experimenting with this header to see how they work.
</p>

**Solutions**

``` html
```

## Off-Platform Project: Fotomatic

<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project you will fix a broken version of a responsive website
called Fotomatic. You will be provided specs to help guide you in making
adjustments to the broken code. Download the broken code
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/capstone-1/capstone_fotomatic_start.zip">here</a>
and the specs
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/capstone-1/specs/fotomatic_spec_landing_v2.png">here</a>.
You can also see a working version of the final product
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/courses/freelance-1/capstone-1/solution/index.html">here</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
As you fix Fotomatic’s bugs, remember to use the skills you acquired in
the Chrome DevTools article to help you decipher and update the site’s
CSS. Chrome DevTools are essential for debugging – they allow you to
view current style values, toggle rules, and test different rule values.
</p>

## Fotomatic Project Solution

<p class="p__1qg33Igem5pAgn4kPMirjw">
You can download the solution code to the Fotomatic project
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/PRO/skill-paths/learn-how-to-build-websites/F1C1_solution_2019.zip">here</a>.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Try not to peek at the solution code until you’ve completed this part of
the project, or unless you’re really stuck and your struggle has become
totally unproductive. Looking at the code before that moment will
deprive you of an important learning opportunity and will make it harder
for you to achieve your ultimate outcome.
</p>

## WEB DEVELOPMENT FOUNDATIONS

### Challenge Project: Company Home Page with Flexbox

<h4 id="heading-overview" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Overview
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
​This project is slightly different than others you have encountered thus
far on Codecademy. Instead of a step-by-step tutorial, this project
contains a series of open-ended requirements which describe the project
you’ll be building. There are many possible ways to correctly fulfill
all of these requirements, and you should expect to use the Internet,
Codecademy, and other resources when you encounter a problem that you
cannot easily solve. ​
</p>
<h4 id="heading-project-goals" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Project Goals
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you’ll be using flexbox to design and build the layout
for a company’s homepage. You can choose to build a new homepage for an
existing company or imagine your own dream company! ​
</p>
<h4 id="heading-setup-instructions" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Setup Instructions
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you choose to do this project on your computer instead of Codecademy,
you can download what you’ll need by clicking the “Download” button
below. If you need help setting up your computer, read our article about
setting up a text editor for HTML/CSS development.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>
<h2 class="fit-full fcn-task-header">
Prerequisites
</h2>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
To complete this project, you should have completed Codecademy’s Flexbox
curriculum in any of the following:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/paths/full-stack-engineer-career-path">Full-Stack
Engineering Career Path</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/paths/front-end-engineer-career-path">Front-End
Engineering Career Path</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/paths/learn-how-to-build-websites">Learn
How to Build Websites Skill Path</a>
</li>
</ul>

</article>

<h2 class="fit-full fcn-task-header">
Project Requirements
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
You’re going to build a company homepage for a real or imagined company.
You’ll get to decide exactly what content to include for this company,
but you should at least include:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A title and logo or splash image.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A mission statement or brief description of the company.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A list or set of images and titles representing the product or products
of the company.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A section describing some of the company’s employees or teammates.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you want, you can tour our
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/PRO/independent-practice-projects/flexbox-business-site/example-site/index.html">example
site</a> for inspiration or to see how we used flexbox. Your site will
probably look very different from ours, and that’s great!
</p>

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
Your project should use flexbox styling for layout. Aim to use flexbox’s
advantages, such as easy horizontal and vertical positioning, flexible
element flows as the page size changes, and great styling for repeated
elements.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In our example project, we used flexbox to:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Create a centered navbar at the top of the page.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Create a flexible display of company products that changes from a more
grid-like list to a column list as the page shrinks.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Create a flexible display of company employees.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Our example site is not an elaborate use of flexbox–we’re sure you can
come up with other uses of flexbox in your layout, such as taking
advantage of <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-grow</code>
or <code class="code__2rdF32qjRVp7mMVBHuPwDS">flex-shrink</code>.
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
Your page should also use custom styles for other properties, such as
colors, fonts, and other layout properties such as borders and padding.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Our example site uses:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
A simple color scheme using CSS named colors, but yours can be more
elaborate with hexadecimal, RGB, or HSL colors.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Fonts from the
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://fonts.google.com/">Google
Fonts API</a>.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Custom images. A great source for project images when you’re practicing
web design is
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://unsplash.com/">Unsplash</a>.
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Get creative! Customizing your site’s look and feel is one of the most
exciting parts of building your own websites. You can review any of
these other CSS properties in our
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/learn-css">Learn
CSS</a> course.
</p>

</article>

<h2 class="fit-full fcn-task-header">
Project Solution
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
Great work! Visit
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/t/company-home-page-challenge-project-css-flexbox/462383">our
forums</a> to compare your project to our sample solution code. You can
also learn how to host your own solution on GitHub so you can share it
with other learners!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember, this is just one possible solution. Your own project may be
coded totally differently, have more or less content, and look totally
different! We’re providing our solution for you get a sense of one way
to flexbox to help with page layout. There are multiple ways to solve
these projects, and you’ll learn more by seeing others’ code.
</p>

</article>

**Solutions**

``` html
```

## WEB DEVELOPMENT FOUNDATIONS

### Challenge Project: Responsive Club Website

<h4 id="heading-overview" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Overview
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
​This project is slightly different than others you have encountered thus
far on Codecademy. Instead of a step-by-step tutorial, this project
contains a series of open-ended requirements which describe the project
you’ll be building. There are many possible ways to correctly fulfill
all of these requirements, and you should expect to use the Internet,
Codecademy, and other resources when you encounter a problem that you
cannot easily solve. ​
</p>
<h4 id="heading-project-goals" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Project Goals
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
In this project, you’ll be building your own club group page that will
dynamically respond as you adjust the size of your screen! ​
</p>
<h4 id="heading-setup-instructions" class="h4__1cJx3E4QhkKjfWj3jLsTFU">
Setup Instructions
</h4>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you choose to do this project on your computer instead of Codecademy,
you can download what you’ll need by clicking the “Download” button
below. If you need help setting up your computer, read our article about
setting up a text editor for HTML/CSS development.
</p>

**Instructions**

<span class="tasksHelp__2gwNuLZ9kdz9gCp9vw39no">Mark the tasks as
complete by checking them off</span>
<h2 class="fit-full fcn-task-header">
Prerequisites
</h2>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-1">1.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
To complete this project, you should have completed the Codecademy
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/learn-responsive-design">Responsive
Design course</a>, or the same lessons in the
<a target="_blank" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.codecademy.com/learn/paths/learn-how-to-build-websites">Learn
How to Build Websites Path</a>.
</p>

</article>

<h2 class="fit-full fcn-task-header">
Project Requirements
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
In this project, you’ll build a webpage for a local club. You can base
it on real-life organization you belong to or make one up! You’ll get to
choose everything about your page: the club name, the page layout and
styling, any images that you want to use, and more! You can check out
our
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://content.codecademy.com/PRO/independent-practice-projects/responsive-club-site/example-site/index.html">example
site</a> for some inspiration and experiment with what elements are
responsive. We’ll provide the full code for this site in the solution
section at the end of this project.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
A helpful resource for finding beautiful images for your sites is
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://unsplash.com/">Unsplash</a>.
</p>

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
Your project should demonstrate many of the responsive design tools you
learned. In our example project, we use percentages and relative units,
such as <code class="code__2rdF32qjRVp7mMVBHuPwDS">em</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rem</code>, in our CSS to
size and position page elements. We also made our website responsive by
incorporating media queries to resize elements based on the size of the
screen.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Possible responsive design concepts to demonstrate: ​
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Making images toggle to certain percentages in terms of
<code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code> after a certain
minimum screen size.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Using a <code class="code__2rdF32qjRVp7mMVBHuPwDS">@media</code> rule to
change page layout and behavior based on size breakpoints.
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Employing responsive units
<code class="code__2rdF32qjRVp7mMVBHuPwDS">em</code> and
<code class="code__2rdF32qjRVp7mMVBHuPwDS">rem</code> to size and space
elements with <code class="code__2rdF32qjRVp7mMVBHuPwDS">width</code>
and <code class="code__2rdF32qjRVp7mMVBHuPwDS">padding</code>.
</li>
</ul>

</article>

<h2 class="fit-full fcn-task-header">
Project Solution
</h2>

<article class="fit-full fcn-task fcn-task--complete">

<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" class="gamut-sd6ku5-Svg eol2zvm0">
<title>
Check Icon
</title>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.552 3.93a1.5 1.5 0 01.017 2.122l-13.778 14a1.5 1.5 0 01-2.056.077L.513 13.813a1.5 1.5 0 011.974-2.258l6.158 5.385L21.431 3.948a1.5 1.5 0 012.121-.017z" fill="currentColor"></path>
</svg>

<span class="fcn-task__number" data-testid="task-4">4.</span>

<p class="p__1qg33Igem5pAgn4kPMirjw">
Great work! Visit
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://discuss.codecademy.com/t/responsive-club-website-css/462382">our
forums</a> to compare your project to our sample solution code. You can
also learn how to host your own solution on GitHub so you can share it
with other learners!
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Remember, this is just one possible solution. Your own project may be
coded totally differently, have more or less content, and look totally
different! We’re providing our solution for you get a sense of one way
to use responsive units and media queries to affect page layout. There
are multiple ways to solve these projects, and you’ll learn more by
seeing others’ code.-
</p>

</article>

**Solutions**

``` html
```

## Review: Making a Website Responsive

<p class="p__1qg33Igem5pAgn4kPMirjw">
Congratulations! The goal of this unit was to establish a foundation in
responsive web design and give you the tools to create websites that use
different layouts which work on a variety of devices.
</p>
<p class="p__1qg33Igem5pAgn4kPMirjw">
Having completed this unit, you are now able to:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Understand responsive web design
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Use CSS Grid and Flexbox for layout, positioning, and responsiveness
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Use media queries
</li>
</ul>
<p class="p__1qg33Igem5pAgn4kPMirjw">
If you are interested in learning more about these topics, here are some
additional resources:
</p>
<ul class="ul__11icM1EC_0uPj3OY0Skp4r">
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Resource:
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://codepip.com/games/grid-garden/">Grid
Garden</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Article:
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.smashingmagazine.com/2011/01/guidelines-for-responsive-web-design/">Responsive
Web Design</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Article:
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://www.taniarascia.com/you-dont-need-a-framework/">You
Don’t Need a Framework: Understanding the Fundamentals of Responsive
Design</a>
</li>
<li class="li__1KqBjwbWA3ze6V0BvXq9Rx">
Article:
<a target="_blank" rel="noopener" class="e14vpv2g1 gamut-xro1w8-ResetElement-Anchor-AnchorBase e1bhhzie0" href="https://css-tricks.com/snippets/css/complete-guide-grid/">A
Complete Guide to CSS Grid</a>
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
