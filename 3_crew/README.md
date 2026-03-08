# CrewAI has several offerings

## CrewAI Enterprise

A multi-agent platform for deploying running and monitoring Agentic AI

## CrewAI UI Studio

A no-code / lo-code product for creating multi-agent solutions

## CrewAI open-source framework

Orchestrate high performing AI agents with ease and scale

### CrewAI Crews

Autonomous solutions with AI teams of Agents with different rules

### CrewAI Flows

Stuctured automations by dividing complex tasks into precise workflows

## Install

```powershell
uv tool install crewai
```

## Create a project

```powershell
crewai create crew my_crew
```

## Run

```powershell
crewai run
```

## Memory 

### Short-Term Memory
Temporarily stores recent interactions and outcomes using RAG, enabling agents to access relevant information during context executions.

### Long-Term Memory
Preservers valuable insights and learnings, building knowledge over time.

### Entity Memory
Information about people, places and concepts encountered during tasks, facilitating deeper understanding and relationshio mapping. Uses RAG to store entity information.

### Contextual Memory
Maintains the context of interactions by combining all the above.

### User Memory
Stores user-specific information and preferences, enhancing personalization and user experience (this is up yo us to manage and include in prompts)