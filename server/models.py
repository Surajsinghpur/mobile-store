from extensions import db  # Import db from extensions


class Mobile(db.Model):
    __tablename__ = 'mobiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    details = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Mobile {self.name}>"


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    mobile_id = db.Column(db.Integer, db.ForeignKey('mobiles.id'), nullable=False)
    customer_name = db.Column(db.String(120), nullable=False)
    delivery_date = db.Column(db.String(120), nullable=False)

    # Establish a relationship to the Mobile model
    mobile = db.relationship('Mobile', backref=db.backref('bookings', lazy=True))

    def __repr__(self):
        return f"<Booking {self.customer_name} - Mobile ID {self.mobile_id}>"
