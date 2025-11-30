load("@rules_python//python:defs.bzl", "py_binary")
load("@aspect_bazel_lib//lib:transitions.bzl", "platform_transition_filegroup")
load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_image_layer")
load("@rules_oci//oci:defs.bzl", "oci_image", "oci_load")

py_binary(
    name = "tts_app",
    srcs = ["main.py"],
    main = "main.py",
    deps = [
        "@pypi_audio_tts//torch",
        "@pypi_audio_tts//numpy",
    ],
)

py_image_layer(
    name = "main_layer",
    binary = ":tts_app",
    root = "/app",
)

oci_image(
    name = "image",
    base = "@ubuntu",
    tars = [":main_layer"],
    # Formula: /app + /backend/audio/tts + /server
    entrypoint = ["/app/backend/audio/tts/server"],
)