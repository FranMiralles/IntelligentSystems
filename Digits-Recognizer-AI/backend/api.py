from flask import Flask, request, jsonify
from flask_cors import CORS
from modelsIA import processDecisionTree, processRandomForest

app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app)

@app.route('/', methods=['GET'])
def root():
    return "root"

@app.route('/api/processDecisionTree', methods=['GET'])
def trainDecisionTree():
    test_size = request.args.get('test_size', default=0.2, type=float)
    random_state = request.args.get('random_state', default=42, type=int)

    result = processDecisionTree(test_size=test_size, random_state=random_state)
    return jsonify({'output': result})

@app.route('/api/processRandomForest', methods=['GET'])
def trainRandomForest():
    test_size = request.args.get('test_size', default=0.2, type=float)
    random_state = request.args.get('random_state', default=42, type=int)
    n_estimators = request.args.get('n_estimators', default=42, type=int)

    result = processRandomForest(test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(port=5000)