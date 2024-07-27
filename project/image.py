import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
import numpy as np

# モデルのロード 
model = tf.keras.models.load_model('image_model.h5')

# テスト画像のパス
img_path = 'project/static/images'

# 画像の読み込みと前処理
img = image.load_img(img_path, target_size=(48, 48), color_mode='grayscale') # Change target_size to (48, 48) and convert to grayscale
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
#x = preprocess_input(x) # Remove this line as VGG16 preprocessing is not needed

# 予測の実行
preds = model.predict(x)

# 結果の表示 - decode_predictions is not applicable for this model
print('Predicted:', preds)

# Get the predicted class index
predicted_class_index = np.argmax(preds)

# Assuming you have a list of class names
class_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']  # Replace with your actual class names

# Print the predicted class
print('Predicted class:', class_names[predicted_class_index])