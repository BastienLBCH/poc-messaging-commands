start-dev:
	docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:22.0.1 start-dev
	venv/bin/python3 pocMessagingServiceCommands manage.py runserver 8000