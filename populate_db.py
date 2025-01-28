from models import Projektas, db
from app import app

with app.app_context():
    projects = [
        Projektas(brand='BMW', model='320', year= 2004 ,price=8000, image='images/cars/bmw-320-2004.jpeg'),
        Projektas(brand='BMW', model='550', year= 2015 , price=13500, image='images/cars/bmw-550-2015.jpeg'),
        Projektas(brand='BMW', model='330', year=  2018, price=14000, image='images/cars/bmw-330-2018.jpeg'),
        Projektas(brand='BMW', model='M3', year= 1996 , price=35500, image='images/cars/bmw-m3-1996.jpeg'),
        Projektas(brand='BMW', model='M5', year= 2018 , price=55000, image='images/cars/bmw-m5-2018.avif'),
        Projektas(brand='Audi', model='A4', year= 2005 , price=12000, image='images/cars/bmw-a4-2005.jpg'),
        Projektas(brand='Audi', model='A5', year=  2008, price=15000, image='images/cars/bmw-a5-2008.jpg'),
        Projektas(brand='Audi', model='A6', year= 2016 , price=18500, image='images/cars/bmw-a6-2016.jpg'),
        Projektas(brand='Audi', model='RS4', year= 2003 , price=35000, image=None),
        Projektas(brand='Audi', model='RS6', year= 2018 , price=65000, image=None),
        Projektas(brand='Mercedes-Benz', model='C135', year= 2013 , price=12500, image=None),
        Projektas(brand='Mercedes-Benz', model='S65', year= 2019 , price=42000, image=None),
        Projektas(brand='Mercedes-Benz', model='C63', year= 2015 , price=19430, image=None),
        Projektas(brand='Mercedes-Benz', model='C63 AMG', year= 2023 , price=89000, image=None),
        Projektas(brand='Mercedes-Benz', model='G35', year= 2014 , price=32000, image=None),
        Projektas(brand='VW', model='Passat', year= 2005 , price=8000, image=None),
        Projektas(brand='VW', model='Scirocco', year= 2015 , price=18000, image=None),
        Projektas(brand='VW', model='Golf', year= 2000 , price=3000, image=None),
        Projektas(brand='Ferrari', model='418', year= 2005 , price=125000, image=None),
        Projektas(brand='Aston Martin', model='DB9', year= 2008 , price=25000, image=None),

    ]

    db.session.add_all(projects)
    db.session.commit()
    print('duomenys sukurti')