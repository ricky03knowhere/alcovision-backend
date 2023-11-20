from app import db
from datetime import datetime


class Bus(db.Model):
    bus_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    bus_name = db.Column(db.String(50), nullable=False)
    bus_route = db.Column(db.String(50), nullable=False)
    information = db.Column(db.String(246), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Bus {self.full_name}>"
