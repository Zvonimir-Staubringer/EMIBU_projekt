
IEEE 830-1998 Software Requirements Specification

## TITLE: "EMIBU: Design made with love!"

# Table of Contents

1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
   1. [Product Perspective](#21-product-perspective)
   2. [Product Functions](#22-product-functions)
   3. [User Classes and Characteristics](#23-user-classes-and-characteristics)
   4. [Operating Environment](#24-operating-environment)
   5. [Design and Implementation Constraints](#25-design-and-implementation-constraints)
   6. [User Documentation](#26-user-documentation)
   7. [Assumptions and Dependencies](#27-assumptions-and-dependencies)
3. [Specific Requirements](#3-specific-requirements)
   1. [Functional Requirements](#31-functional-requirements)
      1. [Guest User Requirements](#311-guest-user-requirements)
      2. [Registered User Requirements](#312-registered-user-requirements)
      3. [Admin (Seller) Requirements](#313-admin-(seller)-requirements)
4. [System Interfaces](#4-system-interfaces)
   1. [User Interfaces](#41-user-interfaces)
   2. [Hardware Interfaces](#42-hardware-interfaces)
   3. [Software Interfaces](#43-software-interfaces)
5. [Other Nonfunctional Requirements](#5-other-nonfunctional-requirements)
6. [Other Requirements](#6-other-requirements)

## 1. Introduction

### 1.1 Purpose 

The purpose of this document is to provide a Software Requirements
Specification (SRS) for the development of “EMIBU”, a web
application that enables users to view and purchase products from the
EMIBU family store, among other features. This document describes the
requirements of the web application from the perspectives of the user,
system, and customer.

### 1.2 Document Conventions

This document is written using the IEEE 830-1998 standard for software
requirements specifications. It will include user, system, and customer 
requirements for the completion of the project. 

### 1.3 Intended Audience and Reading Suggestions

This document is intended for the developers and designers working on the
"EMIBU" project. It's recommended that readers start from the
beginning and read the document from start to finish to get a complete picture
of the project requirements. 

### 1.4 Product Scope

The scope of "EMIBU" is to create a web application that allows
users to find for available items with ease, get a full description of said
items, see their previous purchases, etc. It will also provide an easy and 
secure payment experience.

### 1.5 References 

1. IEEE 830-1998: IEEE Standard for Software Requirements Specifications (IEEE,
   1998).
2. Django 5.1. documentation

### 1.6 Overview

The "EMIBU" web application will be a platform for users see available
products, look at their past purchases and request custom projects. The 
application will also provide a secure payment system.

The sections of this document are as follows:
- Section 2: Overall Description


## 2. Overall Description

### 2.1 Product Perspective

EMIBU is a web application designed to help users see available products from
the family store EMIBU.

The user interface is designed to be intuitive and easy to use, with an Admin
dashboard, User dashboard, and a Guest dashboard. It will contain a list of 
products that EMIBU family business makes and sells. Users can click on a
particular product to see it's description and to put it into their cart.

Guest users can put items into their cart, request custom projects to be made and finish
their purchase through a payment method. Registered users additionaly are able to
see previous purchases they made. Users are notified when the purchase is complete, and the
payment is handled using a regular card payment.

EMIBU also offers the seller to add a new item to the web store.

With EMIBU, users will be able to more easily make a purchase from the EMIBU family
business while getting a quicker overview of available products.

EMIBU is a self-contained web application that will be hosted on a
web server. It will be accessible through a web browser.


  
### 2.2 Product Functions

"EMIBU" will provide the following functions:

- User Interface: Users will be able to navigate between pages on the web 
 application, view available products posted by the seller, make a request 
 for a custom project (contact the seller), see their cart and total price amount.

- Adding items to cart: Users will be able to add items to their cart through a 
 simple UI.

- Choosing delivery and completing purchases: Users will be directed to a safe payment
 method to complete their purchase before which they will choose their desired delivery
 method.

- Custom project request contact: The web application will include an option to contact the seller
 for a custom project. The payment will then have to be done in person and not through 
 the web application.

- Product listing: The web application will provide a listing of all available products 
 and their prices, which users can then add into their carts.

### 2.3 User Classes and Characteristics

The product will have three logical user classes: Admin (Seller), Registered User, 
and Guest User.
Admin (Seller) is a user class with a superuser status, and can access the Admin
dashboard. Admin (Seller) users can create, edit, delete users as well as add more 
products to the listing.

Guests users will be able to register for additional features.

#### 2.3.1 Admin (Seller)

Admin users will be able to manage the web application, including managing
users and managing products. Admin users will also be able to see all purchases made
by the Users. 

#### 2.3.2 Guest User

Users will be able to view products, add products to their cart, proceed to delivery 
and payment methods.

#### 2.3.3 Registered User

Users will be able to view products, add products to their cart, proceed to delivery 
and payment methods. Additonaly, registered users will be able to see their previous
purchases from the User Interface.

### 2.4 Operating Environment

The web application will be hosted on a web server. It will be accessible
through a web browser. 

### 2.5 Design and Implementation Constraints

The web application will be written in Python using the Django framework. It
will be hosted on a web server. The data will be stored in a SQLite database.
No further design and implementation constraints are known at this time.

### 2.6 User Documentation

No documentation will be provided to users.

### 2.7 Assumptions and Dependencies

The application will use a secure card payment method which will only request from 
a user to enter a faux credit card credentials. The complete secure payment method
is to be implemented at a later date.

The application will not have an automated quality assurance process. The application
will not provide an in app method of communicating for a Custom project request.
Further contact is to be decided between user and Admin (Seller).



## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 Guest User Requirements

##### 3.1.1.1 Guest User Registration

**Req G1** - The web application will allow users to register for an account.

The web application will allow users to register for an account. Users will
provide their name, email address, and password. The web application will
verify that the email address is unique and not already used by another user. A guest
user does not have to register to access Guest User dashboard. 

##### 3.1.1.2 Guest User Dashboard

**Req G2** - The web application will provide a dashboard for users to view 
listed products and access their shopping cart.

The web application will provide a dashboard for users to view available products
and add them to their carts. The dashboard will provoide a way to enter the cart
and complete the purchase of selected products.

##### 3.1.1.3 User Shopping Cart

**Req G3** - The web application will provide a shopping cart for users to view
and remove selected products.

The web application will provide a shopping cart for users to view and remove their 
selected products. The web application will provide the following information and 
options:

- Added Products and the number of them added
- Price of each seperate product
- Total price of all products
- Button to proceed with the payment

##### 3.1.1.4 Product listing

**Req G4** - The web application will allow users to see all available products.

The web application will allow users to see products listed by the seller. The web
application will provide the following information and options: 

- Product name
- Product description
- Product price
- Product availability
- The ability to add the product to cart

##### 3.1.1.5 Custom Project Request

**Req G5** - The web application will allow users to request a custom project.

The web application will allow users to request a custom project. Users
will access a seperate page for requesting a custom project. The web application 
will provide a form to be filled out with requested information (name, surname, email, 
description of requested project (optionally adding an image url for a similar product)).
The web application will verify that each field is not empty.

**Note:** Further contact will be continued through email or other desired channel.

##### 3.1.1.6 Payment processing

**Req G6** - The web application will allow users to complete purchases online with a 
card payment.

The web application will allow users to complete purchases online with a card payment. 
The web application will request users card information and verify the given card 
information is as per standard. 

**Constrainst and considerations:** The web application will not be responsible for users 
card information. The payment method will not be implemented due to the security risk. 
The web application will simply check if the given information is as per standard.
In this way, the application will not be responsible for the users confidential information.
All the communication between the users and the admins regarding the payment will be done
outside of the application. The admins will then confirm the purchase through the Admin dashboard.

#### 3.1.2 Registered User Requirements

Registered user requirements focus on the specific funtionalities that Users that register 
for an account will be able to use. 

Registered users use the same registration and login process as guest users. The only difference
is that registered users will use their login credentials to directly access their information,
while guest users must first register.

User interface options intented for the registered users will be visible only to users that
have gone through the registration and login process.

Guest user interface options and functions will be visible to all users,
including the registered users.

##### 3.1.2.1 User Registration

**Req R1** - The web application will allow guest users to register, allowing guest users 
to see new dashboard features.

The web application will allow guest users to go through the registration process. During
the registration process, the user will provide their name, password and email, creating 
their account.

##### 3.1.2.2 Registered User Login

**Req R2** - The web application will allow users to log in to their account.

The web application will allow users to log in to their account. Users will
provide their email address and password. The web application will verify that
the email address and password match the information in the database.

##### 3.1.2.3 Registered User Logout

**Req R3** - The web application will allow users to log out of their account.

The web application will allow users to log out of their account. Users will
click on a "Log Out" button in the Navigation. The web application will
terminate the user's session.

##### 3.1.2.4 Registered User Dashboard

**Req R4** - The web application will provide a dashboard for registered users to
view their account information.

The web application will provide a dashboard for registered users to view their
account information. The dashboard for registered users will be the same one for the
guest users described in **Req G2**. The only difference is that the dashboard for
registered users will include the following information and options:

- Access to their profile
- Viewing of previous purchases
- Viewing of requested custom projects

##### 3.1.2.5 Registered Users Profile

**Req R6** - The web application will provide a profile for registered users to
view their account information.

The web application will provide a profile for registered users to view their
account information. The profile for registered users will will include the following 
information and options:

- User information such as their name and email
- A list of previous purchases
- A list of previously requested custom projects

#### 3.1.3 Admin (Seller) Requirements

The web application will verify that the image used on a product is unique.
The web application will verify that the product price is a positive number.

Admin (Seller) requirements focus on the specific funtionalities that Admins (Sellers) will be able
to use. Admins (Sellers) are created by the system administrator in the Admin Dashboard.
The Admins use the Django Admin interface to manage the system.

##### 3.1.3.1 Admin (Seller) Dashboard

**Req A1** - The web application will provide a dashboard for admins (sellers) to
manage the system. 

The web application will provide a dashboard for admins (sellers) to manage the system.
The dashboard will use the Django Admin interface as well as allowing the admins to access 
to all features available to guest and registered users. The dashboard will allow admins 
to manage the following:

- Users (create, edit, delete)
- Products (create, edit, delete)

##### 3.1.3.2. Adding products to listing

**Req A2** - The web application will allow admins (sellers) to create a new product 
which will be displayed in the products listing.

The web application will allow admins (sellers) to create a new product. The web 
application will add the productto the database. The web application will display
 the new product in the products listing.

### 3.2 Usability Requirements

The web application will be designed to be easy to use. The web application will
be designed to be intuitive and easy to learn. 



### 3.3 Reliability Requirements

None at this time

### 3.4 Performance Requirements

None at this time

### 3.5 Supportability Requirements

None at this time

### 3.6 Design Constraints

None at this time

## 4. System Interfaces

### 4.1 User Interfaces

The application will have a user interface that is accessible via a web
browser. The interface will be designed to be intuitive and user-friendly,
optimized for mobile and desktop devices.


The web application will use a standard web interface with a top navigation bar
and a main content area. The web application will be primarily used on a
desktop computer and a responsive design is not required.

The top navigation bar will have the following links:

* On the left side:
  - Logo (link to the home page)
  - Products (a link to the Products listing page)
  - Contact (a link to the Contact page)

* On the right side:
  - Cart (a link to the Cart page)
  - Login (a link to the Login page) if the user is not logged in
  - Profile (a link to the Profile page) if the user is logged in
  - Logout (a link to the Logout page) if the user is logged in


### 4.2 Hardware Interfaces
The application will be hosted on a secure web server running on Linux or Windows.

### 4.3 Software Interfaces
The application will use Django 5.1, the database will be SQLite, frontend framework will be Bootstrap.

### 4.4 Communications Interfaces
The application will have a secure communication interface for secure data transfer.

## 5. Other Nonfunctional Requirements

### 5.1 Security Requirements
The application will use the Django's default User management system. The
application will use Django's default authentication system. The application
will use Django's default authorization system. The application will use Django's
default password reset system.

### 5.2 Safety Requirements
The application must be designed to prevent the user from performing any unsafe actions or operations.

### 5.3 Business Rules
The application will have business rules in place to ensure the safety and security of user data.

### 5.4 Quality Attributes
The application must have a high quality user interface with good usability and responsiveness. The application must also have an uptime of at least 99.

## 6. Other Requirements

### 6.1 Business Requirements

None at this time

### 6.2 Regulatory Requirements

None at this time
