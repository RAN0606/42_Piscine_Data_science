# Makefile

# Variables
DOCKER_COMPOSE_FILE = docker-compose.yml

# Default target
.PHONY: help
help:
	@echo "Makefile for Docker Compose commands"
	@echo "Usage:"
	@echo "  make start   - Start containers"
	@echo "  make stop    - Stop containers"
	@echo "  make clean   - Stop and remove containers"
	@echo "  make rm      - Remove containers, networks, volumes, and images"

# Start containers
.PHONY: start
start:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d

.PHONY: load
load:
	python3 automatic_table.py && python3 items_table.py



# Stop containers
.PHONY: stop
stop:
	docker-compose -f $(DOCKER_COMPOSE_FILE) stop

# Clean containers (stop and remove containers)
.PHONY: clean
clean:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

# Remove containers, networks, volumes, and images
.PHONY: rm
rm:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down --rmi all --volumes --remove-orphans
