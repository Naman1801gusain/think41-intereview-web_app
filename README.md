# E-commerce RESTful API

A Flask-based RESTful API that provides customer data and order statistics from an SQLite database.

## Features

- ✅ List all customers with pagination
- ✅ Get specific customer details including order count
- ✅ Get customer orders
- ✅ Get basic order statistics
- ✅ Proper JSON response format
- ✅ Error handling (customer not found, invalid ID, etc.)
- ✅ Appropriate HTTP status codes
- ✅ CORS headers for frontend integration

## API Endpoints

### 1. List All Customers
```
GET /api/customers?page=1&per_page=10
```
**Parameters:**
- `page` (optional): Page number (default: 1)
- `per_page` (optional): Items per page (default: 10, max: 100)

**Response:**
```json
{
  "customers": [...],
  "pagination": {
    "page": 1,
    "per_page": 10,
    "total_count": 1000,
    "total_pages": 100,
    "has_next": true,
    "has_prev": false
  }
}
```

### 2. Get Customer Details
```
GET /api/customers/{customer_id}
```
**Response:**
```json
{
  "customer": {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "age": 30,
    "gender": "Male",
    "state": "CA",
    "city": "Los Angeles",
    "country": "USA",
    "created_at": "2023-01-01",
    "order_count": 5
  }
}
```

### 3. Get Customer Orders
```
GET /api/customers/{customer_id}/orders
```
**Response:**
```json
{
  "customer_id": 1,
  "orders": [...],
  "total_orders": 5
}
```

### 4. Get Statistics
```
GET /api/statistics
```
**Response:**
```json
{
  "statistics": {
    "unique_customers": 500,
    "total_orders": 1500,
    "avg_items_per_order": 2.5,
    "delivered_orders": 1200,
    "returned_orders": 50
  }
}
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Database (if not already done)
```bash
python setup_database.py
python load_data.py
python verify_data.py
```

### 3. Run the API
```bash
python app.py
```

The API will be available at `http://localhost:5000`

### 4. Test the API
```bash
python test_api.py
```

## Testing with curl

### List customers:
```bash
curl "http://localhost:5000/api/customers?page=1&per_page=5"
```

### Get customer details:
```bash
curl "http://localhost:5000/api/customers/1"
```

### Get customer orders:
```bash
curl "http://localhost:5000/api/customers/1/orders"
```

### Get statistics:
```bash
curl "http://localhost:5000/api/statistics"
```

## Error Handling

The API handles various error cases:

- **404 Not Found**: Customer not found
- **400 Bad Request**: Invalid pagination parameters
- **500 Internal Server Error**: Database or server errors
- **405 Method Not Allowed**: Wrong HTTP method

## HTTP Status Codes

- `200 OK`: Successful request
- `400 Bad Request`: Invalid parameters
- `404 Not Found`: Resource not found
- `405 Method Not Allowed`: Wrong HTTP method
- `500 Internal Server Error`: Server error

## Database Schema

### Users Table
- `id` (PRIMARY KEY)
- `first_name`, `last_name`, `email`
- `age`, `gender`
- `state`, `city`, `country`
- `created_at`

### Orders Table
- `order_id` (PRIMARY KEY)
- `user_id` (FOREIGN KEY)
- `status`, `num_of_item`
- `created_at`, `shipped_at`, `delivered_at`, `returned_at` 