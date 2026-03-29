# MCP Fetch in Docker

This directory builds a local Docker image with `mcp-server-fetch` installed and starts a persistent container named `mcp-fetch`.

## Build and start the persistent container

```powershell
docker compose up -d --build
```

## Verify the container is running

```powershell
docker ps --filter name=mcp-fetch
```

## Test the MCP server manually

```powershell
docker exec -i mcp-fetch python -m mcp_server_fetch
```

The command above starts the MCP server over stdio inside the running container. Your notebook can connect to it using `docker exec -i`.

## Stop the container

```powershell
docker compose down
```

## Notebook configuration

Use this in the notebook:

```python
fetch_mcp_server = StdioServerParams(
    command="docker",
    args=[
        "exec",
        "-i",
        "mcp-fetch",
        "python",
        "-m",
        "mcp_server_fetch",
    ],
    read_timeout_seconds=30,
)
```
