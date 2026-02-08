# DRF E-Commerce API

A comprehensive **Django REST Framework** e-commerce API that provides a complete backend solution for online shopping platforms. This API includes user authentication, product management, shopping orders, payment processing, and product reviews/comments.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)

## Features

### Core Features

- **User Management**
  - Custom user model with email authentication
  - User profile management
  - Address management for shipping
  - JWT token-based authentication

- **Product Management**
  - Product catalog with categories
  - Product filtering and search
  - Product images and descriptions (rich HTML editor)
  - Inventory/stock management
  - Discount/offer system with percentage off
  - Product availability status

- **Shopping & Orders**
  - Shopping cart functionality
  - Order management with multiple statuses (Pending, Paid, Processing, Shipped)
  - Order tracking and history
  - Order items management

- **Payment Processing**
  - Transaction management
  - Payment status tracking (Pending, Success, Fail)
  - Order-to-transaction relationship
  - Payment reference tracking

- **Product Reviews**
  - Product comments/reviews system
  - User-based reviews
  - Comment management

- **API Documentation**
  - Swagger UI for interactive API exploration
  - ReDoc for alternative documentation
  - OpenAPI schema generation

## Tech Stack

- **Backend Framework**: Django 6.0.1
- **API Framework**: Django REST Framework
- **Authentication**: Django REST Framework Simple JWT
- **Database**: SQLite3 (default)
- **Text Editor**: TinyMCE
- **Filtering**: django-filters
- **API Documentation**: drf-yasg (Swagger/OpenAPI)
- **Python**: 3.8+

## Project Structure

```
drf_ecommerce/
├── accounts/              # User authentication and profile management
│   ├── models.py         # Custom User and UserAddress models
│   ├── serializers.py    # User serializers
│   ├── views.py          # Authentication endpoints
│   ├── urls.py           # Account routes
│   └── permissions.py    # Custom permissions
│
├── shop/                 # Product catalog management
│   ├── models.py         # Category, Product, Image models
│   ├── serializers.py    # Product serializers
│   ├── views.py          # Product endpoints
│   ├── filters.py        # Product filtering
│   └── urls.py           # Shop routes
│
├── orders/               # Order management
│   ├── models.py         # Order and OrderItem models
│   ├── serializers.py    # Order serializers
│   ├── views.py          # Order endpoints
│   ├── urls.py           # Order routes
│   └── utils.py          # Order utilities
│
├── payment/              # Payment processing
│   ├── models.py         # Transaction model
│   ├── views.py          # Payment endpoints
│   ├── urls.py           # Payment routes
│   ├── services/         # Payment service logic
│   └── utils.py          # Payment utilities
│
├── comments/             # Product comments/reviews
│   ├── models.py         # Comment model
│   ├── serializers.py    # Comment serializers
│   ├── views.py          # Comment endpoints
│   ├── urls.py           # Comment routes
│   └── permissions.py    # Comment permissions
│
├── config/               # Project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
│
├── media/                # User uploaded files
├── static/               # Static files
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database
└── .env                  # Environment variables
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/cod-F123/drf_commerce.git
   cd drf_ecommerce
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file in project root**
   ```bash
   SECRET_KEY=your-secret-key-here
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database

The project uses SQLite3 by default. To use a different database (PostgreSQL, MySQL), update `DATABASES` in `config/settings.py`.

## Running the Project

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the API**
   - Main API: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`
   - Django Shell: `python manage.py shell`

## API Documentation

### Interactive Documentation

- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **ReDoc**: `http://127.0.0.1:8000/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/swagger.json`

## API Endpoints

### Authentication (Accounts)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/accounts/register/` | User registration |
| POST | `/accounts/login/` | User login |
| POST | `/accounts/token/` | Get JWT token |
| GET | `/accounts/profile/` | Get user profile |
| PUT | `/accounts/profile/` | Update user profile |
| GET | `/accounts/addresses/` | Get user addresses |
| POST | `/accounts/addresses/` | Create new address |

### Products (Shop)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/shop/categories/` | List all categories |
| GET | `/shop/products/` | List all products |
| GET | `/shop/products/<id>/` | Get product details |
| GET | `/shop/products/<id>/images/` | Get product images |

### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/orders/` | List user orders |
| POST | `/orders/` | Create new order |
| GET | `/orders/<id>/` | Get order details |
| PUT | `/orders/<id>/` | Update order |
| GET | `/orders/<id>/items/` | Get order items |

### Payment
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/payment/transaction/` | Create payment transaction |
| GET | `/payment/transaction/<id>/` | Get transaction status |

### Comments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/comments/product/<id>/` | Get product comments |
| POST | `/comments/` | Create comment |
| DELETE | `/comments/<id>/` | Delete comment |

## Database Models

### User (Accounts)
- Custom user with email authentication
- Fields: email, password, username (optional), first_name, last_name
- Relationships: Orders, Comments, Addresses

### UserAddress
- Store user delivery addresses
- Fields: user, address, zip_code

### Category (Shop)
- Product categories
- Fields: name, image

### Product (Shop)
- Individual products
- Fields: name, category, image, description, price, stock, discount, is_exist, slug, date_added
- Properties: is_offered, offered_price

### ProductImage (Shop)
- Additional product images
- Fields: product, image

### Order
- Customer orders
- Fields: user, address, zip_code, total_amount, status, created_at, payed_at, shipped_at, order_id
- Status choices: Pending, Payed, Processing, Shipped
- Relationships: OrderItems, Transaction

### OrderItem
- Individual items in an order
- Fields: order, product, quantity, price

### Transaction (Payment)
- Payment transactions
- Fields: order, amount, ref_id, authority_id, transaction_status, created_at
- Status choices: PENDING, SUCCESS, FAIL

### Comment
- Product reviews/comments
- Fields: user, product, content, rating, created_at

---

**Contact**: mohammad.javad.d3v@gmail.com  
**License**: BSD License