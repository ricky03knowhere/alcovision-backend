from app import app
from app.controller import AlertController, BusController
from flask import request, jsonify
from datetime import datetime



# @socketio.on('connect')
# def connect():
#     print('Client connected')

# @socketio.on('disconnect')
# def disconnect():
#     print('Client disconnected')
    
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")

@app.route("/")
def index():
    return AlertController.index()


@app.route("/api/v1/alerts/<bus_id>")
def bus_alert(bus_id):
    return AlertController.bus_alert(bus_id)


@app.route("/api/v1/alerts", methods=["POST"])
def alert():
    return AlertController.save()


@app.route("/api/v1/buses")
def buses():
    return BusController.index()
