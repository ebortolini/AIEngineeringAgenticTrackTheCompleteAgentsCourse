# 5 Workflow design patterns

## Prompt Chaining

Decomposit into fixed subtasks

```mermaid
flowchart LR
	IN((IN))
	LLM1([LLM1])
	Gate{Gate}
	LLM2([LLM2])
	LLM3([LLM3])
	OUT((OUT))
	IN --> LLM1 --> Gate --> LLM2 --> LLM3 --> OUT
	style IN fill:#ff7f0e,stroke:#222,stroke-width:2px
	style OUT fill:#ff7f0e,stroke:#222,stroke-width:2px
	style LLM1 fill:#a67c00,stroke:#222,stroke-width:2px
	style LLM2 fill:#a67c00,stroke:#222,stroke-width:2px
	style LLM3 fill:#a67c00,stroke:#222,stroke-width:2px
	style Gate fill:#1f77b4,stroke:#222,stroke-width:2px,stroke-dasharray: 5 5
```

## Routing

Direct an input into a specialized subtask, ensuring separation of concerns.

```mermaid
flowchart LR
	IN((IN))
	Router[LLM Router]
	LLM1([LLM1])
	LLM2([LLM2])
	LLM3([LLM3])
	OUT((OUT))

	IN --> Router --> LLM2 --> OUT
	Router --> LLM1
	Router --> LLM3

	LLM1 --> OUT
	LLM3 --> OUT

	style IN fill:#ff7f0e,stroke:#222,stroke-width:2px
	style OUT fill:#ff7f0e,stroke:#222,stroke-width:2px
	style Router fill:#a67c00,stroke:#222,stroke-width:2px
	style LLM1 fill:#a67c00,stroke:#222,stroke-width:2px
	style LLM2 fill:#a67c00,stroke:#222,stroke-width:2px
	style LLM3 fill:#a67c00,stroke:#222,stroke-width:2px
```


## Parallelization

Braking down tasks and running  multiple subtasks concurrently.

```mermaid
flowchart LR
    IN((IN))
    Coordinator[Coordinator]
    LLM1([LLM1])
    LLM2([LLM2])
    LLM3([LLM3])
    Aggregator[Aggregator]
    OUT((OUT))

    IN --> Coordinator
    Coordinator --> LLM1
    Coordinator --> LLM2
    Coordinator --> LLM3

    LLM1 --> Aggregator
    LLM2 --> Aggregator
    LLM3 --> Aggregator

    Aggregator --> OUT

    style IN fill:#ff7f0e,stroke:#222,stroke-width:2px
    style OUT fill:#ff7f0e,stroke:#222,stroke-width:2px
    style Coordinator fill:#1f77b4,stroke:#222,stroke-width:2px
    style Aggregator fill:#1f77b4,stroke:#222,stroke-width:2px
    style LLM1 fill:#a67c00,stroke:#222,stroke-width:2px
    style LLM2 fill:#a67c00,stroke:#222,stroke-width:2px
    style LLM3 fill:#a67c00,stroke:#222,stroke-width:2px
```

## Orchestrator Worker

Complex tasks are broken down dynamically and combined

```mermaid
flowchart LR
    IN((IN))
    Orchestrator[Orchestrator]
    LLM1([LLM1])
    LLM2([LLM2])
    LLM3([LLM3])
    Synthesizer[Synthesizer]
    OUT((OUT))

    IN --> Orchestrator
    Orchestrator --> LLM1
    Orchestrator --> LLM2
    Orchestrator --> LLM3

    LLM1 --> Synthesizer
    LLM2 --> Synthesizer
    LLM3 --> Synthesizer

    Synthesizer --> OUT

    style IN fill:#ff7f0e,stroke:#222,stroke-width:2px
    style OUT fill:#ff7f0e,stroke:#222,stroke-width:2px
    style Orchestrator fill:#a67c00,stroke:#222,stroke-width:2px
    style Synthesizer fill:#a67c00,stroke:#222,stroke-width:2px
    style LLM1 fill:#a67c00,stroke:#222,stroke-width:2px
    style LLM2 fill:#a67c00,stroke:#222,stroke-width:2px
    style LLM3 fill:#a67c00,stroke:#222,stroke-width:2px
```

## Evaluation Optimizer

LLM output is validated by another

```mermaid
flowchart LR
  IN((IN))
  G[LLM Generator]
  E[LLM Evaluator]
  OUT((OUT))

  IN --> G
  G -->|Solution| E
  E -->|Rejected with feedback| G
  E -->|Accepted| OUT

  style IN fill:#ff7f0e,stroke:#222,stroke-width:2px
  style OUT fill:#ff7f0e,stroke:#222,stroke-width:2px
  style G fill:#a67c00,stroke:#222,stroke-width:2px
  style E fill:#a67c00,stroke:#222,stroke-width:2px

  linkStyle 0 stroke:#888,stroke-width:2px
  linkStyle 1 stroke:#888,stroke-width:2px
  linkStyle 2 stroke:#d62728,stroke-width:3px
  linkStyle 3 stroke:#2ca02c,stroke-width:3px
```