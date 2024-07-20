# create_appをimport
from project import create_app

app = create_app()

if __name__ == '__main__':
    # Flask起動
    # port:ポート番号の設定
    app.run(debug=True,port=5000)