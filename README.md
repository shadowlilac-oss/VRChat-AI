To generate the requirements.txt:

```bash
bazel run //:update_audio_tts.update
bazel run //:update_audio_stt.update
bazel run //:update_text.update
bazel run //:update_jupyter.update
```

To launch jupyter
```bash
bazel run --spawn_strategy=local //jupyter:jupyter
```