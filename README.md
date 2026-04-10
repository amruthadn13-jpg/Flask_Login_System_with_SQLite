# 🔐 Flask Login System with SQLite

## 📌 Overview

This project is a simple **Login System** built using **Flask (Python)** and **SQLite database**, with a basic HTML frontend.

It demonstrates how backend and frontend interact in a real-world application:

* User inputs data via HTML form
* Backend processes request using Flask
* Data is validated using SQLite database
* Response is sent back to frontend

---

## ⚙️ Features

✔️ User login form (HTML)
✔️ Backend authentication using Flask
✔️ SQLite database integration
✔️ Username existence check
✔️ Password validation
✔️ Dynamic message display (success / error)

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML
* **Database:** SQLite3

---

## 📂 Project Structure

```id="b1r8f2"
flask-login-system-sqlite/
│
├── app.py                # Flask backend application
├── users.db             # SQLite database
│
├── templates/
│   └── login.html       # Frontend login page
│
└── README.md            # Project documentation
```

---

## 🔄 How It Works

1️⃣ User opens the login page
2️⃣ Enters username & password
3️⃣ Form sends POST request to Flask server
4️⃣ Flask checks database:

* If user exists
* If password matches
  5️⃣ Result is sent back and displayed on UI

---

## 🧠 Backend Logic (Flask)

* `/` route handles both:

  * **GET** → Show login page
  * **POST** → Process login

* Uses:

```python id="q1w2e3"
request.form.get()
```

to get form data

* Connects to SQLite:

```python id="q4w5e6"
sqlite3.connect("users.db")
```

* Validates:

```python id="q7w8e9"
SELECT * FROM users WHERE username=?
```

---

## 🌐 Frontend (HTML)

* Simple login form:

```html id="h1h2h3"
<form method="POST">
```

* Takes:

  * Username
  * Password

* Displays message dynamically:

```html id="h4h5h6"
{{ message }}
```

---

## ▶️ How to Run

### 1️⃣ Install Flask

```bash id="r1r2r3"
pip install flask
```

### 2️⃣ Run the application

```bash id="r4r5r6"
python app.py
```

### 3️⃣ Open browser

```id="r7r8r9"
http://127.0.0.1:5000/
```

---

## 📸 Sample Output

* ✅ `Welcome admin`
* ❌ `Wrong Password`
* ❌ `User Not Found`

---

## 🔐 Important Note (Security)

⚠️ Passwords are stored in **plain text** (not secure)

### Recommended Improvements:

* Use password hashing (`bcrypt`)
* Add user registration system
* Use sessions for login management
* Prevent SQL injection (already partially handled using `?`)

---

## 🚀 Future Enhancements

* 🔑 Signup / Registration page
* 🔒 Secure authentication (hashed passwords)
* 🍪 Session & logout system
* 🎨 Improve UI with CSS / Bootstrap
* 🌐 Convert into REST API

---

## 👩‍💻 Author

**Amrutha D N**

---

⭐ If you like this project, consider giving it a star!
