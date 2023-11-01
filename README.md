# Blogi

Welcome,

This project is created for users to share their experiences in the world. Are you traveling, hiking, partying or other activities? You are free to share it with friends, family or anyone by introducing them to this website.
On our website you can like and comment on your posts and other people posts. You can also update your image and details.

[Live project here](https://blogi-177f0953c4d1.herokuapp.com)

## Table of Contents

- [Blogi](#blogi)
  - [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
    - [Strategy](#strategy)
    - [User Stories](#user-stories)
    - [Admin Stories](#admin-stories)
  - [Scope](#scope)
  - [Featues](#featues)
  - [Future Features](#future-features)
  - [Testing](#testing)

## User Experience

### Strategy
This site was created respecting the Five Planes Of Website Design:

### Project Goal
Create a website for the owner and users.

Project Objectives:

- To create a website with a simple and intuitive User Experience;
- To add content that is relevant and helps create a better image of the owner of the website and the users as well;
- To differentiate between users and staff members accounts;
- To implement fully functional features that will make users achieve their goals of sharing ideas and reacting to other users posts;
- To make the website available and functional on every device.

### User stories

As a user I would like to be able to...

- View the list of posts so that I can select one to read
  
- Click on a post and read the full text

- View the number of likes on each post so that i can see which is the most popular or most viral

- View comments on an individual post so that i can read conversations

- Register an account to be able to like and comment

- Make a post on any topic

- Manage my post. I can edit, update or delete my post

- Create profile and view other users profile

- Edit and update my profile

### Admin stories

As an admin I would like to be able to...

- Create, read, update and delete posts so that i can manage the blog contents

- Create draft posts so that i can finish writing the content later

- Approve or disapprove comments so that i can filter our objectionable comments

- View the number of likes on each post so that i can see which is the most popular or most viral

- View comments on an individual post so that i can read the conversation

- Delete a post from the home page when i am signed in


### Agile Methodology

This project was developed using the Agile methodology.
All epics and user stories implementation progress was registered using Github. As the user stories were accomplished,
they were moved in the Github board from To Do, to in-progress and Done lists.

![User stories](media/images/userstories.png)


### Featues
* Colour Scheme
  * Simple colour scheme was used during the development of this project
  * Constrting colours for easy legibility and style
  Colour scheme used are:
  #212529 
  #234E5A 
  #107C7C 
  #3FAA85 
  #F9FAFC 
  #ff0000

* Fonts used are Roboto and Lato. Sans-serif was used as an alternative

* Pages were planned out on [Figma](https://www.figma.com) using wireframes


* Logo
  * The logo is a simple word which demonstrates the intent of the website
  * The logo serves as a link to return to the home page
  
  ![Logo](media/images/logoimage.png)

* Base Template

  * Header with navigation bar and search
  ![Header with navigation and search](media/images/navbarimage.png)

  * The navigation bar contains the links:
    * The logo - This the logo of the site owner. The logo also serves as a link to return a user back to home page
    * Home - The home link redirects the user back to the home page
    * Add Blogs - This button gives the registered user the ability to add their posts
    * Hello User - This displays the name of the registered user
    * Profile - This redirects the user to the user's profile page
    * Logout - This button logs out the user
    * Search - The search provides the ability for a user to search for a post by topic

  * Footer with social media links
  ![Footer with social media links](media/images/footerimage.png)

* Home Page
  * Introduction telling you about the site and what to do

  ![Introduction](media/images/introimage.png)

  * List of Posts to be selected from
  * Posts are ordered by the newly posted
  * On each post are the title, the author's name, the date and time of post, the content of the post.
  Also, there are two buttons that displays the ability to like and comment on a post. It shows the counts on likes and comments.
  Still on each post there is a readmore button that redirects the visitor or user to another page where the full post is displayed.
  * Pagination - The post list is paginated when more than six post loaded on page

  ![List of posts](media/images/postlist.png)

* Post Detail Page
  * The detail page displays the title at the top of the page
  * There is a profile pics of the post's author, the name and also the date and time of posts. From the author's name links a user to the author's profile page
  * By the right of the page, a registerd user can access a blue and red buttons for editing and deleting posts respectively
  * Then there is the post's image which relates to the post
  * After the image there is the content.
  * Below the content a registered user can like and comment on a post

  ![Post Details](media/images/postdetails.png)

* Create a post
  * Title - The form to create the post provides an input that takes the title of the posts
  * Slug - This input requests the user to copy the title and paste here since this will be used in the url to represent the post
  * Content - This takes the content of the blog from the user
  * Image - This provides the ability for the user to upload an image
  * Post button - This submits the post to the database as well as displays post on home page

  ![Create a post](media/images/createform.png)

* Profile
  * On the profile page there is an image holder for the user's profile photo.
  * Then there is a list of the user's details
  * There is an edit button that enables the users to edit and update their profiles

  ![Profie page](media/images/createform.png)

* Update profile
  Users can edit and update their profile

  ![Edit Profile](media/images/editprofile.png)

* User's Profile
  Both registered and unregistered user can access profiles

  ![User's Profile](media/images/userprofile.png)

* When a user or admin intends to delete posts, the user will be asked to be sure before deleting
![User's Profile](media/images/deletewarning.png)


* Account pages

  * Login logout and signup pages connected with allauth

* Messages

  * Review submission, sign in and out message confirmation
  * Times out after 3 seconds

## Testing

## Deployment
### Deploy on Heroku
 1. Create Pipfile 
 
 In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all requirements will be created. 
 
 2. Setting up Heroku

    * Go to the Heroku website (https://www.heroku.com/) 
    * Login to Heroku and choose *Create App* 
    * Click *New* and *Create a new app*
    * Choose a name and select your location
    * Go to the *Resources* tab 
    * From the Resources list select *Heroku Postgres*
    * Navigate to the *Deploy* tab
    * Click on *Connect to Github* and search for your repository
    * Navigate to the *Settings* tab
    * Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.    

3. Deployment on Heroku

    * Go to the Deploy tab.
    * Choose the main branch for deploying and enable automatic deployment 
    * Select manual deploy for building the App 
    
### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
- On [My Repository Page](https://github.com/chikadim/blogi), press <i>Fork</i> in the top right of the page
- A forked version of my project will appear in your repository<br></br>

### Clone the repository
For creating a clone of the repository on your local machine, use<b>Clone</b>:
- On [My Repository Page](https://github.com/chikadim/blogi), click the <i>Code</i> green button, right above the code window
- Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL
- Your clone was created
<hr>

## Credits
### Content
* The contents of the posts were [Open AI](https://www.openai.com) 
### Media
* All images were gotten from [Unsplash](https://www.unsplash.com)
### Code
* Code Institute tutorials
* [Stack overflow](https://www.stackoverflow.com)
* [More inspiration](https://data-flair.training)
