import sys
import grpc
from concurrent import futures

from backend.text import server_lib
from shared.proto.services.llm import llm_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))

    # Register the imported class
    llm_pb2_grpc.add_LLMServicer_to_server(CalculatorServicer(), server)

    port = os.environ['SERVER_PORT']
    server.add_insecure_port(f'[::]:{port}')
    print(f"Audio Server starting on port {port}...")
    server.start()
    server.wait_for_termination()

def main():
    print("Good Morning!")
    serve()

if __name__ == "__main__":
    main()