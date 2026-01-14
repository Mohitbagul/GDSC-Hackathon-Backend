
---

## 🚀 Getting Started (Local Setup)

Follow the steps below to run the **Hospital Management System Backend** on your local machine.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/hospital-management-backend.git
cd hospital-management-backend
```

---

### 2️⃣ Create a Virtual Environment

#### Windows

```bash
python -m venv env
env\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv env
source env/bin/activate
```

You should see `(env)` in your terminal once activated.

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root and add the following:

```env
MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net
DATABASE_NAME=hospital_management

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

⚠️ Replace `<username>` and `<password>` with your MongoDB Atlas credentials.

---

### 5️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

---

### 6️⃣ Access the API

* **Base URL:**

  ```
  http://127.0.0.1:8000
  ```

* **Swagger Docs:**

  ```
  http://127.0.0.1:8000/docs
  ```

* **ReDoc:**

  ```
  http://127.0.0.1:8000/redoc
  ```

---

## 🔐 Authentication Flow (Important)

1. **System Admin (Developer)** is created directly in MongoDB
2. System Admin creates **Hospitals**
3. Hospital Admin creates:

   * Doctors
   * Receptionists
4. Receptionist creates:

   * Patients
   * Appointments
5. Doctors can view their appointments

All routes are **JWT-protected & role-based**.

---

## 🛠 Tech Stack

* **Backend:** FastAPI
* **Database:** MongoDB Atlas
* **Auth:** JWT (Role Based Access)
* **ORM:** Motor (Async MongoDB Driver)

---

## 📌 Notes

* Appointments are **date-based** (no fixed time)
* Token numbers are auto-generated per doctor per day
* Designed for easy future scaling

---

