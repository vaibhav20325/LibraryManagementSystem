# LibraryManagementSystem

### Django Project

### Made by: Vaibhav Agarwal

The Project is hosted on Heroku at http://vaibhavlib.herokuapp.com/

(Note: I have not committed the changes that I had to make to host it on Heroku)

The Admin has username admin and password admin

There are 5 users user1, user2, user3, user4, user5 with passwords pass1, pass2, pass3, pass4, pass5 respectively.

User 1 is a Librarian.

I haven't given hyperlinks for all the pages on the site so the user would have to use the given urls

Admin can make a user a librarian by assigning the user staff member and the group Librarian using the Admin Portal.

A Librarian can edit the books from the Admin Portal.

The project has the following pages

**/**

This is the Home Page where the user can see all the book, newest arrivals, and popular books. The user can also 
Search for a book by mentioning either its Title, Publisher, Author, Genre or ISBN code. Currently the Search would 
look for exact matches in the database.

http://vaibhavlib.herokuapp.com/

**/admin**

This is the Default Admin Portal. Only the Admin and Librarians can access this page. Admins can access everything on
this page but the Librarians can only access and edit the Books.

http://vaibhavlib.herokuapp.com/admin/

**/register**

This is the registration page where a new user can register.

http://vaibhavlib.herokuapp.com/register/

**/login**

This is the login page where existing users can login.

http://vaibhavlib.herokuapp.com/login/

**/logout**

This logs out the user and redirects the user to the Home Page.

http://vaibhavlib.herokuapp.com/logout/

**/review**

This is the page where Librarians or admin can see all the Pending requests and either Accept or Reject them.
This page is only visible to staff members, so only the users having staff status can access this page.

http://vaibhavlib.herokuapp.com/review/

**/{book_id}**

There exists a page for every book where all the details of the book can be seen along with its rating and reviews.
If you are an Anonymous User this is all what you will see. If you are logged in then if the book is available then 
you can request to issue it for a certain number of days by clicking the Request Button. If you have already issued
the book then you will see the Renew Button to request extension of the due date by a certain number of days. If the book 
is not available then the Request Button would not be visible. Logged in users can Rate the book and write a comment but only once.
They can see the appropriate fields only if they haven't reviewed the book yet.

Eg - http://vaibhavlib.herokuapp.com/1

**/profile**

This is the profile page where Logged in users can see their basic information, upcoming deadlines, pending requests, 
and books that they have borrowed and returned. Anonymous users can't access this page.

http://vaibhavlib.herokuapp.com/profile/

### **DataBase**

Database used sqlite3

There are 3 custom classes :

**Book**

Book Object has the following fields:
* title
* author
* publisher
* genre
* summary
* isbn
* location
* availability
* status
* date_added


**Request**

Request Object has the following fields:
* user (This is a foreign key)
* status
* r_date (request date)
* d_date (due date)
* book

**Rating**

Rating Object has the following fields:
* user (This is a foreign key)
* book (This is a foreign key)
* rating
* review

**Access Control**

I have implemented Access control by using the Django methods .is_authenticated which returns False if the user is not logged in i.e. Anonymous User
and .is_staff which checks if the user has staff access (The Librarian and Admin are the only ones with staff status) . I have used these to restrict part of the pages from the users.

**Other Stuff**

The project has two apps - main and register. Register is for the registration stuff, main is for everything else.

I have mainly used forms with POST method for all the buttons except the search button on the home page which uses GET method

I have created HTML pages for all the pages that extend from a template page base.html

The user is interacting with the pages through forms, which sends the responses to a python file view.py inside the main app, which processes these responses and make
 appropriate mmodifications.
 
 The Librarian can mark a book as lost using the Admin Portal. Currently, for a user to return an issued book, the Librarian would have to make the appropriate changes in the Admin Portal.
 
 Currently I have assumed quantity of each book as 1. So if a book is issued to a user then it automatically becomes unavailable.
 
 **Bugs**
 
 The renew system isn't working perfectly currently. I haven't taken into account random inputs by the users like requesting a book for -3 days. 
