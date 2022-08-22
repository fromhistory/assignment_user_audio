#db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

# Set up connection with Google SQL Database  

def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn

# Function to validate data 
def checkPostedData(postedData, functionName):

    if functionName == "users":
        if "name" not in postedData or "email" not in postedData or "address" not in postedData or "image" not in postedData:
            return 301
        return 200

# Functions to retrive information from the database for User and Audio

def get_users():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM users;')
        users = cursor.fetchall()
        if result > 0:
            got_users = jsonify(users)
        else:
            got_users = 'No Users in DB'
    conn.close()
    return got_users

def get_user_id(id):
    conn = open_connection()
    with conn.cursor() as cursor:
        id = int(id)
        result = cursor.execute('SELECT * FROM users WHERE id = %s', (id))
        users = cursor.fetchall()
        if result > 0:
            got_users = jsonify(users)
        else:
            got_users = 'No Users in DB'
    conn.close()
    return got_users


def get_user_name(name):
    conn = open_connection()
    with conn.cursor() as cursor:
        name = str(name)
        result = cursor.execute('SELECT * FROM users WHERE name = %s', (name))
        users = cursor.fetchall()
        if result > 0:
            got_users = jsonify(users)
        else:
            got_users = 'No Users in DB'
    conn.close()
    return got_users

def get_user_email(email):
    conn = open_connection()
    with conn.cursor() as cursor:
        name = str(email)
        result = cursor.execute('SELECT * FROM users WHERE email = %s', (email))
        users = cursor.fetchall()
        if result > 0:
            got_users = jsonify(users)
        else:
            got_users = 'No Users in DB'
    conn.close()
    return got_users
    

def get_user_address(address):
    conn = open_connection()
    with conn.cursor() as cursor:
        address = str(address)
        result = cursor.execute('SELECT * FROM users WHERE address = %s', (address))
        users = cursor.fetchall()
        if result > 0:
            got_users = jsonify(users)
        else:
            got_users = 'No Users in DB'
    conn.close()
    return got_users

def update_user(user):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('UPDATE users SET name = %s, email = %s, address= %s WHERE id = %s', (user["name"], user["email"], user["address"], user["id"]))
    conn.commit()
    conn.close() 


def add_users(user):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO users (name, email, address, image) VALUES(%s, %s, %s, %s)', (user["name"], user["email"], user["address"], user["image"]))
    conn.commit()
    conn.close()


def delete_user(user):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM users WHERE id = %s', (user["id"]))
    conn.commit()
    conn.close()


def add_audio(audio):

    audio['ticks'] = str(audio['ticks'])
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO audio (ticks, step_count, selected_tick, user_id) VALUES(%s, %s, %s, %s)', (audio["ticks"], audio["step_count"], audio["selected_tick"], audio["user_id"]))
    conn.commit()
    conn.close()


def get_audio():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM audio;')
        audio = cursor.fetchall()
        if result > 0:
            got_audio = jsonify(audio)
        else:
            got_audio = 'No Audio in DB'
    conn.close()
    return got_audio


def update_audio(audio):

    audio['ticks'] = str(audio['ticks'])
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('UPDATE audio SET ticks = %s, step_count = %s, selected_tick= %s WHERE session_id = %s', (audio["ticks"], audio["step_count"], audio["selected_tick"], audio["session_id"]))
    conn.commit()
    conn.close()



def get_audio_id(session_id):
    conn = open_connection()
    with conn.cursor() as cursor:
        session_id = int(session_id)
        result = cursor.execute('SELECT * FROM audio WHERE session_id = %s', (session_id))
        audio = cursor.fetchall()
        if result > 0:
            got_audio = jsonify(audio)
        else:
            got_audio = 'No audio in DB'
    conn.close()
    return got_audio
    







