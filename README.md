# Cafeterias Web App

A web application and RESTful API for managing and displaying information about different cafes.

---

## 🛠️ Tech Stack

- Python
- Flask  
- SQLite  
- HTML/CSS

---

## 📚 Features

- SQLite database
- Web interface built with Flask
- REST API with full CRUD functionality:
  - `GET /cafes` - Retrieve all cafes
  - `GET /cafes/open?from=HH:MM&to=HH:MM` - Filter cafes by opening hours
  - `POST /cafes` - Add a new cafe
  - `PUT /cafes/<id>` - Update a cafe
  - `DELETE /cafes/<id>` - Delete a cafe
