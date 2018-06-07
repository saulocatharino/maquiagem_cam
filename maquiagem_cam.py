#!/usr/bin/python
# -*- coding: utf-8 -*-
# Desenvolvido por Saulo Catharino | saulocatharino@gmail.com

from PIL import Image, ImageDraw
import face_recognition
import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def tudo():

    ret, frame = cap.read()
    rob_small_frame = frame[:, :, ::-1]
    face_landmarks_list = face_recognition.face_landmarks(rob_small_frame)

    for face_landmarks in face_landmarks_list:

        frame = frame[:, :, ::-1]
        pil_image = Image.fromarray(frame)
        d = ImageDraw.Draw(pil_image, 'RGBA')
        #d.polygon(face_landmarks['chin'], fill=(0, 150, 0, 128))
        #d.polygon(face_landmarks['nose_tip'])
        #d.polygon(face_landmarks['nose_bridge'])

        # Traça as sobrancelhas
        d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
        d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
        d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
        d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

        # Pinta os lábios
        d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
        d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
        d.line(face_landmarks['top_lip'], fill=(150, 64, 0, 0), width=8)
        d.line(face_landmarks['bottom_lip'], fill=(150, 64, 0, 0), width=8)

        # Pinta ao redor dos olhos
        d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
        d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

        # Cria linha ao redor dos olhos
        d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
        d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

        image = np.array(pil_image)
        image = image[:, :, ::-1]
        cv2.imshow("Rosto com Maquiagem", image)
        frame = frame[:, :, ::-1]
        cv2.imshow("Rosto sem Maquiagem", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()


while True:
    tudo()
