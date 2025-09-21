# 🛍️ Handcraft Store - E-commerce Platform

A Django-based e-commerce website for selling beautiful handcrafted products.

-**Website Name** : Handmade Heaven

## ✨ Features

- **👥 User Authentication**
  - User registration and login
  - Password protection
  - User profiles

- **🛒 Shopping Experience**
  - Product catalog with categories
  - Shopping cart functionality
  - Order management system
  - Order history tracking

- **🎨 Admin Panel**
  - Add/edit/delete products
  - Manage categories
  - View orders and users

- **📱 Responsive Design**
  - Mobile-friendly interface
  - Clean, modern UI
  - Easy navigation
    
| Feature | Status | Description |
|---------|--------|-------------|
| User Auth | ✅ | Login/Register system |
| Products | ✅ | CRUD operations |
| Shopping Cart | ✅ | Add/remove items |
| Orders | ✅ | Order history |
## 🚀 Live Demo

- **Main Store**: [https://handcraft-store-g5te.onrender.com](https://handcraft-store-g5te.onrender.com)

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| **Django** | Backend framework |
| **Python** | Programming language |
| **SQLite** | Development database |
| **HTML/CSS** | Frontend templates |
| **JavaScript** | Interactive elements |
| **Render** | Deployment platform |

## 📦 Installation

### Prerequisites
- Python 3.10+
- pip (Python package manager)
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Chetana1203/handcraft_store.git
   cd handcraft_store
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## 📁 Project Structure

```
handcraft_store/
├── handcraft_store/     # Django project settings
│   ├── settings.py     # Configuration
│   ├── urls.py         # URL routing
│   └── wsgi.py         # WSGI application
├── products/           # Products app
│   ├── models.py       # Database models
│   ├── views.py        # Business logic
│   ├── urls.py         # App URLs
│   └── templates/      # HTML templates
├── accounts/           # Authentication app
│   ├── views.py        # Auth logic
│   └── templates/      # Login/register templates
├── media/              # Uploaded images
├── static/             # CSS, JS, images
├── templates         
├── Procfile
├── render.yaml         # Render File
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🎯 Usage

### For Customers
1. **Browse products** on the home page
2. **Register/Login** to your account
3. **Add items** to your shopping cart
4. **Checkout** to place orders
5. **View order history** in your account

### For Administrators
1. **Access admin panel** at `/admin`
2. **Manage products** and categories
3. **View orders** and customer information
4. **Upload product images** and set prices

## 🌐 Deployment

This project is deployed on **Render.com** with the following configuration:

- **Runtime**: Python 3.10
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate && python create_superuser.py`
- **Start Command**: `gunicorn handcraft_store.wsgi:application`
- **Database**: SQLite (development)


## 📝 License

This project is created for educational purposes as part of a Django learning journey.

## 🙋‍♂️ Support

If you have any questions or issues:

1. Check the [GitHub Issues](https://github.com/Chetana1203/handcraft_store/issues)
2. Create a new issue with details about your problem

