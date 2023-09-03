# Peer-graded Assignment: Little Lemon API project

## Introduction

By working through the lessons in this course, you revisited the necessary concepts and knowledge of back-end development. Using the Django REST Framework, you put your skills into practice to build an API for the Little Lemon restaurant.
You completed exercises, received general instructions and code snippets, and utilized links to resources from previous courses to complete this task.
You demonstrated your web development skills by writing code to create an API that handles table bookings for the Little Lemon restaurant.
The API can receive HTTP requests such as GET, POST, PUT and DELETE, and updates the Django models, which in turn, updates the data in a MySQL database.
Now, you will participate in a peer review exercise in which you will submit your completed project for two of your peers to review.
You will also be required to review a project of two of your peers.
The grading criteria are covered in more detail below.

This project was created for the completion of **Meta Back-End Developer Capstone** course.

### API paths
Index View (With Littlelemon logo)
    - GET restaurant/menu/

Authentication
    - Create a new user
        - POST /auth/users/
        - Payload example:
        {
            "email": "rogue@email.com",
            "username": "rogue",
            "password": "littlelemon!123"
        }
    - Generate auth token
        - POST /auth/token/login/
        - Payload example
        {
            "username": "rogue",
            "password": "littlelemon!123"
        }

Menu API (No Authentication Required)
base path: /restaurant/menu/items/
    - List all menu items
        - GET /restaurant/menu/items/
    - Create a new menu item
        - POST /restaurant/menu/items/
        - Payload example:
            {
                "title": "Classic Cheeseburguer",
		        "price": 10.9,
		        "inventory": 2
            }
    - Detail a menu item
        - GET /restaurant/menu/items/<int:pk>/
    - Update a menu item
        - PUT/PATCH /restaurant/menu/items/<int:pk>/
        - Payload example:
            {
                "title": "Cheeseburguer Oldschool",
		        "price": 14.9,
		        "inventory": 1
            }
    - Delete a menu item
        - DELETE /restaurant/menu/items/<int:pk>/

Booking API (Authentication Required)
base path: /restaurant/booking/tables/
    - List all bookings
        - GET /restaurant/booking/tables/
    - Create a new booking
        - POST /restaurant/booking/tables/
        - Payload example:
            {
                "name": "Tiefling Wizard",
                "no_of_guests": 6,
                "bookingDate": "2023-09-15T12:00:03Z"
            }
    - Detail a booking
        - GET /restaurant/booking/tables/<int:pk>/
    - Update a booking
        - PUT/PATCH /restaurant/booking/tables/<int:pk>/
        - Payload example:
            {
                "name": "Half-Orc Barbarian",
                "no_of_guests": 10,
                "bookingDate": "2023-09-16T12:00:03Z"
            }
    - Delete a booking
        - DELETE /restaurant/booking/tables/<int:pk>/
Please find the list to the paths to be tested in the review of the Peer-graded Assignment in the [Readme.txt](./Readme.txt) file.
