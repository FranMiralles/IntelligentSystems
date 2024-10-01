from flask import Flask, request, jsonify
from flask_cors import CORS
from modelsIA import base64_to_grayscale_array, resize_image_to_8x8, trainModel, predictFromModel
from modelsIA import DECISION_TREE_MODEL, RANDOM_FOREST_MODEL, BAGGING_MODEL, ADABOOST_MODEL, GRADIENT_BOOSTING_MODEL, DECISION_TREE_FILE, RANDOM_FOREST_FILE, BAGGING_FILE, ADABOOST_FILE, GRADIENT_BOOSTING_FILE


app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app)

@app.route('/', methods=['GET'])
def root():
    return "root"


@app.route('/api/trainDecisionTree', methods=['GET'])
def trainDecisionTree():
    test_size = request.args.get('test_size', default=0.2, type=float)
    random_state = request.args.get('random_state', default=42, type=int)
    result = trainModel(modelName=DECISION_TREE_MODEL, test_size=test_size, random_state=random_state)
    return jsonify({'accuracy': result})

@app.route('/api/trainRandomForest', methods=['GET'])
def trainRandomForest():
    test_size = request.args.get('test_size', default=0.2, type=float)
    random_state = request.args.get('random_state', default=42, type=int)
    n_estimators = request.args.get('n_estimators', default=100, type=int)
    result = trainModel(modelName=RANDOM_FOREST_MODEL, test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    return jsonify({'accuracy': result})

@app.route('/api/trainBagging', methods=['GET'])
def trainBagging():
    test_size = request.args.get('test_size', default=0.2, type=float)
    random_state = request.args.get('random_state', default=42, type=int)
    n_estimators = request.args.get('n_estimators', default=100, type=int)
    result = trainModel(modelName=BAGGING_MODEL, test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    return jsonify({'accuracy': result})

@app.route('/api/trainAdaboost', methods=['GET'])
def trainAdaboost():
    test_size = request.args.get('test_size', default=0.2, type=float)
    random_state = request.args.get('random_state', default=42, type=int)
    n_estimators = request.args.get('n_estimators', default=100, type=int)
    result = trainModel(modelName=ADABOOST_MODEL, test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    return jsonify({'accuracy': result})

@app.route('/api/trainGradientBoosting', methods=['GET'])
def trainGradientBoosting():
    test_size = request.args.get('test_size', default=0.2, type=float)
    random_state = request.args.get('random_state', default=42, type=int)
    n_estimators = request.args.get('n_estimators', default=100, type=int)
    result = trainModel(modelName=GRADIENT_BOOSTING_MODEL, test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    return jsonify({'accuracy': result})

@app.route('/api/trainAll', methods=['GET'])
def trainAll():
    test_size = request.args.get('test_size', default=0.2, type=float)
    random_state = request.args.get('random_state', default=42, type=int)
    n_estimators = request.args.get('n_estimators', default=100, type=int)
    result1 = trainModel(modelName=DECISION_TREE_MODEL, test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    result2 = trainModel(modelName=RANDOM_FOREST_MODEL, test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    result3 = trainModel(modelName=BAGGING_MODEL, test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    result4 = trainModel(modelName=ADABOOST_MODEL, test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    result5 = trainModel(modelName=GRADIENT_BOOSTING_MODEL, test_size=test_size, random_state=random_state, n_estimators=n_estimators)
    return jsonify({'accuracyDT': result1, 'accuracyRF': result2, 'accuracyB': result3, 'accuracyAB': result4, 'accuracyGB': result5})


@app.route('/api/image', methods=['GET'])
def image():
    image = request.args.get('image')
    grayscale_array = base64_to_grayscale_array(image)
    
    if grayscale_array is None:
        return jsonify({'error': 'Invalid image data'}), 400

    resized_image = resize_image_to_8x8(grayscale_array)
    
    if resized_image is None:
        return jsonify({'error': 'Image resizing failed'}), 400

    classification = predictFromModel(DECISION_TREE_FILE, resized_image)
    classificationRF = predictFromModel(RANDOM_FOREST_FILE, resized_image)
    classificationB = predictFromModel(BAGGING_FILE, resized_image)
    classificationAB = predictFromModel(ADABOOST_FILE, resized_image)
    classificationGB = predictFromModel(GRADIENT_BOOSTING_FILE, resized_image)
    return jsonify({'decisionTree': classification, 'randomForest': classificationRF, 'predictB': classificationB, 'predictAB': classificationAB, 'predictGB': classificationGB})


if __name__ == '__main__':
    app.run(port=5000)