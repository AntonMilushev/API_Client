# API Client

API_Client is a project that serves as an API client, designed to interact with external APIs and store responses in a database. The project is containerized using Docker for easy deployment.

## Overview
 The primary goal of API_Client is to facilitate the interaction with external APIs and persist the received data in a database. This can be particularly useful for scenarios where frequent API calls are required, and you want to store and analyze the responses over time.

## Features
 -API Interaction: Fetch data from external APIs. \
 -Database Storage: Save API responses to a connected database. \
 -Dockerized: Run the entire application in Docker containers.

## Technologies Used 
Docker: Containerization for a consistent and reproducible environment.\
Requests Library: Python library for making HTTP requests to APIs. \
PostgreSQL: Lightweight and embedded database for storing API responses.

## Setup Follow these steps to set up and run the API_Client:

Clone the repository: git clone https://github.com/AntonMilushev/API_Client.git

Navigate to the project directory: nt 
```bash
 cd API_Client 
```
Build and run Docker containers

```bash
docker-compose up -d
```
Run the following command to connect to your API Script container:
```bash
docker exec -it <id_of_api_container> /bin/bash
```
Once connected you can run the python script:
```bash
python api_client.py
```
Run the following command to connect to your PostgreSQL database container:
```bash
docker exec -it <id_of_db_container> psql -U user -d jokes
```
Once connected, you can run SQL queries to view the data:
```bash
SELECT * FROM jokes;
```
### And enjoy the joke.
