import dlib
import os
import numpy as np
from config import MODELS_DIR

class FaceEncoder:
    def __init__(self):
        predictor_path = os.path.join(MODELS_DIR, "shape_predictor_68_face_landmarks.dat")
        face_rec_model_path = os.path.join(MODELS_DIR, "dlib_face_recognition_resnet_model_v1.dat")
        
        if not os.path.exists(predictor_path):
            raise FileNotFoundError(f"dlib shape predictor not found at {predictor_path}")
        
        self.predictor = dlib.shape_predictor(predictor_path)
        self.face_recognizer = dlib.face_recognition_model_v1(face_rec_model_path)

    def encode(self, image, face_box):
        shape = self.predictor(image, face_box)
        return np.array(self.face_recognizer.compute_face_descriptor(image, shape))