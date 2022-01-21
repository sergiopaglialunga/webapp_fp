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
    team_name varchar(255) DEFAULT '',
    goalkeeper varchar(255) DEFAULT '',
    defender1 varchar(255) DEFAULT '',
    defender2 varchar(255) DEFAULT '',
    defender3 varchar(255) DEFAULT '',
    midfielder1 varchar(255) DEFAULT '',
    midfielder2 varchar(255) DEFAULT '',
    midfielder3 varchar(255) DEFAULT '',
    midfielder4 varchar(255) DEFAULT '',
    forward1 varchar(255) DEFAULT '',
    forward2 varchar(255) DEFAULT '',
    forward3 varchar(255) DEFAULT '',
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