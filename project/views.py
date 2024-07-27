from flask import request, jsonify, Blueprint, current_app, send_from_directory
import os
from werkzeug.utils import secure_filename
from project.image import classify_image
from models import create_bgm

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


# BGM表示ルート
@bp.route('/bgm/<emotion>',methods=['GET'])
def bgm(emotion):
    # BGMの生成ロジックをimportし記載
    #bgm = "bgm.mp4"
    bgm = create_bgm(emotion, 'bgm', 6.0)    #現状、wavファイル"bgm.wav"
    return jsonify({'bgm': bgm}),201
