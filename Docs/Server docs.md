# REST API Manual
<!-- TOC depthFrom:1 depthTo:3 withLinks:1 updateOnSave:1 orderedList:0 -->

- [REST API Manual](#rest-api-manual)
	- [/](#)
		- [app.post('/')](#apppost)
		- [app.get('/')](#appget)
	- [/video](#video)
		- [app.get('/video/:p?')](#appgetvideop)
	- [/picture](#picture)
		- [app.get('/picture/:p?')](#appgetpicturep)
		- [app.post('/picture/:name?/:file?')](#apppostpicturenamefile)
		- [app.post('/peoplePictureUpload')](#apppostpeoplepictureupload)
	- [/people](#people)
		- [app.get('/people')](#appgetpeople)
		- [app.delete('/people/:id?')](#appdeletepeopleid)
		- [app.get('/peoplePhotos/:id?')](#appgetpeoplephotosid)
		- [app.delete('/peoplePhotos/:id?')](#appdeletepeoplephotosid)
	- [/Del](#del)
		- [app.delete('/del')](#appdeletedel)
		- [app.delete('/del/:name?')](#appdeletedelname)
	- [/Audio](#audio)
		- [app.get('/audio')](#appgetaudio)
		- [app.post('/audio/:name?/:status?')](#apppostaudionamestatus)
		- [app.post('/audio/:FN?/:CN?/:PN?')](#apppostaudiofncnpn)
		- [app.delete('/audio/:name?/:src?')](#appdeleteaudionamesrc)
	- [Random](#random)
		- [app.post('/fav/:name?/:status?')](#apppostfavnamestatus)
		- [app.get('/buzz')](#appgetbuzz)
		- [app.get('/peopleNames')](#appgetpeoplenames)
		- [app.post('/upload')](#apppostupload)
		- [app.post('/Reinforce')](#apppostreinforce)
		- [app.post('/OpenDoor/:name?/:status?')](#apppostopendoornamestatus)

<!-- /TOC -->

## /

### app.post('/')
Used to see if server is alive.

### app.get('/')
used to get all photos from the Database

## /video

### app.get('/video/:p?')
turns on video stream for the web UI

``` javascript
if(p == 0)
  turn on video stream
else if (p == 1)
  turn off video stream
```

## /picture

### app.get('/picture/:p?')

Take a picture from the camera.

``` javascript
if(p == 0)
  take it without facial recognition
else if (p == 1)
  take it with facial recognition
```

### app.post('/picture/:name?/:file?')
enrolls new user

``` javascript
name = name of the user that you want to enroll

file = name of the first seed picture used for enrollment
```

### app.post('/peoplePictureUpload')
used by dropzone.js for file upload

## /people

### app.get('/people')
gets all the people as a json encoded string

### app.delete('/people/:id?')
remoove a user form the system
``` javascript
id = id of the person you want to delete
```

### app.get('/peoplePhotos/:id?')

get a json string of all the photos in the system for a single user.

``` javascript
if (id == 1)
  the door opens for that person
else if(id == 0)
  door does not open for that person
```

### app.delete('/peoplePhotos/:id?')
delete a single photo from that persons Dataset

``` javascript
id = id of picture you wish to delete
```

## /Del

### app.delete('/del')

deletes all pictures

### app.delete('/del/:name?')

delete one picture

``` javascript
name = id of picture that you want to delete
```

## /Audio

### app.get('/audio')

get all audio files form the DB

### app.post('/audio/:name?/:status?')

post a new audio file and set its status

### app.post('/audio/:FN?/:CN?/:PN?')

for form data of the audio resource,

``` javascript
FN = File name
CN = name given to the file for displaying on the dashboard
PN = ID of person for whom this file is for
```

### app.delete('/audio/:name?/:src?')

delete an audio file

``` javascript
name = new name for the file
src = location of file on server
```

``` javascript
name = new name for the file

if (status == 1) set it active
else if(status == 0) sont set it active
```

## Random

### app.post('/fav/:name?/:status?')

alter a pictures Favorite status

``` javascript
name = id of picture you want to change the status of

if(status == 1)
  picture is liked
else if (picture == 0)
  picture not liked
```

### app.get('/buzz')

ring the buzzer


### app.get('/peopleNames')

Get the names of all the people in the system

### app.post('/upload')

for uploading audio files using dropzoneJS

### app.post('/Reinforce')
upload a new picture to server for adding additional pictures to a persons dataset

### app.post('/OpenDoor/:name?/:status?')
modify weather the door should open for a person or not

``` javascript
name = id of the person

if(status == 0)
  dont open door for that person
else if (status == 1)
  open door for this person
```
