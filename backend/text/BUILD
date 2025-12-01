load("@aspect_bazel_lib//lib:transitions.bzl", "platform_transition_filegroup")
load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_image_layer")
load("@rules_oci//oci:defs.bzl", "oci_image", "oci_load")


py_library(
    name = "server_lib",
    srcs = ["server_lib.py"],
    deps = [
        "@pypi_text//openai",
        "//shared/proto/services/llm:llm_python_lib_server"
    ],
)

py_binary(
    name = "server",
    srcs = ["main.py"],
    main = "main.py",
    deps = [
        ":server_lib",
        "//shared/proto/services/llm:llm_python_lib_server"
    ],
)

py_image_layer(
    name = "main_layer",
    binary = ":server",
    root = "/",
)

oci_image(
    name = "image",
    base = "@ubuntu",
    tars = [":main_layer"],
    entrypoint = ["/backend/text/server"],
)

platform(
    name = "x86_64_linux",
    constraint_values = [
        "@platforms//os:linux",
        "@platforms//cpu:x86_64",
    ],
)

platform_transition_filegroup(
    name = "platform_image",
    srcs = [":image"],
    target_platform = ":x86_64_linux",
)

oci_load(
    name = "image_load",
    image = ":platform_image",
    repo_tags = ["vrcai_text_backend:latest"],
)