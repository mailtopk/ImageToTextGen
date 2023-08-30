import os
import streamlit as st
from dotenv import load_dotenv
from imagetotext import image_to_text
from PIL import Image
from tempfile import NamedTemporaryFile

load_dotenv()

app_title = os.environ.get('APP_TITLE')

st.title(app_title)

image_file = st.file_uploader('Upload image...', type=['jpg', 'png'] )
if image_file is not None:
    image = Image.open(image_file.name)
    
    with st.spinner('Please wait..'):
        text_description = image_to_text('sample1.png')
        st.write(text_description)
        st.image(image=image, caption="image to text")
    
