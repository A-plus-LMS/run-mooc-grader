import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONTAINER_MODE = True
CONTAINER_SCRIPT = os.path.join(BASE_DIR, "scripts/docker-compose-run.sh")

