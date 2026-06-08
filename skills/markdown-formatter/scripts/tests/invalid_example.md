---
title: "Gradient descent notes"
tags: [math, optimization]
date_created: 2026-04-03
date_changed: 2026-04-01
---

# Gradient descent notes

This file intentionally violates multiple rules. Run validate_all.py to see all findings.

## VIOLATION: Rule 9 — plain blockquote

> This is a plain blockquote without an admonition marker.
> It will be flagged as an error.

> [!INFO]
> This uses an invalid admonition type (INFO is not in the allowed set).

## VIOLATION: Rule 3 — code block without language

```
def gradient_descent(theta, alpha):
    return theta - alpha * grad(theta)
```

Another with tilde fence:

~~~python
echo "tilde fences are also flagged"
~~~

## VIOLATION: Rule 11 — bare display math without environment

$$
E = mc^2
$$

Also forbidden commands:

$$\begin{equation}
\def\myvar{x} f(\myvar) = \myvar^2
\end{equation}$$

## VIOLATION: Rule 11 — wrong delimiters

\[E = mc^2\]

\(inline with wrong delimiters\)

## VIOLATION: Rule 7 — footnote too long and before its reference

[^long-fn]: This footnote is extremely long and should be converted to an admonition or a
    dedicated subsection. It explains in great detail the mathematical foundations of the concept,
    including historical context, alternative derivations, and implementation considerations that
    span well beyond the two-line threshold. This is clearly too much content for a footnote.

See the algorithm described above[^long-fn] for details.

## VIOLATION: Rule 7 — numeric footnote IDs in a multi-footnote document

See reference [^1] and also [^2] and further [^3] and finally [^4].

[^1]: First numeric footnote.
[^2]: Second numeric footnote.
[^3]: Third numeric footnote.
[^4]: Fourth numeric footnote.

## VIOLATION: Rule 8 — non-compact table (aligned/padded)

| Hyperparameter     | Typical range           | Effect                   |
| ------------------ | ----------------------- | ------------------------ |
| learning rate      | $10^{-4}$ to $10^{-1}$ | Step size per iteration  |
| convergence tol    | $10^{-6}$ to $10^{-4}$ | Stopping criterion       |

## Note on rule 0 violations above

The front matter at the top of this file has `date_changed: 2026-04-01` which is BEFORE
`date_created: 2026-04-03`. This will produce a warning.

## VIOLATION: Rule 14 — import artifacts from Google Docs

### **1\. Bold header with backslash-escaped number**

This header above uses `**bold**` wrapping and `1\.` escaped dot — common from Google Docs.
It should be `### 1. Bold header with backslash-escaped number`.

This text ends with a sentence and a bare numeric citation.3
This line has trailing double-spaces making a hard line break instead of a paragraph break.5
And the citation numbers map to a numbered Works Cited list at the bottom rather than proper GFM footnotes.

Another paragraph without blank line separator — consecutive lines with no blank line between
them render as a single Markdown paragraph, losing the paragraph structure from the original document.

3. Philosophy of language - Wikipedia, https://en.wikipedia.org/wiki/Philosophy_of_language
5. Lexical Semantics, https://oxfordre.com/...
