from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect('ecommerce.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

@app.route('/api/customers', methods=['GET'])
def get_customers():
    """List all customers with pagination"""
    try:
        # Get pagination parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # Validate parameters
        if page < 1:
            return jsonify({'error': 'Page number must be greater than 0'}), 400
        if per_page < 1 or per_page > 100:
            return jsonify({'error': 'Per page must be between 1 and 100'}), 400
        
        offset = (page - 1) * per_page
        
        conn = get_db_connection()
        
        # Get total count for pagination info
        total_count = conn.execute('SELECT COUNT(*) FROM users').fetchone()[0]
        
        # Get customers with pagination
        customers = conn.execute('''
            SELECT id, first_name, last_name, email, age, gender, 
                   state, city, country, created_at
            FROM users 
            ORDER BY id 
            LIMIT ? OFFSET ?
        ''', (per_page, offset)).fetchall()
        
        # Convert to list of dictionaries
        customers_list = []
        for customer in customers:
            customers_list.append(dict(customer))
        
        # Calculate pagination info
        total_pages = (total_count + per_page - 1) // per_page
        
        conn.close()
        
        return jsonify({
            'customers': customers_list,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total_count': total_count,
                'total_pages': total_pages,
                'has_next': page < total_pages,
                'has_prev': page > 1
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/customers/<int:customer_id>', methods=['GET'])
def get_customer_details(customer_id):
    """Get specific customer details including order count"""
    try:
        conn = get_db_connection()
        
        # Get customer details with order count
        customer = conn.execute('''
            SELECT u.id, u.first_name, u.last_name, u.email, u.age, u.gender,
                   u.state, u.city, u.country, u.created_at,
                   COUNT(o.order_id) as order_count
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            WHERE u.id = ?
            GROUP BY u.id
        ''', (customer_id,)).fetchone()
        
        conn.close()
        
        if customer is None:
            return jsonify({'error': 'Customer not found'}), 404
        
        # Convert to dictionary
        customer_dict = dict(customer)
        
        return jsonify({
            'customer': customer_dict
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/customers/<int:customer_id>/orders', methods=['GET'])
def get_customer_orders(customer_id):
    """Get all orders for a specific customer"""
    try:
        conn = get_db_connection()
        
        # First check if customer exists
        customer_exists = conn.execute('SELECT id FROM users WHERE id = ?', (customer_id,)).fetchone()
        if not customer_exists:
            conn.close()
            return jsonify({'error': 'Customer not found'}), 404
        
        # Get orders for the customer
        orders = conn.execute('''
            SELECT order_id, status, created_at, shipped_at, delivered_at, 
                   returned_at, num_of_item
            FROM orders 
            WHERE user_id = ?
            ORDER BY created_at DESC
        ''', (customer_id,)).fetchall()
        
        conn.close()
        
        # Convert to list of dictionaries
        orders_list = []
        for order in orders:
            orders_list.append(dict(order))
        
        return jsonify({
            'customer_id': customer_id,
            'orders': orders_list,
            'total_orders': len(orders_list)
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/orders', methods=['GET'])
def get_all_orders():
    """Get all orders with pagination"""
    try:
        # Get pagination parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # Validate parameters
        if page < 1:
            return jsonify({'error': 'Page number must be greater than 0'}), 400
        if per_page < 1 or per_page > 100:
            return jsonify({'error': 'Per page must be between 1 and 100'}), 400
        
        offset = (page - 1) * per_page
        
        conn = get_db_connection()
        
        # Get total count for pagination info
        total_count = conn.execute('SELECT COUNT(*) FROM orders').fetchone()[0]
        
        # Get orders with customer information
        orders = conn.execute('''
            SELECT o.order_id, o.user_id, o.status, o.created_at, o.shipped_at, 
                   o.delivered_at, o.returned_at, o.num_of_item,
                   u.first_name, u.last_name, u.email
            FROM orders o
            LEFT JOIN users u ON o.user_id = u.id
            ORDER BY o.created_at DESC
            LIMIT ? OFFSET ?
        ''', (per_page, offset)).fetchall()
        
        # Convert to list of dictionaries
        orders_list = []
        for order in orders:
            orders_list.append(dict(order))
        
        # Calculate pagination info
        total_pages = (total_count + per_page - 1) // per_page
        
        conn.close()
        
        return jsonify({
            'orders': orders_list,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total_count': total_count,
                'total_pages': total_pages,
                'has_next': page < total_pages,
                'has_prev': page > 1
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order_details(order_id):
    """Get specific order details"""
    try:
        conn = get_db_connection()
        
        # Get order details with customer information
        order = conn.execute('''
            SELECT o.order_id, o.user_id, o.status, o.created_at, o.shipped_at, 
                   o.delivered_at, o.returned_at, o.num_of_item,
                   u.first_name, u.last_name, u.email
            FROM orders o
            LEFT JOIN users u ON o.user_id = u.id
            WHERE o.order_id = ?
        ''', (order_id,)).fetchone()
        
        conn.close()
        
        if order is None:
            return jsonify({'error': 'Order not found'}), 404
        
        # Convert to dictionary
        order_dict = dict(order)
        
        return jsonify({
            'order': order_dict
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """Get basic order statistics"""
    try:
        conn = get_db_connection()
        
        # Get various statistics
        stats = conn.execute('''
            SELECT 
                COUNT(DISTINCT user_id) as unique_customers,
                COUNT(*) as total_orders,
                AVG(num_of_item) as avg_items_per_order,
                COUNT(CASE WHEN status = 'delivered' THEN 1 END) as delivered_orders,
                COUNT(CASE WHEN status = 'returned' THEN 1 END) as returned_orders
            FROM orders
        ''').fetchone()
        
        conn.close()
        
        return jsonify({
            'statistics': dict(stats)
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 