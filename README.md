# LibraryManagementSystem

### Django Project

### Made by: Vaibhav Agarwal

The Project is hosted on Heroku at http://vaibhavlib.herokuapp.com/

(Note: I have not committed the changes that I had to make to host it on Heroku)

Admin can make a user a librarian by assigning the user staff member and the group Librarian using the Admin Portal.

A Librarian can edit the books from the Admin Portal.

The project has the following pages

**/**

This is the Home Page where the user can see all the book, newest arrivals, and popular books. The user can also 
Search for a book by mentioning either its Title, Publisher, Author, Genre or ISBN code.

**/admin**

This is the Default Admin Portal. Only the Admin and Librarians can access this page. Admins can access everything on
this page but the Librarians can only access and edit the Books.

**/register**

This is the registration page where a new user can register.

**/login**

This is the login page where existing users can login.

**/logout**

This logs out the user and redirects the user to the Home Page.

**/review**

This is the page where Librarians or admin can see all the Pending requests and either Accept or Reject them.
This page is only visible to staff members, so only the users having staff status can access this page.

**/{book_id}**

There exists a page for every book where all the details of the book can be seen along with its rating and reviews.
If you are an Anonymous User this is all what you will see. If you are logged in then if the book is available then 
you can request to issue it for a certain number of days by clicking the Request Button. If you have already issued
the book then you will see the Renew Button to request extension of the due date by a certain number of days. If the book 
is not available then the Request Button would not be visible. Logged in users can Rate the book and write a comment but only once.
They can see the appropriate fields only if they haven't reviewed the book yet.

**/profile**

This is the profile page where Logged in users can see their basic information, upcoming deadlines, pending requests, 
and books that they have borrowed and returned. Anonymous users can't access this page.

###**DataBase**

There are 3 custom classes :

* **Book**



* **Request**

* **Rating**

