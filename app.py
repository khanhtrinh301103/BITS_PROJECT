from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/run-notebook', methods=['GET'])
def run_notebook():
    # URL of the notebook in Google Colab
    notebook_url = "https://colab.research.google.com/drive/1K4pukgH1k3d4kWnXp66hZjqAGjh4n4gL"

    # API to run the notebook
    colab_api_url = f"https://colab.research.google.com/drive/1K4pukgH1k3d4kWnXp66hZjqAGjh4n4gL#scrollTo=QTkHgXyJb0GB"

    # Set up the request to run the notebook
    response = requests.get(colab_api_url)
    if response.status_code == 200:
        result = {'status': 'success', 'message': 'Notebook executed successfully'}
    else:
        result = {'status': 'error', 'message': 'Failed to execute the notebook'}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
