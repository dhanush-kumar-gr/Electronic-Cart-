# Electronic Cart + - Full-Stack eCommerce Platform

A modern, full-featured eCommerce platform for electronic products built with Flask (Python) and vanilla HTML/CSS/JavaScript.

## Project Structure

```
ECOM+++++/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── config.py           # Configuration settings
│   ├── models.py           # Database models
│   ├── routes/
│   │   ├── auth.py         # Authentication routes
│   │   ├── products.py     # Product routes
│   │   ├── cart.py         # Cart routes
│   │   ├── orders.py       # Order routes
│   │   └── admin.py        # Admin routes
│   ├── utils/
│   │   ├── auth_helper.py  # JWT helpers
│   │   └── validators.py   # Input validators
│   ├── schema.sql          # Database schema
│   ├── seed_data.py        # Sample data seeder
│   └── requirements.txt    # Python dependencies
└── frontend/
    ├── index.html          # Homepage
    ├── product.html        # Product detail page
    ├── cart.html           # Shopping cart
    ├── checkout.html       # Checkout page
    ├── login.html          # Login/Signup page
    ├── orders.html         # Order history
    ├── admin.html          # Admin panel
    ├── css/
    │   ├── style.css       # Main styles
    │   ├── components.css  # Reusable components
    │   └── responsive.css  # Responsive styles
    └── js/
        ├── api.js          # API service layer
        ├── auth.js         # Authentication logic
        ├── cart.js         # Cart management
        ├── products.js     # Product rendering
        ├── checkout.js     # Checkout logic
        └── admin.js        # Admin panel logic
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Linux/Mac
   ```

3. Add Stripe keys to `.env`:
   ```bash
   STRIPE_SECRET_KEY=sk_test_...
   STRIPE_WEBHOOK_SECRET=whsec_...
   FRONTEND_URL=http://localhost:8080
   ```


3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database and seed sample data:
   ```bash
   python seed_data.py
   ```

5. Run the Flask server:
   ```bash
   python app.py
   ```
   The backend will start at `http://localhost:5000`

### Frontend

Open `frontend/index.html` in a browser OR serve with a simple HTTP server:
```bash
cd frontend
python -m http.server 8080
```
Then visit `http://localhost:8080`

## Admin Credentials (Default)
- Email: `admin@electroniccartplus.com`
- Password: `admin123`

## Test User Credentials
- Email: `john@example.com`
- Password: `password123`

## API Documentation

See [API_DOCS.md](API_DOCS.md) for full API documentation.
