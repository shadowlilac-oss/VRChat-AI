load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "tts_app",
    srcs = ["main.py"],
    main = "main.py",
    deps = [
        "@pypi_audio_tts//torch",
        "@pypi_audio_tts//numpy",
    ],
)