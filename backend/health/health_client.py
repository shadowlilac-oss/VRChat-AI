# client_check_arg.py
import grpc
import argparse
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc


def check_server_status(server_address):
    try:
        with grpc.insecure_channel(server_address) as channel:
            health_stub = health_pb2_grpc.HealthStub(channel)

            response = health_stub.Check(
                health_pb2.HealthCheckRequest(service='')  # Empty string checks the overall server status
            )

            if response.status == health_pb2.HealthCheckResponse.ServingStatus.SERVING:
                print(f"gRPC Server at {server_address} is running and serving.")
                return True
            else:
                print(f"gRPC Server at {server_address} is running, but reported status: {response.status}")
                return False

    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            print(f"gRPC Server at {server_address} is unavailable or down.")
        else:
            print(f"An RPC Error occurred: {e.details()}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Check the health of a gRPC server using the standard Health Check Protocol."
    )

    parser.add_argument(
        '--addr',
        type=str,
        default='localhost:50051',
        help='The gRPC server address and port (e.g., 192.168.1.1:50051). Defaults to localhost:50051.'
    )

    # 3. Parse the arguments
    args = parser.parse_args()

    # 4. Call the check function with the parsed address
    print(f"Attempting to check status of gRPC server at: {args.addr}")
    check_server_status(args.addr)


if __name__ == '__main__':
    main()