from flask import Flask, Response, request, jsonify
from faker import Faker
import random

from models.employees import *


faker = Faker()

app = Flask(__name__)
app.config["CACHE_TYPE"] = "simple"
app.secret_key = "This will change later but for now the secret key is HELLO WORLD"


@app.route("/api/add/employee", methods=["POST"])
def add_employee():
    data = request.get_json()
    new_hire = Employee(
        data['First Name'],
        data['Middle Initial'],
        data['Last Name'],
        data['Occupation'],
        data['Date of Birth'],
        data['Phone Number'],
        data['Email'],
        data['Occupation Steps'],
        data['SSN']
    )
    new_hire.createEmployeeDict()
    return Response("Created employee!", 200)

@app.route("/api/get/employee", methods=["POST"])
def get_specific_employees():
    data = request.get_json()
    person = ModifyEmployee(data['SSN'])
   
    if person.check_status() == False:
        return Response("No Employee!", 400)
    else:
        return person.get_employee(), 200
    

@app.route("/api/get/employees", methods=["GET"])
def get_all_employees():
    with open("data/hotel.json") as hotel_data:
      data = json.load(hotel_data)
    return jsonify(data['employees']['info'])

@app.route("/api/employee/modify", methods=["POST"])
def modify_specific_employees():
    data = request.get_json()
    if data['Modification'] == "Fire":
        Ex_Employee = ModifyEmployee(data["SSN"]).deleteEmployee()
        Response(f"{data['Name']} has been terminated!", 200)
    if data["Modification"] == "Modify":
        print(data)
        Updated_Employee = ModifyEmployee(
            data["SSN"]
        ).modifyEmployee(
            {
                "Name" :  data["Name"],
                "Job Title" : data['Occupation'],
                "Date of Birth" :  data['Date of Birth'],
                "Phone" : data['Phone Number'],
                "Email" :  data['Email'],
                "Occupation Steps" : data['Occupation Steps'],
                "SSN" :  data['SSN'],
                "Age" : data["Age"]
            }
            
        )
    return Response("Hwey", 200)







if __name__ == "__main__":
    app.run(debug=True)