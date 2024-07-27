import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# モデルの読み込み
model = tf.keras.models.load_model('image_model.h5')

# クラスラベル（モデル訓練時に使用したものと一致させる必要があります）
class_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']  # 例: 7つのクラス

# 画像の読み込みと前処理
def preprocess_image(img_path, target_size=(48, 48)):
    img = image.load_img(img_path, target_size=target_size, color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # 正規化
    img_array = np.expand_dims(img_array, axis=0)  # バッチサイズの次元を追加
    return img_array

# 画像のパス
img_path = 'project/static/images/'
img_array = preprocess_image(img_path)

# 予測
predictions = model.predict(img_array)
predicted_class_index = np.argmax(predictions, axis=1)

# クラスラベルの表示
predicted_label = class_labels[predicted_class_index[0]]
print(f'予測された感情ラベル: {predicted_label}')
