# Final Project

## Explanation of the app

The application is a Fantasy Football app 

The users have to sign up with a username and password

When the users sign in, they can pick a football team 
choosing players from a list of options.

When the users sign in again, they will be able to see the 
football team that they saved the last time.

The users will be able to pick a different team that would replace
the previous one.

## Database

The database has 3 tables:

1. Users: storing user name, password and user id

2. Teams: storing the team id, team name, players, and 
the user id that will link the Users table.

3. ID: it will store temporary data that I need to access in different parts
of the app, like user id and user name.

## Technical description

This project was made with containerization technology, using 3 Docker images:

1. Web application: a Dockerfile was used to run a container for the web app, 
deploying the application on the browser, on port 5000.

2. Database: a mysql image was used to create a database.

3. A phpMyAdmin image was used as a database administration tool to be able to manage 
the database using a graphical interface that was accessed on port 8080 on the browser.

A Docker compose file was used to define and run the Docker containers with a single command 
using a configuration file where the 3 different services were declared.

Finally, a Multibranch Pipeline was built using Jenkings, committing it to my project’s 
source control repository in Git Hub. A Jenkinsfile was created defining the Pipeline build process.

## Testing

I made a unit test to check that a part of the application was operating in the right way. 

This helped me to isolate what was broken in my application to fix it faster.

## Video recording

Link to the video that shows the app, hosted on Google drive: 

https://drive.google.com/file/d/16GWb8RL_j1Gro3mufE7fvGI4aPYKTowc/view?usp=sharing
