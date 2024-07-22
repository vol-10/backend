from flask import request, jsonify, Blueprint, current_app, send_from_directory
import os
from werkzeug.utils import secure_filename

# BluePrint設定
bp = Blueprint('main', __name__)


# 画像投稿ルート
@bp.route('/images', methods=['POST'])
def post_image():
    images = request.files['picture']
    
    picture = secure_filename(images.filename)
    images.save(os.path.join(current_app.config['UPLOAD_FOLDER'],picture))
    
    return jsonify({
        'picture': images,
    }),201


# 画像表示ルート
@bp.route('/picture/<filename>',methods=['GET'])
def picture(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],filename)

# BGM表示ルート
@bp.route('/bgm',methods=['GET'])
def bgm():
    # BGMの生成ロジックをimportし記載
    return jsonify({'bgm'}),201