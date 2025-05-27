import unittest
import grpc
from face_recognition_protos import embed_pb2
from face_recognition_protos import embed_pb2_grpc

class TestFaceEmbedder(unittest.TestCase):

    def setUp(self):
        self.channel = grpc.insecure_channel("localhost:7178")
        self.stub = embed_pb2_grpc.FaceEmbedderStub(self.channel)
        with open("leo_messi.webp", "rb") as f:
            self.image_data = f.read()

    def test_embedding_success(self):
        request = embed_pb2.ImageRequest(image=self.image_data)
        response = self.stub.GetEmbedding(request)

        self.assertFalse(response.error, f"Got error from service: {response.error}")
        self.assertEqual(len(response.embedding), 512, "Embedding vector should have 512 elements")

    def tearDown(self):
        self.channel.close()


if __name__ == "__main__":
    unittest.main()
