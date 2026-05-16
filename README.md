#  Notes App — Django DRF Backend

Built this while learning Django REST Framework. This serves as the "Engine" for the Notes App.

---

##  What I Built

A professional-grade Notes API where users can:

- Register and Login (JWT Auth)
- Manage notes with nested subtasks (Full CRUD)
- Search and Filter through their notes
- Paginate results for better performance

_Note: Each user can only access their own data (Protected by permissions)._

## Stack

- **Django REST Framework**: For building the API.
- **SimpleJWT**: For secure, token-based authentication.
- **SQLite**: Current development database (PostgreSQL ready).

##  How to Run (For Developers)

1. **Clone the repo:** `git clone [your-repo-link]`
2. **Create Virtual Env:** `python -m venv venv`
3. **Activate Env:** `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. **Install Packages:** `pip install -r requirements.txt`
5. **Migrate Database:** `python manage.py migrate`
6. **Start Server:** `python manage.py runserver`

_Server will start at http://127.0.0.1:8000/_

## API Endpoints (Quick Reference)

| Method | Endpoint              | Description                                  |
| ------ | --------------------- | -------------------------------------------- |
| POST   | `/api/auth/register/` | Create account                               |
| POST   | `/api/auth/login/`    | Get Access/Refresh tokens                    |
| GET    | `/api/notes/`         | List all notes (Search/Pagination available) |
| POST   | `/api/notes/`         | Create a new note with subtasks              |

---

##  Where I Struggled

- Nested serializers took me a long time to understand.
- Pagination had a lot of bugs before it worked.
- JWT logout and blacklisting was confusing at first.

##  What I Learned

- How REST APIs work end-to-end.
- JWT authentication flow (Access vs Refresh tokens).
- How to handle nested data (notes with subtasks) in serializers.

---

Built by Abhay Singh
