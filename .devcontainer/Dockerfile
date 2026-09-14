# Usamos la imagen oficial de Python para DevContainers
FROM python:3.12-slim-bookworm

# Copiamos uv directamente desde la imagen oficial de Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Actualizamos repositorios de sistema si hace falta
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends gcc git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*    

# Configuramos uv para que por defecto instale los paquetes a nivel de sistema
# dentro del contenedor (así evitamos que los alumnos tengan que activar entornos virtuales)
ENV UV_SYSTEM_PYTHON=1