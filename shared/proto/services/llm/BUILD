load("@rules_proto_grpc_python//:defs.bzl", "python_grpc_library")
load("@rules_proto//proto:defs.bzl", "proto_library")

proto_library(
    name = "llm",
    srcs = ["llm.proto"],
    deps = [
        "//shared/proto/utils/text:text",
        "//shared/proto/utils/status:control",
        "//shared/proto/utils/status:status",
    ],
    visibility = ["//visibility:public"],
)

python_grpc_library(
    name = "llm_python_lib_server",
    protos = [":llm"],
    deps = [
        "@pypi_text//protobuf",
        "@pypi_text//grpcio",
        "//shared/proto/utils/text:text_py_proto",
        "//shared/proto/utils/status:control_py_proto",
        "//shared/proto/utils/status:status_py_proto",

    ],
    visibility = ["//visibility:public"],
)