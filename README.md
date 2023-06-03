# fastapi sample
Building Microservice using FastAPI.

[FastAPI](https://fastapi.tiangolo.com/) fast and robust web framework for building APIs with Python 3.7+ 
## Features
1. OpenAPI by default
2. Automatic data model documentation
3. Security and Authentication 
4. Automatic validation for path, query
5. Cookies , WebSocket, CORS
6. Run a Server Manually - Uvicorn

We can compare Fast with Go and Nodejs

## Getting Started
1. Install dependencies
```zsh
pip install -r requirements.txt
```
2. Sample microservice 
```zsh
cd customer_service
uvicorn app.main:app
```
3. Test  API docs locally [http://localhost:8000/api/v1/customer/docs](http://localhost:8000/api/v1/customer/docs)

## Docker build
1. Build and deploy microservice 
```zsh
docker compose up -d
```
2. Docker compose service list

* Postgres - Database
* Nginx - Reverse proxy
* customer - microservice
s

3 Test API's

 Open docker deployed API docs [http://localhost:8080/api/v1/customer/docs](http://localhost:8080/api/v1/customer/docs)


