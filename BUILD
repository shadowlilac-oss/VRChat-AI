load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_uv//uv:pip.bzl", "pip_compile")

pip_compile(
    name = "update_audio_tts",
    requirements_in = "requirements/requirements_audio_tts.in",        # The file you edit
    requirements_txt = "requirements/requirements_audio_tts.txt", # The file Bazel reads
)

pip_compile(
    name = "update_audio_stt",
    requirements_in = "requirements/requirements_audio_stt.in",
    requirements_txt = "requirements/requirements_audio_stt.txt",
)

pip_compile(
    name = "update_jupyter",
    requirements_in = "requirements/requirements_jupyter.in",
    requirements_txt = "requirements/requirements_jupyter.txt",
)

pip_compile(
    name = "update_text",
    requirements_in = "requirements/requirements_text.in",
    requirements_txt = "requirements/requirements_text.txt",
)