from flask import Flask, request, render_template, jsonify
import os
from models import db,Dataset
from datetime import datetime 
from flask import jsonify

app = Flask(__name__)

app.config.from_pyfile('settings.py')
db.init_app(app)

# storing the required url in directory_path
directory_path = r'D:\learning\aetrex_daemon\source_data\offline\scans'
#Calling the function to get subdirectories in the directory_path
def get_subdirectories(directory):
    return [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]

#route to the home page.
@app.route("/")
def home():
    return render_template('home.html')

#calling the route for adding the subdirectories
@app.route('/add_data', methods=['POST'])
def add_user():
    subdirectories = get_subdirectories(directory_path)
    print(subdirectories)
    for subdirectory in subdirectories:
        existing_subdirectory = Dataset.query.filter_by(name=subdirectory).first()
        print(existing_subdirectory)
        if not existing_subdirectory:
            print("not")
            new_subdirectory = Dataset(
                name=subdirectory,
                processed_at=datetime.now(),
                status='pending'
            )
            db.session.add(new_subdirectory)
            message = "The subdirectories have been successfully processed and added to the database."
        else:
            existing_subdirectory.processed_at = datetime.now()
            existing_subdirectory.status = 'success'
            message ="No new data "

    db.session.commit()

    return render_template('landingpage.html')

if __name__ == '__main__':
    app.run(debug=True)
