from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Welcome to your AWS CodePipeline Practice App!",
        "version": "1.0.0",
        "environment": "AWS Cloud"
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Cloud environments often expect the app to run on port 80 or 8080
    app.run(host='0.0.0.0', port=8080)
