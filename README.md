# 🛑 The Anti-Frontend Club

> **"We don't design. We deploy."**

Welcome to **The Anti-Frontend Club**, a sarcastic yet highly robust web application built purely to demonstrate advanced Backend Architecture, Server-Side logic, and Database Optimization. 

This project was born out of a Backend Developer's sheer frustration with centering `div`s and fixing `z-index` bugs. Instead of fighting with CSS, this project fights inefficient database queries and broken APIs. 

## 🧠 The Story Behind The Idea
Frontend developers always claim that centering a div is easy. We disagree. We built this application to shift the focus back to where it matters: **The Server**. The project serves as a comprehensive dashboard that combines humor with hardcore backend concepts like Query Execution Planning, Server-Sent Events (SSE), and third-party API integration.

## 🚀 Core Features

1. **The Centering Challenge (Vanilla JS & DOM Manipulation)**
   A classic frontend nightmare. Users are challenged to click a button to "center a div," but the button continuously calculates viewport boundaries and escapes cursor hover events.

2. **CSS Cry Room (RESTful API & SQLite)**
   A digital burn book for CSS traumas. Users submit their frontend frustrations via a `POST` request. The Flask backend validates the payload, interacts with an SQLAlchemy ORM, saves the record to a SQLite database, and returns the generated DB ID asynchronously.

3. **The Query Graveyard (Database Optimization & Autopsy)**
   The crown jewel of the backend. Users submit raw SQL queries (e.g., `CROSS JOIN`). The Flask server intercepts the query, wraps it in `EXPLAIN QUERY PLAN`, and runs it against the SQLite engine to analyze the execution strategy. 
   * **Sarcasm Engine:** A custom Python logic that detects performance bottlenecks (like `SCAN` operations indicating a Full Table Scan missing an Index) and roasts the user for writing inefficient, unoptimized queries. Built-in security prevents destructive operations like `DROP` or `UPDATE`.

4. **No-Bullshit API Tester (Server-Side Requests)**
   A built-in API testing tool. Instead of relying on client-side fetch, the Flask server itself makes HTTP requests using the Python `requests` library to test external endpoints, calculating exact server-to-server response times and status codes.

5. **Live Server Console (Server-Sent Events - SSE)**
   A real-time, unidirectional event stream. As users interact with the dashboard, the backend pushes live execution logs directly to the frontend console without requiring page reloads, mimicking a real server terminal.

## ⚙️ Tech Stack & Architecture

* **Backend:** Python 3, Flask
* **Database:** SQLite, Flask-SQLAlchemy (ORM)
* **Frontend:** HTML5, CSS3 (Minimalistic Hacker Theme), Vanilla JavaScript (Fetch API)
* **Architecture:** **Clean Architecture via Flask Blueprints**. The application is strictly modularized into distinct domains (Routes, Models, Static, Templates, Utils) to ensure maintainability and scalability.

## 📂 Project Structure
```text
app/
├── models/         # SQLAlchemy Database Models (Complaint, QueryCorpse)
├── routes/         # Flask Blueprints for decoupled routing
├── static/         # Separated CSS and Vanilla JS modules
├── templates/      # Jinja2 HTML Templates (Base and SPA Dashboard)
├── utils/          # Helper functions and configurations
run.py              # Application Entry Point
requirements.txt    # Python Dependencies
