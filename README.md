# BUSINESS PERFORMANCE DASHBOARD APP
# Overview

The Business Performance Dashboard is a web application designed to help businesses view, analyze, search, and manage sales information stored in a cloud database.

This project was developed to strengthen my skills in web application development, database integration, Python programming, CRUD operations, data analysis, and software architecture. The application builds upon a Python-based business dashboard and transforms it into an interactive web application using the Django framework.

The application connects to a MongoDB Atlas cloud database containing sales records. Users can navigate through the application to view business information, search for sales records, add new sales, update existing sales, and delete sales records.

To start the application on a local computer, open a terminal in the project directory and activate the virtual environment:

    .\.venv\Scripts\Activate.ps1

Then start the Django development server:

    python manage.py runserver

After the server starts, open the following address in a web browser:

    http://127.0.0.1:8000/

The purpose of this software is to create a practical business application that demonstrates how a Python web framework can interact with a cloud database and dynamically generate web pages based on data and user input.

This project also helped me develop a better understanding of the separation between the user interface, application logic, and database operations. It allowed me to take an existing Python and MongoDB business dashboard and expand it into an interactive web application using Django.

The demonstration video shows the application running on the local development server, navigation through the web pages, interaction with the sales data, and a walkthrough of the main sections of the code.


[Software Demo Video](https://youtu.be/eUudPCSqp20)


# Web Pages

The application contains several dynamically generated web pages that are connected through Django URL routing and a shared base.html template

## Home Page

The Home page is the main entry point of the application. It introduces the Business Performance Dashboard and provides navigation links to the main features of the application.

The page provides access to:

Business Dashboard
Search Sales
Add Sale

The page also displays information about the technologies used in the application, including MongoDB Atlas, Django, Pandas, and Matplotlib.

The base.html template provides the common navigation bar, messages, Bootstrap styling, and footer used throughout the application.

## Dashboard Page

The Dashboard page displays business information generated from sales data stored in MongoDB Atlas.

The Django view retrieves sales records from MongoDB and uses Python and Pandas to process the data.

The dashboard dynamically calculates and displays:

- Total sales
- Average sale
- Highest sale
- Lowest sale
- Number of transactions
- Top product category
- Top sales month
- Sales by category
- Monthly sales

The page also generates interactive charts using Chart.js. The data for the charts is calculated by Python and passed from the Django view to the HTML template.

This means the dashboard changes based on the current information stored in the MongoDB database.

## Search Sales Page

The Search Sales page allows users to search the sales database using multiple search criteria.

Users can search using:

- Product
- Category
- Salesperson
- Region
- Date

The user can combine multiple filters or leave filters empty.

The Django view receives the user's input through the request, sends the search criteria to the MongoDB CRUD function, and displays the matching records dynamically. 

The results are displayed in a table containing information such as:

- Date
- Product
- Category
- Salesperson
- Region
- Sales amount

Each result also contains buttons that allow the user to edit or delete that specific sales record.

## Add Sale Page

The Add Sale page allows users to enter information for a new sales transaction.

The user provides information such as:

- Date
- Product
- Category
- Salesperson
- Region
- Quantity
- Unit price

The Django view receives the submitted information and sends it to the MongoDB CRUD function.

The application calculates the total sales amount using:

Sales = Quantity × Unit Price

The new record is then stored in MongoDB Atlas.

After the sale is successfully added, the application displays a confirmation message and returns the user to the Search Sales page.

## Update Sale Page

The Update Sale page allows users to modify an existing sales record.

The user reaches the Update Sale page by selecting the Edit button from a sales record displayed on the Search Sales page.

Django uses the MongoDB document ID to identify the selected record.

The existing information is retrieved from MongoDB and displayed in the update form.

The user can modify the sales information and submit the changes.

The updated information is then sent to MongoDB through the CRUD update function.

The application also recalculates the total sales amount using the quantity and unit price.

After the record is successfully updated, the user receives a confirmation message and is returned to the Search Sales page.


## Delete Sale Page

The Delete Sale page allows users to remove an existing sales record from MongoDB.

The user reaches the Delete Sale page by selecting the Delete button from a sales record displayed on the Search Sales page.

The application displays information about the selected record and asks the user to confirm the deletion.

If the user confirms, Django sends the MongoDB document ID to the delete CRUD function.

The record is removed from MongoDB Atlas and the user receives a confirmation message.

If the user cancels the operation, the record remains unchanged.

## Page Navigation

The application uses Django URL routing to connect the different pages.

The general navigation flow is:

Home → Dashboard

Home → Search Sales

Home → Add Sale

Search Sales → Update Sale

Search Sales → Delete Sale

The Django URL configuration determines which Python view function handles each request.

The view processes the request, retrieves or modifies database information when necessary, and sends dynamically generated information to the appropriate HTML template.

A shared base.html template provides a consistent layout across the application.


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
- Chart.js
- HTML
- CSS
- Bootstrap
- Git
- GitHub
- PowerShell

Python was the primary programming language used to develop the application.

Django was used as the web application framework. It handles HTTP requests, URL routing, views, templates, and the local development server.

PyMongo was used to connect the Python application to the MongoDB Atlas cloud database and perform database operations.

MongoDB Atlas was used as the cloud database for storing the sales records.

Pandas was used to process and analyze sales data for the Business Performance Dashboard.

Matplotlib was used in the original Python dashboard to create sales visualizations.

Chart.js was used in the Django web application to dynamically display sales charts in the browser.

Bootstrap was used to improve the layout, responsiveness, and visual appearance of the HTML pages.

The python-dotenv library was used to load the MongoDB connection string from the .env file so that database credentials are not placed directly in the source code.

The application separates the web interface from the database and CRUD operations. Database operations are organized in the database package, while Django views process requests and HTML templates are responsible for displaying the information to users.

The CRUD functionality includes:

- Creating new sales records
- Reading sales records
- Searching sales records
- Updating existing sales records
- Deleting sales records


# Useful Websites

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/6.0/intro/tutorial01/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [PyMongo Documentation](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)
- [Python Documentation](https://docs.python.org/3/)


# Future Work

- Improve validation for user input when adding and updating sales.
- Improve error handling for invalid or missing MongoDB document IDs.
- Add additional sorting and filtering options to the Search Sales page.
- Add pagination when displaying a large number of sales records.
- Add more business analytics and visualizations to the Dashboard.
- Improve the visual design and responsiveness of the web application.
- Add user authentication and different levels of access.
- Add additional reports to help users analyze business performance.
- Add export functionality for sales reports.
- Improve confirmation and feedback messages after database operations.
- Deploy the application to a production hosting environment.
- Continue improving the application based on user feedback and testing.