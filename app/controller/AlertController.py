from app import app
from app.model.alert import Alert
from app.model.bus import Bus
from app.utils.utils import format_array

from app import response, db
from flask import request
from flask_socketio import SocketIO

from threading import Lock


thread = None
thread_lock = Lock()

socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

def index():
    try:
        alert = Alert.query.all()
        data = format_array(alert)
        return response.success(data, "success")
    except Exception as err:
        print("Error =>>> ", err)


def bus_alert(bus_id):
    try:
        alert = Alert.query.filter_by(bus_id=bus_id).order_by(Alert.created_at.desc()).limit(5).all()
        bus = Bus.query.filter(Bus.bus_id == bus_id)

        data_bus = format_array(bus)
        if not alert:
            data = {"bus": data_bus, "alerts": "This bus has no alert!"}
            return response.bad_request(data, "This bus has no alert!")

        data_alert = format_array(alert)
        data = {"bus": data_bus, "alerts": data_alert}
        return response.success(data, "success")

    except Exception as err:
        print("Error : ", err)


def save():
    try:
        bus_id, category = request.json.values()
        alerts = Alert(bus_id=bus_id, category=category)

        db.session.add(alerts)
        
        print("IO ADD")
        socketio.emit('message', {'alerts': category})
        db.session.commit()

        return response.success([request.json], "Data Successfuly Added.")
    except Exception as err:
        print("Error : ", err)



# socketio.run(app, port=5005)