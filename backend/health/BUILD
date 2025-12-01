load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_image_layer")

py_binary(
    name = "client",
    srcs = ["health_client.py"],
    main = "health_client.py",
    deps = [
        "@pypi_health//grpcio_health_checking",
        "@pypi_health//protobuf",
        "@pypi_health//grpcio",
    ],
)