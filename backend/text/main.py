import sys
import grpc
import os
from concurrent import futures

from backend.text import server_lib
from shared.proto.services.llm import llm_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))

    # Register the imported class
    llm_pb2_grpc.add_LLMServicer_to_server(server_lib.LLMServicer(), server)

    port = os.environ.get('TEXT_SERVER_PORT', "50051")
    server.add_insecure_port(f'[::]:{port}')
    print(f"Server starting on port {port}...")
    server.start()
    server.wait_for_termination()

def main():
    print("Good Morning!")
    serve()

if __name__ == "__main__":
    main()