# LinkVault

LinkVault is a web application built using Flask that allows users to store and categorize useful links. Users can log in, create categories, and save links under different categories for easy access.

## Features

- User Registration and Authentication
- Category Creation
- Link Storage and Categorization
- User-specific Data Management

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/linuxer77/LinkVault.git
   cd LinkVault
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

### Running the Application

1. Set the environment variables:

   ```bash
   export FLASK_APP=main.py
   export FLASK_ENV=development
   ```

2. Run the Flask development server:

   ```bash
   flask run
   ```

3. Open your web browser and go to `http://127.0.0.1:5000/`.

## Project Structure

- `main.py`: The main entry point of the application.
- `app/`: Contains the Flask application instance.
- `app/templates/`: HTML templates.
- `app/forms.py`: Form classes for user registration, login, and category creation.
- `app/models.py`: Database models for User, Category, and Link.
- `app/routes.py`: Route definitions for handling web requests.
- `app/static/`: Static files (CSS, JS, images).

## Usage

1. **Register an Account:**
   - Navigate to `/register`.
   - Fill in the registration form and submit.

2. **Log In:**
   - Navigate to `/login`.
   - Fill in your credentials and log in.

3. **Create a Category:**
   - After logging in, navigate to `/create_category`.
   - Fill in the category name and submit.

4. **Add Links:**
   - After creating a category, you will be redirected to the category page.
   - Add links related to the category.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

For any questions or inquiries, please contact [linuxer77](https://github.com/linuxer77).
