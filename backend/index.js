const express = require('express');
const app = express();
const mysql = require('mysql');
const cors = require('cors');

app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
    user: "root",
    host: 'localhost',
    password: 'password',
    database: 'detroit_crema'
});

db.connect((err) => {
    if(err) {
        console.error('Error connecting to the database', err);
        return;
    }
    console.log('Connected to the database');
});

app.get('/api/data/:ID', (req, res) => {
    const id = req.params.id;
    console.log('Recieved request for ID:', id);
    const sql = 'SELECT * FROM pressuretime WHERE id = ID';
    db.query(sql, [id], (err, result) => {
        if(err) {
            console.error('Error querying the database: ', err);
            res.status(500).json({error: 'Error querying the database'});
            return;
        }
        if (result.length === 0) {
            console.log('Row not found for ID:', id);
            res.status(404).json({ error: 'Row not found'});
        }else {
            console.log('Returning data for ID:', id);
            res.json(result[0]);
        }
        
    });
});

app.post('/create', (req, res) => {
    const point1 = req.body.point1;
    const point2 = req.body.point2;
    const point3 = req.body.point3;
    const point4 = req.body.point4;
    const point5 = req.body.point5;
    const time1 = req.body.time1;
    const time2 = req.body.time2;
    const time3 = req.body.time3;
    const time4 = req.body.time4;
    const time5 = req.body.time5;

    db.query('INSERT INTO pressuretime (point1, point2, point3, point4, point5, time1, time2, time3, time4, time5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        [point1, point2, point3, point4, point5, time1, time2, time3, time4, time5], (err, result) => {
            if(err) {
                console.log(err);
            } else {
                res.send("Values Inserted");
            }
        }
    );
});

app.listen(3001, () => {
    console.log("Your server is running on port 3001");
})