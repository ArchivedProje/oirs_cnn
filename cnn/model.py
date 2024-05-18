import tensorflow as tf


class Model:
    def __init__(self, path_to_model, img_height=150, img_width=150):
        self.model = tf.keras.models.load_model(path_to_model)
        self.img_height = img_height
        self.img_width = img_width

    def predict(self, filename):
        img = tf.keras.utils.load_img(filename, target_size=(self.img_height, self.img_width))
        img_arr = tf.keras.utils.img_to_array(img)
        img_arr /= 255
        prediction = self.model.predict(img_arr.reshape(1, *img_arr.shape), verbose=0).flatten()
        if prediction > 0.5:
            return 'не заражен с вероятностью ' + str(prediction[0])
        return 'заражен с веротяностью ' + str(1 - prediction[0])
