---
title: "Symmetries Between $\\sin$ and $\\cos$"
date: 2022-06-04T12:00:00-04:00
draft: false
summary: "Cool geometric and algebraic symmetries. Several embedded Desmos graphs."
tags: ["ACT", "Math", "LaTeX"]
---

## Geometry

We must start with the most basic definition.

### Lemma 1: In a right triangle, given angle $\\theta$, $\\sin \\theta = \\frac{\\text{opposite}}{\\text{hypotenuse}}$ and $\\cos \\theta = \\frac{\\text{adjacent}}{\\text{hypotenuse}}$

But it's definitely best to visualize:

![Basic geometric definition of sine and cosine](img/sincos-definition.jpg#center)

From the definitions, we get that the green side is $h\\cos \\theta$ because $\\cos \\theta = \\frac{\\text{adjacent}}{\\text{hypotenuse}} \\implies \\text{adjacent} = h\\cos \\theta$. Similarly, the blue side is $h\\sin \\theta$. Letting $h=1$, the adjacent side is just $\\cos \\theta$, and the opposite side is $\\sin \\theta$. With this setup, we can show **Lemma 2**.

### Lemma 2: $\\cos \\theta = \\sin(\\frac{\\pi}{2} - \\theta)$ and $\\sin \\theta = \\cos(\\frac{\\pi}{2} - \\theta)$ for arbitrary $\\theta$

*Proof*. Consider $\\alpha=\\frac{\\pi}{2}-\\theta$. In the triangle with hypotenuse 1, the green side is $\\cos \\theta = \\frac{\\text{adjacent}}{1}$. It is also $\\sin \\alpha = \\frac{\\text{opposite}}{1}$. Hence, $\\cos \\theta = \\sin(\\frac{\\pi}{2} - \\theta)$. Similar reasoning holds for the latter identity and for arbitrary $h$.

![geometric proof of separation by 90 degrees](img/sincos-identity-90.jpg#center)

Here's a Desmos graph where you can see the identity for yourself: [^1]

{{< rawhtml >}}
<p align="center">
<iframe class="center" src="https://www.desmos.com/calculator/csddcvviru" style="border:0px #ffffff none;"
name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="400px" width="600px"
allowfullscreen></iframe>
</p>
{{< /rawhtml >}}

[^1]: You can press the ▶️ on the left to view the animation.

Back to **Lemma 1**, why should the basic definition be limited to a static right triangle? What about a dynamic right triangle, perhaps one like this: [^2]

{{< rawhtml >}}
<p align="center">
<iframe class="center" src="https://www.desmos.com/calculator/ko2y1gnr7d" style="border:0px #ffffff none;"
name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="400px" width="600px"
allowfullscreen></iframe>
</p>
{{< /rawhtml >}}

[^2]: Note that there is no magic going on here. There's nothing in Desmos that specifically generates an arbitrary right triangle - this graph uses only the sine and cosine knowledge shown above!

In this graph, the x coordinates always involve $\\cos \\theta$, and the y coordinates always involve $\\sin \\theta$. Thinking of the black line as a vector [^3], we see that to get the horizontal component of the vector, we multiply its length by $\\cos \\theta$. To get its vertical component, we multiply its length by $\\sin \\theta$. In other words, $\\cos \\theta$ projects to $x$, and $\\sin \\theta$ projects to $y$.

[^3]: Since we can vary its length $r$ and its angle $t$

This applies to the graph of a circle as well. Note that, again, $x$ always goes with $\\cos \\theta$, and $y$ always goes with $\\sin \\theta$.

{{< rawhtml >}}
<p align="center">
<iframe class="center" src="https://www.desmos.com/calculator/jwpjnk3tqk" style="border:0px #ffffff none;"
name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="400px" width="600px"
allowfullscreen></iframe>
</p>
{{< /rawhtml >}}

To make this idea even more clear, you should take a look at this [circle animation on Khan Academy](https://www.khanacademy.org/computer-programming/circle/4597064320155648). [^4]

[^4]: ![Sine and cosine circle animation from Khan Academy](img/sincos-animation.jpg) A still screenshot of the animation [here](https://www.khanacademy.org/computer-programming/circle/4597064320155648).

## Algebra

There is an algebraic symmetry that is, in my opinion, as beautiful as the symmetries above. This symmetry also allows us to prove [$e^{ix} = \\cos x + i\\sin x$](../eulers_formula/) for any $x$.

### Lemma 3: $\\cos x = 1 - \\frac{x^2}{2} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + \\cdots$, and $\\sin x = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\cdots$ [^5]

[^5]: Note that the cosine expansion contains only even powers of $x$ (including $x^0 = 1$) divided by even factorials, and the sine expansion contains only odd powers of $x$ divided by odd factorials.

*Proof*. Consider that the [Taylor series](https://en.wikipedia.org/wiki/Taylor_series) [^6] expansion of $f(x)$ about the point $a$ is $$f(a)+f'(a)(x-a) + \\frac{f''(a)}{2!}(x-a)^2 + \\frac{f'''(a)}{3!}(x-a)^3 + \\cdots + \\frac{f^{(n)}(a)}{n!}(x-a)^n + \\cdots$$

The Maclaurin expansion is the Taylor series centered at $a=0$, so the Maclaurin expansion of $f(x)$ is $$f(0) + f'(0)x + \\frac{f''(0)}{2!}x^2 + \\frac{f'''(0)}{3!}x^3 + \\cdots + \\frac{f^{(n)}(0)}{n!}x^n + \\cdots$$

Let $f(x) = \\cos x$. We know that [^7]

![Derivatives of cosine](img/cos_derivatives.jpg#center)

Using that $\\cos(0) = 1$ and $\\sin(0) = 0$, we have that the first few terms of the Maclaurin series are $1 + 0x -\\frac{x^2}{2} + 0x^3 + \\frac{x^4}{4!}$. Now, we write the pattern: $$\\cos x = \\sum\_{n=0}^{\\infty} \\frac{(-1)^n}{2n!} x^{2n} $$

Any odd power will have $\\sin(0)=0$ and so can be ignored. Hence, we use only the even numbers $2n$ in our summation. Using that $f(x)=\\cos x$ and $f''(x) = -\\cos x$, we note that the signs alternate each (even) term, so we also have $(-1)^n$ in the summation.

[^6]: I might write an article about the Taylor series! For now, the tl;dr is that the Taylor expansion of a complicated function is a highly accurate approximation that is made up of less complicated polynomial terms, which are much easier to work with.

[^7]: Note here that the cycle length is 4, which is the same as that of the powers of $i$.

Similar reasoning holds for $\\sin x = \\sum\_{n=0}^{\\infty} \\frac{(-1)^n}{(2n+1)!}x^{2n+1}$.

Lastly, there are also two trigonometric identities that I have always found interesting, in terms of symmetry.

### Lemma 4: Angle sum and difference identities

$$\sin(\alpha + \beta) = \sin(\alpha) \cos(\beta) + \cos(\alpha) \sin(\beta)$$

$$\sin(\alpha - \beta) = \sin(\alpha) \cos(\beta) - \cos(\alpha) \sin(\beta)$$

$$\cos(\alpha + \beta) = \cos(\alpha) \cos(\beta) - \sin(\alpha) \sin(\beta)$$

$$\cos(\alpha - \beta) = \cos(\alpha) \cos(\beta) + \sin(\alpha) \sin(\beta)$$

I won't prove these identities here, but I will write about the symmetries. Note that the $\\sin$ identities have matching signs; that is, if there is a $+$ on the left side, there's a $+$ on the right side. However, the multiplications are mismatched in that $\\sin$ is multiplied by $\\cos$ and vice versa.

On the other hand, the $\\cos$ identities have matching multiplication in that $\\cos$ multiplies $\\cos$, and $\\sin$ multiplies $\\sin$. The signs, however, are mismatched.
