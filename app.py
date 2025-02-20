from flask import Flask, jsonify, request
#Difficulty in installing the connector. still to troubleshoot
    
app = Flask(__name__)
    
    #MySQL  configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'banking_system'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    
mysql = MySQL(app)
    
@app.route('/')
def home():
        return "Welcome to the Banking System!"
    
if __name__ == '__main__':
        app.run(debug=True)





