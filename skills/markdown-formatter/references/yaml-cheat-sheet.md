---
title: YAML
date: 2020-12-29 18:26:55
background: bg-[#b42e28]
tags:
  - config
  - format
categories:
  - Programming
intro: |
  This is a quick reference cheat sheet for understanding and writing YAML format configuration files.
plugins:
  - copyCode
---

# `YAML` cheat sheet

## TOC

- [`YAML` cheat sheet](#yaml-cheat-sheet)
  + [TOC](#toc)
  + [Getting Started](#getting-started)
    - [Introduction](#introduction)
    - [Scalar types](#scalar-types)
      + [Equivalent JSON](#equivalent-json)
    - [Variables](#variables)
      + [Equivalent JSON](#equivalent-json-1)
    - [Comments](#comments)
    - [Multiline strings](#multiline-strings)
      + [Equivalent JSON](#equivalent-json-2)
    - [Inheritance](#inheritance)
      + [Equivalent JSON](#equivalent-json-3)
    - [Reference](#reference)
      + [Equivalent JSON](#equivalent-json-4)
    - [Folded strings](#folded-strings)
      + [Equivalent JSON](#equivalent-json-5)
    - [Two Documents](#two-documents)
  + [YAML Collections](#yaml-collections)
    - [Sequence](#sequence)
      + [Equivalent JSON](#equivalent-json-6)
    - [Mapping](#mapping)
      + [Equivalent JSON](#equivalent-json-7)
    - [Mapping to Sequences](#mapping-to-sequences)
      + [Equivalent JSON](#equivalent-json-8)
    - [Sequence of Mappings](#sequence-of-mappings)
      + [Equivalent JSON](#equivalent-json-9)
    - [Sequence of Sequences](#sequence-of-sequences)
      + [Equivalent JSON](#equivalent-json-10)
    - [Mapping of Mappings](#mapping-of-mappings)
      + [Equivalent JSON](#equivalent-json-11)
    - [Nested Collections](#nested-collections)
      + [Equivalent JSON](#equivalent-json-12)
    - [Unordered Sets](#unordered-sets)
      + [Equivalent JSON](#equivalent-json-13)
    - [Ordered Mappings](#ordered-mappings)
      + [Equivalent JSON](#equivalent-json-14)
  + [YAML Reference](#yaml-reference)
    - [Terms](#terms)
    - [Document indicators](#document-indicators)
    - [Collection indicators](#collection-indicators)
    - [Alias indicators](#alias-indicators)
    - [Special keys](#special-keys)
    - [Scalar indicators](#scalar-indicators)
    - [Tag Property (usually unspecified)](#tag-property-usually-unspecified)
    - [Misc indicators](#misc-indicators)
    - [Core types (default automatic tags)](#core-types-default-automatic-tags)
    - [Escape Codes](#escape-codes)
      + [Numeric](#numeric)
      + [Protective](#protective)
      + [C](#c)
      + [Additional](#additional)
    - [More types](#more-types)
    - [Language Independent Scalar Types](#language-independent-scalar-types)
  + [Also see](#also-see)

## Getting Started

### Introduction

[YAML](https://yaml.org/) is a data serialization language designed to be directly writable and readable by humans

- YAML does not allow the use of tabs
- Must be space between the element parts
- YAML is CASE sensitive
- End your YAML file with the `.yaml` or `.yml` extension
- YAML is a superset of JSON
- Ansible playbooks are YAML files {.marker-round}

### Scalar types

<!-- prettier-ignore -->
```yaml
n1: 1            # integer
n2: 1.234        # float

s1: 'abc'        # string
s2: "abc"        # string
s3: abc          # string

b: false         # boolean type

d: 2015-04-05    # date type
```

#### Equivalent JSON

```json {.wrap}
{
  "n1": 1,
  "n2": 1.234,
  "s1": "abc",
  "s2": "abc",
  "s3": "abc",
  "b": false,
  "d": "2015-04-05"
}
```

Use spaces to indent. There must be space between the element parts.

### Variables

```yaml
some_thing: &VAR_NAME foobar
other_thing: *VAR_NAME
```

#### Equivalent JSON

<!-- prettier-ignore -->
```json {.wrap}
{
  "some_thing": "foobar",
  "other_thing": "foobar"
}
```

### Comments

```yaml
# A single line comment example

# block level comment example
# comment line 1
# comment line 2
# comment line 3
```

### Multiline strings

```yaml
description: |
  hello
  world
```

#### Equivalent JSON

```json {.wrap}
{ "description": "hello\nworld\n" }
```

### Inheritance

```yaml
parent: &defaults
  a: 2
  b: 3

child:
  <<: *defaults
  b: 4
```

#### Equivalent JSON

```json {.wrap}
{
  "parent": {
    "a": 2,
    "b": 3
  },
  "child": {
    "a": 2,
    "b": 4
  }
}
```

### Reference

```yaml
values: &ref
  - Will be
  - reused below

other_values:
  i_am_ref: *ref
```

#### Equivalent JSON

<!-- prettier-ignore -->
```json {.wrap}
{
  "values": [
    "Will be",
    "reused below"
  ],
  "other_values": {
    "i_am_ref": [
      "Will be",
      "reused below"
    ]
  }
}
```

### Folded strings

```yaml
description: >
  hello world
```

#### Equivalent JSON

```json {.wrap}
{ "description": "hello world\n" }
```

### Two Documents

```yaml
---
document: this is doc 1
---
document: this is doc 2
```

YAML uses `---` to separate directives from document content.

## YAML Collections

### Sequence

```yaml
- Mark McGwire
- Sammy Sosa
- Ken Griffey
```

#### Equivalent JSON

<!-- prettier-ignore -->
```json {.wrap}
[
  "Mark McGwire",
  "Sammy Sosa",
  "Ken Griffey"
]
```

### Mapping

<!-- prettier-ignore -->
```yaml
hr:  65       # Home runs
avg: 0.278    # Batting average
rbi: 147      # Runs Batted In
```

#### Equivalent JSON

```json {.wrap}
{
  "hr": 65,
  "avg": 0.278,
  "rbi": 147
}
```

### Mapping to Sequences

```yaml
attributes:
  - a1
  - a2
methods: [getter, setter]
```

#### Equivalent JSON

```json {.wrap}
{
  "attributes": ["a1", "a2"],
  "methods": ["getter", "setter"]
}
```

### Sequence of Mappings

<!-- prettier-ignore -->
```yaml
children:
  - name: Jimmy Smith
    age: 15
  - name: Jimmy Smith
    age: 15
  -
    name: Sammy Sosa
    age: 12
```

#### Equivalent JSON

<!-- prettier-ignore -->
```json {.wrap}
{
  "children": [
    {"name": "Jimmy Smith", "age": 15},
    {"name": "Jimmy Smith", "age": 15},
    {"name": "Sammy Sosa", "age": 12}
  ]
}
```

### Sequence of Sequences

<!-- prettier-ignore -->
```yaml
my_sequences:
  - [1, 2, 3]
  - [4, 5, 6]
  -
    - 7
    - 8
    - 9
    - 0
```

#### Equivalent JSON

```json {.wrap}
{
  "my_sequences": [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 0]
  ]
}
```

### Mapping of Mappings

```yaml
Mark McGwire: { hr: 65, avg: 0.278 }
Sammy Sosa: { hr: 63, avg: 0.288 }
```

#### Equivalent JSON

```json {.wrap}
{
  "Mark McGwire": {
    "hr": 65,
    "avg": 0.278
  },
  "Sammy Sosa": {
    "hr": 63,
    "avg": 0.288
  }
}
```

### Nested Collections

```yaml
Jack:
  id: 1
  name: Franc
  salary: 25000
  hobby:
    - a
    - b
  location: { country: 'A', city: 'A-A' }
```

#### Equivalent JSON

```json {.wrap}
{
  "Jack": {
    "id": 1,
    "name": "Franc",
    "salary": 25000,
    "hobby": ["a", "b"],
    "location": {
      "country": "A",
      "city": "A-A"
    }
  }
}
```

### Unordered Sets

```yaml
set1: !!set
  ? one
  ? two
set2: !!set { 'one', 'two' }
```

#### Equivalent JSON

```json {.wrap}
{
  "set1": { "one": null, "two": null },
  "set2": { "one": null, "two": null }
}
```

Sets are represented as a Mapping where each key is associated with a null value

### Ordered Mappings

```yaml
ordered: !!omap
  - Mark McGwire: 65
  - Sammy Sosa: 63
  - Ken Griffy: 58
```

#### Equivalent JSON

<!-- prettier-ignore -->
```json {.wrap}
{
  "ordered": [
    { "Mark McGwire": 65 },
    { "Sammy Sosa": 63 },
    { "Ken Griffy": 58 }
  ]
}
```

## YAML Reference

### Terms

- Sequences aka arrays or lists
- Scalars aka strings or numbers
- Mappings aka hashes or dictionaries {.marker-round}

Based on the YAML.org [refcard](https://yaml.org/refcard.html).

### Document indicators

|symbol|description|
| ----- | ------------------- |
| `%`   | Directive indicator |
| `---` | Document header     |
| `...` | Document terminator |

### Collection indicators

|symbol|description|
| ---- | ------------------------------- |
| `?`  | Key indicator                   |
| `:`  | Value indicator                 |
| `-`  | Nested series entry indicator   |
| `,`  | Separate in-line branch entries |
| `[]` | Surround in-line series branch  |
| `{}` | Surround in-line keyed branch   |

### Alias indicators

|symbol|description|
| --- | --------------- |
| `&` | Anchor property |
| `*` | Alias indicator |

### Special keys

|symbol|description|
| ---- | ------------------------------- |
| `=`  | Default "value" mapping key     |
| `<<` | Merge keys from another mapping |

### Scalar indicators

|symbol|description|
| ----- | --------------------------------- | --------------------------------------------- | ----------- |
| `''`  | Surround in-line unescaped scalar |
| `"`   | Surround in-line escaped scalar   |
| ` | `                                 | Block scalar indicator                        |
| `>`   | Folded scalar indicator           |
| `-`   | Strip chomp modifier (`| -`or`>-`)                                     |
| `+`   | Keep chomp modifier (`| +`or`>+`)                                     |
| `1-9` | Explicit indentation modifier (`| 1`or`>2`). <br/> Modifiers can be combined (`| 2-`, `>+1`) |

### Tag Property (usually unspecified)

|symbol|description|
| -------- | ----------------------------------------------------------- |
| `none`   | Unspecified tag (automatically resolved by application)     |
| `!`      | Non-specific tag (by default, `!!map`/`!!seq`/`!!str`)      |
| `!foo`   | Primary (by convention, means a local `!foo` tag)           |
| `!!foo`  | Secondary (by convention, means `tag:yaml.org,2002:foo`)    |
| `!h!foo` | Requires `%TAG !h! <prefix>` (and then means `<prefix>foo`) |
| `!<foo>` | Verbatim tag (always means `foo`)                           |

### Misc indicators

|symbol|description|
| ---------------- | ---------------------------- |
| `#`              | Throwaway comment indicator  |
| <code>\`@</code> | Both reserved for future use |

### Core types (default automatic tags)

|symbol|description|
| ------- | ---------------------------------------- |
| `!!map` | `{Hash table, dictionary, mapping}`      |
| `!!seq` | `{List, array, tuple, vector, sequence}` |
| `!!str` | Unicode string                           |

### Escape Codes

#### Numeric

- `\x12` (8-bit)
- `\u1234` (16-bit)
- `\U00102030` (32-bit)

{.cols-2 .marker-none}

#### Protective

- `\\` (\\)
- `\"` (")
- `\` ( )
- `\<TAB>` (TAB)

{.cols-3 .marker-none}

#### C

- `\0` (NUL)
- `\a` (BEL)
- `\b` (BS)
- `\f` (FF)
- `\n` (LF)
- `\r` (CR)
- `\t` (TAB)
- `\v` (VTAB)

{.cols-3 .marker-none}

#### Additional

- `\e` (ESC)
- `\_` (NBSP)
- `\N` (NEL)
- `\L` (LS)
- `\P` (PS)

{.cols-3 .marker-none}

### More types

|symbol|description|
| -------- | --------------------------- |
| `!!set`  | `{cherries, plums, apples}` |
| `!!omap` | `[one: 1, two: 2]`          |

### Language Independent Scalar Types

|symbol|description|
| ------------------------- | ------------------------------------------ |
| `{~, null}`               | Null (no value).                           |
| `[1234, 0x4D2, 02333]`    | [Decimal int, Hexadecimal int, Octal int]  |
| `[1_230.15, 12.3015e+02]` | [Fixed float, Exponential float]           |
| `[.inf, -.Inf, .NAN]`     | [Infinity (float), Negative, Not a number] |
| `{Y, true, Yes, ON}`      | Boolean true                               |
| `{n, FALSE, No, off}`     | Boolean false                              |

## Also see

- [YAML Reference Card](https://yaml.org/refcard.html) _(yaml.org)_
- [Learn X in Y minutes](https://learnxinyminutes.com/docs/yaml/) _(learnxinyminutes.com)_
- [YAML lint online](http://www.yamllint.com/) _(yamllint.com)_
