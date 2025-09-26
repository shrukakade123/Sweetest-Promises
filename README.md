Sweetest Promises - Stylish Scaffold
-----------------------------------
This scaffold contains a stylish Django project with pages: home, services, packages, portfolio, booking, contact, auth.
To run:
1. python -m venv venv && source venv/bin/activate
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver
Notes:
- Add ServiceCategory, Service, Package, PortfolioItem via admin to populate content.
- Static JS includes lightbox and simple confetti effect for booking success.
