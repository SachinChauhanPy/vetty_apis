# Vetty APIs

This project is a Django-based application that provides APIs for interacting with the cryptocurrency market. The APIs include functionality for user authentication, API key generation, listing coins, retrieving coin categories, fetching specific coin market data, and monitoring the health of third-party integrations.

---

## Features

- **Authentication**:
  - User login and logout.
  - API Key generation and management for secure access to APIs.
- **API Endpoints**:
  - List all coins with their IDs.
  - Retrieve coin categories with pagination.
  - Fetch specific coin market data in CAD currency.
  - Health check for third-party API integration (CoinGecko).
- **Third-Party Integration**:
  - Uses the CoinGecko API to fetch real-time cryptocurrency data.
- **Frontend**:
  - Integrated with Bootstrap 5.3 for styling.
  - Notyf for toast notifications.
  - FontAwesome icons for enhanced UI.
- **Technology Stack**:
  - Python 3.12.4
  - Django 5.1.4
  - Django REST Framework (DRF)
  - DRF-YASG for API documentation.

---

## Table of Contents

1. [Installation](#installation)
2. [Directory Structure](#directory-structure)
3. [Endpoints](#endpoints)
4. [Usage](#usage)
5. [Contribution](#contribution)
6. [License](#license)

---

### **Prerequisites**

Ensure you have the following installed on your system:

- **Python**: Version 3.12.4
- **Database**: Any Django-supported database (SQLite by default)
- **Virtual Environment Tool**: `venv` or `virtualenv`
- **pip**: Python package manager

---

### **Installation Steps**

1. **Clone the Repository**:
   Clone the project repository to your local machine using the following command:
   ```bash
   git clone https://github.com/SachinChauhanPy/vetty_apis.git
   cd vetty_apis
   ```

2. **Set Up a Virtual Environment**:
   Create and activate a virtual environment for the project:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Project Dependencies**:
   Install all required Python packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory of your project and add the required environment variables for example:
   ```plaintext
    DEBUG=True
    SECRET_KEY=django-insecure-i)vc#nh!u6a84g66ivnw+8t8*dah9f@b43bxeq@nv*@0vd8iv%
    COINGECKO_API_KEY=CG-ccv6EEZErAeUBG9oaQuP5o8M
    GECKO_URL=https://api.coingecko.com/api/v3/
    API_VERSION=v1
   ```

5. **Apply Database Migrations**:
   Run the Django migrations to set up the database schema:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**:
   Create an admin user to access the Django Admin interface:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   Start the Django development server to serve the application:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   Open a web browser and go to:
   ```plaintext
   http://127.0.0.1:8000/
   ```

## Directory Structure
```
<vetty_apis>/
├── templates/                 # HTML templates for rendering pages
│   ├── accounts/              # Account-specific templates
│   │   └── login.html         # Login page template
│   ├── commons/               # Shared templates across the project
│       ├── base.html          # Base HTML structure for all pages
│       ├── color-modes.html   # Template for handling color modes
│       └── navbar.html        # Navigation bar template
│   ├── crypto/
│       └── dashboard.html     # Dashboard page for api-keys
├── accounts/                  # User and authentication functionality
│   ├── apis/
│   │   ├── v1/
│   │   │   ├── urls.py        # API routes for account-specific actions
│   │   │   ├── views.py       # API views for account management
│   ├── migrations/            # Database migration files
│   ├── models.py              # User-related models
│   ├── tests.py               # Unit tests for accounts-related features
│   ├── urls.py                # URL configuration for accounts
│   └── views.py               # Views for account-specific actions
├── crypto/                    # Handles cryptocurrency-related APIs
│   ├── apis/
│   │   ├── v1/
│   │   │   ├── urls.py        # API routes for cryptocurrency features
│   │   │   ├── views.py       # API views for interacting with CoinGecko
│   ├── migrations/            # Database migration files
│   ├── models.py              # Models for cryptocurrency-related data
│   ├── tests.py               # Unit tests for crypto APIs
│   ├── urls.py                # URL configuration for crypto-related pages
│   └── views.py               # Views for cryptocurrency-specific actions
├── vetty_apis/                # Main project settings and configurations
│   ├── settings.py            # Django project settings
│   ├── urls.py                # Root URL routing for the project
│   ├── wsgi.py                # WSGI configuration for deployment
├── assets/                    # Static assets (CSS, JavaScript, etc.)
├── .env                       # Environment variables for configuration
├── .gitignore                 # Git ignore file
├── db.sqlite3                 # SQLite database file
├── manage.py                  # Django's management script
├── requirements.txt           # Python dependencies for the project
└── README.md                  # Project documentation
```
---

### Base URL
`http://127.0.0.1:8000/`

### Accounts APIs

| Method | Endpoint                 | Description                             | Auth Required |
|--------|---------------------------|-----------------------------------------|---------------|
| POST   | `/api/accounts/api-key/`  | Generate an API key for authenticated users. | Yes           |

### Crypto APIs

| Method | Endpoint                             | Description                                         | Auth Required |
|--------|--------------------------------------|-----------------------------------------------------|---------------|
| GET    | `/api/crypto/coins/list/`            | List all coins with their IDs and pagination.      | Yes |
| GET    | `/api/crypto/coins/categories/`      | List coin categories with pagination.              | Yes |
| GET    | `/api/crypto/coins/<coin_id>/`       | Fetch market data for a specific coin (in CAD).    | Yes |
| GET    | `/api/crypto/health/`                | Check the health of the CoinGecko API.             | Yes |

---

## Usage

### Authentication
- To authenticate requests, use the generated API key.
- Include the API key in the `Authorization` header:
  ```http
  Authorization: Api-Key <your-api-key>
  ```

### Example Requests
#### **1. Fetch All Coins**
```bash
curl -X GET "http://127.0.0.1:8000/api/crypto/coins/list/" \
-H "Authorization: Api-Key <your-api-key>"
```

#### **2. Fetch Specific Coin**
```bash
curl -X GET "http://127.0.0.1:8000/api/crypto/coins/bitcoin/" \
-H "Authorization: Api-Key <your-api-key>"
```

#### **3. Health Check**
```bash
curl -X GET "http://127.0.0.1:8000/api/crypto/health/"
```

---
Here’s the **test case running guide** formatted for your `README.md` file:

---

## Running Test Cases

This project includes automated test cases to ensure the correctness and reliability of its functionalities. Follow these steps to run the test suite:

### Prerequisites

- Ensure that the project is set up correctly by following the installation instructions.
- Make sure you are in the project directory where `manage.py` is located.

---

### Steps to Run Tests

1. **Activate the Virtual Environment**:
   Before running tests, activate the Python virtual environment:
   ```bash
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

2. **Run All Tests**:
   To run all the test cases across the project, execute:
   ```bash
   python manage.py test
   ```

3. **Run Tests for a Specific App**:
   If you want to test a specific app (e.g., `accounts` or `crypto`), use:
   ```bash
   python manage.py test <app-name>
   ```
   Example:
   ```bash
   python manage.py test accounts
   python manage.py test crypto
   ```

4. **Run a Specific Test Case**:
   To run an individual test case or method, provide the full path to the test class or method:
   ```bash
   python manage.py test <app-name>.tests.<TestClass>.<test_method>
   ```
   Example:
   ```bash
   python manage.py test crypto.tests.CoinListViewTest.test_coin_list_with_api_key
   ```

---

### Test Output

When you run tests, Django will create a temporary test database and execute the tests. Below are examples of successful and failed test outputs:

- **Successful Tests**:
   ```
   Creating test database for alias 'default'...
   System check identified no issues (0 silenced).
   ...
   ----------------------------------------------------------------------
   Ran 10 tests in 1.234s

   OK
   Destroying test database for alias 'default'...
   ```

- **Failed Tests**:
   ```
   Creating test database for alias 'default'...
   System check identified no issues (0 silenced).
   F
   ======================================================================
   FAIL: test_example (crypto.tests.ExampleTestCase.test_example)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
       ...
   AssertionError: Expected X but got Y
   ----------------------------------------------------------------------

   Ran 10 tests in 1.345s

   FAILED (failures=1)
   Destroying test database for alias 'default'...
   ```

