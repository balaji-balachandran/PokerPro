from flask import Flask, request, jsonify
import threading
import algorithm

app = Flask(__name__)

# Storage to hold results from /hand and /board clients
hand_results = []
board_results = []

@app.route('/hand', methods=['POST'])
def hand():
    """Handles data submissions from the 'hand' client."""
    data = request.json  # Get JSON data from client
    if not data:
        return jsonify({"error": "No data provided"}), 400

    hand_results.append(data)  # Store data in hand_results
    return jsonify({"message": "Hand data received successfully", "hand_results": hand_results})

@app.route('/board', methods=['POST'])
def board():
    """Handles data submissions from the 'board' client."""
    data = request.json  # Get JSON data from client
    if not data:
        return jsonify({"error": "No data provided"}), 400

    board_results = data  # Store data in board_results
    return jsonify({"message": "Board data received successfully", "board_results": board_results})

@app.route('/get_results', methods=['GET'])
def get_results():
    """Provides all stored results from /hand and /board."""
    return jsonify({
        "hand_results": hand_results,
        "board_results": board_results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
