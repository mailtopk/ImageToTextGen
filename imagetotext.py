import os
from PIL import Image
from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
from dotenv import load_dotenv


load_dotenv()
model_dir = os.environ.get('MODEL_DIR')
model_name = os.environ.get("MODEL_NAME")
print(model_dir)
print(model_name)

def load_model():
    # Load model directly, firs time this may few min to download the model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", cache_dir=model_dir)
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model


def image_to_text(image_path):
    processor, model = load_model()
    raw_image = Image.open(image_path).convert('RGB')
    inputs = processor(raw_image, return_tensors='pt')
    output = model.generate(**inputs, max_new_tokens=15000)
    image_text = processor.decode(output[0], skip_special_tokens=True)
    print(image_text)
    
    return image_text

if __name__ == "__main__":
    image_to_text('sample1.png')