# AI Engineer Production Track: Deploy LLMs & Agents at Scale

## Github
[Master AI Agentic Engineering - build autonomous AI Agents](https://github.com/ed-donner/agents)

## Udemy
[AI Engineer Agentic Track: The Complete Agent & MCP Course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/)

## Local setup with uv (recommended)

This repository is set up to use [`uv`](https://docs.astral.sh/uv/) for dependency and environment management.

### 1) Install uv

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2) Sync dependencies

From the repository root:

```powershell
uv sync
```

This creates a local virtual environment in `.venv` and installs notebook tooling.

### 3) Run notebooks

Option A (recommended): JupyterLab

```powershell
uv run jupyter lab
```

Option B: classic Notebook

```powershell
uv run jupyter notebook
```

### 4) (Optional) Register a dedicated kernel

If your editor does not automatically detect the `.venv` interpreter:

```powershell
uv run python -m ipykernel install --user --name ai-engineering-agentic-track --display-name "Python (uv: ai-engineering-agentic-track)"
```

Then select that kernel inside VS Code/Jupyter.

### Common commands

```powershell
uv add <package-name>      # add dependency
uv remove <package-name>   # remove dependency
uv lock                    # refresh lockfile
uv sync                    # install from lockfile
```
