from flask import request, jsonify, Blueprint, current_app, send_from_directory
import os
from werkzeug.utils import secure_filename
from project.image import classify_image
from project.models import create_bgm

# BluePrint設定
bp = Blueprint('main', __name__)



@bp.route('/images', methods=['POST'])
def post_image():
    if 'picture' not in request.files:
        print("No file part in the request")
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['picture']
    
    if file.filename == '':
        print("No selected file")
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File successfully uploaded', 'filename': filename}), 201
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to upload file'}), 500



@bp.route('/classify/<filename>', methods=['GET'])
def classify(filename):
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    emotion = classify_image(file_path)
    return jsonify({'emotion': emotion})


# BGM保存ルート
@bp.route('/bgm/<emotion>',methods=['GET'])
def bgm(emotion):
    bgm = create_bgm(emotion, 'bgm', 6.0)    # bgm = 'filename.mp3'
    
    return jsonify({'bgm': bgm}),201

# BGM表示ルート
@bp.route('/sounds/<filename>', methods=['GET'])
def get_sound(filename):
    file_path = os.path.join(current_app.config['UPLOAD_SOUNDS'], filename)
    if os.path.exists(file_path):
        return send_from_directory(current_app.config['UPLOAD_SOUNDS'], filename)
    else:
        return jsonify({'error': 'File not found'}), 404