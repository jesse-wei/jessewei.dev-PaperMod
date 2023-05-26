[![Netlify Status](https://api.netlify.com/api/v1/badges/9d745180-286f-4084-bd0e-046e2c5d22ef/deploy-status)](https://app.netlify.com/sites/cheerful-mousse-b9d87b/deploys)
[![CI](https://github.com/jesse-wei/jessewei.dev-PaperMod/actions/workflows/ci.yml/badge.svg)](https://github.com/jesse-wei/jessewei.dev-PaperMod/actions/workflows/ci.yml)

# THIS REPO IS DEPRECATED

See my [blog post](https://jessewei.dev/blog/2023/papermod/) about why I switched to [al-folio](https://github.com/alshedivat/al-folio).

The source for my website's code is at [https://github.com/jesse-wei/jesse-wei.github.io](https://github.com/jesse-wei/jesse-wei.github.io). [https://jessewei.dev](https://jessewei.dev) points there.

---

## jessewei.dev-PaperMod

This website should still be deployed at [https://main--cheerful-mousse-b9d87b.netlify.app](https://main--cheerful-mousse-b9d87b.netlify.app).

It was made using [Hugo](https://gohugo.io) with the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme. Deployed on [Netlify](https://www.netlify.com).

## Deploy locally

First, [install Hugo](https://gohugo.io/installation/).

Then, run the following commands:

```bash
git clone --recurse-submodules --no-single-branch https://github.com/jesse-wei/jessewei.dev-PaperMod.git
cd jessewei.dev-PaperMod
hugo server
```

[scripts/build](scripts/build) is used for Netlify deployment.

## How I set up this site

See my [blog post](https://jessewei.dev/blog/2023/papermod/).

## PaperMod diff

My auto-generated [PaperMod diff](https://main--cheerful-mousse-b9d87b.netlify.app/posts/papermod_diff) page shows the changes I made to the PaperMod theme using `diff` output.

I describe how I set up the page in the link above.
