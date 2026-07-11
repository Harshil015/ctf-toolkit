#!/bin/bash

echo "[*] Spinning up CTF Docker environment..."
cd infra/

# Build and run in detached mode
docker-compose up -d --build

echo "[*] Dropping into CTF shell..."
# Execute bash inside the running container
docker exec -it ctf_toolkit bash

echo "[*] Exited container."
echo "[*] The container is still running in the background."
echo "[*] To stop it completely: cd infra/ && docker-compose down"
