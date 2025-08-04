# 🛒 E-commerce RESTful API

A comprehensive Flask-based RESTful API that provides customer data and order statistics from an SQLite database. Built for the Think41 assessment with full CRUD operations and robust error handling.

## 🚀 Features

- ✅ **Customer Management**: List all customers with pagination
- ✅ **Customer Details**: Get specific customer details including order count
- ✅ **Order Management**: Get all orders for a specific customer
- ✅ **Order Details**: Get specific order details with customer information
- ✅ **Statistics**: Get comprehensive order statistics
- ✅ **Pagination**: Efficient pagination for large datasets
- ✅ **Error Handling**: Robust error handling (customer not found, order not found, etc.)
- ✅ **HTTP Status Codes**: Appropriate HTTP status codes for all responses
- ✅ **CORS Support**: CORS headers for frontend integration
- ✅ **JSON Responses**: Proper JSON response format
- ✅ **Database**: SQLite database with 100,000+ customers and 125,000+ orders

## 📋 API Endpoints

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
**Parameters:**
- `customer_id` (required): The ID of the customer to retrieve

**Response:**
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
**Parameters:**
- `customer_id` (required): The ID of the customer whose orders to retrieve

**Response:**
**Response:**
```json
{
  "customer_id": 1,
  "orders": [...],
  "total_orders": 5
}
```

### 4. Get All Orders
```
GET /api/orders?page=1&per_page=10
```
**Parameters:**
- `page` (optional): Page number (default: 1)
- `per_page` (optional): Items per page (default: 10, max: 100)

**Response:**
```json
{
  "orders": [...],
  "pagination": {
    "page": 1,
    "per_page": 10,
    "total_count": 125226,
    "total_pages": 12523,
    "has_next": true,
    "has_prev": false
  }
}
```

### 5. Get Specific Order Details
```
GET /api/orders/{order_id}
```
**Parameters:**
- `order_id` (required): The ID of the order to retrieve

**Response:**
**Response:**
```json
{
  "order": {
    "order_id": 1,
    "user_id": 1,
    "status": "delivered",
    "created_at": "2022-01-15",
    "shipped_at": "2022-01-16",
    "delivered_at": "2022-01-18",
    "returned_at": null,
    "num_of_item": 3,
    "first_name": "Rhonda",
    "last_name": "Potter",
    "email": "rhonda@example.com"
  }
}
```

### 6. Get Statistics
```
GET /api/statistics
```
**Response:**
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

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd think41
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup database**
   ```bash
   python setup_database.py
   python load_data.py
   python verify_data.py
   ```

4. **Run the API**
   ```bash
   python app.py
   ```

5. **Test the API**
   ```bash
   python test_api.py
   ```

The API will be available at `http://localhost:5000`

## 🛠️ Setup Instructions

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

## 🧪 Testing with curl

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

### Get all orders:
```bash
curl "http://localhost:5000/api/orders?page=1&per_page=5"
```

### Get specific order details:
```bash
curl "http://localhost:5000/api/orders/1"
```

### Get statistics:
```bash
curl "http://localhost:5000/api/statistics"
```

## ⚠️ Error Handling

The API handles various error cases with appropriate HTTP status codes:

- **404 Not Found**: Customer not found, Order not found, Endpoint not found
- **400 Bad Request**: Invalid pagination parameters, Invalid request format
- **500 Internal Server Error**: Database or server errors
- **405 Method Not Allowed**: Wrong HTTP method used

## 📊 HTTP Status Codes

- `200 OK`: Successful request
- `400 Bad Request`: Invalid parameters
- `404 Not Found`: Resource not found
- `405 Method Not Allowed`: Wrong HTTP method
- `500 Internal Server Error`: Server error

## 🗄️ Database Schema

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

## 🎯 Current Status

### ✅ **Milestone 3 Complete!**
- **Customer API**: ✅ Fully implemented with pagination
- **Order API**: ✅ Fully implemented with customer relationships
- **Error Handling**: ✅ Comprehensive error handling for all endpoints
- **Testing**: ✅ All 7 test cases passing
- **Documentation**: ✅ Complete API documentation
- **Git Commits**: ✅ Changes committed and pushed to GitHub

### 📊 **Database Statistics**
- **Total Customers**: 100,000
- **Total Orders**: 125,226
- **Unique Customers with Orders**: 80,044
- **Average Items per Order**: 1.45

### 🔧 **API Endpoints Status**
- `GET /api/customers` - ✅ Working
- `GET /api/customers/{id}` - ✅ Working
- `GET /api/customers/{id}/orders` - ✅ Working
- `GET /api/orders` - ✅ Working
- `GET /api/orders/{id}` - ✅ Working
- `GET /api/statistics` - ✅ Working

### 🧪 **Test Results**
```
✅ All 7 test cases passed
✅ Error handling working correctly
✅ Pagination working properly
✅ JSON responses properly formatted
✅ HTTP status codes correct
``` 