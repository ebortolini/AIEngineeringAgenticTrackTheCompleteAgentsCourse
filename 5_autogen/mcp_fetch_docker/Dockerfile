FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    PIP_NO_CACHE_DIR=1

RUN pip install --no-cache-dir mcp-server-fetch

WORKDIR /workspace

CMD ["python", "-m", "mcp_server_fetch"]
