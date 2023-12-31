1. install pip (python)
2. Tạo môi trường ảo lưu trữ package bằng venv
  python -m venv venv

3. Install các thư viện (dùng file requirements.txt)
pip install -r requirements.txt
<!-- pip freeze | xargs pip uninstall -y -->

4. Run
  source venv/bin/activate
  cd core
  python manage.py runserver