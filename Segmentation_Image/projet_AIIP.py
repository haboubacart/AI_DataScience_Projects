# -*- coding: utf-8 -*-
"""
Auteurs : Bouraï Yannis 
          M'Baye Alioune
          Tidjani Boukari Haboubacar
ING3, Option IA
"""

#les bibliothèques
from skimage import io
from random import sample
from mpl_toolkits.mplot3d import Axes3D
import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


#affichage des histogrammes
def afficher_histogramme(img, nb_pixel_a_afficher):
  width = img.size[0] 
  height = img.size[1]
  RGB = []
  for y in range(0, height):
      row = ""
      for x in range(0, width):
          RGB.append(img.getpixel((x,y)))
  # on cree une liste de nb_pixel_a_afficher aleatoire à afficher
  liste_point = sample(RGB, nb_pixel_a_afficher)
  fig = plt.figure()
  ax = Axes3D(fig)
  ax.set_xlabel('R')
  ax.set_ylabel('G')
  ax.set_zlabel('B')
  fig.add_axes(ax)
  for i in range(len(liste_point)):
      pixel_col = '#%02x%02x%02x' % liste_point[i]
      ax.scatter(liste_point[i][0], liste_point[i][1], liste_point[i][2], c = pixel_col)
  plt.show()


#Fonction kmeans pour la clasification des images
def Kmeans_Image_segmentation(img, K):
  
  # on transforme l'image en un vecteur d'une seule dimension
  vectorized = img.reshape((-1,3))
  vectorized = np.float32(vectorized)
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
 
  attempts=10
  ret,label,center = cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
  center = np.uint8(center)
  res = center[label.flatten()]
  result_image = res.reshape((img.shape))
  return result_image

#Fonction d'ffichage des resultats pour plusieurs valeurs de k (nombre de classe) en meme temps
def afficher_resultat(img, K1, K2, K3, K4, K5):
  figure_size = (20,15)
  plt.figure(figsize=figure_size)
  plt.subplot(2,3,1),plt.imshow(img)
  plt.subplot(2,3,2),plt.imshow(Kmeans_Image_segmentation(image,K1))
  plt.subplot(2,3,3),plt.imshow(Kmeans_Image_segmentation(image,K2))
  plt.subplot(2,3,4),plt.imshow(Kmeans_Image_segmentation(image,K3))
  plt.subplot(2,3,5),plt.imshow(Kmeans_Image_segmentation(image,K4))
  plt.subplot(2,3,6),plt.imshow(Kmeans_Image_segmentation(image,K5))
  plt.show()

#Fonction pour enregistrer sauvegarder les images obtenue par application de l'algorithme (si on le souhaite)
def enregister_images_segmenteee(image, K1, K2, K3, K4, K5)):
    io.imsave('data/imgK2.jpg',Kmeans_Image_segmentation(image,K1))
    io.imsave('data/imgK4.jpg',Kmeans_Image_segmentation(image,K2))
    io.imsave('data/imgK8.jpg',Kmeans_Image_segmentation(image,K3))
    io.imsave('data/imgK16.jpg',Kmeans_Image_segmentation(image,K4))
    io.imsave('data/imgK32.jpg',Kmeans_Image_segmentation(image,K5))

if __name__ == '__main__':
  #lire l'image pour Kmeans
  #image = image = io.imread('data/image_perroquet.jpg')

  #afficher l'image de depart
  #io.imshow(image)

  #l'histogramme de l'image de depart
  #afficher_histogramme(Image.open("data/image_perroquet.jpg"), 2000)

  #lancer kmeans et afficher les resultats 
  #afficher_resultat(img, 2, 4, 8, 16, 32)

  #Enregistre dans le dossier data les images obtenues pour les valeurs de k
  #enregister_images_segmenteee(image, 2, 4, 8, 16, 32)


  #################### afficher les histogrammes des images segmentées ##############################

  # k = 2
  #afficher_histogramme(Image.open("data/imgK2.jpg"), 2000)
   # k = 4
  #afficher_histogramme(Image.open("data/imgK4.jpg"), 2000)
   # k = 8
  #afficher_histogramme(Image.open("data/imgK8.jpg"), 2000)
   # k = 16
  #afficher_histogramme(Image.open("data/imgK16.jpg"), 2000)
   # k = 32
  #afficher_histogramme(Image.open("data/imgK32.jpg"), 2000)

