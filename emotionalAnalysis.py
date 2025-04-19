import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.8,
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["Age", "Gender", "Emotions", "Emotional Analysis"],
                        properties = {
                            "Age": genai.types.Schema(
                                type = genai.types.Type.NUMBER,
                            ),
                            "Gender": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "Emotions": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                items = genai.types.Schema(
                                    type = genai.types.Type.STRING,
                                ),
                            ),
                            "Emotional Analysis": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        },
                    ),
        system_instruction=[
            types.Part.from_text(text="""You are a children emotional analysis expert. You will receive the details about the child like Age, Gender and the message from the child. you are going to communicate with another AI agent. So you should carefully analyse the message and provide the emotional analysis without losing the context and provide to the another agent via output. the output should be relevant and empathetic. You are a empathatic person. you will respond to children politely and empathatic by understanding the needs and guide in a good way."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
