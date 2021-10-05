# [St John's](https://high-school-manager-project.herokuapp.com/)   

![Various Devices](https://github.com/salute03/high-school-manager-project/static/img/responsive.jpg.png)

"St John's" - Practical Python and Data-Centric Development Milestone Project.

The main purpose of this full-stack MongoDB-based Flask project is to create a database for educational to allows users to create, read, update and delete (CRUD) assignments.
This web page is maily used by class teachers of  [St John's] High Shcool during the covid-19 lock down, to create Assignments for students, From which students can read the questions. At the same time, it gives the opportunity to create an account and benifit from having convenient access to all features of the website.
Registered users can add new recipes, edit and delete their own ones, as well as edit their username and password or delete account.  

---


## UX
My main goal in UX was to built a website easy to navigate, simple design and simple to use; where users can create assignments, view all the assignments created by teachers,
teachers can edit and delete their assignments. The target audience for this webpage are teachers and students of St John's High school.

### User Stories
**As a user, I want/expect:**
- to read the assignment, showing the subject, topic, questions, deu date, mark for the assignment and The teacher's name.
- to register my profile, through the register page
- to login to the webpage
- to create assignments
- to edit assignments 
- to delete assignments
- to log out
- to use the website from any device (laptop, tablet, mobile)
### Design
The goal in design was to create a website that is overall user friendly, simple to navigate and appealing to the sight.
#### Framework
[Materialize](https://materializecss.com/), front-end framework based on Material Design was chosen for this project for its modern interface and ease of use. It was used for creating features such as navbar, cards, forms, modal, as well as for its grid.  
[JQuery](https://jquery.com/) was used for initializing some Materialize elements listed above, as well as for custom functions, simple DOM manipulation.

### Wireframes
[Balsamiq Wireframes](https://balsamiq.com/) was used to create all wireframes for the project.

Initial wireframes with some comments for both desktop and mobile devices can be found [here](https://github.com/irinatu17/MyCookBook/tree/master/mycookbook/wireframes).

---

## Features
### Existing Features

#### Navbar   
The navbar is fixed at the top of the page, this allows a user to easily navigate throughout the website. The logo is located in the top right corner on a desktop. It redirects the user to the home page when clicked.
On the smaller resolutions (tablet, mobile) the navbar is collapsed into a burger icon. A slide out menu opens when the burger icon is clicked.  
The navebar holds the the Home, Log In and Register button at the top right coner before a user (teacher) is registered.

While logged in, The navebar holds the Home, Profile, Create Assignment and Log out buttons.

#### Register
It stores the registered user to the database and redirects thr user to the user's profile.


#### Profile
It holds and displays the users profile once registered.
#### Create Assignment
It displays forms for creating assignments and has a create assignment button that stores the content in the database
and displayed the created content on the home page in an acordion fron materialize.

#### Edit assignment
It displays form for editing assignments and holds an edit assignment button which edits the assignment and display the content
on the home page, it holds a cancel button which redirects back to create assignment page.

#### LogIn
It logs in a registered user, to give access to editing and deleting of assignments as well as creating assignment

#### Logout
It redirects back to home page and logout registered user.




---

## Technologies Used

- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [Am I Responsive](http://ami.responsivedesign.is/) - for creation of the images in the readme file and checking responsiveness.
- [ImgBB](https://imgbb.com/) - to host images used in README
### Front-End
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - to build the foundation of the project.
- [CSS](https://developer.mozilla.org/en-US/docs/Archive/CSS3) - to create custom styles.
- [JS](https://www.javascript.com) - to create some functionalities.
### Back-End
- [Python 3.8.2](https://www.python.org/) -  back-end programming language used in this project.
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/) - microframework for building and rendering pages.
- [MongoDB Atlas](https://www.mongodb.com/) - NoSQL database for storing back-end data.
- [PyMongo](https://api.mongodb.com/python/current/) - for Python to get access the MongoDB database.
- [WTForms 2.2.1](https://pypi.org/project/WTForms/) - for creating forms with validation.
- [Werkzeug 0.16.1](https://werkzeug.palletsprojects.com/en/0.16.x/) - to generate and verify password hashing.
- [Jinja 2.10.1](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python, to display back-end data in HTML.
- [Heroku](https://heroku.com/) - to host the project.
### Libraries
- [Materialize 1.0.0](https://materializecss.com/) - main responsive modern front-end framework used for grid and responsivesness.
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project.
- [JQuery 3.5.0](https://jquery.com/) - to simplify DOM manipulation and to initialize Materialize functions.
---

## Testing
### Manual Testing 
#### User stories testing
All the following manual testing was implemented on both desktop and mobile devices.
##### Home
The home button worked on clicked, it redirects back to he home page and it worked across all devices.
#### Register
After filling the form, On clicking the "Register" button, i was logined in as a user and a profile page was created for me.
##### Login
Clicking on the "Login" button in the navbar opens the form, allowing me to login to my account. I tried to leave empty fields or input incorrect details, but I was not able to submit the form if something was entered incorrectly. After a successful login I was redirected to the home page, seeing the message that I was logged in. 
I also checked the link to the Register page at the bottom of the form, which worked well.

##### Delete Assignment
The delete button functions correctly as it removes content from the page.

##### Edit Assignment
The edit button worked perfectly and only a registered user can edit assignment.

#### Debugger

I was manually testing the app with **debugger**: `debug=True` throughout all the development process. 
Every time when there was an error (when app crashed), the debugger displayed an error message in the terminal to the view, that allowed me to find the location of the error and fix it.


### Validators
#### Html
All the HTML files were tested through [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Since it does not recognize Jinja2 templating language, it showed a number of errors. Apart from that, no other errors were found across the html pages.
#### CSS
CSS files were tested through [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). Since it does not recognize CSS variables (I use `:root{}` for colours and fonts variables), there were several Parse Errors found.  
As well as that, there are a few error warnings for some -webkit, -moz pseudo element selectors. Both errors can be safely ignored as they are not errors in fact. The rest of the CSS files was completely valid.
#### JavaScript
JS file was tested through [Esprima](https://esprima.org/demo/validate.html) and [JSHint](https://jshint.com/) validators, code was syntactically valid.  "$" was not defined by JSHint (it is necessary for jQuery Materialize initializing).
#### Python
All python files were tested through [PEP8 Online](http://pep8online.com/) validator and were completely PEP8 compliant, 


### Compatibility and Responsiveness
This website had been being tested during the development across **multiple browsers** (Chrome,FireFox, microsoft edge) and on **multiple devices**: mobile (iPhone 5, 6, 8, Samsung Galaxy, Sony Xperia), tablets(iPad, iPadPro) and laptops 
As well as on **Google Chrome's developer tools** to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness.   
The i used **lighthouse** to test and check the performance rate of the website.
I also used [Am I Responsive](http://ami.responsivedesign.is/) online tool for checking responsiveness on different devices.   


---

## Deployment
### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE  (I used [GitPod](https://www.gitpod.io/) online IDE for creating this project)
- [MongoDB Atlas](https://www.mongodb.com/) (for creation your database)
- [Github](https://github.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python](https://www.python.org/)   
#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:   
`git clone https://github.com/salute03/high-school-manager-project`    
Alternatively, you can save a copy of this repository by clicking the green button "Clone or download" , then "Download Zip" button, and after extract the Zip file to your folder.
2. In the terminal window change directory (CD) to the correct file location (directory that you have just created).
3. Set up environment variables:
    - Create **.env** file in the root directory.
    - On the top of the file add `import os` to set the environment variables in the operating system.
    - Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax:
    `os.environ["SECRET_KEY"] = "YourSecretKey"`   
    `os.environ["MONGO_URI"] = "YourMongoURI"`  
    .
4. Install all requirements from the **requirements.txt** file putting this command into your terminal:   
`pip3 install -r requirements.txt`  
*Note: GitPod does not require `sudo`, so if you use another IDE, you will need to include `sudo` in the beginning of the command: `sudo pip3 install -r requirements.txt`.*
5. Create a new Database called "high_school_managers" in [MongoDB Atlas](https://www.mongodb.com/).   
*You can sign up for free account, if you do not have one.*
6. In "high_school_managers" database create five following collections:


```
###### assignments
```
_id: <ObjectId>
days_name: <String>
subject_name: <String>
topic_name: <String>
question: <String>
due_date: <String>
mark: <String>
created_by: <String>
```

###### Monday
```
_id: <ObjectId>
days_name: <String>
```
###### Tuesday
```
_id: <ObjectId>
days_name: <String>
```
###### Wednesday
```
_id: <ObjectId>
days_name: <String>
```
###### thursday
```
_id: <ObjectId>
days_name: <String>
```
###### Friday
```
_id: <ObjectId>
days_name: <String>
```

###### Users
```
_id: <ObjectId>
username: <String>
password: <String>
```
7. You will now be able to run the application using the following command `python3 app.py`.   

### Heroku Deployment
To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:
1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:  
`pip3 freeze > requirements.txt`
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:   
`echo web: python app.py > Procfile`
3. `git add`, `git commit` and `git push` these files to GitHub repository
4. Create a **new app** in Heroku, assigning a name (must be unique) and set a region (for my project I set Europe)
5. From the Heroku dashboard link the new Heroku app to your GitHub repository:    
    - "Deploy" -> "Deployment method" -> "GitHub"
    - then "Enable automatic deployment"
6. To start the web process, put the following command into the terminal: `heroku ps:scale web=1` to scale dynos
7. In the **Settings** tab of the new Heroku app, click on "Reveal Config Vars" and set the following config vars:
    - **IP** : 0.0.0.0
    - **PORT** : 5000
    - **MONGO_URI** : `<link to your MongoDB database>`
    - **SECRET_KEY** : `<your secret key>`
    - **DEBUG**: **FALSE**  
*Note: your MONGO_URI and SECRET_KEY must match the ones you entered in .env.py file*

8. The app will be deployed and ready to run. Click "Open App" to view the app.   

**Note**: if you have not linked GitHub and Heroku following step N.5, alternatively as the last step of deployment, you can put the following command into your terminal:   
 `heroku login`, after a successful log in `git push heroku master` - to push the app to Heroku, and finally click "Open App" in Heroku dashboard to view the app.

---

## Credits
 I received inspiration for this project from a task manager project in the Code Institute module.
 Most of the codes in python are from Tim Nelson  (the instructor of the Task manager project in code institue module).
 Most of the codes in style.css was written by me. 


### Acknowledgements
 Code Institute tutors, fellow students, my friends and my family for the time, assistance and support!
 Slack Community
 my Mentor Marcel Mulders for his deepest support.
 
---

**This project is for educational use only.**
