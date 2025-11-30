load("@rules_proto//proto:defs.bzl", "proto_library")

proto_library(
    name = "control",
    srcs = ["control.proto"],
)

proto_library(
    name = "status",
    srcs = ["status.proto"],
)

py_proto_library(
    name = "control_py_proto",
    deps = [":control"],
)

py_proto_library(
    name = "status_py_proto",
    deps = [":status"],
)