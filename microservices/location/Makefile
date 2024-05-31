# Name of the Docker image
IMAGE_NAME = location-service

# Docker tag
TAG = latest

# Dockerfile location
DOCKERFILE = Dockerfile

# Build Docker image
build:
	docker build -t $(IMAGE_NAME):$(TAG) -f $(DOCKERFILE) .

# Show Docker images
images:
	docker images $(IMAGE_NAME)

# Remove Docker images
clean:
	docker rmi -f $(IMAGE_NAME):$(TAG)
