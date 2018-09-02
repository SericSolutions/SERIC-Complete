var express = require('express');
var cors = require('cors')
var fileUpload = require('express-fileupload')
var app = express();

app.use(cors())
app.use(fileUpload());

var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('Pictures.db')
const
{
	exec
} = require('child_process');
var sleep = require('sleep');

var mjpg = null;

app.post('/', function(req, res)
{
	console.log("POST request for HOME made");
	res.send(JSON.stringify(
	{
		done: "yes"
	}, null, 3));
})

app.get('/', function(req, res)
{
	console.log("GET request for Pictures made");

	var query = "SELECT pictureName, fav, date, link, personName from main \
   INNER JOIN faces on faces.id = main.id Order by CAST(pictureName as INTEGER) DESC;"

	db.all(query, function(err, rows)
	{
		res.send(rows);
	});
})

app.get('/video/:p?', function(req, res)
{
	console.log("GET Request for Video made ");
	var startCommand = './mjpg/mjpg_streamer \
	-o "./mjpg/output_http/output_http.so -w ./mjpg/www" \
  -i "./mjpg/input_raspicam/input_raspicam.so -x 720 -y 480 -fps 24 -ex night"'

	var endCommand = "pkill -INT mjpg_streamer";

	if (req.params.p == 1)
	{
		// Request to activate the video stream
		if (mjpg == null)
		{
			mjpg = exec(startCommand);
			sleep.msleep(250);
			res.send(JSON.stringify(
			{
				process: "make"
			}, null, 3));
		}
		else
		{
			res.send(JSON.stringify(
			{
				process: "none"
			}, null, 3));
		}
	}
	else if (req.params.p == 0)
	{
		// Request to END the video stream
		if (mjpg != null)
		{
			exec(endCommand);
			mjpg = null;
			res.send(JSON.stringify(
			{
				process: "kill"
			}, null, 3));
		}
		else
		{
			res.send(JSON.stringify(
			{
				process: "none"
			}, null, 3));
		}
	}
});

app.get('/picture/:p?', function(req, res)
{
	console.log("GET request to TAKE Picture");

	var command = "python FacialRecognitionCliInterface.py " + req.params.p;
	var query = "SELECT pictureName, fav, date, link, personName from main \
  INNER JOIN faces on faces.id = main.id Order by CAST(pictureName as INTEGER) DESC LIMIT 1"

	exec(command, function(error, stdout, stderr)
	{
		db.all(query, function(err, rows)
		{
			res.send(rows);
		});
	})
});

app.post('/picture/:name?/:file?', function(req, res)
{
	console.log("Request to deposit new user form");

	var name = req.params.name;
	var nameOfFile = req.params.file;
	var path = `./data/${nameOfFile}`;
	var command = `python FacialRecognitionCliInterface.py 2 "${name}" "${path}"`;

	console.log(command);

	exec(command, function(error, stdout, stderr)
	{
		res.send(JSON.stringify(
		{
			done: "yes"
		}, null, 3));
	});
})

app.post('/peoplePictureUpload', function(req, res)
{
	console.log("Request to Upload new user picture made");

	if (!req.files)
		return res.status(400).send('No files were uploaded.');

	let sampleFile = req.files.file;

	var fileName = sampleFile.name;
	var filePath = `./data/${fileName}`

	sampleFile.mv(filePath, function(err)
	{
		if (err) return res.status(500).send(err);
		res.send('File uploaded!');
	})
});

app.get('/people', function(req, res)
{
	console.log("GET request for people list");

	var query = "SELECT * from faces where id >= 1;"
	db.all(query, function(err, rows)
	{
		res.send(rows);
	});
})

app.delete('/people/:id?', function(req, res)
{
	console.log("DELETE request for User");

	var name = req.params.id;
	var deleteQuery = `DELETE from enroll where personID = ${name};`
	var deleteQuery2 = `DELETE from faces where id = ${name};`;
	var getQuery = `SELECT id from enroll where personID = ${name};`
	var command;

	db.all(getQuery, function(err, rows)
	{
		console.log(rows);
		for (var i in rows)
		{
			command = `rm data/enroll/${rows[i].id}.jpg`
			exec(command);
			console.log(command);
		}
		db.all(deleteQuery, function(err, rows)
		{
			db.all(deleteQuery2, function(err, rows)
			{
				res.send(JSON.stringify(
				{
					done: "yes"
				}, null, 3));
			})
		});
	});
});

app.post('/Reinforce', function(req, res)
{
	console.log("Request to Reinforce person made");

	if (!req.files)
		return res.status(400).send('No files were uploaded.');

	let sampleFile = req.files.file;

	var id = req.body.id;
	var fileName = sampleFile.name;
	var filePath = `./data/${fileName}`
	console.log(id);


	sampleFile.mv(filePath, function(err)
	{
		if (err) return res.status(500).send(err);

		var command = `python FacialRecognitionCliInterface.py 3 "${id}" "${filePath}"`
		console.log(command)
		exec(command);
		res.send('File uploaded!');
	})
});

app.post('/OpenDoor/:name?/:status?', function(req, res)
{
	console.log("Post request for OpenDoor made")

	var name = req.params.name;
	var status = req.params.status;
	var query = `UPDATE FACES SET OpenDoor = ${status} WHERE id = ${name}`
	db.all(query, function(err, rows)
	{
		res.send('{Done: yes}');
	});
});

app.get('/peoplePhotos/:id?', function(req, res)
{
	console.log("GET request for people Photos");
	var id = req.params.id;

	var query = `select enroll.id from enroll \
  inner join faces on personID = faces.id where personID = ${id};`
	db.all(query, function(err, rows)
	{
		res.send(rows);
	});
})

app.delete('/peoplePhotos/:id?', function(req, res)
{
	console.log("DELETE request for User Picture");

	var name = req.params.id;
	var query = `DELETE from enroll where id = ${name};`;
	var command = `rm data/enroll/${name}.jpg`;

	db.all(query, function(err, rows)
	{
		exec(command);
		res.send('{Done: yes}');
	});
});

app.delete('/del', function(req, res)
{
	console.log("DELETE request for ALL Pictures");

	var name = req.params.name;
	var query = "DELETE from main;";
	var command = "rm data/*";

	db.all(query, function(err, rows)
	{
		exec(command);
		res.send('{Done: yes}');
	});
});

app.delete('/del/:name?', function(req, res)
{
	console.log("DELETE request for Picture");

	var name = req.params.name;
	var link = "poop";
	var q1 = `DELETE from main where pictureName = ${name}`;
	var q2 = `SELECT link from main where pictureName = ${name}`

	db.all(q2, function(err, rows)
	{
		link = rows[0].link;
		var del = `rm ${link}`;
		db.all(q1, function(err, rows)
		{
			exec(del);
			res.send('{Done: yes}');
		});
	});
});

app.post('/fav/:name?/:status?', function(req, res)
{
	console.log("Post request for Favorite made")

	var name = req.params.name;
	var status = req.params.status;
	//var query = "UPDATE MAIN SET fav = " + status + " WHERE pictureName = '" + name + "';";
	var query = `UPDATE MAIN SET fav = ${status} WHERE pictureName = '${name}'`
	db.all(query, function(err, rows)
	{
		res.send('{Done: yes}');
	});
});

app.get('/buzz', function(req, res)
{
	console.log("GET request for Buzzer made");

	var command = "python buzz.py";

	exec(command, function(error, stdout, stderr)
	{
		res.send(JSON.stringify(
		{
			done: "yes"
		}, null, 3));
	});
});

app.get('/audio', function(req, res)
{
	console.log("Get Request for audio made");

	var query = "select no, name ,src, active, personName from faces inner join audio on rec = id;"

	db.all(query, function(err, rows)
	{
		res.send(rows);
	});
})

app.post('/audio/:name?/:status?', function(req, res)
{
	console.log("POST request for AUDIO made");

	var name = req.params.name;
	var status = req.params.status;

	//var query = "UPDATE audio SET active = " + status + " WHERE No = '" + name + "';";
	var query = `UPDATE audio SET active = ${status} WHERE No = '${name}'`;
	console.log(q);
	db.all(query, function(err, rows)
	{
		res.send('{Done: yes}');
	});
});

app.delete('/audio/:name?/:src?', function(req, res)
{
	console.log("DELETE request for AUDIO made");

	var name = req.params.name;
	var src = req.params.src;

	var query = `DELETE from audio where No = ${name}`;
	var command = "rm data/audio/" + src;

	db.all(query, function(err, rows)
	{
		exec(command);
		res.send('{Done: yes}');
	});
});

app.get('/peopleNames', function(req, res)
{
	console.log("GET request for peopleNames made");

	var query = "SELECT personName as text, Id from faces;"

	db.all(query, function(err, rows)
	{
		res.send(rows);
	});
})

app.post('/upload', function(req, res)
{
	console.log("Request to UPLOAD file made");

	if (!req.files)
		return res.status(400).send('No files were uploaded.');

	let sampleFile = req.files.file;

	sampleFile.mv('./data/audio/' + sampleFile.name, function(err)
	{
		if (err) return res.status(500).send(err);
		res.send('File uploaded!');
	});
});

app.post('/audio/:FN?/:CN?/:PN?', function(req, res)
{
	console.log("POST for AUDIO FORM made");

	var CN = req.params.CN;
	var FN = req.params.FN;
	var PN = req.params.PN;

	var query = `INSERT into audio VALUES (null,'${CN}','${FN}',1,${PN})`;
	db.all(query, function(err, rows)
	{
		res.send('{Done: yes}');
	});
});

var server = app.listen(8081, function()
{

	var host = server.address().address
	var port = server.address().port

	var message = `SERIC Server Started On Port ${port}`

	console.log(message);
})
