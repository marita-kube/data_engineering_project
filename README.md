# data_engineering_project

This project uses **uv** with `pyproject.toml` and `uv.lock` for dependency management.

## Prerequisites
- Python installed
- `uv` installed  
  ```bash
  pip install uv
git clone <https://github.com/marita-kube/data_engineering_project.git>
cd <data_pipeline>

## Create a virtual environment
uv venv
## Activate the virtual environment: for Macs
source .venv/bin/activate
## Activate the virtual environment: for Windows
.venv\Scripts\activate
## Install the dependencies
uv sync

## Alternatively, run the commands in one liner as below.
uv venv && source .venv/bin/activate && uv sync

# The project runs in docker. Install and set up docker to manage the project

This project sets up a local development environment using **Docker Compose** with:
- PostgreSQL (NY Taxi database)
- pgAdmin
- Kestra
- PostgreSQL backend for Kestra

### PostgreSQL (New York Taxi Datasets)
- Database: `new_york_taxi`
- User / Password: `root / root`
- Port: `5432`

### pgAdmin
- URL: http://localhost:8085
- Email: `admin@admin.com`
- Password: `root`

### Kestra
- UI: http://localhost:8080
- API: http://localhost:8081
- Login:
  - Email: `admin@kestra.io`
  - Password: `Admin1234`

Kestra uses its own PostgreSQL database (`kestra`) for metadata, queues, and storage.

## Prerequisites
- Docker
- Docker Compose

## Start the project 
    ```bash
    docker compose up -d

## Stop the project
docker compose down

## To remove docker volumes

docker compose down -v

### *NB: * This is for local environment only. Do not use this credentials in Production.