import requests
import json

BASE_URL = "http://localhost:5000/api"

def test_api():
    """Test the API endpoints"""
    
    print("Testing RESTful API...")
    print("=" * 50)
    
    # Test 1: Get customers with pagination
    print("1. Testing GET /api/customers")
    try:
        response = requests.get(f"{BASE_URL}/customers?page=1&per_page=5")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Total customers: {data['pagination']['total_count']}")
            print(f"Customers returned: {len(data['customers'])}")
            print("✅ Customers endpoint working!")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Connection error: {e}")
    
    print("\n" + "-" * 30)
    
    # Test 2: Get specific customer details
    print("2. Testing GET /api/customers/1")
    try:
        response = requests.get(f"{BASE_URL}/customers/1")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            customer = data['customer']
            print(f"Customer: {customer['first_name']} {customer['last_name']}")
            print(f"Order count: {customer['order_count']}")
            print("✅ Customer details endpoint working!")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Connection error: {e}")
    
    print("\n" + "-" * 30)
    
    # Test 3: Get customer orders
    print("3. Testing GET /api/customers/1/orders")
    try:
        response = requests.get(f"{BASE_URL}/customers/1/orders")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Total orders for customer: {data['total_orders']}")
            print("✅ Customer orders endpoint working!")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Connection error: {e}")
    
    print("\n" + "-" * 30)
    
    # Test 4: Get statistics
    print("4. Testing GET /api/statistics")
    try:
        response = requests.get(f"{BASE_URL}/statistics")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            stats = data['statistics']
            print(f"Total orders: {stats['total_orders']}")
            print(f"Unique customers: {stats['unique_customers']}")
            print(f"Average items per order: {stats['avg_items_per_order']:.2f}")
            print("✅ Statistics endpoint working!")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Connection error: {e}")
    
    print("\n" + "-" * 30)
    
    # Test 5: Test error handling
    print("5. Testing error handling - Customer not found")
    try:
        response = requests.get(f"{BASE_URL}/customers/99999")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 404:
            print("✅ Error handling working correctly!")
        else:
            print(f"❌ Expected 404, got {response.status_code}")
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    test_api() 