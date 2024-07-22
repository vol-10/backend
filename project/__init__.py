from flask import Flask
from flask_cors import CORS

import os

# cors設定
# CORS:今回で言えば、Flaskの内容をReactで表示できるようにすることかな？
cors = CORS()

# Flaskアプリケーション登録
def create_app(config_filename='config.py'):
    # アプリ名
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config.from_pyfile(config_filename)
    cors.init_app(app)
    
    # 画像パス設定
    app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(),'project/static/images/')
    # blueprint設定
    from project.views import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app