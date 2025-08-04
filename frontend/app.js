// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';
let currentPage = 1;
let currentSearch = '';
let allCustomers = [];
let filteredCustomers = [];

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    loadStatistics();
    loadCustomers();
    setupSearchListener();
    checkApiStatus();
});

// Check API connection status
async function checkApiStatus() {
    try {
        const response = await fetch(`${API_BASE_URL}/statistics`);
        const statusElement = document.getElementById('api-status');
        if (response.ok) {
            statusElement.textContent = 'Connected';
            statusElement.className = 'badge bg-success';
        } else {
            statusElement.textContent = 'Error';
            statusElement.className = 'badge bg-danger';
        }
    } catch (error) {
        const statusElement = document.getElementById('api-status');
        statusElement.textContent = 'Disconnected';
        statusElement.className = 'badge bg-danger';
    }
}

// Load statistics
async function loadStatistics() {
    try {
        const response = await fetch(`${API_BASE_URL}/statistics`);
        const data = await response.json();
        const stats = data.statistics;
        
        const statsContainer = document.getElementById('statsContainer');
        statsContainer.innerHTML = `
            <div class="col-md-3 mb-3">
                <div class="card stats-card">
                    <div class="card-body text-center">
                        <i class="fas fa-users fa-2x mb-2"></i>
                        <h5 class="card-title">${stats.unique_customers.toLocaleString()}</h5>
                        <p class="card-text">Active Customers</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3 mb-3">
                <div class="card stats-card">
                    <div class="card-body text-center">
                        <i class="fas fa-shopping-cart fa-2x mb-2"></i>
                        <h5 class="card-title">${stats.total_orders.toLocaleString()}</h5>
                        <p class="card-text">Total Orders</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3 mb-3">
                <div class="card stats-card">
                    <div class="card-body text-center">
                        <i class="fas fa-box fa-2x mb-2"></i>
                        <h5 class="card-title">${stats.avg_items_per_order.toFixed(1)}</h5>
                        <p class="card-text">Avg Items/Order</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3 mb-3">
                <div class="card stats-card">
                    <div class="card-body text-center">
                        <i class="fas fa-check-circle fa-2x mb-2"></i>
                        <h5 class="card-title">${stats.delivered_orders.toLocaleString()}</h5>
                        <p class="card-text">Delivered Orders</p>
                    </div>
                </div>
            </div>
        `;
    } catch (error) {
        showError('Failed to load statistics');
    }
}

// Load customers with pagination
async function loadCustomers(page = 1, search = '') {
    showLoading(true);
    hideError();
    
    try {
        const url = `${API_BASE_URL}/customers?page=${page}&per_page=12`;
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        allCustomers = data.customers;
        
        if (search) {
            filterCustomers(search);
        } else {
            filteredCustomers = allCustomers;
        }
        
        displayCustomers();
        displayPagination(data.pagination);
        showLoading(false);
        
    } catch (error) {
        showError('Failed to load customers: ' + error.message);
        showLoading(false);
    }
}

// Filter customers based on search term
function filterCustomers(searchTerm) {
    const term = searchTerm.toLowerCase();
    filteredCustomers = allCustomers.filter(customer => 
        customer.first_name.toLowerCase().includes(term) ||
        customer.last_name.toLowerCase().includes(term) ||
        customer.email.toLowerCase().includes(term)
    );
}

// Display customers in cards
function displayCustomers() {
    const container = document.getElementById('customersContainer');
    
    if (filteredCustomers.length === 0) {
        container.innerHTML = `
            <div class="col-12 text-center">
                <div class="alert alert-info">
                    <i class="fas fa-info-circle me-2"></i>
                    No customers found matching your search criteria.
                </div>
            </div>
        `;
        return;
    }
    
    container.innerHTML = filteredCustomers.map(customer => `
        <div class="col-md-6 col-lg-4 mb-4">
            <div class="card customer-card h-100" onclick="showCustomerDetails(${customer.id})">
                <div class="card-body">
                    <div class="d-flex align-items-center mb-3">
                        <div class="customer-avatar me-3">
                            ${getInitials(customer.first_name, customer.last_name)}
                        </div>
                        <div>
                            <h6 class="card-title mb-1">${customer.first_name} ${customer.last_name}</h6>
                            <small class="text-muted">${customer.email}</small>
                        </div>
                    </div>
                    <div class="row text-center">
                        <div class="col-6">
                            <small class="text-muted">Age</small>
                            <div class="fw-bold">${customer.age}</div>
                        </div>
                        <div class="col-6">
                            <small class="text-muted">Location</small>
                            <div class="fw-bold">${customer.city}, ${customer.state}</div>
                        </div>
                    </div>
                    <div class="text-center mt-3">
                        <span class="order-badge">
                            <i class="fas fa-shopping-cart me-1"></i>
                            ${customer.order_count || 0} orders
                        </span>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

// Display pagination controls
function displayPagination(pagination) {
    const container = document.getElementById('paginationContainer');
    
    if (pagination.total_pages <= 1) {
        container.innerHTML = '';
        return;
    }
    
    const { page, total_pages, has_next, has_prev } = pagination;
    
    container.innerHTML = `
        <button class="btn btn-outline-primary" ${!has_prev ? 'disabled' : ''} 
                onclick="changePage(${page - 1})">
            <i class="fas fa-chevron-left"></i> Previous
        </button>
        
        <span class="mx-3">
            Page ${page} of ${total_pages}
        </span>
        
        <button class="btn btn-outline-primary" ${!has_next ? 'disabled' : ''} 
                onclick="changePage(${page + 1})">
            Next <i class="fas fa-chevron-right"></i>
        </button>
    `;
}

// Change page
function changePage(page) {
    currentPage = page;
    loadCustomers(page, currentSearch);
}

// Show customer details in modal
async function showCustomerDetails(customerId) {
    try {
        const response = await fetch(`${API_BASE_URL}/customers/${customerId}`);
        const data = await response.json();
        const customer = data.customer;
        
        const modalBody = document.getElementById('customerModalBody');
        modalBody.innerHTML = `
            <div class="row">
                <div class="col-md-4 text-center">
                    <div class="customer-avatar mx-auto mb-3" style="width: 100px; height: 100px; font-size: 2rem;">
                        ${getInitials(customer.first_name, customer.last_name)}
                    </div>
                    <h5>${customer.first_name} ${customer.last_name}</h5>
                    <p class="text-muted">${customer.email}</p>
                </div>
                <div class="col-md-8">
                    <div class="row">
                        <div class="col-6 mb-3">
                            <strong>Age:</strong> ${customer.age}
                        </div>
                        <div class="col-6 mb-3">
                            <strong>Gender:</strong> ${customer.gender}
                        </div>
                        <div class="col-6 mb-3">
                            <strong>City:</strong> ${customer.city}
                        </div>
                        <div class="col-6 mb-3">
                            <strong>State:</strong> ${customer.state}
                        </div>
                        <div class="col-6 mb-3">
                            <strong>Country:</strong> ${customer.country}
                        </div>
                        <div class="col-6 mb-3">
                            <strong>Order Count:</strong> 
                            <span class="order-badge">${customer.order_count}</span>
                        </div>
                        <div class="col-12 mb-3">
                            <strong>Created:</strong> ${new Date(customer.created_at).toLocaleDateString()}
                        </div>
                    </div>
                    <button class="btn btn-primary" onclick="loadCustomerOrders(${customer.id})">
                        <i class="fas fa-shopping-cart me-2"></i>
                        View Orders
                    </button>
                </div>
            </div>
            <div id="ordersContainer" class="mt-4"></div>
        `;
        
        const modal = new bootstrap.Modal(document.getElementById('customerModal'));
        modal.show();
        
    } catch (error) {
        showError('Failed to load customer details');
    }
}

// Load customer orders
async function loadCustomerOrders(customerId) {
    try {
        const response = await fetch(`${API_BASE_URL}/customers/${customerId}/orders`);
        const data = await response.json();
        
        const ordersContainer = document.getElementById('ordersContainer');
        
        if (data.orders.length === 0) {
            ordersContainer.innerHTML = `
                <div class="alert alert-info">
                    <i class="fas fa-info-circle me-2"></i>
                    No orders found for this customer.
                </div>
            `;
            return;
        }
        
        ordersContainer.innerHTML = `
            <h6><i class="fas fa-shopping-cart me-2"></i>Customer Orders (${data.total_orders})</h6>
            <div class="table-responsive">
                <table class="table table-sm">
                    <thead>
                        <tr>
                            <th>Order ID</th>
                            <th>Status</th>
                            <th>Items</th>
                            <th>Created</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${data.orders.map(order => `
                            <tr>
                                <td>#${order.order_id}</td>
                                <td><span class="badge bg-${getStatusColor(order.status)}">${order.status}</span></td>
                                <td>${order.num_of_item}</td>
                                <td>${new Date(order.created_at).toLocaleDateString()}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;
        
    } catch (error) {
        document.getElementById('ordersContainer').innerHTML = `
            <div class="alert alert-danger">
                <i class="fas fa-exclamation-triangle me-2"></i>
                Failed to load orders.
            </div>
        `;
    }
}

// Setup search functionality
function setupSearchListener() {
    const searchInput = document.getElementById('searchInput');
    let searchTimeout;
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            currentSearch = this.value;
            if (currentSearch) {
                filterCustomers(currentSearch);
                displayCustomers();
            } else {
                filteredCustomers = allCustomers;
                displayCustomers();
            }
        }, 300);
    });
}

// Clear search
function clearSearch() {
    document.getElementById('searchInput').value = '';
    currentSearch = '';
    filteredCustomers = allCustomers;
    displayCustomers();
}

// Utility functions
function getInitials(firstName, lastName) {
    return (firstName.charAt(0) + lastName.charAt(0)).toUpperCase();
}

function getStatusColor(status) {
    const colors = {
        'delivered': 'success',
        'shipped': 'primary',
        'processing': 'warning',
        'returned': 'danger',
        'cancelled': 'secondary'
    };
    return colors[status.toLowerCase()] || 'secondary';
}

function showLoading(show) {
    document.getElementById('loadingSpinner').style.display = show ? 'block' : 'none';
}

function showError(message) {
    const errorElement = document.getElementById('errorMessage');
    errorElement.textContent = message;
    errorElement.style.display = 'block';
}

function hideError() {
    document.getElementById('errorMessage').style.display = 'none';
} 