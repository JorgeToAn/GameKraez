# FSDI FINAL PROJECT - Tech Storm

Tech Storm is an online store project made using the Django framework.

## Functionality

### Users

Users have one of two roles, Manager or Customer:

- Managers are able to access the Django admin page where they may create/edit/delete products to sell, create other manager accounts.
- Customers are created through the regular sign up page, they're able to browse the store and add product to their cart, then being able to proceed to order those products to a specified shipping address.

### Main page

The main page shows some of the products that are available in the store while being able to access directly to those products pages and add them to their cart.
It also provides some quick buttons to access the different categories of the catalog.

### Navbar

The navbar provides controls for accessing the main page, the catalog, the login page and the cart. It also has a search bar where you can input the name of a product and it will redirect you into the catalog page and search by that name.

### Catalog

The catalog page shows all the available products, it shows up to 5 products per page, pagination navigation is provided to see all of the products.
On one side the user is provided with some controls to filter their catalog through name, category, price range and order these products by price (ascending, descending or none).

### Products

Products have a detail page where it shows the product's name, description, price and related reviews, if the user desires they can add the product into the cart or create a review.
To create, edit or delete products, a manager account needs to access the admin page and manipulate the objects through there.

### Reviews

Reviews are created for a specific product and a title, subtitle, body and score is submitted, these reviews are shown in the corresponding product detail page.

### Cart and payment

Once the user has their order, they can review their order in the cart page, they can see the products in their order and have controls to change the quantity and removing the product from the cart.
A summary is shown that calculates the subtotal, tax and total of the order.
Once the payment is started, the user is redirected to fill the shipping address form and finalize their order.
No actual payment info is entered but a payment object that has a transaction ID and date is created and linked to the order.
After that, the user is alerted that the payment has been submitted and is redirected to the main page.

### Feedback

Any user can submit a feedback form, containing a first name, last name, email, comment and score. Managers are able to access a feedback list page where all submitted feedback is shown.

## Technologies used

The project was built on the Django framework, the database uses the default Python's SQLite, it also uses some django extensions such as django-crispy-forms for styling forms and djang-countries to create country fields in models.

## Steps to run the project

1. Download the source code
2. Create a virtual environment inside the project folder
3. Activate the venv and install the extensions required through the requirements.txt
4. Run the server with "python3 manage.py runserver"
