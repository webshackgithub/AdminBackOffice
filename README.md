# Service Admin Backoffice

A modern, responsive Service Administration Dashboard built with **Django**, **Tailwind CSS**, **Alpine.js**, and **HTMX**. This project provides a comprehensive UI/UX for managing users, analytics, and service settings with support for both Light and Dark modes.

## 🚀 Tech Stack

-   **Backend:** Python 3.12+, Django 5.x
-   **Templating:** Django Templates
-   **Frontend:**
    -   **Tailwind CSS** (Styling)
    -   **Alpine.js** (Interactivity: Modals, Dropdowns, Dark Mode)
    -   **HTMX** (Dynamic server interactions)
-   **Icons:** Heroicons (SVG)

## 🛠 Prerequisites

-   Python 3.12 or higher
-   Node.js & npm (for Tailwind CSS build process)

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/webshackgithub/AdminBackOffice.git
    cd service_admin_backoffice
    ```

2.  **Set up the Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    # If requirements.txt is missing, install basic deps:
    pip install django django-allauth python-dotenv
    ```

4.  **Install Node Dependencies (for Tailwind):**
    ```bash
    npm install
    ```

5.  **Initialize the Database:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

## 🏃‍♂️ Running the Project

You need to run two processes (or just the Django server if relying on the CDN version of Tailwind for development, though local build is recommended).

1.  **Start the Tailwind Watcher (in a new terminal):**
    ```bash
    npm run dev
    ```

2.  **Start the Django Development Server:**
    ```bash
    python manage.py runserver
    ```

3.  **Access the Admin Panel:**
    Open your browser and navigate to `http://localhost:8000`.

## 📂 Project Structure

```
service_admin_backoffice/
├── apps/                   # Django Apps
│   ├── common/             # Shared utilities & views
│   ├── dashboard/          # Main Dashboard logic
│   └── users/              # User management logic
├── config/                 # Project Settings (Django)
│   ├── settings/           # Modular settings (base, local, prod)
│   ├── urls.py             # Main URL routing
│   └── wsgi.py
├── static/                 # Static files (CSS, Images, JS)
│   └── css/
│       └── input.css       # Tailwind source CSS
├── templates/              # HTML Templates
│   ├── components/         # Reusable UI (Sidebar, Header, Modals)
│   ├── dashboard/          # Dashboard pages
│   ├── users/              # User pages
│   └── base.html           # Main layout wrapper
├── manage.py
├── package.json            # Node dependencies
└── tailwind.config.js      # Tailwind configuration
```

## ✨ Key Features

-   **Dark Mode Support:** "Softer Dark" theme available globally.
-   **Dashboard:** 4-column Stats Grid, Revenue Chart placeholder, Recent Activity table.
-   **Navigation:** Breadcrumbs, Sidebar with active states, specific UI for active apps.
-   **Profile Modal:** Interactive settings with save capabilities.

## 🤝 Contributing

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.
