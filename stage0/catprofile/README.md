```markdown
# 🐱 HNGi13 Stage 0 Backend Task — Profile API

## 🚀 Overview

This is a RESTful API built with Django for the HNGi13 Stage 0 Backend Task. The API exposes a single endpoint, `/me`, which returns profile information along with a random cat fact fetched dynamically from the [Cat Facts API](https://catfact.ninja/fact).

**Key Features:**
- Integration with a third-party API (Cat Facts API)
- Dynamic JSON responses with profile data and a cat fact
- Graceful error handling for robust performance
- Clean and maintainable code structure

---

## 🧩 API Endpoint

### GET `/me`

Returns a JSON response containing user profile details, a timestamp, and a random cat fact.

**Example Response:**
```json
{
  "status": "success",
  "user": {
    "email": "your-email@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T12:34:56.789Z",
  "fact": "Cats can jump up to six times their length."
}
```

---

## 🛠️ Tech Stack

- **Framework**: Django
- **HTTP Client**: `requests` (for fetching cat facts)
- **Language**: Python 3.10+
- **Database**: SQLite (default, not used in this project)
- **Environment**: Localhost or cloud-hosted (e.g., Heroku, Railway)

---

## ⚙️ Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/catprofile.git
   cd catprofile
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the Django Server**
   ```bash
   python manage.py runserver
   ```

6. **Test the Endpoint**
   Open your browser or use a tool like Postman to visit:
   ```
   http://127.0.0.1:8000/me
   ```
   You should see a JSON response with your profile and a random cat fact 🐾.

---

## 🧱 Project Structure

```plaintext
catprofile/
├── manage.py               # Django management script
├── db.sqlite3             # SQLite database (not used in this project)
├── requirements.txt        # Project dependencies
├── catprofile/            # Main project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myprofile/             # Django app for /me endpoint
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py           # Defines /me route
│   └── views.py          # Logic for profile data and cat fact
└── README.md              # This file
```

---

## 🧠 How It Works

1. The `/me` endpoint triggers the `me` view in `myprofile/views.py`.
2. The view:
   - Fetches a random cat fact from the [Cat Facts API](https://catfact.ninja/fact).
   - Constructs a JSON response with:
     - User profile (`email`, `name`, `stack`)
     - Current UTC timestamp
     - Random cat fact
3. If the Cat Facts API fails or times out, a fallback message is returned to ensure the API remains operational.

---

## 🧯 Error Handling

- **Mechanism**: Uses a `try-except` block to handle API failures.
- **Fallback Message**: If the Cat Facts API is unavailable, the `fact` field returns:
  ```
  "Could not fetch cat fact at the moment. Please try again later."
  ```
- **Timeout**: A 3-second timeout is set for API requests to prevent hanging.
- **Response**: Always returns a `200 OK` status with `Content-Type: application/json`.

**Example Fallback Response:**
```json
{
  "status": "success",
  "user": {
    "email": "johndoe@gmail.com",
    "name": "John Doe",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T12:35:00.120Z",
  "fact": "Could not fetch cat fact at the moment. Please try again later."
}
```

---

## 🧾 Dependencies

| Package   | Purpose                            |
|-----------|------------------------------------|
| Django    | Web framework for building the API |
| requests  | HTTP client for fetching cat facts |
| tzdata      | for UTC time stamp.                          |
Install dependencies:
```bash
pip install django requests tzdata
```

Generate `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## 🏁 Submission Checklist

✅ `/me` endpoint returns `200 OK`  
✅ JSON response follows the specified format  
✅ Timestamp updates dynamically in UTC  
✅ Cat fact fetched fresh with each request  
✅ Fallback message works if the Cat Facts API fails  
✅ Project hosted successfully (Railway)  
✅ Repository includes this `README.md`  
✅ Blog post shared  

---
