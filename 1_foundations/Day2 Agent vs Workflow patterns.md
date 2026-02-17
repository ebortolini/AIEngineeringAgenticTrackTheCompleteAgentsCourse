# Agent vs Workflow Patterns in LLM Design Applications

Agents:
 - Open-ended
 - Feedback loops
 - No fidex paths
  
```mermaid
flowchart LR
  HUMAN((HUMAN))
  LLM[LLM Call]
  ENV((ENVIRONMENT))
  STOP[STOP]

  HUMAN --> LLM
  LLM -- Action --> ENV
  ENV -- Feedback --> LLM
  LLM --> STOP

  style HUMAN fill:#ff7f0e,stroke:#222,stroke-width:2px
  style ENV fill:#ff7f0e,stroke:#222,stroke-width:2px
  style LLM fill:#a67c00,stroke:#222,stroke-width:2px
  style STOP fill:#1f77b4,stroke:#222,stroke-width:2px
```

## Risk of Agent Frameworks

- Unpredictable path
- Unpredictable output
- Unpredictable costs

## Mitigate risks:

- Monitor
- Guardrails to ensure your agents behave safely, consistenly, and within your intended boundaries