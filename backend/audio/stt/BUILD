load("@aspect_bazel_lib//lib:transitions.bzl", "platform_transition_filegroup")
load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_image_layer")
load("@rules_oci//oci:defs.bzl", "oci_image", "oci_load")

py_binary(
    name = "server",
    srcs = ["main.py"],
    main = "main.py",
    deps = [
        "@pypi_audio_stt//transformers",
        "@pypi_audio_stt//flash_attn",
        "@pypi_audio_stt//torch",
    ],
)
