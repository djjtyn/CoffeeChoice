# MS4

[![Build Status](https://travis-ci.org/djjtyn/ms4.svg?branch=master)](https://travis-ci.org/djjtyn/ms4)

# Overview
For my final milestone project I have chosen to create an django ecommerce site for Nespresso coffee pods. Users 
will be able to purchase a wide range of Nespresso coffee capsules and have them delivered to their home address. 
The purchases are done via Stripe. Included on this site is also a coffee blog which users will be able to read posts on. Users can also leave comments for each individual blog post for other users of the site to see. Users can also leave coffee reviews for each individual coffee for other users of the site to see. 
All the media and static files I have stored using cloud storage by making use of Amazon’s S3 service. 
Admin login for this site as as follows:
User:admin
password:password12345
The deployed site can be found here: https://coffechoice.herokuapp.com/

# UX
This website is designed for people who have nespresso coffee machines and want to purchase or find out 
information on coffee capsules which can be used in their machine. If a user has an opinion on a coffee capsule 
available on the site, they can choose to post a review in which they can express their opinion or if a user is 
curious about what a coffee is like, then they can read the reviews left by other users.
The site is also designed for people who are interested in developments in the nespresso coffee industry by 
allowing the site owner to post blog posts which users can leave comments under.

## User Stories
As a user I am looking to purchase coffee capsules for my Nespresso machine. I can use this website to select 
various coffee capsules which I can add to my cart and then purchase.
As a user, I am looking for a particular coffee capsule to purchase. I can use the search bar above the area 
showing all the coffee available to filter the coffee to only show the coffee that matches my search query.
As a user I am only looking for coffees in the Vertuo range. I can click the vertuo range button above the 
search bar to filter the coffee listing to only show those listed in the vertuo range.
As a user I am only looking for coffees in the Original range. I can click the original range button above the 
search bar to filter the coffee listing to only show those listed in the  original range.
As a user, I have an opinion on a particular coffee capsule available on the website. I can choose to leave a 
review of this coffee.
As a user I am curious about what a particular coffee is like. I can find out by going to the coffee review page 
to check if any other user has left a review which I can read.
As a user, I want to keep up to date with developments within the coffee world. I can do this by viewing the blog 
section of the site.
As a user, I am looking for something to read about coffee. I can go to the sites blog page and browse the blog 
posts.
As a user, I want to express an opinion I have on a particular blog post. I can do this by posting a comment 
underneath the blog post.

## Owner Stories
As site owner, I want to update the site to include newer coffees as they become available or edit an existing 
coffee on the site. I can do this by logging into the django admin page and adding or editing a coffee which will then be visible on the live site.
As site owner, I want to add blog posts to the site. I can do this by logging into the django admin page and 
adding a blog post which will then be visible on the live site.

## Wireframes
### Login(Mobile)
![image](static/wireframes/Login(mobile).png)
### Login(Desktop)
![image](static/wireframes/Login(desktop).png)
### Register(Mobile)
![image](static/wireframes/Register(Mobile).png)
### Register(Dekstop)
![image](static/wireframes/Register(Desktop).png)
### Index(Mobile)
![image](static/wireframes/index(mobile).png)
### Index(Desktop)
![image](static/wireframes/index(desktop).png)
### all_coffee(Mobile)
![image](static/wireframes/all_coffee(mobile).png)
### all_coffee(Desktop)
![image](static/wireframes/all_coffee(desktop).png)
### coffee_review(Mobile)
![image](static/wireframes/coffee_review(mobile).png)
### coffee_review(Desktop)
![image](static/wireframes/coffee_review(desktop).png)
### blog-listings (Mobile)
![image](static/wireframes/allblogposts(mobile).png)
### blog-listings (Desktop)
![image](static/wireframes/allblogposts(desktop).png)
### blog-post (Mobile)
![image](static/wireframes/allblogpostdetail(mobile).png)
### blog-post (Desktop)
![image](static/wireframes/allblogpostdetail(desktop).png)
## add comment/review (Mobile)
![image](static/wireframes/addreview_comment(mobile).png)
## add comment/review (Desktop)
![image](static/wireframes/addreview_comment(desktop).png)








