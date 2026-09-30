

```mermaid
classDiagram

    Animal <|-- Duck

    Animal <|-- Fish

    Animal <|-- Zebra

    Animal : +int age

    Animal : +String gender

    Animal: +isMammal()

    Animal: +mate()

    class Duck{

      +String beakColor

      +swim()

      +quack()

    }

    class Fish{

      -int sizeInFeet

      -canEat()

    }

    class Zebra{

      +bool is_wild

      +run()

    }
```


```mermaid
flowchart TD

    A[Christmas] -->|Get money| B(Go shopping)

    B --> C{Let me think}

    C -->|One| D[Laptop]

    C -->|Two| E[iPhone]

    C -->|Three| F[fa:fa-car Car]
```


```mermaid
sequenceDiagram

    Alice->>+John: Hello John, how are you?

    Alice->>+John: John, can you hear me?

    John-->>-Alice: Hi Alice, I can hear you!

    John-->>-Alice: I feel great!
```


```mermaid
erDiagram

    CUSTOMER ||--o{ ORDER : places

    ORDER ||--|{ ORDER_ITEM : contains

    PRODUCT ||--o{ ORDER_ITEM : includes

    CUSTOMER {

        string id

        string name

        string email

    }

    ORDER {

        string id

        date orderDate

        string status

    }

    PRODUCT {

        string id

        string name

        float price

    }

    ORDER_ITEM {

        int quantity

        float price

    }
```

```mermaid
stateDiagram-v2

    [*] --> Still

    Still --> [*]

    Still --> Moving

    Moving --> Still

    Moving --> Crash

    Crash --> [*]
```

```mermaid
mindmap

  root((mindmap))

    Origins

      Long history

      ::icon(fa fa-book)

      Popularisation

        British popular psychology author Tony Buzan

    Research

      On effectiveness<br/>and features

      On Automatic creation

        Uses

            Creative techniques

            Strategic planning

            Argument mapping

    Tools

      Pen and paper

      Mermaid
```

```mermaid
block-beta

  columns 3

  user(("User")):3

  space:3

  ui["Web UI"] api["API Server"] db[("Database")]

  

  user --> ui

  ui --> api

  api --> db

  

  style user fill:#ffe0b2,stroke:#fb8c00

  style db fill:#bbdefb,stroke:#1e88e5
```


```mermaid
venn-beta
    
    title "Finding the Product Sweet Spot"

    set Desirable

    set Feasible

    set Viable

    union Desirable,Feasible["Worth prototyping"]

    union Feasible,Viable["Cheap to run"]

    union Desirable,Viable["Hard to build"]

    union Desirable,Feasible,Viable["Sweet spot"]
```

```mermaid
xychart-beta

    title "Sales Revenue"

    x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

    y-axis "Revenue (in $)" 4000 --> 11000

    bar [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]

    line [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
```

