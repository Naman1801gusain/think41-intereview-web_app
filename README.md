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

---

## 🎨 **MILESTONE 4: CUSTOMER MANAGEMENT FRONTEND**

### 📁 **FILES CREATED FOR MILESTONE 4:**

#### **1. `frontend/index.html`** 
**What it does:**
- Main HTML page for the customer management frontend
- Beautiful UI with Bootstrap 5 styling
- Search bar, statistics cards, customer grid
- Customer details modal
- Responsive design for all devices

#### **2. `frontend/app.js`**
**What it does:**
- JavaScript application that handles all functionality
- Connects to your API at `http://localhost:5000/api`
- Loads customers with pagination
- Real-time search functionality
- Shows customer details and order history
- Handles loading states and errors

#### **3. `frontend/README.md`**
**What it does:**
- Documentation for the frontend application
- Setup instructions
- Feature descriptions
- Technical details

#### **4. `serve_frontend.py`**
**What it does:**
- Simple HTTP server to serve the frontend
- Runs on port 3000
- Opens browser automatically
- Handles CORS for API communication

### 🎯 **WHAT EACH FILE ACCOMPLISHES:**

#### **`frontend/index.html` - The User Interface**
- ✅ **Customer List View**: Cards showing customer info
- ✅ **Search Bar**: Real-time search input
- ✅ **Statistics Dashboard**: Overview cards
- ✅ **Responsive Design**: Works on mobile/desktop

#### **`frontend/app.js` - The Brain**
- ✅ **API Integration**: Fetches data from your Flask API
- ✅ **Search Functionality**: Filters customers by name/email
- ✅ **Customer Details**: Shows full customer info in modal
- ✅ **Order History**: Displays customer orders
- ✅ **Error Handling**: Shows error messages
- ✅ **Loading States**: Spinner during API calls

#### **`serve_frontend.py` - The Server**
- ✅ **Serves HTML/CSS/JS files**
- ✅ **Handles CORS** for API communication
- ✅ **Opens browser** automatically
- ✅ **Easy to run** with one command

### 🔄 **HOW THEY WORK TOGETHER:**

1. **`serve_frontend.py`** starts the server
2. **`frontend/index.html`** loads in browser
3. **`frontend/app.js`** connects to your API
4. **Your Flask API** (`app.py`) provides the data
5. **Database** (`ecommerce.db`) stores the data

**Complete flow: Frontend ↔ API ↔ Database** 🎉

### ✅ **MILESTONE 4 REQUIREMENTS MET:**

- ✅ **Customer List View**: Display all customers in card format with pagination
- ✅ **Search Functionality**: Real-time search by name or email
- ✅ **Customer Summary**: Show customer name, email, and order count
- ✅ **API Integration**: Fetch data from your Customer API endpoints
- ✅ **Basic Styling**: Modern UI with Bootstrap 5 and custom CSS

### 🚀 **SETUP INSTRUCTIONS:**

#### **1. Start the Backend API**
```bash
python app.py
```

#### **2. Start the Frontend Server**
```bash
python serve_frontend.py
```

#### **3. Access the Application**
Open your browser and go to: `http://localhost:3000/frontend/index.html`

### 🎯 **ADDITIONAL FEATURES IMPLEMENTED:**

- **Statistics Dashboard**: Overview of key metrics
- **Customer Details Modal**: Click any customer for full details
- **Order History**: View customer orders within the modal
- **API Status Indicator**: Real-time connection status
- **Loading States**: Smooth loading indicators
- **Error Handling**: Graceful error messages
- **Responsive Design**: Works on all devices

**These 4 files create a complete, professional customer management system that meets all Milestone 4 requirements!** 🎉 