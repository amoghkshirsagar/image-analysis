import ollama
import json
import base64

import base64

# Function to convert an image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def promptHandle(prompt, model, image):
    if image:
        image_path = image
        base64_string = image_to_base64(image_path)
    print(prompt)
    print(model)
    response = ollama.generate(
        model=model,
        prompt=prompt,
        images=[base64_string]
    )
    print(response.response)
    return response.response