# E-Learning Platform

This repository contains the code for an e-learning platform built using Django. The project covers various advanced topics including model inheritance, authentication systems, class-based views, RESTful API development, and real-time communication with Django Channels. Additionally, the application is containerized using Docker for easy deployment.

## Features

- **Class-Based Views and Mixins**: Utilize class-based views and mixins to manage content. Work with groups and permissions to restrict access, and apply form sets and model form sets to manage course modules and their content. Implement JavaScript drag-and-drop functionality for reordering.

- **Public Views and Course Catalog**: Create public views for the course catalog and develop a registration and enrollment system for students. Implement functionality to display various types of course module content and use the Django caching framework with Memcached and Redis.

- **Django REST Framework**: Develop a RESTful API using Django REST framework. Create serializers and views for models, add authentication, and restrict access using permissions. Implement custom permissions, ViewSet, and router setups. Use the `requests` library to consume the API from an external Python script.

- **Real-Time Chat Server**: Create a chat server using Django Channels with WebSocket consumers and clients. Enable communication between consumers using a channel layer with Redis, and convert the consumer to be fully asynchronous.

## Installation

### Prerequisites

- Docker
- Docker Compose

### Steps

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Aren2020/EducaWeb.git
   cd EducaWeb
   ```

2. **Build the Docker Image**:
   ```sh
   docker-compose build
   ```

3. **Run the Docker Containers**:
   ```sh
   docker-compose up
   ```

4. **Apply Migrations**:
   ```sh
   docker-compose exec web python educa/manage.py migrate
   ```

5. **Create a Superuser**:
   ```sh
   docker-compose exec web python educa/manage.py createsuperuser
   ```

6. **Collect Static**:
   ```sh
   docker-compose exec web python educa/manage.py collectstatic
   ```

7. **Access the Application**:
   Open your web browser and navigate to `http://localhost:80`.

## Usage

- **Admin Interface**: Accessible at `http://localhost:80/admin`.
- **API Endpoints**: Accessible at `http://localhost:80/api`.
- **Real-Time Chat**: Accessible through the main application interface after logging in

