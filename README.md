# DRF Authentication Project

This is a Django project with Django REST Framework (DRF) for implementing authentication using email and password.

## Installation

1. **Create a virtual environment and activate it:**

   For Linux/Mac:
   ```bash
   virtualenv myenv
   source myenv/bin/activate
   ```
   For Window:
   ```bash
   virtualenv myenv
   myenv\Scripts\Activate.ps1
   ```
2. Clone the repository:

    ```bash
    git clone https://github.com/aditya2sahu/WolfPackTask.git
    cd WolfPackTask
    ```
4. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage
1. Start the development server:
```bash
python manage.py runserver
```
3. Create a superuser:
```bash
python manage.py createsuperuser
```
5. Open your web browser and go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to access the admin panel.

## Endpoints

- **Sign Up:** [http://127.0.0.1:8000/sing_up](http://127.0.0.1:8000/sing_up)  
  Use this endpoint to sign up for a new account.

- **Login:** [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login)  
  Use this endpoint to obtain JWT tokens. Send a POST request with email and password.

- **Refresh Token:** [http://127.0.0.1:8000/refresh_token](http://127.0.0.1:8000/refresh_token)  
  Use this endpoint to refresh JWT tokens. Send a POST request with a refresh token.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

