CREATE TABLE main (
  pictureName INTEGER PRIMARY KEY AUTOINCREMENT,
  fav  boolean,
  date int,
  link varchar(255),
  id int
);

CREATE TABLE enroll(
id INTEGER PRIMARY KEY AUTOINCREMENT,
personID int,
FOREIGN KEY (personID) REFERENCES faces (id)
);


CREATE TABLE audio(
  No integer primary key AUTOINCREMENT,
  Name varchar(25),
  src varchar(255),
  active boolean,
  rec int
);


CREATE TABLE faces(
  id INTEGER PRIMARY KEY  AUTOINCREMENT,
  personName text,
  OpenDoor boolean
);


CREATE TABLE antidata(
  id int,
  personID int,
  foreign key(personID) references faces(id)
);
