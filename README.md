# 🏥 Pharmaቤት Inventory Management System

A comprehensive Django-based inventory management system designed for pharmacies. This system provides robust functionality for managing products, suppliers, sales tracking, and inventory monitoring with an intuitive web interface.

![Dashboard Screenshot]("https://github.com/user-attachments/assets/330e6d96-ac10-4ff2-b2a5-c752594093d7")
<img width="1355" height="643" alt="Dashboard_one" src="https://github.com/user-attachments/assets/330e6d96-ac10-4ff2-b2a5-c752594093d7" />


## 🌟 Features

### 📊 Dashboard & Analytics
- **Overview**: Get instant insights into your inventory status with dynamic statistics
- **Key Metrics Display**: Track total products, suppliers, low stock items, and expiring products
- **Recent Sales Activity**: Monitor recent sales
- **Expiry Alerts**: Displays list of products approaching expiration dates
- **Quick Actions Panel**: Fast access to common operations like adding products or recording sales

### 📦 Product Management
- **Comprehensive Product Catalog**: Manage detailed product information including names, categories, quantities, and expiry dates
- **Category Classification**: Organize products by type (Medicine and Cosmetic)
- **Stock Level Monitoring**: Track current stock, minimum thresholds, and visual indicator for low-stock 
- **Expiry Date Tracking**: Monitor product expiration dates with visual indicators
- **Product Search & Filtering**: Advanced search functionality with category-based filtering
- **Detailed Product Views**: Complete product information including supplier details and stock history

### 🚚 Supplier Management
- **Supplier Directory**: Maintain supplier contact information
- **Supplier-Product Relationships**: Track which suppliers provide which products
- **Contact Management**: Store email addresses and phone numbers
- **Supplier Statistics**: View product counts per supplier

### 💰 Sales & Transaction Management
- **Sales Recording**: Easy-to-use interface for recording product sales
- **Transaction History**: Complete sales history with timestamps and quantities
- **Most Sold Products**: Analytics showing best-selling products
- **Stock Deduction**: Automatic inventory updates when sales are recorded

### 👥 User Management & Authentication
- **Role-Based Access Control**: Admin and Staff user roles with appropriate permissions
- **Secure Authentication**: Email-based login system with password protection
- **Staff Registration**: Admin users can register new staff members
- **User Profile Management**: Manage user accounts and permissions

### 🎨 Modern User Interface
- **Responsive Design**: Optimized for desktop and mobile devices
- **Professional Styling**: Clean, modern interface with intuitive navigation
- **Color-Coded Status Indicators**: Visual cues for stock levels, categories, and alerts
- **Interactive Elements**: Hover effects, smooth transitions, and user-friendly forms

## 🛠️ Technology Stack

- **Backend Framework**: Django 
- **Database**: SQLite for development
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with Bootstrap components
- **Authentication**: Django's built-in authentication system
- **Form Handling**: Django Forms with custom validation

## 📋 Prerequisites

Before installing the Pharmaቤት Inventory Management System, ensure you have the following installed on your system:

- Python
- pip 
- Git 
- Django

## 📱 Functionalities

#### Adding New Products
1. Click on "Add Product" from the dashboard or navigation menu
2. Fill in the product details:
   - Product Name
   - Category (Medicine/Cosmetic)
   - Quantity
   - Minimum Stock Level
   - Expiry Date
   - Select Supplier
3. Click "Add Product" to save

#### Viewing and Managing Products
- Navigate to the "Products" section to view all products
- Use the search bar to find specific products
- Filter products by category or stock status
- Click "View Details" to see comprehensive product information
- Update or delete products using the action buttons

### Managing Suppliers

#### Adding New Suppliers
1. Navigate to "Add Supplier"
2. Enter supplier information:
   - Supplier Name
   - Email Address
   - Phone Number
3. Click "Add Supplier" to save

#### Supplier Management
- View all suppliers in the "Suppliers" section
- Search for specific suppliers
- View supplier details including associated products
- Update supplier information as needed

### Recording Sales

1. Navigate to "Record Sale" or use the quick action button
2. Select the product being sold from the dropdown
3. Enter the quantity sold
4. Click "Record Sale" to complete the transaction

The system will automatically:
- Update the product stock levels
- Record the sale in the transaction history
- Update dashboard statistics

### Monitoring Inventory

#### Dashboard Monitoring
- Check the main dashboard for inventory status
- Monitor low stock alerts and expiring products
- Review recent sales activity

#### Reports and Analytics
- View "Most Sold Products" for sales performance analysis
- Check expiry alerts for products requiring attention
- Monitor supplier and their product distribution

## 📸 Screenshots

### Login Page
![Login Page]("https://github.com/user-attachments/assets/86c6e8fd-cfba-4b52-8e8c-8e33329d26aa")
*Authentication system with email-based login*
<img width="1355" height="648" alt="Login" src="https://github.com/user-attachments/assets/86c6e8fd-cfba-4b52-8e8c-8e33329d26aa" />

### Dashboard Overview
![Dashboard]("https://github.com/user-attachments/assets/330e6d96-ac10-4ff2-b2a5-c752594093d7")
<img width="1355" height="643" alt="Dashboard_one" src="https://github.com/user-attachments/assets/330e6d96-ac10-4ff2-b2a5-c752594093d7" />
![Dashboard 2 : About to expire products list]("https://github.com/user-attachments/assets/1ed3111c-a059-4d11-a28c-4fe200bfba49")
<img width="1338" height="630" alt="Dashboard_two" src="https://github.com/user-attachments/assets/1ed3111c-a059-4d11-a28c-4fe200bfba49" />

*Comprehensive dashboard with real-time statistics and quick actions*

### Products Management
![Products List]("https://github.com/user-attachments/assets/88cd453e-6421-4bcd-83ea-bea20aa93a46")
*Product catalog with search, filtering, and detailed information*
<img width="1351" height="638" alt="products" src="https://github.com/user-attachments/assets/88cd453e-6421-4bcd-83ea-bea20aa93a46" />

### Product Details
![Product Details]("https://github.com/user-attachments/assets/5dcd5931-aefd-4342-9583-172d757f92d8")
*Detailed product view with stock information, supplier details, and expiry tracking*
<img width="1343" height="637" alt="Detail_one" src="https://github.com/user-attachments/assets/5dcd5931-aefd-4342-9583-172d757f92d8" />

### Add Product Form
![Add Product]("https://github.com/user-attachments/assets/6e635d37-a0ae-4dd0-830f-14067037ef8e")
*User-friendly form for adding new products with supplier selection*
<img width="1358" height="633" alt="addProduct" src="https://github.com/user-attachments/assets/6e635d37-a0ae-4dd0-830f-14067037ef8e" />

### Suppliers Management
![Suppliers List]("https://github.com/user-attachments/assets/b7325af3-5569-4494-9d09-d90074cbb359")
*Supplier directory with contact information and product statistics*
<img width="1351" height="641" alt="Suppliers" src="https://github.com/user-attachments/assets/b7325af3-5569-4494-9d09-d90074cbb359" />

### Supplier Details
![Supplier Details]("https://github.com/user-attachments/assets/c3093201-ca22-4092-86f4-0562ed899dd9")
*Comprehensive supplier information with associated products*
<img width="1349" height="641" alt="supplier_detail" src="https://github.com/user-attachments/assets/c3093201-ca22-4092-86f4-0562ed899dd9" />

### Add Supplier Form
![Add Supplier]("https://github.com/user-attachments/assets/2979c04c-64ad-42b9-bd7f-e9572212ae04")
*Simple form for registering new suppliers*
<img width="1358" height="641" alt="addSupplier" src="https://github.com/user-attachments/assets/2979c04c-64ad-42b9-bd7f-e9572212ae04" />

### Sales Recording
![Record Sale]("https://github.com/user-attachments/assets/2201d9c6-7276-489f-9509-b440f701e537")
*Intuitive interface for recording product sales*
<img width="1353" height="643" alt="recordsale" src="https://github.com/user-attachments/assets/2201d9c6-7276-489f-9509-b440f701e537" />

### Most Sold Products
![Most Sold]("https://github.com/user-attachments/assets/5fb8f0d3-8386-4b01-874d-57c018068a3a")
*Analytics view showing best-performing products*
<img width="1359" height="643" alt="mostsold" src="https://github.com/user-attachments/assets/5fb8f0d3-8386-4b01-874d-57c018068a3a" />

### Staff Registration
![Register Staff]("https://github.com/user-attachments/assets/c49ee060-0347-442f-b1d7-ce3cc503a68f")
*Admin interface for adding new staff members*
<img width="1356" height="641" alt="Register" src="https://github.com/user-attachments/assets/c49ee060-0347-442f-b1d7-ce3cc503a68f" />



