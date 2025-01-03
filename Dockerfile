# استفاده از تصویر پایه Python
FROM python:3.9-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی فایل‌های مورد نیاز به دایرکتوری کاری
COPY requirements.txt .
COPY app.py .
COPY c.css .

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# تنظیم دستور اجرای برنامه
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
