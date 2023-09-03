Exercise: Display the Little Lemon available booking times
Lab assets
You are provided with a basic setup for the Django environment for the project and app inside the zip file below.

The zip file contains an updated template to be used along with supportive files to run the lab.

Note: The virtual environment using pipenv has been added as a part of the zip file. You must activate the virtual environment and ensure dependencies
are installed.

Your goal is to implement reservation data retrieved from an API and update the HTML document to display the data using JavaScript.

Objective
Implement changes for updating the HTML form data using JavaScript

Introduction
In parts one and two of the final assessment, you connected a model and built a form to accept reservation details from an end-user on the Little
Lemon website. In this exercise, you must use JavaScript to perform the following actions:

Create new bookings and refresh current bookings

Refresh bookings for a date when the date is changed

Dynamically process available time slots

Initial lab instructions
This lab will require you to modify the following files:

views.py

templates/bookings.html

Starter code has already been added to the following files:

settings.py

forms.py

models.py

urls.py (app-level)

urls.py (project-level)

Once you set up the project, make sure you oversee the contents of all the files and follow the steps accordingly. The zip file added here may contain
some additional stylesheets and formatting so it is recommended to use it as the starter code instead of building on your existing project from part
two.

You have already built the project named LittleLemon and added an app inside the project called restaurant.

Follow the instructions below and ensure you check the output at every step.

Note: Make sure you have installed MySQL on your local machine and set up the admin user. In this lab, to keep it simple, you are going to begin with
the root user with credentials. The root user by default has the password which is either password or <blank>. In case of a blank password, simply
press Enter. The password will not be visible on screen as it’s being typed.

This is part three of the final assessment and it deals with utilizing JavaScript functionalities. It will include changes in the view logic and the
booking template created for processing the booking form data.

Steps
Step 1:

Run the following command to activate the virtual environment:

pipenv shell

Note: Make sure you run the command in the main working directory containing the manage.py file.

Step 2:

To make sure you have the necessary dependencies in place, run the following commands inside pipenv:

pipenv install django

pipenv install mysqlclient

Step 3:

Make sure you check the code inside all the supporting files you will need for the exercise. It includes a few changes from the endpoint of part two.

Step 4:

In the terminal run both commands to perform the migrations.

Note: Make sure you have created the correct MySQL user, assigned privileges, and configured the same database before you perform the migrations.

Run the necessary commands to make sure the user is created and can access the database. In case you are using the root user, make sure you have the
correct password for the root user added inside the settings.py file

Note: The migrations performed here are not necessary as the changes are already in place. It is however a good practice to perform migrations before
you begin working on a new code block.

Step 5:

Open the file views.py and create a view function called bookings() below the @csrf_exempt decorator. Pass a request object to it as an argument.

Note: The necessary imports are already added inside the views.py file. URL configurations are already in place at the app-level urls.py file for the
view function.

Step 6:

Inside the view function bookings(), add the following pseudo code:

If value of request.method is equal to “POST”

Create a variable called data and assign it the value of json.load() with the request object passed as an argument.

Create a variable called exist and assign the following value to it:

Booking.objects.filter(reservation_date=data['reservation_date']).filter( )

Add the code below inside the filter() function above as an argument:

Create a variable reservation_slot and assign the value:

data['reservation_slot']).exists()

If the value of the exist variable is False:

Create a variable called booking and assign the value of the Booking() class object with the following code passed inside it:

first_name=data['first_name'],

reservation_date=data['reservation_date'],

reservation_slot=data['reservation_slot'],

Call the save() function over the booking variable using the dot operator.

Else return HttpResponse() with the following arguments passed inside it:

"{'error':1}" as a string

Variable content_type with the value equal to 'application/json'

Create a variable called date and assign it the value:

request.GET.get('date',datetime.today().date())

Create a variable called bookings and assign it the value:

Booking.objects.all().filter(reservation_date=date)

Create a variable called booking_json and assign it the value:

serializers.serialize('json', bookings)

Return HttpResponse() with the following arguments passed inside it:

booking_json

Variable content_type with the value equal to 'application/json'

Step 7:

Save the views.py file and ensure the code has no errors and that you have followed the pseudo-code accurately.

Step 8:

Now step inside the book.html file and observe the code. There are three code blocks that you need to complete marked inside comments like:

<!-- Part 1 -->

You will be replacing the comments with the pseudo-code as specified in following four steps below.

Step 9 (for part one):

Observe the code added inside the paragraph tag for the first name and replicate the code for the reservation date to replace the code block.

Step 10 (for part two):

Call a function getElementById() over the document with ‘reservation_date’ passed inside it as an argument.

Continue on the same block of code and call the function addEventListener() on it as a suffix using dot operator and pass the following arguments to
it:

‘change’

function that contains the code: {getBookings()}

Step 11 (for part three):

Run a for loop on the constant data. Use a temporary variable called item to run the loop. Add the code inside the curly braces as follows:

Call a log() function over the console and pass item.fields as an argument

Call a push() function over reserved_slots array and pass the item.fields.reservation_slot to it as an argument

            Update the bookings string variable with the code below:

`<p>${item.fields.first_name} - ${formatTime(item.fields.reservation_slot)}</p>`

Step 12 (for part four):

Create a variable called slot_options and assign the following string to it:

'<option value="0" disabled>Select time</option>'

Run a for loop for numbers greater than 10 and less than 20 and add the following code inside the curly braces:

Create a constant called label and assign the function formatTime() to it with i passed inside it as an argument.

If value of reserved.slots.includes(i) is true add the code:

slot_options += `<option value=${i} disabled>${label}</option>`

Else, add the code:

slot_options += `<option value=${i}>${label}</option>`

Note: Make sure all the code blocks have appropriate curly braces where necessary.

Step 13:

Save the file and make sure there are no visible errors inside your HTML file.

Now open the Terminal inside VS Code and add a command to run the server and go to the localhost URL and observe the web page.

Step 14:

Enter your name in the text box and select a date and time of your choice to create a reservation.

The screen should appear similar to the screen below:

Form for making reservations with name, reservation date and time fields and booking entries present
Step 15:

After selecting the options and pressing the Reserve Now button, you should be able to see the screen updated with your details. Note the times
selected earlier are not available for selection.

Form displaying drop down option for selecting reservation time.
Step 16:

Note the change in the content displayed on the screen as per the change in the date selected:

Form with fields for reservation and form entries present for a different date.
Step 17:

Open the MySQL database and observe the entries updated in line with the changes in the reservations performed inside the template.

Conclusion
Part three of the final assessment utilized the functionalities of JavaScript to dynamically process the available time slots and refresh the
available updated times. It also provides an update to dynamically reload the template based on date change. You have successfully implemented the
Django final assessment to create a reservation form and add JavaScript functionalities to dynamically update a form in a Django project. 

