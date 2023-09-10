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
    # Bootstrapping Language-Image Pre-training
    processor = BlipProcessor.from_pretrained(model_name, cache_dir=model_dir)
    model = BlipForConditionalGeneration.from_pretrained(model_name)
    return processor, model


def image_to_text(image_io_bytes):    
    raw_image =  Image.open(image_io_bytes).convert('RGB')    
    processor, model = load_processor_model()    
    inputs = processor(raw_image, return_tensors='pt')
    output = model.generate(**inputs, max_new_tokens=15000)
    return processor.decode(output[0], skip_special_tokens=True)