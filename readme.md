# CoffeChoice

[![Build Status](https://travis-ci.org/djjtyn/ms4.svg?branch=master)](https://travis-ci.org/djjtyn/ms4)

# Overview
For my final milestone project I have chosen to create a django ecommerce site for Nespresso coffee pods.<br> 
Users are able to purchase a wide range of Nespresso coffee capsules and have them delivered to their home address. Users can also leave coffee reviews for each individual coffee for other users of the site to see. The purchases are done via Stripe.<br>
Included on this site is also a coffee blog which publishes blog posts made by the site owner which users will be able to read posts on. Users can also leave comments for each individual blog post for other users of the site to see.<br> 
All the media and static files I have stored using cloud storage by making use of Amazon’s S3 service.<br> 
Admin login for this site as as follows:<br>
User:admin<br>
password:password12345<br>
I have coded the site so that it allows transactions to be made using a test bank card. These card details are:<br>
Card Number: 4242424242424242<br>
CVV: Any 3 digit number<br>
Expiry Date: Any date in the future<br>
The deployed site can be found here: https://coffechoice.herokuapp.com/

# UX
This website is designed for people who have nespresso coffee machines and want to purchase or find out 
information on coffee capsules which can be used in their machine.<br> 
If a user has an opinion on a coffee capsule available on the site, they can choose to post a review in which they can express their opinion or if a user is curious about what a coffee is like, then they can read the reviews left by other users.<br>
The site is also designed for people who are interested in developments in the nespresso coffee industry by 
allowing the site owner to post blog posts which users can leave comments under.

## User Stories
As a user I am looking to purchase coffee capsules for my Nespresso machine. I can use this website to select 
various coffee capsules which I can add to my cart and then purchase.<br>
As a user, I am looking for a particular coffee capsule to purchase. I can use the search bar to filter the coffee to only show the coffee that matches my search query.<br>
As a user I am only looking for coffees in the Vertuo range. I can click the vertuo range button to filter the coffee listing to only show those listed in the vertuo range of coffees.<br>
As a user I am only looking for coffees in the Original range. I can click the original range button to filter the coffee listing to only show those listed in the  original range of coffees.<br>
As a user, I have an opinion on a particular coffee capsule available on the website. I can choose to leave a 
review of this coffee.<br>
As a user I am curious about what a particular coffee is like. I can find out by going to the coffee review page 
to check if any other user has left a review which I can read.<br>
As a user, I want to keep up to date with developments in the coffee world and am looking for something to read about coffee. I can do this by viewing the blog section of the site.<br>
As a user, I want to express an opinion I have on a particular blog post. I can do this by posting a comment 
underneath the blog post.

## Owner Stories
As site owner, I want to update the site to include newer coffees as they become available or edit an existing 
coffee on the site. I can do this by logging into the django admin page and adding or editing a coffee which will then be visible on the live site.<br>
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
### All Coffee(Mobile)
![image](static/wireframes/all_coffee(mobile).png)
### All Coffee(Desktop)
![image](static/wireframes/all_coffee(desktop).png)
### Coffee Review(Mobile)
![image](static/wireframes/coffee_review(mobile).png)
### Coffee Review(Desktop)
![image](static/wireframes/coffee_review(desktop).png)
### Blog-listings (Mobile)
![image](static/wireframes/allblogposts(mobile).png)
### Blog-listings (Desktop)
![image](static/wireframes/allblogposts(desktop).png)
### Blog-post (Mobile)
![image](static/wireframes/blogpostdetail(mobile).png)
### Blog-post (Desktop)
![image](static/wireframes/blogpostdetail(desktop).png)
## Add comment/review (Mobile)
![image](static/wireframes/addreview_comment(mobile).png)
## Add comment/review (Desktop)
![image](static/wireframes/addreview_comment(desktop).png)
<br>
For the background image I chose a colour which I thought represented the colour of coffee mixing with milk. I used this colour as I thought it to be very fitting to the theme of the site.<br>
When the user hovers over each headings icon in the navbar, the icon colour changes to a yellow colour. I chose yellow due to the cart quantity number being yellow as well. The navbar branding changes to a blue colour when hovered over to distinguish this from the other navbar options.<br>
I chose a black background for the authorisation forms as I thought it clearly distinguishes where on the page the form is. I decided to center these forms to allow it to be easier for the user to see where they have to input their information.<br>
Each coffee and blog are contained within cards. These cards have their own background colour which is similar to the main background colour except it's reversed to show the lighter colour on top. I chose to do this as I thought it clearly separated each card's containment area from the background.<br>
For the coffee cards, I chose to show 9 cards at a time when they are shown on the all_coffee page. This was so the page wouldn’t appear too crowded and I have coded pagination buttons to allow the user to go to the previous and next pages which then show another 9 coffee cards when available.<br>
I have enabled four filters on the all_coffee page to filter the coffees. Three of these filters are buttons showing either the full selection of coffees, the original range of coffees or the vertuo range of coffees. I decided to use buttons for this as it makes the site more interactive for the user. The fourth filter is a search filter which is an input field which allows the user to type in the name of a coffee. If there are no results for the query the user is directed to a page which shows that there were no matches found for their search.<br>
The Coffee review pages show a bigger version of whichever card was clicked on to show the review for. There is an add review button below this which when the user clicks on they are taken to a page with a large text area in which they can type text. If there are no reviews yet on the page the user will see the default text ‘be the first to add a review’ which should hopefully entice the user to click the add review button to populate the review area. Once there is a review left this default text is removed and in place will be the reviews which have been left by the user. The layout structure of the review is the time the comment was posted at the top, followed by the name of the user that posted the review and the review itself below this. I chose this layout as I thought it looked like a good way of presenting the information. This is the same layout as the blog post comments section of the site.<br> 
The user cannot post a comment/review unless they are logged into the site. This is so that the comment will automatically pick up the users username to populate their review with. 

# Features
## Existing Features
### User Authentication
This site allows users to register, log in, log out and reset passwords for their accounts.<br>
The benefits for a user of signing are that the user can then purchase coffee capsules. When a user is signed they can also post coffee reviews and post blog comments.

### User Purchases
This site allows users to make purchases for coffee. The purchases are done via Stripe and the user types in their bank card which they want to use.

### Cart
This site allows users to add coffee to a virtual cart which they can choose to amend or purchase.

### Blog
This site has a blog section in which users can read posts created by the site owner. I did not allow users of the site to create a blog as I wanted this to only be an admin feature, but users can post comments under each blog post if they are signed in.

### Coffee Reviews
The site has a review page for every coffee in the database. Users can leave their own reviews in this section of the site or read reviews left by other users of the site.

### Search Bar
The search bar allows the user to search the coffee database for a coffee which matches their search query which will then be shown below the search bar. If there are no search results the user is directed to a page showing that there have been no results for their query.

### Filters
There are two different coffee types available for purchase on the site. These are Vertuo and Original ranges.<br>
When the user goes to look at the coffee on the website they will firstly see a coffee database which consists of all the coffee available on the website. If they only want to see Vertuo range coffees they can click on the vertuo range button which will filter the results to show only the Vertuo range coffees. This also applies for the Original range and there is a corresponding button for this as well.

### Pagination
Each page for coffee listings and blog posts only shows 10 results per page. The user can navigate to the next/prev pages by clicking on the numbers shown below the content. These numbers represent the different page numbers and the current page the user is on is highlighted.

### Navigation Bar
The navigation bar has headings on both the left and right of the screen. Some of the headings differ depending on whether a user is logged in or out of the site. When the user isn’t signed in the navigation bar has ‘coffee’, ‘blog’, ‘cart’, ‘login’ and ‘register’ on the left hand side.<br>
By clicking the ‘coffee’ heading the user is taken to a page which lists all of the coffees available for purchase on the site.<br>
By clicking the ‘blog’ heading the user is taken to a page which lists all of the blog postings the site has from which they can click into individual postings to get more information on it.<br>
By clicking the ‘cart’ heading the user is taken to a page which lists all of the items they have added to their cart.<br>
By clicking the 'login' heading the user is taken to a page which contains a login form which requests their username and password.<br>
By clicking the 'register' heading the user is taken to a page which contains a registration form which requests the a user to input a username, their email address, a password and a password confirmation<br>
When a user is logged in all the headings remain the same except for the login and register headings which are removed. In place of these is a logout heading which when clicked will log the user out of their session.

### Admin Features
When logged into an admin account, the admin can add/edit coffees and blogs shown by navigating to the django admin section and doing it from there once logged in. 

### User Features
When a user is logged in they can post comments on both the coffee review pages and blog posts.<br>
They can also purchase products from the site. If a user doesn’t have an account they will not be able to post comments or purchase products until they register and login.<br>
The site allows users to log in and out of the website. The site will remember all of the items the user previously put into their cart if they close the window without logging out. 

### Amazon S3 Bucket
When an image is uploaded via the django admin page it is stored in a Amazon S3 bucket contained in the cloud.<br>
All the static files are also stored in the bucket.

### Google Maps API
I have made use of the Google Maps API to allow a map to be shown in the sites footer. This map marks the company's location with a marker.

## Future Features
### User Purchase History
A user purchase history page could be added to the site as a future feature. This will allow the logged in user to see which coffees they had purchased previously. I started coding this application but didn't get enough time to finish the code for it.

# Technologies Used
* HTML: This project uses HTML to provide the structure of the page.
* CSS:This project uses CSS to provide styling for the HTML.
* Bootstrap: I have used bootstrap in this project to help provide further structure to the page and aid the responsive design aspect of the site.
* Amazon S3: This project makes use of Amazon S3 to store data such as media and static files in the cloud.
* Font Awesome: I have made use of FontAwesome to attain some of the icons used for the project.
* JQuery: I have made use of jQuery in this project.
* Javascript: I have made use of Javascript in this project.
* Google Maps API: This project makes use of the Google Maps API to show the location of the business in the sites footer.
* Django: This project uses the django framework to connect the html templates, views, urls, models and forms.
* Python3: I have used Python a lot for this project.Python is used to redirect users to particular pages when forms are submitted or buttons are clicked making use of views and functions coded with Python in the django framework. I have also used Python to create models and forms in addition to creating tests for each django part. I have created local environment variables using python.
* Travis: I have used Travis CI to test the projects code
* Heroku: This project has been deployed to Heroku.

# Testing
## Code Validation
HTML Validation was done using the validator found at "https://validator.w3.org/". These tests only failed when the validator tried to validate the code used for django such as for loops and variables. All the HTML tested fine.<br>
CSS Validation was done using the validator found at "https://jigsaw.w3.org/css-validator/". This validation test returned no errors.<br>
Python Validation was done using the Python validator found at https://extendsclass.com/python-tester.html. This validation test returned no errors.

##  Responsive Design
I have ensured that the site works well on all screen sizes by making use of the Bootstrap grid system. I have tested this using Google Dev tools and checked what the site looks like on screens of different sizes.

##  Stripe
I have tested that Stripe is taking payments effectively by using a test card whilst running Stripe in test mode. The card details I have been using are:<br>
Number:4242424242424242<br>
CVV: any 3 digits<br>
Expiry: Any date in the future<br>
These test transactions worked fine.

## Coffee/Blog Posting
I tested that the website owner can upload and edit blog and coffee posts by signing into the django admin panel and uploading new coffees and blogs which worked fine.

## Comments on Blog Posts/ Reviews on Coffee Page
I tested that the user can post comments on both the individual blog post and coffee review pages by signing in with different usernames to see if the comments were posted successfully. I saw that the comments were successfully posted with the logged in user as the comment author.

## Page Redirects/Template Rendering
I tested the site to make sure that the user will be directed to the appropriate page when actions are taken by the user using the site. These all tested fine.

## Search Bar
I had to test the search bar to make sure that if a user typed the name of a coffee into the search bar that this coffee would then be shown to the user. I tested this by typing a coffee name I knew existed into the searchbar and submitting the query to see if the results showed this coffee. This tested fine.<br>
I also had to test to make sure that if there was no match for the query the user typed into the search bar, that they would be presented with a page showing there were no results found. I tested this by typing a coffee name and text that was not a coffee into the search bar to see what happened. This also tested fine.

## Filters
I had to test to make sure all the coffee filter buttons were working. I tested the all coffee filter button by clicking it and ensuring the page then showed every single coffee in the coffee database which tested fine. I tested the Vertuo Range button by ensuring when a user clicks it that they are only shown the Verto range coffees which tested fine. I tested the Original Range button by ensuring when a user clicks it that they are only shown the Original range coffees which tested fine.

## Django Testing
I tested a lot of the code using django testing methods. These tests were done on the models, views and forms. I wasn’t able to get 100% coverage in these tests and was unsure of how to code the test files to ensure I was getting close to 100%.

## Travis CI
I have used Travis CI to test the projects code.

# Bugs
If the user attempts to purchase something when their cart has less than 50c worth of items in it the site crashes. This is due to Stripe requiring the amount to be at least €0.50 eur in order to process a payment.<br>
The password reset email is not being sent. This is due to compatibility issues between the versions of Django and Python I have in the project. <br>
I have not come across any other bugs in the code yet.

# Deployment
Since deploying I have changed the environment's secret key so it is not contained in any github pushes.<br>
I have been regularly adding and committing changes to the projects local repository and pushing these to Github. I have used Gitpod entirely for coding and have been pushing any additions I make to the local repository onto Github as a precaution in case the changes didn't save in the project workspace so there are no differences between the deployed version and the development version.<br>
I have deployed this site on Heroku. The Heroku URL for this project is :https://coffechoice.herokuapp.com/<br>
To clone or download the code used to create the site, you can find it on github here:https://github.com/djjtyn/ms4
choose the option to either download or clone and follow the instructions on screen. The project dependencies are boto3, botocore, dj-database-url, Django, django-forms-bootstrap, django-storages, docutils, gunicorn, jmespath, Pillow, psycopg2, pytz, s3transfer and stripe to run so these will also need to be installed by the code editor in the terminal window to run as designed.<br>
For media and static files storage, I have used a bucket I created in Amazon S3 which stores all data in the cloud.

# Credits
## Media
I do not own any of the rights to any of the pictures used on this website. All of the coffee pictures I got from Ebay and Amazon.<br>
The blog pictures I got from using Google.

## Content
I have used a Nespresso coffee book to get coffee details for each coffee which I have used in the coffee listing information.

## Acknowledgement
* Amazon S3: I am using an Amazon S3 bucket to store all of the media and static files on the cloud.
* Stack Overflow: I used a lot of information on Stack Overflow to allow me to enhance the site's functionality.
* Code Institute: I have used a lot of code I have learned using the Code Institute full stack frameworks module.























