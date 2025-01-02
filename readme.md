# Checklist Web Application

## Overview
The Checklist Web Application is a user-friendly platform that allows users to manage their tasks efficiently. Users can add tasks, mark them as complete, view completed tasks, and organize tasks into categories. This application incorporates authentication to secure user data.

## Features
- **User Authentication**:
  - Registration and login functionality.
  - Redirect users to the Add Item page after logging in.
  - Restrict access to certain pages (e.g., View Checklist) for logged-in users only.

- **Task Management**:
  - Add new tasks with a title, category, and optional phone number.
  - Mark tasks as complete.
  - View completed tasks with associated details such as creation date, category, and phone number.

- **Dynamic Navigation**:
  - Navbar items are dynamically shown based on the user's authentication status.

## Technologies Used
- **Backend**: Django 5.1.4
- **Frontend**: HTML, CSS, Bootstrap (for styling and responsiveness)
- **Database**: SQLite (default Django database)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/checklist-web-app.git
   cd checklist-web-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv myvenv
   source myvenv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage
### Authentication
- Register or log in to access task management features.
- Logged-in users are redirected to the Add Item page upon successful login.

### Task Management
1. **Add a Task**:
   - Navigate to the Add Item page.
   - Fill in the task details (title, category, phone number).
   - Submit the form to add the task.

2. **View and Manage Tasks**:
   - On the Add Item page, view all active tasks.
   - Mark tasks as complete or delete them as needed.

3. **View Completed Tasks**:
   - Navigate to the View Checklist page to see a list of completed tasks, including their creation date, category, and phone number.

### Navbar Visibility
- The "View Checklist" link appears only when the user is logged in.
- The "Login" and "Register" links are hidden when the user is authenticated.

## Project Structure
```
checklist-web-app/
├── checklist/
│   ├── migrations/       # Database migrations
│   ├── templates/       # HTML templates
│   ├── static/          # Static files (CSS, JS, images)
│   └── views.py         # View functions
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Key Files
- **`models.py`**: Defines the data models for users and tasks.
- **`views.py`**: Contains logic for handling requests and rendering templates.
- **`urls.py`**: Maps URLs to view functions.
- **`templates/`**:
  - `add_item.html`: Page for adding and viewing active tasks.
  - `view_checklist.html`: Page for viewing completed tasks.

## Future Enhancements
- Add search and filter functionality for tasks.
- Enable task editing.
- Integrate user-specific notifications for upcoming deadlines.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/) for styling.

---

Thank you for using the Checklist Web Application! If you encounter any issues or have feature requests, feel free to open an issue on the repository.

