# DRF Commerce API

A complete Django REST Framework e-commerce backend for managing users, products, comments, orders, and payment transactions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Docker Setup](#docker-setup)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [License](#license)

## Overview

This project is structured as a monorepo-style Django app where the Django project and its apps live inside the `core/` directory, while the root of the repository contains the Docker configuration and environment files.

## Features

- User authentication and authorization with JWT
- Custom user model and address handling
- Product catalog with categories, filters, stock, and discounts
- Order management and order item tracking
- Payment and transaction flow
- Product comments/reviews system
- Swagger/OpenAPI documentation
- Docker-based local development setup

## Tech Stack

- Python 3.13
- Django 6.0.1
- Django REST Framework
- djangorestframework-simplejwt
- django-filter
- drf-yasg
- django-cors-headers
- django-tinymce
- SQLite3 (default database)
- Docker / Docker Compose

## Project Structure

```text
drf_commerce/
├── dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── LICENSE
├── .env
├── core/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── accounts/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── comments/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── orders/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── payment/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── utils.py
│   │   └── services/
│   │       └── transaction.py
│   ├── shop/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── filters.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── media/
│   ├── static/
│   └── templates/
│       └── ...
└── ...
```

## Installation

### Prerequisites

- Python 3.10+
- pip
- virtualenv (recommended)
- Docker and Docker Compose (optional, for containerized setup)

### Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/cod-F123/drf_commerce.git
   cd drf_commerce
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Go to the Django project folder:

   ```bash
   cd core
   ```

5. Run database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

## Environment Variables

Create a `.env` file in the project root (`drf_commerce/.env`) with values similar to:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
TIME_ZONE=UTC
CSRF_TRUSTED_ORIGINS=http://localhost:8000
CORS_ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```

The Django settings use `python-decouple` to read these values.

## Running the Project

### Run locally

From the `core/` directory:

```bash
python manage.py runserver
```

Then open:

- API: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Swagger docs: http://127.0.0.1:8000/swagger/

## Docker Setup

The project includes Docker configuration at the repository root.

### Build and run with Docker Compose

From the project root:

```bash
docker compose up --build
```

This will start the application using the Dockerfile and the `docker-compose.yml` file. The Django project runs inside the `core` folder and is exposed on port `8000`.

If you want to stop the container:

```bash
docker compose down
```

## API Documentation

The project exposes Swagger and ReDoc endpoints:

- Swagger UI: http://127.0.0.1:8000/swagger/
- ReDoc: http://127.0.0.1:8000/redoc/
- OpenAPI JSON: http://127.0.0.1:8000/swagger.json

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/accounts/register/` | User registration |
| POST | `/accounts/token/` | Get JWT token |
| POST | `/accounts/token/refresh/` | Refresh access token |
| GET | `/accounts/user/<email>/` | Get user profile |
| PUT | `/accounts/update-username/<email>/` | Update username |
| POST | `/accounts/change-password/<email>/` | Change password |
| POST | `/accounts/update-info/<email>/` | Update user info |
| GET | `/accounts/address/` | List addresses |
| POST | `/accounts/address/` | Create address |
| GET | `/accounts/address/<id>/` | Get one address |
| PUT | `/accounts/address/<id>/` | Update address |
| DELETE | `/accounts/address/<id>/` | Delete address |

### Shop

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/shop/category-list/` | List categories |
| GET | `/shop/product-list/` | List products |
| GET | `/shop/product/<slug>/` | Get product details |

### Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/orders/` | List user orders |
| POST | `/orders/` | Create order |
| GET | `/orders/<id>/` | Get order details |
| PUT | `/orders/<id>/` | Update order |
| DELETE | `/orders/<id>/` | Delete order |

### Payment

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/payment/start/` | Create payment transaction |
| GET | `/payment/callback-payment/` | Payment callback |
| GET | `/payment/list/` | List transactions |

### Comments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/shop/product/<slug>/` | Get product comments |
| POST | `/comments/` | Create comment |
| DELETE | `/comments/<id>/` | Delete comment |

## Database Models

### User

- Custom user model using email-based authentication
- Fields include email, password, username, first name, last name
- Related to orders, comments, and addresses

### UserAddress

- Stores user shipping addresses
- Fields: user, address, zip_code

### Category

- Product categories
- Fields: name, image

### Product

- Product details
- Fields: name, category, image, description, price, stock, percent_off, is_exist, slug, date_added
- Includes derived properties such as `is_offered` and `offered_price`

### ProductImage

- Extra images related to a product
- Fields: product, image

### Order

- Customer orders
- Fields: user, address, zip_code, total_amount, status, created_at, payed_at, shipped_at, order_id

### OrderItem

- Each item included in an order
- Fields: order, product, quantity, price

### Transaction

- Payment transaction records
- Fields: order, amount, ref_id, authority_id, transaction_status, created_at

### Comment

- Product review/comment entries
- Fields: user, product, content, created_at

## License

This project is licensed under the BSD 3-Clause License.

---

Contact: mohammad.javad.d3v@gmail.com