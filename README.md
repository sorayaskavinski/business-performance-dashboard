# Overview

{Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.}

{Provide a description the web app that you wrote. Describe how to start a test server on your computer and what website to open up to see the first page of the app.}

{Describe your purpose for writing this software.}

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

{Describe each of the web pages you created and how the web app transitions between each of them.  Also describe what is dynamically created on each page.}

# Development Environment

{Describe the tools that you used to develop the software}

{Describe the programming language that you used and any libraries.}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](http://url.link.goes.here)
* [Web Site Name](http://url.link.goes.here)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1
* Item 2
* Item 3


# Business Performance Dashboard (Cloud Database Edition)

### Overview 

This is an expanded Python data analysis dashboard integrated with a cloud-hosted MongoDB Atlas database. Upgraded from a static CSV-based workflow, the application directly interacts with a cloud database to store, retrieve, update, and analyze live business sales data.

It leverages pymongo for database operations, pandas for data cleaning and aggregation, and matplotlib for key visual insights.

### Features:
* Cloud Database Integration: Connects securely to a remote MongoDB Atlas cluster.

* Full CRUD Functionality:

* Create: Insert new sales records and transactions into the cloud database.

* Read: Retrieve stored business records for real-time analysis.

* Update: Modify existing sales entries or status fields directly in the cloud.

* Delete: Remove outdated or duplicate records safely.

* Data Cleaning & Aggregation: Uses Pandas to handle missing data, parse date formats, and group revenue statistics.

* Data Visualization: Generates interactive Matplotlib charts displaying sales trends, category performance, and top revenue drivers.

---


[Software Demo Video](https://youtu.be/ADk4Y53KuKI)


---

### Cloud Database Structure

The application connects to a MongoDB database named business_dashboard using a sales_records collection.
---


# Technologies & Libraries:

* Language: Python 3

* Cloud Database: MongoDB Atlas

* Database Driver: PyMongo (pymongo) / dnspython

* Data Processing: Pandas

* Visualization: Matplotlib / Seaborn

* Environment Management: Python dotenv (for safe URI credential handling)


# How to Run:

* pip install -r requirements.txt

* python main.py

---


# Useful Websites

The following resources can help beginners learn the technologies used in this project:

### MongoDB & Cloud Databases

* [MongoDB Atlas Documentation](https://www.mongodb.com/pt-br/docs/atlas/)

* [PyMongo Official Driver Tutorial](https://www.mongodb.com/pt-br/docs/languages/python/pymongo-driver/current/get-started/)

* [MongoDB Python Crash Course (Real Python)](https://realpython.com/)

---

### Python

Python is the programming language used to develop this application.

* [Python Official Documentation](https://docs.python.org/3/)
* [Python Beginner Tutorial](https://docs.python.org/3/tutorial/)

---

### Pandas

Pandas is the Python library used for importing, cleaning, manipulating, and analyzing data.

* [Pandas Official Documentation](https://pandas.pydata.org/docs/)

* [Pandas Getting Started Guide](https://pandas.pydata.org/docs/getting_started/index.html)

---

### Matplotlib

Matplotlib is the visualization library used to create charts and graphs.

* [Matplotlib Official Documentation](https://matplotlib.org/stable/)

* [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

---

### Data Analysis

These resources provide an introduction to data analysis concepts:

* [Kaggle Learn - Pandas](https://www.kaggle.com/learn/pandas)

* [Kaggle Learn - Data Visualization](https://www.kaggle.com/learn/data-visualization)

---

### Visual Studio Code

Visual Studio Code was used as the development environment.

* [Visual Studio Code Official Website](https://code.visualstudio.com/)

* [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

---

### Git and GitHub

GitHub is used to store and share the source code.

* [GitHub Documentation](https://docs.github.com/)

* [Git Beginner Guide](https://docs.github.com/en/get-started/getting-started-with-git)