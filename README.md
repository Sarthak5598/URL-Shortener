# URL Shortener

Welcome to the URL Shortener project! This application allows users to shorten long URLs into more manageable links.

## Features
- **Shorten URLs:** Convert long URLs into short links.
- **User-Friendly Interface:** Simple web interface for easy URL shortening.
- **Easy Deployment:** Instructions for deployment using Poetry.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)

## Getting Started

To get started with the URL Shortener project, follow these steps.

### Prerequisites
- **Python:** 3.7 or higher.
- **Poetry:** Dependency management and virtual environment tool. Install it from the [official Poetry website](https://python-poetry.org/docs/#installation).

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Sarthak5598/URL-Shortener.git
    cd URL-Shortener
    ```

2. **Install Poetry (if you haven't already):**
   Follow the instructions on the [Poetry installation page](https://python-poetry.org/docs/#installation) to install Poetry on your system.

3. **Install Dependencies:**
    ```bash
    poetry install
    ```

### Running the Project

1. **Activate the Virtual Environment:**
    ```bash
    poetry shell
    ```

2. **Run Migrations (if applicable):**
    ```bash
    python manage.py migrate
    ```

3. **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```

4. **Open your browser and visit** [http://127.0.0.1:8000](http://127.0.0.1:8000) **to use the URL Shortener.**
