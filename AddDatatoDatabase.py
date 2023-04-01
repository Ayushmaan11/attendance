
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://attendence-c8c88-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {

    "852741":
        {
             "name": "Emly Shah",
             "Branch": "IT",
             "Starting_year": 2020,
             "total_attendance": 4,
             "standing": "B",
             "year": 2,
             "Last_attendance_time": "2023-1-12 00:53:33"
        },
    "963852":
        {
             "name": "Elon Musk",
             "Branch": "Civil",
             "Starting_year": 2022,
             "total_attendance": 16,
             "standing": "g",
             "year": 2,
             "Last_attendance_time": "2023-1-12 00:53:33"
        },
    "456789":
        {
             "name": "Saumitra",
             "Branch": "comps",
             "Starting_year": 2020,
             "total_attendance": 10,
             "standing": "g",
             "year": 2,
             "Last_attendance_time": "2023-1-12 00:53:33"
        }


}

for key, value in data.items():
    ref.child(key).set(value)
