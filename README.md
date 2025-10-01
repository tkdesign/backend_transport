# Transport Management System Api

This repository demonstrates an example implementation of a transport management system API on the Django REST Framework.

## Project Overview

The system manages transport orders and their associated waypoints. It provides REST API endpoints for creating, listing, and retrieving transport orders, each of which can have multiple waypoints (Pickup/Delivery locations).

**Core Models:**
- **Order**: Unique order number, customer name, date
- **Waypoint**: Location address, type (Pickup/Delivery), linked to an order

## Features
- **Create Transport Order**: POST `/api/orders/` (with waypoints)
- **List Orders**: GET `/api/orders/` (with optional filters)
- **Retrieve Order Details**: GET `/api/orders/{order_number}/` (with waypoints)

## API Documentation

The OpenAPI schema is available in [`docs/backend_transport-openapi.yaml`](docs/backend_transport-openapi.yaml). You can view it as raw YAML or use an [online Swagger/OpenAPI viewer](https://editor.swagger.io/) by uploading the file.

### Example API Request
```json
{
  "order_number": "ORD123",
  "customer_name": "John Doe",
  "date": "2025-08-21",
  "waypoints": [
    {"location": "New York", "type": "Pickup"},
    {"location": "Boston", "type": "Delivery"}
  ]
}
```

## Setup Instructions

### Requirements
- Python 3.10+
- Git

### Local Installation
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd backend_transport
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Load sample data:**
   ```sh
   python manage.py loaddata test_data.json
   ```
6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

## Notes
- The api and frontend are separate projects.

## Sample Data
Sample transport orders and waypoints are provided in [`transport/fixtures/test_data.json`](transport/fixtures/test_data.json).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Author: Petr Kovalenko