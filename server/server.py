# server/server.py

from concurrent import futures
import grpc
import embed_pb2
import embed_pb2_grpc
from embedder import FaceEmbedder

class EmbedService(embed_pb2_grpc.FaceEmbedderServicer):
    def __init__(self):
        self.embedder = FaceEmbedder()

    def GetEmbedding(self, request, context):
        embedding, error = self.embedder.get_embedding(request.image)
        return embed_pb2.EmbeddingResponse(embedding=embedding or [], error=error)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    embed_pb2_grpc.add_FaceEmbedderServicer_to_server(EmbedService(), server)
    server.add_insecure_port('[::]:7178')
    print("🚀 Embedding service running at :7178")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
