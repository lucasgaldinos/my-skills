---
title: "Introduction to gradient descent"
tags: [math, optimization, machine-learning]
date_created: 2026-04-01
date_changed: 2026-04-02
---

# Introduction to gradient descent

Gradient descent is an optimization algorithm used to minimize a differentiable loss function
by iteratively moving in the direction of steepest descent.

## Symbol notation

| Symbol | Meaning |
|---|---|
| $\theta$ | Model parameters (vector) |
| $\mathcal{L}$ | Loss function to minimize |
| $\alpha$ | Learning rate (step size) |
| $\nabla_\theta$ | Gradient with respect to $\theta$ |
| $t$ | Iteration index |

## Algorithm

The parameter update rule[^update-rule] applied at each iteration is:

[^update-rule]: Derived from the first-order Taylor expansion of $\mathcal{L}$ around $\theta_t$.

$$\begin{equation}
\theta_{t+1} = \theta_t - \alpha \nabla_\theta \mathcal{L}(\theta_t)
\end{equation}$$

Convergence is detected when the gradient norm drops below a threshold:

$$\begin{equation*}
\| \nabla_\theta \mathcal{L}(\theta_t) \|_2 < \epsilon
\end{equation*}$$

> [!NOTE]
> The learning rate $\alpha$ must be chosen carefully. Too large causes oscillation or
> divergence; too small makes convergence impractically slow.

> [!CAUTION]
> Gradient descent finds a local minimum, not necessarily the global one. For non-convex
> loss surfaces, results depend on initialization.

## Implementation

```python src/optim/gradient_descent.py#L12-L28
def gradient_descent(
    loss_fn: Callable,
    theta: np.ndarray,
    alpha: float = 0.01,
    max_iter: int = 1000,
    tol: float = 1e-6,
) -> np.ndarray:
    for _ in range(max_iter):
        grad = compute_gradient(loss_fn, theta)
        if np.linalg.norm(grad) < tol:
            break
        theta -= alpha * grad
    return theta
```

## Hyperparameter summary

| Hyperparameter | Typical range | Effect |
|---|---|---|
| $\alpha$ (learning rate) | $10^{-4}$ to $10^{-1}$ | Step size per iteration |
| $\epsilon$ (convergence tol) | $10^{-6}$ to $10^{-4}$ | Stopping criterion |
| `max_iter` | 100 to 10 000 | Maximum iterations cap |

## Variants

Stochastic gradient descent (SGD) approximates the gradient on a random mini-batch[^sgd]:

[^sgd]: Robbins and Monro (1951). "A stochastic approximation method."

$$\begin{equation*}
\theta_{t+1} = \theta_t - \alpha \nabla_\theta \mathcal{L}_{\text{batch}}(\theta_t)
\end{equation*}$$

> [!TIP]
> For large datasets, SGD typically converges faster in wall-clock time than full-batch
> gradient descent despite noisier updates.

## Citing external sources correctly

When a document imports text from Google Docs or AI-generated academic articles, use
descriptive GFM footnote labels — not bare numbers.

Gradient descent was popularized through the work of Cauchy in the 19th century and later
formalized in machine learning contexts.[^cauchy-gradient] The stochastic variant became
dominant after Robbins and Monro's seminal paper.[^robbins-monro]

The learning rate $\alpha$ acts as the critical hyperparameter governing convergence
speed.[^cauchy-gradient] Too large a value causes oscillation; too small leads to impractical
wall-clock times.

## References

[^cauchy-gradient]: [Méthode générale pour la résolution des systèmes d'équations simultanées — Cauchy (1847)](https://gallica.bnf.fr/ark:/12148/bpt6k2982k/f540) — accessed 2026-04-02.

[^robbins-monro]: [A Stochastic Approximation Method — Robbins & Monro (1951)](https://doi.org/10.1214/aoms/1177729586) — accessed 2026-04-02.
