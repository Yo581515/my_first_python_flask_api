from app import app, db, Drink
from sqlalchemy.exc import IntegrityError

with app.app_context():
    db.create_all()

    try:
        drink1 = Drink(id=2, name="Orangne Soda", description="Tastes like orange")
        db.session.add(drink1)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()  # Roll back the session in case of error for items
        print('A drink with this ID already exists.')

    print(Drink.query.filter(Drink.id < 3).all())