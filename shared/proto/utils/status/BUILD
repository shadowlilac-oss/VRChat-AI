load("@rules_proto//proto:defs.bzl", "proto_library")
load("@protobuf//bazel:py_proto_library.bzl", "py_proto_library")

proto_library(
    name = "control",
    srcs = ["control.proto"],
    visibility = ["//visibility:public"],
)

proto_library(
    name = "status",
    srcs = ["status.proto"],
    visibility = ["//visibility:public"],
)

py_proto_library(
    name = "control_py_proto",
    deps = [":control"],
    visibility = ["//visibility:public"],
)

py_proto_library(
    name = "status_py_proto",
    deps = [":status"],
    visibility = ["//visibility:public"],
)