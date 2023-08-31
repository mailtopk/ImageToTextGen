import os
import io
from PIL import Image
from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
from dotenv import load_dotenv



load_dotenv()
model_dir = os.environ.get('MODEL_DIR')
model_name = os.environ.get("MODEL_NAME")

def load_processor_model():
    # Load model directly, first time this may few min to download the model
    processor = BlipProcessor.from_pretrained(model_name, cache_dir=model_dir)
    model = BlipForConditionalGeneration.from_pretrained(model_name)
    return processor, model


def image_to_text(image):
    image_bytes = bytes(image)
    raw_image =  Image.open(io.BytesIO(image_bytes)).convert('RGB')
    processor, model = load_processor_model()
    inputs = processor(raw_image, return_tensors='pt')
    output = model.generate(**inputs, max_new_tokens=15000)
    image_text = processor.decode(output[0], skip_special_tokens=True)
    io.BytesIO(image_bytes).close()

    return image_text