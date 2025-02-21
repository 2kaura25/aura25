import os
from flask import Flask, render_template, request, redirect, url_for
from firebase import db

app = Flask(__name__)

# Database connection parameters (update these with your actual credentials)
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    if DATABASE_URL is None:
        raise ValueError("❌ DATABASE_URL is not set. Please add it in Render.")
    conn = psycopg2.connect(DATABASE_URL)
    return conn


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tech')
def tech():
    return render_template("tech.html")

@app.route('/nontech')
def nontech():
    return render_template("nontech.html")
# Tech Events Registration

@app.route('/cipher', methods=['GET', 'POST'])
def cipher():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']

        # Save to Firebase Firestore
        event_data = {
            "team_name": team_name,
            "member1_name": member1_name,
            "member1_department_and_year": member1_department_year,
            "member2_name": member2_name,
            "member2_department_and_year": member2_department_year
        }

        # Get reference to "cipher_chase" collection in Firestore
        db.collection('cipher_chase').add(event_data)

        return redirect(url_for('index'))

    return render_template("cipher.html")


@app.route('/scrunch', methods=['GET', 'POST'])
def scrunch():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']

        # Save to Firestore
        event_data = {
            "team_name": team_name,
            "member1_name": member1_name,
            "member1_department_and_year": member1_department_year,
            "member2_name": member2_name,
            "member2_department_and_year": member2_department_year
        }

        # Add data to Firestore collection for Scrunch event
        db.collection('scrunch_and_pick').add(event_data)

        return redirect(url_for('index'))

    return render_template("scrunch.html")

@app.route('/ryz', methods=['GET', 'POST'])
def ryz():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']
        member3_name = request.form['member3_name']
        member3_department_year = request.form['member3_department_and_year']

        # Create a dictionary with the event data
        event_data = {
            "team_name": team_name,
            "member1_name": member1_name,
            "member1_department_and_year": member1_department_year,
            "member2_name": member2_name,
            "member2_department_and_year": member2_department_year,
            "member3_name": member3_name,
            "member3_department_and_year": member3_department_year
        }

        # Save the data to Firebase Firestore
        db.collection('ryz_n_fall').add(event_data)

        return redirect(url_for('index'))

    return render_template("ryz.html")


# Non-Tech Events Registration

@app.route('/booth', methods=['GET', 'POST'])
def booth():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']

        # Create a dictionary with the event data
        event_data = {
            "team_name": team_name,
            "member1_name": member1_name,
            "member1_department_and_year": member1_department_year,
            "member2_name": member2_name,
            "member2_department_and_year": member2_department_year
        }

        # Save the data to Firebase Firestore
        db.collection('booth').add(event_data)

        return redirect(url_for('index'))

    return render_template("booth.html")

@app.route('/dalgona', methods=['GET', 'POST'])
def dalgona():
    if request.method == 'POST':
        member1_name = request.form['player_name']
        member1_department_year = request.form['department_and_year']

        # Create a dictionary with the event data
        event_data = {
            "player_name": member1_name,
            "department_and_year": member1_department_year
        }

        # Save the data to Firebase Firestore
        db.collection('dalgona').add(event_data)

        return redirect(url_for('index'))

    return render_template("dalgona.html")

@app.route('/moviemania', methods=['GET', 'POST'])
def moviemania():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']
        member3_name = request.form['member3_name']
        member3_department_year = request.form['member3_department_and_year']

        # Create a dictionary with the event data
        event_data = {
            "team_name": team_name,
            "member1_name": member1_name,
            "member1_department_and_year": member1_department_year,
            "member2_name": member2_name,
            "member2_department_and_year": member2_department_year,
            "member3_name": member3_name,
            "member3_department_and_year": member3_department_year
        }

        # Save the data to Firebase Firestore
        db.collection('moviemania').add(event_data)

        return redirect(url_for('index'))

    return render_template("moviemania.html")


if __name__ == "__main__":
    app.run(debug=True)
