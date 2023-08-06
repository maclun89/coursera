# Peer-graded Assignment: Little Lemon API project

## Introduction

This reading is an overview of the scope of the project, all the necessary endpoints, and notes that you will have to implement in the final project.
This reading will help you to successfully complete the project so read it carefully and reference it while developing your API project to help you
keep on track.

## Scope

You will create a fully functioning API project for the Little Lemon restaurant so that the client application developers can use the APIs to develop
web and mobile applications. People with different roles will be able to browse, add and edit menu items, place orders, browse orders, assign delivery
crew to orders and finally deliver the orders.
The next section will walk you through the required endpoints with an authorization level and other helpful notes. Your task is to create these
endpoints by following the instructions.

## Structure

You will create one single Django app called LittleLemonAPI and implement all API endpoints in it. Use pipenv to manage the dependencies in the
virtual environment. Review the video about

## Function or class-based views

You can use function- or class-based views or both in this project. Follow the proper API naming convention throughout the project.
Follow Naming conventions

### User groups

Create the following two user groups and then create some random users and assign them to these groups from the Django admin panel.

1. Manager
2. Delivery crew
3. Users not assigned to a group will be considered customers.

## Installation

Unzip Folder LittleLemon.zip
cd LittleLemon
pipenv shell
pip show pipenv
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Review criteria

When you submit your assignment, other learners in the course will review and grade your work. These are the criteria they’ll use to evaluate your
APIs.
In this project, your APIs need to make it possible for your end-users to perform certain tasks and your reviewer will be looking for the following
functionalities.

1. The admin can assign users to the manager group
2. You can access the manager group with an admin token
3. The admin can add menu items
4. The admin can add categories
5. Managers can log in
6. Managers can update the item of the day
7. Managers can assign users to the delivery crew
8. Managers can assign orders to the delivery crew
9. The delivery crew can access orders assigned to them
10. The delivery crew can update an order as delivered
11. Customers can register
12. Customers can log in using their username and password and get access tokens
13. Customers can browse all categories
14. Customers can browse all the menu items at once
15. Customers can browse menu items by category
16. Customers can paginate menu items
17. Customers can sort menu items by price
18. Customers can add menu items to the cart
19. Customers can access previously added items in the cart
20. Customers can place orders
21. Customers can browse their own orders
    You'll also need to give feedback on and grade the assignments of two other learners using the same criteria.

## Error check and proper status codes

You are required to display error messages with appropriate HTTP status codes for specific errors. These include when someone requests a non-existing
item, makes unauthorized API requests, or sends invalid data in a POST, PUT or PATCH request. Here is a full list.

| HTTP Status code   | Reason                                                    |
|--------------------|-----------------------------------------------------------|
| 200 - Ok           | For all successful GET, PUT, PATCH and DELETE calls       |
| 201 - Created      | For all successful POST requests                          |
| 403 - Unauthorized | If authorization fails for the current user token         |
| 401 – Forbidden    | If user authentication fails                              |
| 400 – Bad request  | If validation fails for POST, PUT, PATCH and DELETE calls |
| 404 – Not found    | If the request was made for a non-existing resource       |

## Api Endpoints and criteria

### Default Users

| User Type                    | username       | email                    | password                 |
|------------------------------|----------------|--------------------------|--------------------------|
| `SuperUser`                  | DeanWinchester | dean@winchester.com      | deano123!                |
| `Manager`                    | samuel         | samy@winchester.com      | samy123!                 |
| `Delivery Crew`              | castiel        | castiel@supernatural.com | castiel@123!castiel@123! |
| `Manager`<br>`Delivery Crew` | bobby          | bobby@singer.com         | bobby@123!               |
| `Customer`                   | adam           | adam@supernatural.com    | adam@123!                |
| `Customer`                   | charlie        | charlie@supernatural.com | charlie@123!             |

### Paths

#### Djoser Apis

| Endpoint       | Role                                      | Method | Purpose                                                                     |
|----------------|-------------------------------------------|--------|-----------------------------------------------------------------------------|
| /api/users     | No role required                          | POST   | Creates a new user with name, email and password                            |
| /api/users/me/ | Anyone with a valid user token            | GET    | Displays only the current user                                              |
| /token/login/  | Anyone with a valid username and password | POST   | Generates access tokens that can be used in other API calls in this project |

For details, see [Djoser documentation](https://djoser.readthedocs.io/en/latest/index.html).

#### Menu-items endpoints

| Endpoint                   | Role                    | Method                   | Purpose                                                       |
|----------------------------|-------------------------|--------------------------|---------------------------------------------------------------|
| /api/menu-items            | Customer, delivery crew | GET                      | Lists all menu items. Return a 200 – Ok HTTP status code      |
| /api/menu-items            | Customer, delivery crew | POST, PUT, PATCH, DELETE | Denies access and returns 403 – Unauthorized HTTP status code |
| /api/menu-items/{menuItem} | Customer, delivery crew | GET                      | Lists single menu item                                        |
| /api/menu-items/{menuItem} | Customer, delivery crew | POST, PUT, PATCH, DELETE | Returns 403 - Unauthorized                                    |
| /api/menu-items            | Manager, Admin          | GET                      | Lists all menu items                                          | 
| /api/menu-items            | Manager, Admin          | POST                     | Creates a new menu item and returns 201 - Created             |
| /api/menu-items/{menuItem} | Manager, Admin          | GET                      | Lists single menu item                                        |
| /api/menu-items/{menuItem} | Manager, Admin          | PUT, PATCH               | Updates single menu item                                      |
| /api/menu-items/{menuItem} | Manager, Admin          | DELETE                   | Deletes menu item                                             |

#### User group management endpoints

group_name is str data type, userId is int data type and route = ```/api/groups/{group_name}/users``` | ```/api/groups/{group_name}/users/{userId}```

| Endpoint                                | Group Variable | Role    | Method | Authorized User Types | Purpose                                                                                                                                                |
|-----------------------------------------|----------------|---------|--------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| /api/groups/{group_name}/users          | manager        | Manager | GET    | Manager, Admin        | Returns all managers                                                                                                                                   |
| /api/groups/{group_name}/users          | manager        | Manager | POST   | Manager, Admin        | Assigns the user in the payload to the manager group and returns 201-Created                                                                           |
| /api/groups/{group_name}/users/{userId} | manager        | Manager | DELETE | Manager, Admin        | Removes this particular user from the manager group and returns 200 – Success if everything is okay. If the user is not found, returns 404 – Not found |
| /api/groups/{group_name}/users          | delivery-crew  | Manager | GET    | Manager, Admin        | Returns all delivery crew                                                                                                                              |
| /api/groups/{group_name}/users          | delivery-crew  | Manager | POST   | Manager, Admin        | Assigns the user in the payload to delivery crew group and returns 201-Created HTTP                                                                    |
| /api/groups/{group_name}/users/{userId} | delivery-crew  | Manager | DELETE | Manager, Admin        | Removes this user from the manager group and returns 200 – Success if everything is okay. If the user is not found, returns 404 – Not found            |

#### Categories endpoints

| Methods         | Role     | Method | Purpose                                   | Authorized User Types                   | 
|-----------------|----------|--------|-------------------------------------------|-----------------------------------------|
| /api/categories | Customer | GET    | Returns categories the current user token | Admin, Manager, Delivery Crew, Customer |
| /api/categories | Customer | POST   | Create Category                           | Admin, Manager                          |

#### Cart management endpoints

-```/api/cart/menu-items``` and data type int

| Methods              | Role     | Method | Purpose                                                                                         | Authorized User Types                   | 
|----------------------|----------|--------|-------------------------------------------------------------------------------------------------|-----------------------------------------|
| /api/cart/menu-items | Customer | GET    | Returns current items in the cart for the current user token                                    | Admin, Manager, Delivery Crew, Customer |
| /api/cart/menu-items | Customer | POST   | Adds the menu item to the cart. Sets the authenticated user as the user id for these cart items | Admin, Manager, Delivery Crew, Customer |
| /api/cart/menu-items | Customer | DELETE | Deletes all menu items created by the current user token                                        | Admin, Manager, Delivery Crew, Customer |

#### Order management endpoints

| Methods               | Role          | Method     | Purpose                                                                                                                                                                                                                                                                                                                                               | Authorized User Types                   | 
|-----------------------|---------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| /api/orders           | Customer      | GET        | Returns all orders with order items created by this user                                                                                                                                                                                                                                                                                              | Admin, Manager, Delivery Crew, Customer |
| /api/orders           | Customer      | POST       | Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.                                                                                                                                                     | Admin, Manager, Delivery Crew, Customer |
| /api/orders/{orderId} | Customer      | GET        | Returns all items for this order id. If the order ID doesn’t belong to the current user, it displays an appropriate HTTP error status code.                                                                                                                                                                                                           | Admin, Manager, Delivery Crew, Customer |
| /api/orders           | Manager       | GET        | Returns all orders with order items by all users                                                                                                                                                                                                                                                                                                      | Admin, Manager, Delivery Crew, Customer |
| /api/orders/{orderId} | Customer      | PUT, PATCH | Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1. If a delivery crew is assigned to this order and the status = 0, it means the order is out for delivery. If a delivery crew is assigned to this order and the status = 1, it means the order has been delivered. | Admin, Manager, Delivery Crew, Customer |
| /api/orders/{orderId} | Manager       | DELETE     | Deletes this order                                                                                                                                                                                                                                                                                                                                    | Admin, Manager, Delivery Crew, Customer |
| /api/orders           | Delivery crew | GET        | Returns all orders with order items assigned to the delivery crew                                                                                                                                                                                                                                                                                     | Admin, Manager, Delivery Crew, Customer |
| /api/orders/{orderId} | Delivery crew | PATCH      | A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.                                                                                                                                                                                                 | Admin, Manager, Delivery Crew, Customer |

## Additional step

Implement proper filtering, pagination and sorting capabilities for /api/menu-items and /api/orders endpoints.

| Endpoint        | Filtering   | Ordering        | Pagination                          | Sorting         | Pagination Parameters | Sorting Parameters         |
|-----------------|-------------|-----------------|-------------------------------------|-----------------|-----------------------|----------------------------|
| /api/menu-items | category-id | price, category | Default page size: None all records | price, category | ?page_size=3&page=1   | ?category=1&ordering=price |
| /api/orders     |             |                 | Default page size: 5                |                 |                       |                            |

## Throttling

Finally, apply some throttling for the authenticated users and anonymous or unauthenticated users.

#### Remove single user from a group

## Test Cases
Users, Order and roles are created
### The admin Test Case
1. Ok - The Admin can assign users to the manager group
2. Ok - The Admin can access the manager group with an admin token
3. Ok - The admin can add menu items
4. Ok - The admin can add categories

### The Managers Test Case

1. Ok - Managers can log in
2. Ok - Managers can update the item of the day
3. Ok - Managers can assign users to the delivery crew
4. Ok - Managers can assign orders to the delivery crew

### The Delivery crew Test Case

1. Ok - The delivery crew can log in using their username and password and get access tokens
2. Ok - The delivery crew can access orders assigned to them
3. Ok - The delivery crew can update an order as delivered

### The Customers Test Case

1. Ok - Customers can register
2. Ok - Customers can log in using their username and password and get access tokens
3. Ok - Customers can browse all categories
4. Ok - Customers can browse all the menu items at once
5. Ok - Customers can browse menu items by category
6. Ok - Customers can paginate menu items
7. Ok - Customers can sort menu items by price
8. Ok - Customers can add menu items to the cart
9. Ok - Customers can access previously added items in the cart
10. Ok - Customers can place orders
11. Ok - Customers can browse their own orders

