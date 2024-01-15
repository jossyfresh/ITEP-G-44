# app/routes.py
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()

bp_receive_sensor_data = Blueprint('receive_sensor_data', __name__)

@bp_receive_sensor_data.route('/receive-sensor-data', methods=['POST'])
def receive_sensor_data():
    try:
        data = request.json
        humidity = data.get('humidity')
        temperature = data.get('temperature')
        soil_moisture = data.get('soil_moisture')

        if humidity is not None and temperature is not None and soil_moisture is not None:
            new_sensor_data = {
                'humidity': humidity,
                'temperature': temperature,
                'soil_moisture': soil_moisture
            }

            # Add data to a collection named 'sensor_data'
            db.collection('sensor_data').add(new_sensor_data)

            return jsonify({"status": "success"})

        return jsonify({"status": "error", "message": "Invalid sensor data"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

bp_get_sensor_data = Blueprint('get_sensor_data', __name__)

@bp_get_sensor_data.route('/get-sensor-data', methods=['GET'])
def get_sensor_data():
    try:
        # Retrieve data from the 'sensor_data' collection
        sensor_data_ref = db.collection('sensor_data')
        sensor_data = sensor_data_ref.get()

        if sensor_data:
            # Convert Firestore response to a list of dictionaries
            sensor_data_list = [item.to_dict() for item in sensor_data]
            return jsonify({"status": "success", "data": sensor_data_list})
        else:
            return jsonify({"status": "success", "data": []})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
