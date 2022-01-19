START TRANSACTION; 
USE webapp_dbf;

DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
    user_id int NOT NULL AUTO_INCREMENT,
    user_name varchar(255) NOT NULL,
    user_password varchar(255) NOT NULL,
    PRIMARY KEY (user_id)   
);

CREATE TABLE Teams (
    team_id int NOT NULL AUTO_INCREMENT,
    team_name varchar(255),
    goalkeeper varchar(255),
    defender1 varchar(255),
    defender2 varchar(255),
    defender3 varchar(255),
    midfielder1 varchar(255),
    midfielder2 varchar(255),
    midfielder3 varchar(255),
    midfielder4 varchar(255),
    forward1 varchar(255),
    forward2 varchar(255),
    forward3 varchar(255),
    user_id int NOT NULL,
    PRIMARY KEY (team_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE ID (
    id int,
    user_id int,
    user_name varchar(255)
);

INSERT INTO ID (id) VALUES (1);