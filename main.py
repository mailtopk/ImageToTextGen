import os
import streamlit as st
from dotenv import load_dotenv
from imagetotext import image_to_text
from tempfile import NamedTemporaryFile
from PIL import Image
load_dotenv()

app_title = os.environ.get('APP_TITLE')

st.title(app_title)

image_file = st.file_uploader('Upload image...', type=['jpg', 'png'] )
if image_file is not None:    
    with st.spinner('Please wait..'):
        image_memoryview = memoryview(image_file.getbuffer())
        text_description = image_to_text(image_memoryview)
        st.write(text_description)
        st.image(image=image_file, caption="image to text")
        

