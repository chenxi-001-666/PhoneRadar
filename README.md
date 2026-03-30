# 📱 Phone Radar

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple.svg)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Phone Radar** is a comprehensive mobile review community built with **Django 5.x**. It allows tech enthusiasts to explore phone specifications by brand and publish in-depth, long-form reviews as registered members.

**Phone Radar** 是一个基于 **Django 5.x** 构建的综合型手机评测社区。它允许科技爱好者按品牌浏览手机规格，并作为注册会员发布深度长文评测。

---

## 📖 Storyboard (User Journey) / 用户旅程

1. **Restricted Access**: A guest tries to access the `/index/` page. The system detects the user is not logged in and automatically redirects them to the `/login/` page.
   **访问限制**：访客尝试访问 `/index/` 页面，系统检测到未登录，自动重定向到 `/login/` 页面。

2. **Authentication**: The user creates an account via the `/register/` page. After successful registration, they are redirected to login.
   **身份验证**：用户通过 `/register/` 页面创建账户，注册成功后重定向到登录页面。

3. **Exploration**: Once logged in, the user enters the Dashboard (`/index/`). They can browse phone brands (e.g., Apple, Xiaomi) and specific models.
   **探索浏览**：登录后，用户进入仪表板（`/index/`），可以浏览手机品牌（如 Apple、Xiaomi）和具体型号。

4. **Contribution**: The user clicks the "Write a Review" button. They are taken to a dedicated page where they select a phone model from a dropdown menu and type a detailed review.
   **贡献内容**：用户点击"撰写评测"按钮，进入专门页面，从下拉菜单选择手机型号并撰写详细评测。

5. **Dynamic Updates**: Upon submission, the user is redirected back to the index page where their review appears in their "History." Simultaneously, that review is now visible on that specific phone's Detail Page for all users to see.
   **动态更新**：提交后，用户被重定向回首页，评测显示在"历史记录"中，同时该评测也会出现在对应手机的详情页供所有用户查看。

6. **Secure Exit**: The user logs out, clearing their session and returning to the login screen safely.
   **安全退出**：用户登出，清除会话并安全返回登录页面。

---

## ✨ Features / 功能特点

| Feature | Description |
|---------|-------------|
| **User Authentication** | Secure Login/Register/Logout flow with protected routes using `@login_required` |
| **用户认证** | 安全的登录/注册/登出流程，使用 `@login_required` 保护路由 |
| **Relational Database** | Managed relationships between Brands, Models, and User Reviews |
| **关系型数据库** | 管理品牌、型号和用户评测之间的关联关系 |
| **Single-Model Review Linkage** | Users can link a long-form review to exactly one phone model per post |
| **单型号评测关联** | 用户可将长文评测与单个手机型号精确关联 |
| **Bootstrap 5 UI** | Clean, responsive interface featuring card layouts and professional forms |
| **Bootstrap 5 界面** | 简洁、响应式的界面，包含卡片布局和专业表单 |
| **Dev-Logging** | Real-time HTTP response logging in the server console for debugging |
| **开发日志** | 服务器控制台实时记录 HTTP 响应，便于调试 |

---

## 🛠️ Tech Stack / 技术栈

| Category | Technologies |
|----------|--------------|
| **Backend** | Python 3.11+, Django 5.x |
| **Frontend** | Bootstrap 5, HTML5, CSS3 |
| **Database** | SQLite (Development) |
| **Version Control** | Git |

---

## 🚀 Getting Started / 快速开始

### Prerequisites / 环境要求

- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** - [Download](https://git-scm.com/)
- **Virtual environment tool** (built-in `venv`)

---

### Installation / 安装步骤

#### 1. Clone the repository / 克隆项目

```bash
# Clone the repository / 克隆项目
git clone https://github.com/your-username/PhoneRadar.git

# Navigate to project directory / 进入项目目录
cd PhoneRadar
```

> ⚠️ Replace `your-username` with your actual GitHub username.  
> 请将 `your-username` 替换为你实际的 GitHub 用户名。

---

#### 2. Create and activate virtual environment / 创建并激活虚拟环境

```bash
# Create virtual environment / 创建虚拟环境
python -m venv venv

# Activate on Windows / Windows 激活
venv\Scripts\activate

# Activate on macOS/Linux / macOS/Linux 激活
source venv/bin/activate
```

> ✅ You should see `(venv)` appear at the beginning of your terminal prompt.  
> 激活成功后，终端提示符前会出现 `(venv)`。

---

#### 3. Install Django / 安装 Django

```bash
# Install Django via pip / 通过 pip 安装 Django
pip install django

# Verify installation / 验证安装
django-admin --version
```

> 📦 This will install the latest Django 5.x version.  
> 这将安装最新的 Django 5.x 版本。

---

#### 4. Create requirements.txt (for future use) / 创建依赖文件

```bash
# Generate requirements.txt for easy reinstallation / 生成依赖文件以便重新安装
pip freeze > requirements.txt
```

> 💡 Other users can then run `pip install -r requirements.txt` to install all dependencies.  
> 其他用户之后可以运行 `pip install -r requirements.txt` 来安装所有依赖。

---

#### 5. Set up database migrations / 设置数据库迁移

```bash
# Create migration files / 创建迁移文件
python manage.py makemigrations

# Apply migrations to database / 应用迁移到数据库
python manage.py migrate
```

> 📊 This creates the SQLite database file (`db.sqlite3`) in your project root.  
> 这将在项目根目录下创建 SQLite 数据库文件（`db.sqlite3`）。

---

#### 6. Create a superuser (admin account) / 创建超级管理员账户

```bash
python manage.py createsuperuser
```

You will be prompted to enter:
系统会提示你输入：

| Prompt | Example |
|--------|---------|
| **Username** | `admin` |
| **Email address** | `admin@example.com` |
| **Password** | `your_secure_password` (twice for confirmation) |

> 🔐 Remember these credentials for accessing the admin panel.  
> 请记住这些凭据，用于访问管理后台。

---

#### 7. (Optional) Load sample data / 加载示例数据

If you have fixture files for testing:

```bash
# Load sample brands, models, and reviews / 加载示例品牌、型号和评测
python manage.py loaddata sample_data.json
```

> 💡 Skip this step if you want to start with an empty database.  
> 如果想从空数据库开始，可以跳过此步骤。

---

#### 8. Run the development server / 运行开发服务器

```bash
python manage.py runserver
```

You should see output similar to:
你会看到类似如下的输出：

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 5.x, using settings 'PhoneRadar.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

#### 9. Access the application / 访问应用

Open your browser and visit:
打开浏览器并访问：

| Page | URL | Description |
|------|-----|-------------|
| **Login Page** | http://127.0.0.1:8000/login/ | User login |
| **Register Page** | http://127.0.0.1:8000/register/ | Create new account |
| **Dashboard** | http://127.0.0.1:8000/index/ | Main page (requires login) |
| **Admin Panel** | http://127.0.0.1:8000/admin/ | Admin interface |

> 🔑 Use your superuser credentials to access the admin panel.  
> 使用超级管理员凭据访问管理后台。

---

## 📁 Project Structure / 项目结构

```
PhoneRadar/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies (optional)
├── db.sqlite3               # SQLite database
├── PhoneRadar/              # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   └── wsgi.py
├── reviews/                 # Main application
│   ├── __init__.py
│   ├── admin.py             # Admin interface config
│   ├── models.py            # Database models (Brand, Model, Review)
│   ├── views.py             # Request handlers
│   ├── urls.py              # App URLs
│   └── templates/           # HTML templates
│       └── reviews/
│           ├── index.html   # Dashboard
│           ├── login.html   # Login page
│           ├── register.html # Registration page
│           └── ...
└── static/                  # CSS, JS, images (if any)
```

---

## 🧪 Testing the User Journey / 测试用户旅程

Follow these steps to test the complete workflow:
按照以下步骤测试完整流程：

1. **Start the server** / 启动服务器
   ```bash
   python manage.py runserver
   ```

2. **Try accessing** `/index/` without logging in → Should redirect to `/login/`
   **尝试访问** `/index/` 而不登录 → 应重定向到 `/login/`

3. **Create a new account** at `/register/` → Redirected to `/login/`
   **创建新账户** 访问 `/register/` → 重定向到 `/login/`

4. **Login** with your new credentials → Redirected to `/index/`
   **登录** 使用新凭据 → 重定向到 `/index/`

5. **Browse brands and models** on the dashboard
   **浏览品牌和型号** 在仪表板上

6. **Click "Write a Review"** → Select a phone model → Write review → Submit
   **点击"撰写评测"** → 选择手机型号 → 撰写评测 → 提交

7. **Check your review** appears in "History" section
   **查看评测** 出现在"历史记录"部分

8. **Logout** → Redirected to `/login/`
   **登出** → 重定向到 `/login/`

---

## 🐛 Common Issues & Solutions / 常见问题与解决方案

| Issue / 问题 | Solution / 解决方案 |
|--------------|---------------------|
| `django: command not found` | Activate virtual environment first: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows) |
| `ModuleNotFoundError: No module named 'django'` | Run `pip install django` after activating venv |
| Port 8000 already in use / 端口被占用 | Run `python manage.py runserver 8001` (use different port) |
| Migration errors / 迁移错误 | Delete `db.sqlite3` and `migrations/` folder (except `__init__.py`), then re-run `makemigrations` and `migrate` |
| Login redirect loop / 登录重定向循环 | Check `LOGIN_URL` in `settings.py` is set to `'/login/'` |
| Template not found / 模板未找到 | Ensure templates are in correct directory: `reviews/templates/reviews/` |

---

## 🔧 Development Tips / 开发技巧

### Enable Debug Mode / 启用调试模式

In `PhoneRadar/settings.py`:
```python
DEBUG = True  # Set to False in production / 生产环境设为 False
```

### View Database / 查看数据库

```bash
# Open Django shell / 打开 Django shell
python manage.py shell

# Import models / 导入模型
from reviews.models import Brand, Model, Review

# Query all brands / 查询所有品牌
Brand.objects.all()
```

### Create Superuser if forgotten / 忘记超级管理员密码时

```bash
python manage.py createsuperuser --username your_username --email your@email.com
```

---

## 📝 Next Steps / 后续步骤

- [ ] Add more phone brands and models via admin panel
- [ ] Customize the Bootstrap theme colors
- [ ] Add user profile pictures
- [ ] Implement review voting/rating system
- [ ] Add search functionality
- [ ] Deploy to production (PythonAnywhere, Heroku, or Render)

---

## 🤝 Contributing / 贡献指南

Contributions are welcome! Please feel free to submit a Pull Request.

欢迎贡献！请随时提交 Pull Request。

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License / 许可证

This project is open source and available under the [MIT License](LICENSE).

本项目开源，基于 [MIT 许可证](LICENSE)。

---

## 📧 Contact / 联系方式

For questions or feedback, please open an issue on GitHub.

如有问题或反馈，请在 GitHub 上提交 Issue。
