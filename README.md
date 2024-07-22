# Flask起動コマンド
flask --app app --debug run

# installライブラリ
pip install flask
pip install flask-cors

# もしかしたら必要になるかも
pip install flask-sqlalchemy
pip install flask-migrate


# Flaskを起動したときにでるログを無効にするファイル
# これがないとgithubでmargeするときにコンフリクト起こすやつ
.gitignore
.gitattributes

