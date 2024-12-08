# Lesozavod-website-django 🐍

[![](https://img.shields.io/badge/github(django)-blueviolet?style=for-the-badge)](https://github.com/django)
[![](https://img.shields.io/badge/book(django)-green?style=for-the-badge)](https://www.djangoproject.com/)

$$\normalsize{\textsf{\color{orange}Web application created in Python using the Django framework}}$$

$\normalsize{\textsf{\color{violet}2 stages "Automation of business processes" of the NTO Olympiad (National Technology Olympiad) 2024-2025}}$

### Condition
Sawmill “Lesozavod №10 Belka” is divided into several services of the enterprise. 
The main services are commercial service, production service, and technologist service.

The main departments are the commercial department, the production department, and the technologist department.

- The <ins>commercial service</ins> accepts orders from customers for different types of timber products. 

- The task of the <ins>production service</ins> is dispatching and production of timber products. 

- The <ins>technologist service</ins> controls the condition of production lines and machines. Required to develop an application for automation of the sawmill, to realize the possibility of registration of orders for timber products from customers by employees of the commercial service

<img src="https://i.ibb.co/r4Fy7N1/2024-11-14-223238.png" width="800" height="400">

### Staging:

1. Create an application to manage a sawmill. Divide it into sections for 
services: commercial service, production service, technologist service.


2. Create an object to store information about types of forest products. Information on types of 
Information about types of forest products should be available to commercial service employees, production service employees, and technical service employees 
production service and technologist service

3. Create an object for storing information about the plant's customers - consumers of 
timber products. Information about customers should be available to employees 
commercial service

4. Create an object to register an order from a customer for forest products. Orders for 
orders for forest products should be available to the employees of the commercial service, employees of the 
production service. The following information should be reflected in the order for timber products 
information:
    * Order registration date,
    * Date by which forest products are required to be released (cannot be less than or equal to the date of order registration, equal to the date of order registration),
    * Information about the customer-orderer,
    * Type of forest products required by the customer,
    * Quantity of forest products (for convenience we measure in pieces),
    * Additional information about the order (arbitrary text description),
    * Status of the order (“Draft”, “Approved by the customer”, “Accepted for production”, and
“Fulfilled")

    When registering an order from a customer, it is necessary to check its completion: an order in the status of 
“Approved by the customer” can be registered only if it contains information about the customer, type of forest products and quantity of forest products ordered. 
customer, type of timber products and quantity of timber products to be ordered. By default 
Forest products order is created with “Draft” status

5. In the customer's list of orders for forest products, it is necessary to make color selections based on 
depending on the conditions:
    * An order in the “Draft” status has no color highlighting,
    * An order in the status “Approved by the customer” has orange color highlighting,
    * An order in the status “Accepted for production” has yellow color highlighting,
    * Order in the status “Fulfilled” has green color highlighting.

Filling with test data:
* Enter 6 types of forest products from the Legend.
* Enter at least 2 clients of the Timber plant.
* Enter 3 orders with the status “Approved by the client” with types of timber products:
    <p>i. Raw lumber.</p>
    <p>ii. Dry lumber.</p>
    <p>iii. Laths</p>

## Instructions for connecting to the site "Lesozavod №10 Belka"

| Download the repository |

* In the repository you selected, click the green ‘Code’ button and copy the URL.
* Then, in Visual Studio Code (or other code editor), open a terminal and type the command:
  
```python
  git clone [repository address]
```

| Create a virtual environment |

* Go to the project directory: `cd lesozavod`
* Create a virtual environment using the command:
  
```python
  python -m venv env (replace ‘env’ with the desired environment name)
```

* Activate the virtual environment in Windows: `env\Scripts\activate`
* Or activate the virtual environment in macOS/Linux: `source env/bin/activate`
  
| Install dependencies |

* After activating the virtual environment, install the required libraries from the `requirements.txt` file
 
```python
  pip install -r requirements.txt
```

| Database Migrations |


* Create migrations (if needed)
  
```python
  python manage.py makemigrations
```

* Apply created migrations
  
```python
   python manage.py migrate
```

* Remove migrations if necessary
* app_label (name of the application to be removed)

```python
   python manage.py migrate <app_label> zero
```

| Start the Development Server |

* Start the Django development server

```python
   python manage.py runserver
```

| Additional Notes |
  
* Make sure you have the appropriate version of Python installed, as specified in `requirements.txt`
* And have all the necessary libraries `pip install django` installed
  
  (If you are using a different IDE or editor, you may need to configure the environment so that it can find the virtual environment and installed libraries)
