.DEFAULT_GOAL := help

help:                       
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: \
	help \
	down \
	up \
	migrate \
	makemigrations

down:                      
	@docker compose down

up:                        
	@docker compose up -d --build

migrate:                   
	@docker compose run --rm weather alembic upgrade head

makemigrations:            
	@read -p "Enter migration message: " message; \
	docker compose run --rm weather alembic revision --autogenerate -m "$$message"
