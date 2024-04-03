# TIA Blog Submission

## Blog Description:

This blog is built using Flask, a Python web framework, designed to facilitate the creation, updating, and deletion of blog posts. It incorporates features for user authentication and authorization, allowing for secure management of profiles.

## Blog Features:

- **Create, Update, Delete:** Easily manage blog posts with CRUD operations.
- **Authentication and Authorization:** Secure user access with authentication mechanisms and role-based authorization.
- **Manage Profiles:** Users can maintain their profiles with customizable information.

## Installation and Setup:

1. **Run on Linux:**
    - Ensure you have a Linux environment set up.

2. **Install Python 3.12 or above:**
    - Download and install Python from the official website or package manager.

3. **Create Virtual Environment:**
    - Create a virtual environment using Python 3.12: `python3.12 -m venv [name_of_virtualenv]`.

4. **Install Dependencies:**
    - Use pip to install dependencies from the `requirements.txt` file: `pip install -r requirements.txt`.

5. **Run the Project:**
    - Execute the Flask application: `flask --app core run`.
    - Vist `http://localhost:5000` to see the application

6. **Database Migrations:**
    - Initialize migrations: `flask --app core db init`.
    - Run migrations: `flask --app core db migrate -m "initial migration"`.
    - Apply migrations: `flask --app core db upgrade head`.

## Todos:

- **Dashboard:** Implement a dashboard for users to manage their posts, including creation, viewing, updating, and deletion.
- **Search Functionality:** Integrate a search feature for posts, possibly using Algolia.
- **Comment Section:** Add a comment section for each post for user engagement.
- **Subscriber Management:** Develop routes to collect subscriber emails and send emails to subscribers.
- **Route Authorization:** Secure routes with proper authorization mechanisms.
- **Jinja Template Authorization:** Extend authorization to Jinja templates for enhanced security.
- **Makefile:** Include a Makefile for simplified project management tasks.
- **Dockerfile:** Provide a Dockerfile for containerized deployment.
- **Contact Form Route:** Implement a route for user contact forms.
- **Display Contact Messages:** Show contact messages on user dashboards for easy access.
- **Pagination:** Add pagination functionality for improved navigation through blogs.

## Author:

- **Martin Lubowa**
- **Email:** [martinlubowa@outlook.com](martinlubowa@outlook.com)

---

Feel free to contribute to this project by tackling the Todos or suggesting enhancements. For any issues or queries, please refer to the project's documentation or reach out to the maintainers. Thank you for using our Flask-based blogging platform!