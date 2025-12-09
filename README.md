# **Django Distributed Data Insertion using Multi-Database and Threading**

This project demonstrates a distributed system simulation built with **Django**, where three different types of data — **Users**, **Products**, and **Orders** — are stored in three separate **SQLite databases**. The primary focus of the project is to perform multiple data insertions **concurrently using Python threading**, representing parallel write operations similar to distributed environments.

---

## 🚀 **Project Objective**

✔ Simulate distributed architecture by splitting data across multiple databases
✔ Insert records for Users, Products, and Orders simultaneously
✔ Implement **threading** for concurrency
✔ Perform **application-level validation** (not database validation)
✔ Display real-time results of insertion success/failure

---

## 🏗 **Features**

| Feature                      | Description                               |
| ---------------------------- | ----------------------------------------- |
| Multi Database               | Users, Products, Orders stored separately |
| Threading                    | Parallel data insertion                   |
| Validation                   | Application-side logic validation         |
| Clean Output                 | Result displayed on browser               |
| Simulated Distributed System | Resembles microservices structure         |

---

## 🔧 **Tech Stack Used**

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Python     | Core Language            |
| Django     | Web Framework            |
| SQLite     | Multiple lightweight DBs |
| Threading  | Concurrency              |
| HTML       | Display Results          |

---

## 📁 **Database Structure**

| Model   | Database    |
| ------- | ----------- |
| User    | users.db    |
| Product | products.db |
| Order   | orders.db   |

This separation demonstrates how a distributed application might store data in different storage units across services.

---

## ⚙ **How Concurrency Works**

The application creates **multiple threads**, each responsible for inserting a single record into its specific database. This allows:

➡ Faster operations
➡ Independent write execution
➡ Simulation of concurrent requests

---

## 🧠 **Validations Done in Application Logic**

| Field   | Validation                 |
| ------- | -------------------------- |
| User    | Name + email must exist    |
| Product | Price must not be negative |
| Order   | Quantity must be > 0       |

➡ No database-level constraints were used — per assignment requirement.

---

## ▶ How to Run the Project

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

To execute the distributed insert operation:

Open in browser:

👉 `http://127.0.0.1:8000/run/`

---

## 📌 Output Example

```
Users: [(1,'User Added'), ..., (10,'Invalid')]
Products: [(1,'Product Added'), ..., (10,'Invalid Price')]
Orders: [(1,'Order Added'), ..., (8,'Invalid')]
```

---

## 🗂 Project Structure

```
├── distributedsystem
│   ├── settings.py
│   ├── urls.py
├── treadapp
│   ├── models.py
│   ├── views.py
│   ├── routers.py
├── users.db
├── products.db
├── orders.db
```

---

## 📄 Summary of Learning

✔ Working with multiple databases in Django
✔ Simulating distributed data environments
✔ Using Python threading for parallel operations
✔ Handling validations without database constraints
✔ Returning results through the browser

---

## 🔗 GitHub Repository

➡ Replace this line with your repo link once uploaded
👉 `https://github.com/Mayur-Satpute/django-distributed-data-insertion`

---

## ✍ Author

**Mayur**
📧 [mayursatpute246@gmail.com](mailto:mayursatpute246@gmail.com)
📱 (+91) 9172072739

