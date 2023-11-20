from app import db
from datetime import datetime
from app.model.bus import Bus


class Alert(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    bus_id = db.Column(db.BigInteger, db.ForeignKey(Bus.bus_id, ondelete="CASCADE"))
    category = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Alert {self.id}>"
