# [jessewei.dev](https://jessewei.dev)

Made using [Hugo](https://gohugo.io) with the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

My [old website](https://github.com/jesse-wei/jessewei.dev_old) was raw HTML/CSS 💀. This is a nice change of pace.

## Deploy locally

First, follow the steps in [Hugo Quick Start](https://gohugo.io/getting-started/quick-start/#prerequisites) to install Hugo.

Then, run the following commands:

```bash
git clone https://github.com/jesse-wei/jessewei.dev.git --depth=1
cd jessewei.dev
hugo server
```

## Resources

* [Hugo Quick Start](https://gohugo.io/getting-started/quick-start)
* [Getting Started With Hugo](https://www.youtube.com/watch?v=hjD9jTi_DQ4) (47:41)

## Non-content files I changed

* [config.yml](https://github.com/jesse-wei/jessewei.dev/blob/main/config.yml)
  * Note: I created the directory with the command `hugo new site jessewei.dev -f yml` to use a YAML configuration file.
* [layouts/partials/extend_head.html](https://github.com/jesse-wei/jessewei.dev/blob/main/layouts/partials/extend_head.html)
  * For $\LaTeX{}$ support via [KaTeX](https://katex.org)
* [assets/css/extended/*.css](https://github.com/jesse-wei/jessewei.dev/tree/main/assets/css/extended)
  * For code syntax highlighting via [Hugo Chroma](https://gohugo.io/content-management/syntax-highlighting/) instead of [highlight.js](https://highlightjs.org) (default)
* [.github/workflows/deploy.yml](https://github.com/jesse-wei/jessewei.dev/blob/main/.github/workflows/deploy.yml)
  * For automatic deployment to GitHub Pages, although my site is actually deployed on Netlify following the steps in the Getting Started With Hugo video above.
