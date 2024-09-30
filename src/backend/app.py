# ----------------------------------------------------------------------
# app.py
# ----------------------------------------------------------------------

from flask import Flask, request, jsonify
from flask_cors import CORS
from src.backend import wordhunt

# ----------------------------------------------------------------------

app = Flask(__name__)
CORS(app)


# ----------------------------------------------------------------------
@app.route("/api/find", methods=["POST"])
def find():
    data = request.json
    board = data.get("board", "")
    solver = wordhunt.Wordhunt()
    solver.make_board(board)
    solver.solve()
    solutions = solver.result
    return jsonify(solutions)


# ----------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
