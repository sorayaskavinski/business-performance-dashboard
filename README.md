# BUSINESS PERFORMANCE DASHBOARD APP
# Overview

The Business Performance Dashboard is a web application designed to help businesses view, search, and manage sales information stored in a cloud database.

This project was developed to strengthen my skills in web application development, database integration, Python programming, and software architecture. The application builds upon a Python-based business dashboard and transforms it into an interactive web application using the Django framework.

The application connects to a MongoDB Atlas database containing sales records. Users can navigate through the application to view business information, search for sales records, add new sales, update existing sales, and delete sales records.

To start the application on a local computer, open a terminal in the project directory and activate the virtual environment:

    .\.venv\Scripts\Activate.ps1

Then start the Django development server:

    python manage.py runserver

After the server starts, open the following address in a web browser:

    http://127.0.0.1:8000/

The purpose of this software is to create a practical business application that demonstrates how a Python web framework can interact with a cloud database and dynamically generate web pages based on data and user input.

This project also helped me develop a better understanding of the separation between the user interface, application logic, and database operations. It allowed me to take an existing Python and MongoDB business dashboard and expand it into an interactive web application using Django.

The demonstration video shows the application running on the local development server, navigation through the web pages, interaction with the sales data, and a walkthrough of the main sections of the code.

[Software Demo Video](PASTE-YOUR-YOUTUBE-LINK-HERE)


# Web Pages

The application contains several dynamically generated web pages that are connected through the navigation menu.

## Home Page

The Home page is the main entry point of the application. It introduces the Business Performance Dashboard and provides navigation links to the different features of the application.

The page uses Django templates and a shared base.html template to maintain a consistent layout and navigation throughout the application.

## Dashboard Page

The Dashboard page displays business information generated from sales data stored in MongoDB Atlas.

The application retrieves sales records from the database and uses Python and Pandas to calculate information such as:

- Total sales
- Average sale
- Highest sale
- Lowest sale
- Number of transactions
- Sales by category
- Sales by month

The information displayed on the page is dynamically generated from the current data stored in the database.

## Search Sales Page

The Search Sales page allows users to search the sales database.

Users can search for sales information using different criteria, including:

- Product
- Category
- Salesperson
- Region

The application processes the user's input and retrieves matching records from MongoDB.

The search results are dynamically generated based on the user's search criteria.

## Add Sale Page

The Add Sale page allows users to enter information for a new sales transaction.

The application receives the user's input, calculates the total sale using the quantity and unit price, and stores the new record in MongoDB.

After the record is successfully added, the user receives confirmation that the sale was added.

## Update Sale Page

The Update Sale page allows users to modify an existing sales record.

The user provides the MongoDB document ID of the sale they want to update. The application retrieves the existing record and displays its information.

The user can then modify the fields and submit the changes. The updated information is sent to MongoDB and the existing record is modified.

## Delete Sale Page

The Delete Sale page allows users to remove an existing sales record from the database.

The application identifies the selected record using its MongoDB document ID and asks the user to confirm the deletion before removing the record from MongoDB.

## Page Navigation

The pages are connected through the navigation menu provided by the shared base.html template.

The general navigation flow is:

Home → Dashboard

Home → Search Sales

Home → Add Sale

Home → Update Sale

Home → Delete Sale

Django's URL configuration determines which Python view function handles each request. The view processes the request, retrieves or modifies database information when necessary, and sends dynamically generated content to the appropriate HTML template.


# Development Environment

The project was developed using Visual Studio Code as the primary development environment.

The following tools and technologies were used:

- Visual Studio Code
- Python
- Django
- MongoDB Atlas
- PyMongo
- Pandas
- Matplotlib
- HTML
- CSS
- Git
- GitHub
- PowerShell

Python was the primary programming language used to develop the application.

Django was used as the web application framework. It handles the web requests, URL routing, views, templates, and local development server.

PyMongo was used to connect the Python application to the MongoDB Atlas cloud database and perform database operations.

Pandas was used to load and analyze sales data for the business dashboard.

Matplotlib was used to create charts and visualizations for the sales analysis.

The python-dotenv library was used to load the MongoDB connection string from the .env file without placing the database credentials directly in the source code.

The application separates the web interface from the database and CRUD operations. The existing MongoDB functionality is organized into database-related files, while Django views and templates are responsible for presenting and processing information through the web application.


# Useful Websites

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/6.0/intro/tutorial01/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [PyMongo Documentation](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)
- [Python Documentation](https://docs.python.org/3/)


# Future Work

- Improve the visual design and responsiveness of the web application.
- Add stronger validation for user input when adding and updating sales.
- Improve error handling for invalid MongoDB document IDs.
- Add additional sorting and filtering options to the Search Sales page.
- Add more business analytics and visualizations to the Dashboard.
- Add user authentication and different levels of access.
- Improve confirmation and feedback messages after database operations.
- Add additional reports to help users analyze business performance.
- Deploy the application to a production hosting environment.
- Continue improving the application based on user feedback and testing.