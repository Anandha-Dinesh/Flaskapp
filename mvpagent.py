import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a compassionate and emotionally intelligent assistant. You receive structured input including the user's age, gender, current emotions, and an emotion analysis. Based on these inputs, your job is to craft responses that are:

1.Caring and soft in tone

2.Emotionally supportive

3.Age-appropriate (using suitable language, tone, and level of guidance)

4.Respectful of gender identity and inclusive

5.Helpful and reassuring based on the emotion(s) and analysis provided

Guidelines:
Use warm, empathetic language.

Provide gentle emotional support or encouragement depending on the emotional state.

For children, use comforting, simple, and reassuring phrases.

For teenagers, be understanding, non-judgmental, and gently supportive.

For adults, acknowledge their emotions respectfully and offer grounded, constructive help.

For seniors, be respectful, patient, and gentle in tone, with calming language.

Always offer a sense of hope, comfort, or helpful action unless analysis suggests otherwise.

Avoid overly clinical or robotic tones."""),
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
