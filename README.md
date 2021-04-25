# LibraryManagementSystem

### Django Project

### Made by: Vaibhav Agarwal

The Project is hosted on Heroku at http://vaibhavlib.herokuapp.com/

(Note: I have not committed the changes that I had to make to host it on Heroku)

Admin can make a user a librarian by assigning the user staff member and the group Librarian using the Admin Portal.

A Librarian can edit the books from the Admin Portal.

The project has the following pages

**/**

This is the Home Page where the user can see all the book, newly arrived books, and popular books. The user can also 
Search for a book by mentioning either its Title, Publisher, Author, Genre or ISBN code.

**/admin**

This is the Default Admin Portal.

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

**DataBase**

There are 3 custom classes :

* Book

* Request

* Rating

