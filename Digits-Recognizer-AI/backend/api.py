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
    test_size = request.args.get('test_size')
    random_state = request.args.get('random_state')

    result = processDecisionTree(test_size=test_size, random_state=random_state)

    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(port=5000)