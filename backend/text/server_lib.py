from shared.proto.services.llm import llm_pb2
from shared.proto.services.llm import llm_pb2_grpc
from shared.proto.utils.text import text_pb2
from openai import OpenAI
import os

class LLMServicer(llm_pb2_grpc.LLMServicer):
    def __init__(self):
        print("LLM Server launched successfully!")
        self.__client = OpenAI(
            base_url=os.environ.get('OPENAI_LLM_ADDRESS', ""),
            api_key=os.environ.get('OPENAI_LLM_API_KEY', ""),
        )

    def Generate(self, request, context):

        prompt: str = request.text
        conversation_id: str = request.id

        # Get data from query


        completion = client.chat.completions.create(
            model=os.environ.get('OPENAI_LLM_NAME', ""),
            messages=[
                {"role": "user", "content": "Hello!"},
            ], stream=True
        )

        for t in completion:
            token: str = t.choices[0].delta.content
            if not context.is_active():
                print("Client disconnected, stopping generation.")
                break
            response = llm_pb2.GenerationResponse(
                text=text_pb2.TextChunk(text_chunk=token)
            )
            yield response