# Flask Notes App 📝

A simple web application to take personal notes, built with **Python (Flask)**, **HTML**, and **CSS**.  
Users can add notes and view them instantly.  

## Features
- Add notes  
- View saved notes  
- Delete saved notes  
- Simple user interface  

---

## 🧩 App Evolution (Development Stages)

This project went through four stages of design and functionality improvements:

### 🏁 1. Initial Version
Basic Flask structure with a simple input form and notes display.

![Initial Version](snaps/initial.png)

---

### 🗑️ 3. Delete Button Feature
Added delete functionality allowing users to remove saved notes.

![Delete Button](snaps/delete%20button.png)

---

### 🗃️ 4. With Database Integration
Integrated a database to store notes persistently instead of in-memory.

![With Database](snaps/with%20database.png)

---

### 🎨 2. New Look
Improved UI with a cleaner, more modern layout.

![New Look](snaps/new%20look.png)

---


## 🚀 Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Database:** MySQL

---

## ⚙️ Setup Instructions

1.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Setup Database**
    Make sure you have MySQL installed and running.
    
    Create the database and dedicated user:
    
    **Git Bash / Command Prompt:**
    ```bash
    mysql -u root -p < schema.sql
    ```
    
    **PowerShell:**
    ```powershell
    Get-Content schema.sql | mysql -u root -p
    ```

3.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```bash
    cp .env.example .env
    ```
    Open `.env` and update the values if you changed the password in `schema.sql` or have a different configuration.

4.  **Run Application**
    ```bash
    python personal_notes_app/app.py
    ```
