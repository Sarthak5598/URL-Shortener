URL Shortener

Welcome to the URL Shortener project! This application allows users to shorten long URLs into more manageable links.

Features
Shorten URLs: Convert long URLs into short links.
User-Friendly Interface: Simple web interface for easy URL shortening.
Easy Deployment: Instructions for deployment using Poetry.
Table of Contents
Getting Started
Prerequisites
Installation
Running the Project
Getting Started
To get started with the URL Shortener project, follow these steps.

Prerequisites
Python: 3.7 or higher.
Poetry: Dependency management and virtual environment tool. Install it from the official Poetry website.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/Sarthak5598/URL-Shortener.git
cd URL-Shortener
Install Dependencies:

Use Poetry to install dependencies:

bash
Copy code
poetry install

Running the Project
Activate the Virtual Environment:

bash
Copy code
poetry shell
Run Migrations (if applicable):

bash
Copy code
python manage.py migrate
Start the Development Server:

bash
Copy code
python manage.py runserver
Open your browser and visit http://127.0.0.1:8000 to use the URL Shortener.