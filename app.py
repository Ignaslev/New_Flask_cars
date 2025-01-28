from models import db, Projektas
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# fizinises db prijungimas, konfiguyracija
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicijuojam db
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    search_text = request.args.get('search')
    if search_text:
        filtered_rows = Projektas.query.filter(Projektas.brand.ilike(f'{search_text}%'))

    else:
        filtered_rows = Projektas.query.all()

    cheapest_car = Projektas.query.order_by(Projektas.price.asc()).first()
    most_expensive_car = Projektas.query.order_by(Projektas.price.desc()).first()
    avg_year = db.session.query(db.func.avg(Projektas.year)).scalar()
    avg_price = db.session.query(db.func.avg(Projektas.price)).scalar()

    return render_template('index.html', projects=filtered_rows, cheapest_car=cheapest_car,
                           most_expensive_car=most_expensive_car, avg_year=avg_year, avg_price=avg_price)


@app.route('/project/<int:row_id>')
def one_project(row_id):
    project = Projektas.query.get(row_id)
    if project:
        return render_template('one_project.html', project=project)
    else:
        return f'Car {row_id} does not exist'


@app.route('/project/edit/<int:row_id>', methods=['get', 'post'])
def update_project(row_id):
    project = Projektas.query.get(row_id)
    if not project:
        pass
    if request.method == 'GET':
        return render_template('update_project_form.html', project=project)
    elif request.method == 'POST':
        brand = request.form.get('brandfield')
        model = request.form.get('modelfield')
        year = int(request.form.get('yearfield'))
        price = float(request.form.get('pricefield'))
        image = request.form.get('imagefield')

        project.brand = brand
        project.model = model
        project.year = year
        project.price = price
        if image:
            project.image = image
        else:
            project.image = None
        db.session.commit()
        # return redirect(url_for('home'))
        return redirect(f'/project/{row_id}')


@app.route('/project/delete/<int:row_id>', methods=['post'])
def delete_project(row_id):
    project = Projektas.query.get(row_id)
    if not project:
        return f'Car {row_id} not found'
    else:
        db.session.delete(project)
        db.session.commit()
        return redirect(url_for("home"))


@app.route('/project/new', methods=['get', 'post'])
def create_project():
    if request.method == 'GET':
        return render_template('create_project_form.html')
    if request.method == 'POST':
        brand = request.form.get('brandfield')
        model = request.form.get('modelfield')
        year = request.form.get('yearfield')
        price = request.form.get('pricefield')
        image = request.form.get('imagefield')

        if brand and model and year and price:
            if image:
                new_project = Projektas(brand=brand, model=model, year=year, price=price, image=image)
                db.session.add(new_project)
                db.session.commit()
            else:
                new_project = Projektas(brand=brand, model=model, year=year, price=price, image=None)
                db.session.add(new_project)
                db.session.commit()
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
