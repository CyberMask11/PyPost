# 📝 PyPost

PyPost is a FastAPI-based project where users can **sign up, log in, create posts, edit & delete their own posts**, and **view everyone's posts**.  

---

## ⚡ Features

- 🔑 User signup & login with JWT authentication  
- 📝 Create, update, delete your posts  
- 🌍 View all users' posts  
- 🔍 Search posts by title in real-time  
- 🖤 Sidebar navigation between `Create Post` and `Display Posts`  

---

## 🛠 Tech Stack

- **Backend:** FastAPI, SQLAlchemy, PostgreSQL  
- **Frontend:** HTML, CSS, JS  
- **Auth:** JWT Tokens  

---

## ⏳ TODO / Improvements

- 📷 Photo uploads  
- ⏱ Refresh tokens & automatic logout on token expiry  
- 🖥 Pagination for many posts  

---

## 🚀 Getting Started

1. Clone the repo:
 bash
 git clone https://github.com/CyberMask11/PyPost.git
 cd PyPost

2. Install dependencies:
 pip install -r requirements.txt

3. Configure .env with JWT secret and DB connection

4. Run:
 uvicorn main:app --reload
