#main.py
from flask import Flask, jsonify, request
from db import get_users, add_users, delete_user, update_user, get_user_id, get_user_name, get_user_email, get_user_address, checkPostedData, add_audio, get_audio, update_audio, get_audio_id


app = Flask(__name__)

# Creating routes for the REST APIs to get information from User Table 
@app.route('/', methods=['POST', 'GET', 'DELETE', 'PUT'])
def users():

    if request.method == 'GET':
        return get_users()

    else:

        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400 

        # validate data
        postedData = request.get_json()

        statusCode = checkPostedData(postedData, "users")
    
        if statusCode != 200:
            retJson = {
                "Message":"An error happened. One of JSON keys is missing.",
                "Status Code": statusCode 
            }
            return jsonify(retJson)

        if request.method == 'POST':
            add_users(request.get_json())
            return 'User Added'

        elif request.method == 'PUT':
            update_user(request.get_json())
            return 'User Updated'

        elif request.method == 'DELETE':
            delete_user(request.get_json())
            return 'User Deleted'



@app.route('/id/<id>')
def user_id(id):
    return get_user_id(id)


@app.route('/name/<name>')
def user_name(name):
    return get_user_name(name)


@app.route('/email/<email>')
def user_email(email):
    return get_user_email(email)

@app.route('/address/<address>')
def user_address(address):
    return get_user_address(address)

# Creating Routes for REST APIs to get information from the Audio Table 

@app.route('/audio', methods=['POST', 'GET', 'DELETE', 'PUT'])
def audio():

    if request.method == 'GET':
        return get_audio()

    else:
        # validate input 
        step_count = request.get_json()["step_count"]

        if step_count not in range(10):
            retJson = {"Message": "Step_count must be 0 to 9 in value"}
            return jsonify(retJson)

        selected_tick = request.get_json()["selected_tick"]

        if selected_tick not in range(15):
            retJson = {"Message": "Selected_tick must be 0 to 14 in value"}
            return jsonify(retJson)
        
        ticks = request.get_json()["ticks"]
        for elem in ticks:
            if elem < -100 or elem > -10:
                retJson = {"Message": "Ticks” must range from -10.0 to -100.0"}
                return jsonify(retJson)

        if len(ticks) != 15:
            retJson = {"Message": "The length of the list needs to be 15."}
            return jsonify(retJson)

        if request.method == 'POST':
            add_audio(request.get_json())
            return 'Audio Added'

        elif request.method == 'PUT':
            update_audio(request.get_json())
            return 'Audio Updated'

@app.route('/audio/session_id/<session_id>')
def session_id(session_id):
    return get_audio_id(session_id)

    

if __name__ == '__main__':
    app.run()


