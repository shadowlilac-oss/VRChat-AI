load("@rules_python//python:pip.bzl", "compile_pip_requirements")

compile_pip_requirements(
    name = "update_audio_tts",
    src = "requirements/requirements_audio_tts.in",        # The file you edit
    requirements_txt = "requirements/requirements_audio_tts.txt", # The file Bazel reads
)

compile_pip_requirements(
    name = "update_audio_stt",
    src = "requirements/requirements_audio_stt.in",
    requirements_txt = "requirements/requirements_audio_stt.txt",
)

compile_pip_requirements(
    name = "update_jupyter",
    src = "requirements/requirements_jupyter.in",
    requirements_txt = "requirements/requirements_jupyter.txt",
)

compile_pip_requirements(
    name = "update_text",
    src = "requirements/requirements_text.in",
    requirements_txt = "requirements/requirements_text.txt",
)