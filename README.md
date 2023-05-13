[![Netlify Status](https://api.netlify.com/api/v1/badges/9d745180-286f-4084-bd0e-046e2c5d22ef/deploy-status)](https://app.netlify.com/sites/cheerful-mousse-b9d87b/deploys)

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

## Non-content files I changed

* [config.yml](https://github.com/jesse-wei/jessewei.dev/blob/main/config.yml)
  * Note: I created the directory with the command `hugo new site jessewei.dev -f yml` to use a YAML configuration file.
* [layouts/partials](https://github.com/jesse-wei/jessewei.dev/blob/main/layouts/partials)
  * Comments indicate changes made.
* [assets/css/extended/*.css](https://github.com/jesse-wei/jessewei.dev/tree/main/assets/css/extended)
  * For code syntax highlighting via [Hugo Chroma](https://gohugo.io/content-management/syntax-highlighting/) instead of [highlight.js](https://highlightjs.org) (default).
* [.github/workflows/](https://github.com/jesse-wei/jessewei.dev/blob/main/.github/workflows/)

## Resources

* [Hugo Quick Start](https://gohugo.io/getting-started/quick-start)
* [Getting Started With Hugo](https://www.youtube.com/watch?v=hjD9jTi_DQ4) (47:41)
* [How to set up this blog](https://kpwn.de/2021/09/how-to-set-up-this-blog/)
