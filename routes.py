from flask import Flask, jsonify, request

@app.route('/customer', methods=['POST'])
def add_customers():
    data = request.get_json()
    name = data['name']
    address = data['address']
    phone = data['phone']
    email = data['email']
    dob = data['dob']
    kyc_status = data['kyc_status']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Customer (Name, Address, Phone, Email, DateOfBirth, KYCStatus) VALUES(%s, %s, %s, %s, %s, %s)", 
               (name, address, phone, email, dob, kyc_status))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Customer added successfully!"}), 201

#Get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT* FROM Customers")
    customers = cur.fetchall()
    cur.close()
    return jsonify(customers)