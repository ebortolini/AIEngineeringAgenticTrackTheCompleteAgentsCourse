# Ollama with Docker (CPU, latest)

This file shows a minimal Docker Compose setup for running Ollama locally inside Docker.

Files created:
- `docker-compose.yml` — starts an `ollama` container (image: `ollama/ollama:latest`).

Assumptions:
- Using Docker Desktop on Windows (WSL2 backend).
- CPU-only. If you need GPU support, see the GPU section below.

Quick start
1. Start the service:

```powershell
docker-compose up -d
```

2. Watch logs:

```powershell
docker-compose logs -f ollama
```

3. Pull a model (example):

```powershell
docker exec -it ollama ollama pull <model-name>
```

4. List available models inside the container:

```powershell
docker exec -it ollama ollama ls
```

5. Make a quick HTTP request (replace `<model-name>`):

```powershell
# Windows PowerShell (recommended)
$body = @{ model = '<model-name>'; prompt = 'Say hello'; max_tokens = 32 } | ConvertTo-Json
Invoke-RestMethod -Uri 'http://localhost:11434/v1/completions' -Method Post -ContentType 'application/json' -Body $body
```

Persistent data
- Models and runtime state are stored in the repository folder `./ollama_data` (mapped to `/var/lib/ollama` inside the container).

Optional: GPU support
- For NVIDIA GPUs, install the NVIDIA Container Toolkit on the host and enable `runtime: nvidia` or use `deploy` settings; on Windows use WSL2 GPU support + Docker Desktop GPU settings. If you want, I can add a GPU-enabled compose variant.

Troubleshooting
- If the image name or CLI changes in future releases, consult the official Ollama docs and adjust the `image:` line and any `docker exec` commands accordingly.

Cleanup

```powershell
docker-compose down -v
rm -rf ./ollama_data
```
