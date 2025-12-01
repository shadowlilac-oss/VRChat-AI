load("@rules_proto//proto:defs.bzl", "proto_library")
load("@protobuf//bazel:py_proto_library.bzl", "py_proto_library")

proto_library(
    name = "text",
    srcs = ["text.proto"],
    visibility = ["//visibility:public"],
)

py_proto_library(
    name = "text_py_proto",
    deps = [
        ":text",
    ],
    visibility = ["//visibility:public"],
)
