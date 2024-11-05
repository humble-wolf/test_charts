# Test Charts Project

This project is a Django application designed for rendering charts and includes a REST API for retrieving chart data. The application supports user authentication and utilizes D3.js for data visualization.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Install System Dependencies](#install-system-dependencies)
- [Setting Up the Project](#setting-up-the-project)
- [Usage](#usage)
- [Running Tests](#running-tests)

## Features

- User authentication with optional email verification
- Interactive chart rendering using D3.js
- REST API for accessing chart data
- Clean and organized codebase

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python**: Version 3.10 or higher
- **PostgreSQL**: Version 13 or higher
- **Python Development Headers**: Install via `python3-dev`
- **PostgreSQL Development Files**: Install via `libpq-dev`

## Install System Dependencies

Run the following commands to install the necessary system packages:

```bash
sudo apt install python3-dev
sudo apt install libpq-dev
```

### Setting Up the Project
1. **Clone the Repository**

    ```bash
    git clone https://github.com/humble-wolf/test_charts.git
    cd test_charts
    ```

2. **Install Python Virtual Environment**

   If you don't have `venv` installed, you can install it with:

    ```bash
    sudo apt install python3-venv
    ```

3. **Create and Activate a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install Python Dependencies**

    Install the required Python packages from `requirements/local.txt`:

    ```bash
    pip3 install -r requirements/local.txt
    ```

5. **Run Database Migrations**

    Apply the necessary migrations to set up the database schema:

    ```bash
    python3 manage.py migrate
    ```

6. **Run the Development Server**

    Start the Django development server:

    ```bash
    python3 manage.py runserver
    ```
## Usage

Once the server is running, you can access the application at http://127.0.0.1:8000/.

## Running Tests
To ensure everything is working correctly, run the test suite with:
```bash
pytest
```