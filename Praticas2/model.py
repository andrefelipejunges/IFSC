from keras.preprocessing import image as keras_image
from keras import models
import numpy as np
from PIL import Image

class Model:
  def __init__(self, modelName:str):
    self.model : models.Model = models.load_model(modelName)
    self.medidaBalanceada = 0.67

  def predict_ImagemSelecionada(self, imagePath: str):
    image = self.__CarregarImagem(imagePath)
    image = self.__RedimensionarImagem(image)
    prediction = self.model.predict(image)

    if prediction > self.medidaBalanceada:
      return 'Pessoa'

    return 'Cavalo'     

  def load_weights(self, filename):
    self.model.load_weights(filename)

  def __RedimensionarImagem(self, image):
    image = image.resize((64,64), Image.LINEAR)
    image = keras_image.img_to_array(image)
    image = image/255
    image = np.expand_dims(image, axis = 0)
    return image

  def __CarregarImagem(self, caminho):
    return Image.open(caminho).convert('RGB')    