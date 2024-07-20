from flask import Flask

import os

# Flaskアプリケーション登録
def create_app(config_filename='config.py'):
    # アプリ名
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config.from_pyfile(config_filename)
    
    # blueprint設定
    from project.views import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app