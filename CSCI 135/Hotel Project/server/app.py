from flask import Flask, Response, request, jsonify
from faker import Faker
import random



faker = Faker()

app = Flask(__name__)
app.config["CACHE_TYPE"] = "simple"
app.secret_key = "This will change later but for now the secret key is HELLO WORLD"


fake_employee_data = []
for i in range(0, 3):
    id = random.randint(0, 1000)
    name = faker.name()
    job = faker.job()
    age = faker.random_int(17, 81)
    salary = faker.random_int()
    ssn = f"{faker.random_digit()}{faker.random_digit()}{faker.random_digit()}-{faker.random_digit()}{faker.random_digit()}-{faker.random_digit()}{faker.random_digit()}{faker.random_digit()}{faker.random_digit()}"
    phone = faker.phone_number()
    email = faker.free_email()
    fake_employee_data.append({"id": id, "name" : name, "job" : job, "age" : age, "phone" : phone, "salary": salary, "email" : email, "ssn" : ssn})

@app.route("/api/add/employee", methods=["POST"])
def add_employee():
    data = request.get_json()
    fake_employee_data.append({"id": random.randint(0, 1000), 
    "name" : f"{data['First Name']} {data['Middle Initial']}. {data['Last Name']}", 
    "job" : data['Occupation'], 
    "age" : data['Date of Birth'], 
    "phone" : data['Phone Number'], 
    "salary": random.randint(0, 1000), 
    "email" : data['Email'], 
    "ssn" : data['SSN']})
    
    return jsonify({"Status" : "Great"})

@app.route("/api/get/employee", methods=["POST"])
def get_specific_employees():
    pass

@app.route("/api/get/employees", methods=["GET"])
def get_all_employees():
    
    return jsonify(fake_employee_data)

@app.route("/api/get/today/employees", methods=["POST"])
def get_all_employees_for_date():
    pass




if __name__ == "__main__":
    app.run(debug=True)