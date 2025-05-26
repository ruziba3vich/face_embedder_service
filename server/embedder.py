# server/embedder.py

import numpy as np
import cv2
from insightface.app import FaceAnalysis

class FaceEmbedder:
    def __init__(self):
        self.app = FaceAnalysis(name="buffalo_l", providers=['CPUExecutionProvider'])
        self.app.prepare(ctx_id=0)

    def get_embedding(self, image_bytes: bytes):
        try:
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            faces = self.app.get(img)
            if not faces:
                return None, "No face detected"

            return faces[0].embedding.tolist(), ""
        except Exception as e:
            return None, str(e)
