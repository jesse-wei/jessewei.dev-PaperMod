---
title: "Euler's Formula"
date: 2022-05-01T12:00:00-04:00
draft: false
summary: "$e^{ix} = \\cos x + i \\sin x$. $e^{i\\pi} + 1 = 0$."
---

## Proof 1: By [Taylor series](https://en.wikipedia.org/wiki/Taylor_series)

Here are the Maclaurin expansions [^1] for $\\cos(x), \\sin(x),$ and $e^y$.

[^1]: A Maclaurin series is a Taylor series about the point 0. Also, $y$ is a dummy variable for simplicity here.

$$\\begin{aligned} \\cos(x) &= \\sum\_{n=0}^{\\infty} \\frac{(-1)^n}{(2n)!} x^{2n} = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + \\cdots\\\\ \\sin(x) &= \\sum\_{n=0}^{\\infty} \\frac{(-1)^n}{(2n+1)!} x^{2n+1} = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\cdots\\\\ e^y &= \\sum\_{n=0}^{\\infty} \\frac{y^n}{n!} = 1 + y + \\frac{y^2}{2!} + \\frac{y^3}{3!} + \\frac{y^4}{4!} + \\cdots\\\\ \\end{aligned}$$

Letting $y = ix$, we get [^2]

$$\\begin{aligned} e^{ix} = \\sum\_{n=0}^{\\infty} \\frac{(ix)^n}{n!} = \\sum\_{n=0}^{\\infty}i^n\\frac{x^n}{n!} &= 1 + ix - \\frac{x^2}{2!} - i \\frac{x^3}{3!} + \\frac{x^4}{4!} + i \\frac{x^5}{5!} - \\frac{x^6}{6!} + \\cdots\\\\ &= \\left(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + \\cdots\\right) + i\\left(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + \\cdots\\right)\\\\ &= \\cos(x) + i\\sin(x) \\end{aligned}$$

[^2]: It's just the $e^x$ expansion but with the powers of $i$ $(1, i, -1, -i, 1, \\ldots)$ as coefficients. We note that the only terms with $ \\pm i$ will have $n$ odd since $i^1=-i^3=i$, and vice versa for the terms without $i$. Also, we note that any two terms that are 2 apart will have opposite signs since they differ by $i^2=-1$.

### Lemma 1: The [magnitude](https://en.wikipedia.org/wiki/Complex_number#Conjugate) of $e^{ix}$ is $1 \\quad \\forall x \\in \\mathbb{R}$

*Proof*. We have shown that $e^{ix}$ is a complex number $a+bi$, where $a=\\cos x$ and $b=\\sin x$. The magnitude of a complex number is its distance, on the complex plane, from $(0, 0)$. We find this distance using the distance formula. $$|e^{ix}| = |\\cos(x) + i\\sin(x)\\:| = \\sqrt{\\cos^2(x) + \\sin^2(x)} = \\sqrt{1} = 1 \quad \blacksquare$$

The significance of this result is that on the complex plane [^3], $e^{i\\theta}$ represents a point that is a distance of one unit away from the origin $(0, 0)$. Varying $\\theta$ from $0$ to $2 \\pi$ results in the unit circle.

[^3]: On the complex plane, the x axis represents all real numbers $\\mathbb{R}$ and the y axis represents all imaginary numbers $bi$ for $b \\in \\mathbb{R}$.

The $\\theta$ parameter measures the counterclockwise angle the point makes with the positive x axis. At this point, since we're determining a point's position by its angle, we should wonder how this could be connected with polar coordinates.

A polar coordinate requires an extra parameter, $r$. Otherwise, we are stuck with only the unit circle and can't represent points a distance of, for example, 2 units from the origin. We simply add that parameter $r$ by multiplying by $r$.

### Lemma 2 (polar coordinates): For all points $x+iy$ on the complex plane, there exist $r \\in \\mathbb{R}^{\\geq 0}$ and $\\theta \\in \[0, 2\\pi)$ such that $re^{i\\theta} = r(\\cos \\theta + i \\sin \\theta) = r\\cos \\theta + i(r\\sin \\theta) = x+iy$

## Proof 2: By differential equation

Consider the following differential equation: $$\\frac{df(x)}{dx} = if(x)$$

One solution is $f(x) = e^{ix}$ because $$\\frac{d}{dx}e^{ix} = ie^{ix}$$

Another solution is $f(x) = \\cos(x)+i\\sin(x)$ because$$\\frac{d}{dx}\\left(\\cos(x)+i\\sin(x)\\right) = -\\sin(x)+i\\cos(x) = i\\left(\\cos(x)+i\\sin(x)\\right)$$

and both functions satisfy $f(0) = 1$: $$f(0) = e^{i(0)} = \\cos(0) + i\\sin(0) = 1$$

Hence, the functions are identical; that is, $e^{ix} = \\cos(x)+i\\sin(x)$

### Lemma 3 (Euler's identity): $e^{\\pi i} = -1$

$$
\begin{aligned} e^{\\pi i} &= \\cos(\\pi) + i\\sin(\\pi) \\\\ &= -1 + i(0)\\\\ &= -1\\\\ & \blacksquare \end{aligned}
$$

### $\\ln(-1)=i \\pi$

Take the natural log of both sides of Euler's identity: $$ e^{\\pi i} = -1 \\implies \\pi i = \\ln(-1) $$

So then $\\ln(-23) = \\ln(-1) + \\ln(23) = \\pi i + \\ln(23)$.
