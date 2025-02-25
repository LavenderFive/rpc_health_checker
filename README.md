# rpc_health_checker

This repository contains a simple script for implementing a `/health` endpoint for RPC node clients using Flask.

## Prerequisites

- Docker
- Python 3.12

## Setup

1. Clone the repository:
```sh
git clone https://github.com/yourusername/rpc_health_checker.git
cd rpc_health_checker
```

2. Build the Docker image:
```sh
docker compose up -d
```

## Usage

The Flask application will be running on port `53336`. You can access the `/health` endpoint by navigating to `http://localhost:53336/health`.
In order to monitor the health of the health_checker, you can do: `curl http://localhost:53336/healthz`.

## Development

To develop and test the application locally:

1. Install `uv`:
```sh
pip install uv
```

3. Run the application:
```sh
uv run run.py
```

## License

This project is licensed under the Apache License License.
