---
title: "Flowchart ELK Complex Routing Template"
description: "ELK layout template for complex directed flowcharts with crossing edges and service dependencies."
tags:
  - mermaid
  - template
  - flowchart
  - layout/elk
---

# Flowchart ELK Complex Routing Template

Ask before using this layout unless the user explicitly requests ELK. Use it when a directed flowchart or service dependency map has many crossings under the default layout.

Do not use this as a first choice for simple processes, GitHub-safe output, or unknown renderers.

```mermaid
---
config:
  layout: elk
  elk:
    nodePlacementStrategy: "NETWORK_SIMPLEX"
    mergeEdges: true
    forceNodeModelOrder: false
  flowchart:
    nodeSpacing: 70
    rankSpacing: 90
    curve: "linear"
---
flowchart TD
    Gateway{API Gateway}

    subgraph Auth[Authentication]
        Login[Login]
        Token[Token service]
    end

    subgraph Core[Core services]
        Orders[Order service]
        Users[User service]
        Billing[Billing service]
    end

    Gateway --> Login
    Login -. token request .-> Token
    Gateway --> Orders
    Gateway --> Users
    Orders -. invoices .-> Billing
    Billing -. account status .-> Users
```

Documented ELK keys include `mergeEdges`, `nodePlacementStrategy`, `cycleBreakingStrategy`, `forceNodeModelOrder`, and `considerModelOrder`. Validate in the target renderer.
