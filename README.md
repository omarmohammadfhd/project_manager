# Project Manager API (Django + DRF)

## ✅ Features

- إدارة مشاريع ومهام
- توثيق JWT
- صلاحيات متعددة (مدير المشروع، المكلّف بالمهمة)
- فلترة وبحث ديناميكي
- اختبارات جاهزة

## 🚀 Setup

```bash
git clone <repo-url>
cd project_manager
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🔐 Auth

- POST `/api/token/` — الحصول على access و refresh token
- POST `/api/token/refresh/` — تجديد التوكن

## 📦 Endpoints

- `/api/projects/`
- `/api/tasks/?status=done&assignee=3&search=keyword`

## 🧪 Tests

```bash
python manage.py test
```

## 📄 Notes

- تأكد من إضافة المستخدم كعضو في المشروع لعرض المهام.