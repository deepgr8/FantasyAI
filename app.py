from flask import Flask, request, jsonify,render_template,redirect

app = Flask(__name__)

# Configuration
app.config['DEBUG'] = True  # Enable debug mode for development

# Sample route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Sample API route
@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    return jsonify({"received_data": data})

@app.route('/authentication')
def authentication():
    return render_template('authentication.html')


@app.route('/features')
def features():
    return redirect('/')



# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
