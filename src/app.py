from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

def fetchDetails():
    # Fetch the hostname
    host_name = socket.gethostname()
    # Fetch the IP address using the hostname
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, ip_address = fetchDetails()
    return render_template('index.html', hostname=hostname, ip_address=ip_address)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


