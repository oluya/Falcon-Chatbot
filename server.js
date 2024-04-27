const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');
const session = require('express-session');
const SQLiteStore = require('connect-sqlite3')(session);
const app = express();
const PORT = 3000;
const db = new sqlite3.Database('my_database.db');

// Middleware for parsing request bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files (HTML, CSS, JS)
app.use(express.static('public'));

// Initialize users table
db.serialize(() => {
  db.run("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT)");
});

// Setting up User Session
app.use(session({
  store: new SQLiteStore({ db: 'my_database.db' }),
  secret: 'my secret key',  // Use a strong secret in production
  resave: false,
  saveUninitialized: false,
  cookie: { secure: false }  // Set to true if using https
}));

// Handle registration
app.post('/register', (req, res) => {
  const { name, email, password } = req.body;
  const stmt = db.prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
  stmt.run(name, email, password, function(err) {
    if (err) {
      console.error("Database error:", err.message);
      res.status(500).send('Error registering new user');
    } else {
      res.redirect('/index.html#login'); // Assuming login form is accessible via an anchor tag
    }
  });
  stmt.finalize();
});

// Handle login
app.post('/login', (req, res) => {
  const { name, password } = req.body;
  db.get("SELECT * FROM users WHERE username = ? AND password = ?", [name, password], (err, row) => {
    if (err) {
      res.status(500).send('Error logging in');
    } else if (row) {
      // Setting session variables
      req.session.userId = row.id;
      req.session.username = row.username;
      // Redirect to home.html after successful login
      res.redirect('/home.html'); // Server-side redirect
    } else {
      res.status(401).send('Incorrect credentials');
    }
  });
});


// Handle Logout
app.get('/logout', (req, res) => {
  req.session.destroy(err => {
    if (err) {
      res.status(500).send('Could not log out, please try again');
    } else {
      res.clearCookie('connect.sid');  // Clear the session cookie
      res.redirect('/index.html');  // Redirect to the home page
    }
  });
});


// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
