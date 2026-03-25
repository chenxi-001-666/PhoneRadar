# 📱 Phone Radar

**Phone Radar** is a comprehensive mobile review community built with **Django 5.x**. It allows tech enthusiasts to explore phone specifications by brand and publish in-depth, long-form reviews as registered members.

---

## 📖 Storyboard (User Journey)

1.  **Restricted Access**: A guest tries to access the `/index/` page. The system detects the user is not logged in and automatically redirects them to the `/login/` page.
2.  **Authentication**: The user creates an account via the `/register/` page. After successful registration, they are redirected to login.
3.  **Exploration**: Once logged in, the user enters the Dashboard (`/index/`). They can browse phone brands (e.g., Apple, Xiaomi) and specific models.
4.  **Contribution**: The user clicks the "Write a Review" button. They are taken to a dedicated page where they select a phone model from a dropdown menu and type a detailed review.
5.  **Dynamic Updates**: Upon submission, the user is redirected back to the index page where their review appears in their "History." Simultaneously, that review is now visible on that specific phone's Detail Page for all users to see.
6.  **Secure Exit**: The user logs out, clearing their session and returning to the login screen safely.

---

## ✨ Features

- **User Authentication**: Secure Login/Register/Logout flow with protected routes using `@login_required`.
- **Relational Database**: Managed relationships between Brands, Models, and User Reviews.
- **Single-Model Review Linkage**: Users can link a long-form review to exactly one phone model per post.
- **Bootstrap 5 UI**: Clean, responsive interface featuring card layouts and professional forms.
- **Dev-Logging**: Real-time HTTP response logging in the server console for debugging.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.11+, Django 5.x
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite (Default)

---

## 🚀 Getting Started

### 1. Prerequisites
- Python installed on your machine.
- Git installed.

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/your-username/PhoneRadar.git](https://github.com/your-username/PhoneRadar.git)
cd PhoneRadar

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django