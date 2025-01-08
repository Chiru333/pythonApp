from flask import Flask, jsonify



app = Flask(__name__)



@app.route('/')

def home():

  return "Welcome to the AWS Infra Test App!"



@app.route('/health')

def health_check():

  return jsonify({"status": "UP"}), 200



if __name__ == '__main__':

  app.run(host='0.0.0.0', port=5000)

