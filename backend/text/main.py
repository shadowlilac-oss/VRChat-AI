import sys
import grpc
import os
import time
from concurrent import futures

from backend.text import server_lib
from shared.proto.services.llm import llm_pb2_grpc
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    llm_pb2_grpc.add_LLMServicer_to_server(server_lib.LLMServicer(), server)

    health_servicer = health.HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    port = os.environ.get('TEXT_SERVER_PORT', "50051")
    server.add_insecure_port(f'[::]:{port}')
    print(f"Server starting on port {port}...")
    server.start()
    server.wait_for_termination()

def main():
    serve()

if __name__ == "__main__":
    main()