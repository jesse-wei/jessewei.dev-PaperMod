---
title: "Overview of Hugo/PaperMod and Setting Up This Site"
date: 2023-05-14T20:13:59-04:00
draft: false
cover:
    image: img/hugo_logo_wide.svg
    alt: "Hugo logo"
    caption: "Hugo logo"
    hidden: false
summary: "This post provides an overview of Hugo (PaperMod theme) and details the steps I took in setting up this website."
tags: ["Hugo", "PaperMod", "Markdown", "HTML", "CSS", "Blog", "Website", "Portfolio"]
---

## Introduction

This post was written with two audiences in mind: people who are new to Hugo and people with Hugo experience. If you're new to Hugo, then I recommend reading this post from start to finish. If you have experience with Hugo, then I recommend skimming. Specifically, I would read [Clone/fork](#clonefork) for setup instructions and then skip over the [Hugo/PaperMod overview](#overview-of-hugo-and-papermod) to get to [My website](#my-website), which describes specific features of my website. Please see the Table of Contents above if you haven't already.

To make this website, I used the static site generator [Hugo](https://gohugo.io/) with the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme. I use [Netlify](https://www.netlify.com) to host.

In this post, I provide an overview of Hugo/PaperMod and describe the modifications I made to the original theme in setting up this website.

## Credit

This post is inspired by Konstantin's similarly-titled [blog post](https://kpwn.de/2021/09/how-to-set-up-this-blog/).

## Resources

Before proceeding, I'd like to share five excellent resources that I used and reference throughout this post. The top three are crucial because they cover Hugo and PaperMod. The bottom two describe very specific features that I reference in [My website](#my-website).

My goal is to make the rest of this post self-contained, but if something doesn't make sense, please use the first three resources.

* [^1] [Hugo Quick Start](https://gohugo.io/getting-started/quick-start)
  * Super quick to read and follow along, < 5 min.
* [^2] [Getting Started With Hugo](https://www.youtube.com/watch?v=hjD9jTi_DQ4) (47:41)
* [^3] [PaperMod demo site/documentation](https://adityatelange.github.io/hugo-PaperMod/) and its [source](https://github.com/adityatelange/hugo-PaperMod/tree/exampleSite)
* [^4] [Konstantin's How to Set Up This Blog](https://kpwn.de/2021/09/how-to-set-up-this-blog/)
* [^5] [Check links in Hugo with htmltest](https://robb.sh/posts/check-links-in-hugo-with-htmltest/)

[^1]: [Hugo Quick Start](https://gohugo.io/getting-started/quick-start)

[^2]: [Getting Started With Hugo](https://www.youtube.com/watch?v=hjD9jTi_DQ4)

[^3]: [PaperMod demo site/documentation](https://adityatelange.github.io/hugo-PaperMod/) and its [source](https://github.com/adityatelange/hugo-PaperMod/tree/exampleSite)

[^4]: [Konstantin's How to Set Up This Blog](https://github.com/KwnyPwny/hugo-blog/tree/main/layouts/shortcodes)

[^5]: [Check links in Hugo with htmltest](https://robb.sh/posts/check-links-in-hugo-with-htmltest/)

## Setup

First, follow the steps [here](https://gohugo.io/installation/) to install Hugo. You should also have Git installed. [^6]

[^6]: I assume you already do, surely.

### Clone/fork

Run these commands.

```sh
git clone --recurse-submodules --no-single-branch https://github.com/jesse-wei/jessewei.dev.git
cd jessewei.dev
hugo server
```

`--recurse-submodule` clones the PaperMod [submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

Additionally, you may clone with `--depth=1` to save some disk space.

`hugo server` starts up a server for you to view the site.

### Why clone/fork?

At this point, you could start from scratch instead of cloning/forking my website. However, resources [^1] and [^2] already describe how to start from scratch.

So, I'll cut to the chase and have you clone my website and describe changes I made.

If something doesn't make sense, then I recommend first reading/watching the [resources](#resources).

In addition, if you notice some specific feature of my website that I don't explain, then use inspect element to inspect the code for that feature. Then run `grep -ir` in this repo to find the relevant code. `-r` makes the search recursive, and `-i` makes the search case-insensitive.

## Overview of Hugo and PaperMod

Skip or skim this section if you're already familiar with Hugo and PaperMod (e.g., if you read/watched the [resources](#resources)). I describe specific features of my website in [My website](#my-website).

### Repo structure

Here's the structure of the repository. I omit unimportant stuff, and certainly changes will be made, but this is all the important stuff:

```text
jessewei.dev
├── assets              Overrides PaperMod/assets
│   └── css
├── config.yml          Site-wide configuration file
├── content
│   ├── about.md
│   ├── act
│   ├── archives.md
│   ├── classes
│   ├── discord.md
│   ├── posts
│   ├── privacy.md
│   ├── projects
│   ├── search.md
│   └── teaching
├── layouts             Overrides PaperMod/layouts
│   ├── _default
│   │   └── single.html
│   └── partials
│       ├── comments.html
│       ├── extend_head.html
│       ├── footer.html
│       ├── header.html
│       ├── index_profile.html
│       └── social_icons.html
├── static              Images, etc.
│   ├── SAPsim_still_cropped.jpg
│   ├── SAPsim_still_full.jpg
│   └── ...
└── themes
    └── PaperMod
```

There are 4 crucial parts of the repo.

### `config.yml`

This is the configuration file for the website containing all site-wide parameters.

### `content/`

This is the directory where site content (posts) goes.

Site content should be Markdown files.

The front matter of a Markdown file contains metadata about the post. For example, the front matter of this post is (TODO: update)

```md
---
title: "How to Set Up This Website"
date: 2023-05-14T20:13:59-04:00
draft: true
cover:
    image: img/hugo_logo_wide.svg
    alt: "Hugo logo"
    caption: "Hugo logo"
summary: "This post details the steps I took and decisions I made in making my website using Hugo with the PaperMod theme."
tags: []
---
```

This information is used to generate the post's page. It's quite intuitive what these fields do (check by seeing how something in front matter renders on the page), so I won't go into detail.

For a list of variables you can use, see [Variables | Front Matter](https://adityatelange.github.io/hugo-PaperMod/posts/papermod/papermod-variables/#page-variables) from PaperMod documentation.

### `layouts/` and `assets/`

The files in these directories override the files in `themes/PaperMod/layouts/` and `themes/PaperMod/assets/`, respectively. If the path of a file in `layouts/` exactly matches that of a file in `themes/PaperMod/layouts/`, then your site will use the file in `layouts/` instead of the one in `themes/PaperMod/layouts/`. Same for `assets/`.

Essentially, `themes/PaperMod/layouts/` and `themes/PaperMod/assets/` specify defaults. If you want to make a change, override the default. However, don't modify the `PaperMod` submodule directly because that might cause merge conflicts if you pull updates.

`layouts/` contains HTML files that specify the structure of pages.

Let's look at `PaperMod/layouts/_default/`.

```text
themes/PaperMod/layouts/_default
├── _markup
├── archives.html
├── baseof.html
├── index.json
├── list.html
├── rss.xml
├── search.html
├── single.html
└── terms.html
```

#### baseof

In particular, here's `baseof.html`.

```go-html-template {lineNos=true}
<!DOCTYPE html>
<html lang="{{ site.Language }}" dir="{{ .Language.LanguageDirection | default "auto" }}">

<head>
    {{- partial "head.html" . }}
</head>

<body class="
{{- if (or (ne .Kind `page` ) (eq .Layout `archives`) (eq .Layout `search`)) -}}
{{- print "list" -}}
{{- end -}}
{{- if eq site.Params.defaultTheme `dark` -}}
{{- print " dark" }}
{{- end -}}
" id="top">
    {{- partialCached "header.html" . .Page -}}
    <main class="main">
        {{- block "main" . }}{{ end }}
    </main>
    {{ partialCached "footer.html" . .Layout .Kind (.Param "hideFooter") (.Param "ShowCodeCopyButtons") -}}
</body>
```

This is the base template for all pages. Notice it has all parts of an HTML document: `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`.

It's mostly HTML. However, note the code in braces `{{ ... }}` or `{{- ... -}}`. This is [Go template](https://golang.org/pkg/text/template/) code. It's a templating language that Hugo uses to generate HTML.

Note on line 2 that a [site variable](https://gohugo.io/variables/site/) `site.Language` is directly inserted into an HTML attribute. Some site variables are in `config.yml`, and others are built-in to Hugo.

Note on line 5 that a partial `head.html` is inserted. A partial is an HTML snippet that can be inserted into a page. As we can see here, the partial `head.html` (which can be found under `layouts/partials/head.html`) is the `<head>` code of all pages.

Does this mean all pages have the same `<head>` code?

Nope, notice one last thing on line 9: conditionals! By checking the values of some variables, we can conditionally insert HTML code. Lines 9-14 just insert some classes, but it's also possible to insert entire HTML snippets or partials. So although all pages have the same template for `<head>`, the actual `<head>` code depends on parameters.

On lines 16 and 20, we see partials defining the header and footer of a page. In the middle is `<main>` for the content of a page.

#### single

This page (and most pages) is a single (`layouts/_default/single.html`).

A portion of `single.html` is below.

```go-html-template
{{- define "main" }}

<article class="post-single">
  <header class="post-header">
    {{ partial "breadcrumbs.html" . }}
    <h1 class="post-title">
      {{ .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h1>
    {{- if .Description }}
    <div class="post-description">
      {{ .Description }}
    </div>
    {{- end }}
    {{- if not (.Param "hideMeta") }}
    <div class="post-meta">
      {{- partial "post_meta.html" . -}}
      {{- partial "translation_list.html" . -}}
      {{- partial "edit_post.html" . -}}
      {{- partial "post_canonical.html" . -}}
<!-- Rest of code omitted -->
```

Notice this code goes in the `"main"` block from line 17 of `baseof.html`. The code is quite intuitive, so you should be able to see how this code (in addition to front matter and site variables) causes certain elements to appear at the top of this page.

#### Changing layout

You should rarely have to modify the `layout` of a page. Most pages are singles. You can see an example of a list layout at my [projects](/projects/) page. However, I did not specify this layout manually: It's automatically a list layout because `projects/` has directories but no `index.md` file.

```text
content/projects
├── 566
├── leds
├── mips_emulator
├── neuroruler
├── rubiks_541
└── sapsim
```

I have two pages where I manually set the layout. One is [Search](/search), and the other is [Archives](/archives).

Here's the front matter of `search.md`.

```md
---
title: "Search"
layout: "search"
summary: "search"
---
```

And similar for `archives.md`.

### `static/`

The fourth and final important part is `static/`. This is where static files, such as images, go.

I don't have very many images here because I prefer to group images with the post itself in `content/`.

Note that after compilation, files in `static/` are copied to the root directory `/`. So, when accessing a file in `static/`, you should prepend a `/` to the file path. For example, the image `static/1.jpg` should be accessed as `/1.jpg`. In practice, I've found that the leading `/` can often be omitted. Just know that something like `/static/1.jpg` won't work.

### Shortcodes

I want to briefly mention [shortcodes](https://gohugo.io/content-management/shortcodes/). Quite a few of them are [built in to Hugo](https://gohugo.io/content-management/shortcodes/#use-hugos-built-in-shortcodes) and PaperMod, and they're very convenient.

I'll show a few examples. Note that when I show the code, I put a space between `{` and `<` so that the shortcode is parsed as text and not executed. To use it, remove that space.

#### Raw HTML

```go-html-template
{{ < rawhtml >}}
<p align="center" style="color: red;"><strong>This is raw HTML</strong></p>
{{ < /rawhtml >}}
```

{{< rawhtml >}}
<p align="center" style="color: red;"><strong>This is raw HTML</strong></p>
{{< /rawhtml >}}

#### Figure

See the [htmltest](#htmltest) section for an example of a figure. Here's the code that generates it:

```go-html-template
{{ < figure src="img/htmltest.jpg" caption="htmltest GH action output" alt="htmltest GH action output" align="center">}}
```

#### YouTube embed

```go-html-template
{{ < youtube hjD9jTi_DQ4 >}}
```

{{< youtube hjD9jTi_DQ4 >}}

#### GitHub gist

```go-html-template
{{ < gist jesse-wei 0b2472f020b41b8767882291c536102c >}}
```

{{< gist jesse-wei 0b2472f020b41b8767882291c536102c >}}

### Deploy

Resource 2 describes how to deploy to Netlify. Here's a [timestamp](https://youtu.be/hjD9jTi_DQ4?t=2230) for that portion of the video.

## My website

Now I'll describe features of my website.

### config.yml

The latest version of my `config.yml` is [here](https://github.com/jesse-wei/jessewei.dev/blob/main/config.yml).

I think I use reasonable values, and I use comments to explain decisions I consider non-obvious. I'll explain some specific decisions I made in this file in the below sections as they come up.

### Content

There are a few single pages in `content/`.

For a list layout (e.g., my [Teaching](/teaching) page), see the structure of `content/teaching/`.

```text
content/teaching
├── act.md
├── comp110
│   ├── img
│   └── index.md
├── comp210
│   ├── img
│   └── index.md
└── comp311
    ├── img
    ├── index.md
    └── review
```

My Teaching page has a list layout because `teaching/` doesn't have an `index.md`. Besides the single `act.md`, the rest of the content is in directories with an `index.md` file and images in `img/` (I prefer this to putting images in `static/`). The comp110 writeup is accessible via [jessewei.dev/teaching/comp110](https://jessewei.dev/teaching/comp110).

### $\LaTeX{}$

I enabled $\LaTeX{}$ via [KaTeX](https://katex.org/) in `layouts/partials/extend_head.html`.

The conditional there requires the site param `math` to be enabled. If so, then setting the param `math` in front matter to `false` will disable KaTeX for that page.

### Comments

I enabled comments using [giscus](https://giscus.app).

There are comments at the bottom of almost every page.

I followed the directions on the giscus site to install giscus in my repo and pasted code from the giscus website into `layouts/partials/comments.html`. I also added `comments: true` to config.

In addition, comments show up in [GitHub Discussions](https://github.com/jesse-wei/jessewei.dev/discussions). Make sure to [enable Discussions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/enabling-or-disabling-github-discussions-for-a-repository#) in your GitHub repo.

### Social icons in footer

I added social icons to the footer, as in resource [^4]. I sort of follow what it describes but make some of my own adjustments.

As described there, adding social icons to footer messes with CSS spacing values. For example, a scrollbar appeared on the homepage and Search page (haven't solved this and don't plan to) even though there's enough room for both header and footer to be visible without scrolling. This issue is described more in-depth in resource [^4], under problem 2.

In short, I modified CSS in 4 files. `layouts/partials/footer.html`, `layouts/partials/social_icons.html`, `assets/css/core/theme-vars.css`, and `assets/css/common/profile-mode.css`. The comments in each file describe the changes I made. Most comments in `social_icons.html` are for htmltest, described [below](#htmltest), so ignore those for now.

I disabled footer social icons on the homepage because the homepage already has social icons.

### Other footer changes

Beyond that, I made some other minor changes to the footer.

I added the separator character • between phrases in the footer.

The links were originally like this:

```html
Powered by
<a href="https://gohugo.io/" rel="noopener noreferrer" target="_blank">Hugo</a> &
<a href="https://github.com/adityatelange/hugo-PaperMod/" rel="noopener" target="_blank">PaperMod</a>
```

I removed `target=_blank` and `rel="noopener noreferrer"` because [links should not usually open new tabs](https://www.w3.org/TR/WCAG20-TECHS/G200.html).

I added a privacy policy page and a link to it in the footer.

Lastly, I removed "Powered by Hugo and PaperMod" in the homepage specifically.

### Single

I slightly modified `layouts/_default/single.html`. I moved the ToC above the cover. Notice on this page that the ToC is above the cover image.

<!-- TODO, once I fix bug ### Shortcodes

I copied over the excursion shortcode from [here](https://github.com/KwnyPwny/hugo-blog/tree/main/layouts/shortcodes).

Here's an example:

{{< excursion anchor="excursion" title="Excursion example" >}}

Hello world

```
code block
```

Notice the code block doesn't work, and spacing is messed up :(

{{< /excursion >}} -->

### Syntax highlighting via Chroma

I disabled [highlight.js](https://highlightjs.org) (default) and enabled Hugo Chroma following the [steps in PaperMod documentation](https://adityatelange.github.io/hugo-PaperMod/posts/papermod/papermod-faq/#using-hugos-syntax-highlighter-chroma). This required a few changes in `config.yml` and `assets/css/extended/*.css`.

I want to point out that I disabled line numbers by default for readability. Most code blocks you've seen so far have not had line numbers.

However, you can enable line numbers for a specific code block, as shown in [baseof](#baseof), by adding `{lineNos=true}` to the code block. [^7]

[^7]: You might also be able to enable it by default in a specific post by adding it to front matter, but this didn't work for me.

```html {lineNos=true}
<!DOCTYPE html>
<!-- Omitted -->
```

### Google Analytics

For Google Analytics, just add your Google Analytics tag to `googleAnalytics` in the config. For example, mine has `googleAnalytics: G-Q603T56FWT`.

PaperMod automatically uses the Google Analytics script if `env` is `production` (default). See the bottom of `layouts/partials/head.html`:

```go-html-template
{{- /* Misc */}}
{{- if hugo.IsProduction | or (eq site.Params.env "production") }}
{{- template "_internal/google_analytics.html" . }}
{{- template "partials/templates/opengraph.html" . }}
{{- template "partials/templates/twitter_cards.html" . }}
{{- template "partials/templates/schema_json.html" . }}
{{- end -}}
```

### GitHub workflows

#### htmltest

I added a GH workflow for automatically checking links in my site.

{{< figure src="img/htmltest.jpg" caption="htmltest GH action output" alt="htmltest GH action output" align="center">}}

To enable, see `.github/workflows/htmltest.yml` and its configuration file `.github/.htmltest.yml`. This follows resource [^5].

There was originally >100 lines of garbage output. htmltest complained that the site logo's link at the top left had no alt text, and my LinkedIn link in social icons in the footer returned non-OK exit status 999. Since the header and footer are in all pages, this caused a lot of errors, which made the output unreadable.

I fixed this in `layouts/partials/header.html` by adding non-empty alt text to the logo and in `layouts/partials/social_icons.html` by excluding the LinkedIn link from htmltest using the `data-proofer-ignore` attribute, as specified in [htmltest's README](https://github.com/wjdp/htmltest#see_no_evil-ignoring-content).

The top 3 links are ones I want to keep even though they don't actually work. So I manually ignored them in the post (not `layouts/`) using the `data-proofer-ignore` attribute in rawhtml. [^8]

[^8]: TODO: Create shortcode for a link with `data-proofer-ignore` attribute.

And the `#center` thing is how you can [center an image in Markdown syntax in PaperMod](https://adityatelange.github.io/hugo-PaperMod/posts/papermod/papermod-faq/#centering-image-in-markdown). `#center` also gets appended to an image URL if you use `align="center"` in figure shortcode. But since this causes htmltest to freak out, I added this to `.htmltest.yml`:

```yml
IgnoreURLs:
  # Ignore <img src="*#center"> for centered images in PaperMod, which would cause "hash not found"
  # This is suboptimal because we ideally want to check the image URL without the #center suffix

  # Match internal image path ending in #center
  - .*\.(apng|gif|ico|cur|jpg|jpeg|jfif|pjpeg|pjp|png|svg)#center$
  # Match external image URL ending in #center
  - (https://|http://|www\.).*\.[A-Za-z]+#center$
```

As you can tell by the comments, this is suboptimal and can lead to false negatives. I can think of two solutions.

1. Modify htmltest to ignore specific hashes but check the rest of the URL [^9]
2. Modify PaperMod to center the image without appending `#center`

[^9]: This would ignore any URL with `#center` suffix, not just image URLs.

Lastly, instead of `continue-on-error: true` from resource [^5], I use `if: always()`.

```yml
- name: Test HTML
  # MODIFICATION: Don't use continue-on-error (see below)
  # https://github.com/wjdp/htmltest-action/
  uses: wjdp/htmltest-action@master
  with:
    # For consistency, use the same config file as for local builds
    config: ./.github/.htmltest.yml
- name: Archive htmltest results
  # MODIFICATION
  # Archive result even if Test HTML fails
  # Use if: always() instead of continue-on-error, as in the original file
  # Source: https://stackoverflow.com/questions/62045967/github-actions-is-there-a-way-to-continue-on-error-while-still-getting-correct
  if: always()
```

`if: always()` will cause logging to occur even if Test HTML fails. `continue-on-error: true` would do the same. However, `continue-on-error: true` would cause GH Actions to display a green checkmark when Test HTML fails, which is misleading.
