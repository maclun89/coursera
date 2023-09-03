# Peer-graded Assignment: Little Lemon API project

## Introduction

By working through the lessons in this course, you revisited the necessary concepts and knowledge of back-end development. Using the Django REST
Framework, you put your skills into practice to build an API for the Little Lemon restaurant.
You completed exercises, received general instructions and code snippets, and utilized links to resources from previous courses to complete this task.
You demonstrated your web development skills by writing code to create an API that handles table bookings for the Little Lemon restaurant.
The API can receive HTTP requests such as GET, POST, PUT and DELETE, and updates the Django models, which in turn, updates the data in a MySQL
database.
Now, you will participate in a peer review exercise in which you will submit your completed project for two of your peers to review.
You will also be required to review a project of two of your peers.
The grading criteria are covered in more detail below.

This project was created for the completion of **Meta Back-End Developer Capstone** course.

### API paths

| Endpoint                | Role                    | Method | Purpose                                                  |
|-------------------------|-------------------------|--------|----------------------------------------------------------|
|                         | Customer, delivery crew | GET    | Index View (With Littlelemon logo)                       |
| restaurant/menu/        | Customer, delivery crew | GET    | Lists all menu items. Return a 200 – Ok HTTP status code |
| /auth/users/            | Customer, delivery crew | GET    | Create a new user. Return a 200 – Ok HTTP status code    |
| /auth/token/login/      | Customer, delivery crew | GET    | Create a new user. Return a 200 – Ok HTTP status code    |
| /restaurant/menu/items/ | Customer, delivery crew | GET    | Create a new user. Return a 200 – Ok HTTP status code    |

- List all menu items
- GET /restaurant/menu/items/
- Create a new menu item
- POST /restaurant/menu/items/
- Payload example:

- Detail a menu item
- GET /restaurant/menu/items/<int:pk>/
- Update a menu item
- PUT/PATCH /restaurant/menu/items/<int:pk>/
- Payload example:

- Delete a menu item
- DELETE /restaurant/menu/items/<int:pk>/

Booking API (Authentication Required)
base path: /restaurant/booking/tables/

- List all bookings
- GET /restaurant/booking/tables/
- Create a new booking
- POST /restaurant/booking/tables/
- Payload example:

- Detail a booking
- GET /restaurant/booking/tables/<int:pk>/
- Update a booking
- PUT/PATCH /restaurant/booking/tables/<int:pk>/
- Payload example:

- Delete a booking
- DELETE /restaurant/booking/tables/<int:pk>/
  Please find the list to the paths to be tested in the review of the Peer-graded Assignment in the [Readme.txt](./Readme.txt) file.
