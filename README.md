[![Netlify Status](https://api.netlify.com/api/v1/badges/9d745180-286f-4084-bd0e-046e2c5d22ef/deploy-status)](https://app.netlify.com/sites/cheerful-mousse-b9d87b/deploys)
[![htmltest](https://github.com/jesse-wei/jessewei.dev/actions/workflows/htmltest.yml/badge.svg)](https://github.com/jesse-wei/jessewei.dev/actions/workflows/htmltest.yml)

# [jessewei.dev](https://jessewei.dev)

Made using [Hugo](https://gohugo.io) with the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

My [old website](https://github.com/jesse-wei/jessewei.dev_old) was raw HTML/CSS 💀. This is a nice change of pace.

## Deploy locally

First, [install Hugo](https://gohugo.io/installation/).

Then, run the following commands:

```bash
git clone --recurse-submodules --no-single-branch https://github.com/jesse-wei/jessewei.dev.git
cd jessewei.dev
hugo server
```

`--recurse-submodules` will clone the PaperMod [submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules). In addition, you can clone with `--depth=1` to save disk space.

## How I set up this site

See [Overview of Hugo/PaperMod and Setting Up This Site](https://jessewei.dev/posts/setup_site/).
