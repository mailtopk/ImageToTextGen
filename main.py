import os
import io
import streamlit as st
from dotenv import load_dotenv
from imagetotext import image_to_text
from PIL import Image

load_dotenv()
app_title = os.environ.get('APP_TITLE')

# Set title
st.markdown(f"<h1 style='text-align:center;'>{app_title}</h1>", unsafe_allow_html=True)

image_file = st.file_uploader('Upload image...', type=['jpg', 'png'] )
if image_file is not None:    
    with st.spinner('Please wait..'):
        #get image bytes        
        image_memoryview = memoryview(image_file.getbuffer())
        image_bytes = bytes(image_memoryview)
        image_io_bytes = io.BytesIO(image_bytes)
        
        ## Get image description
        text_description = image_to_text(image_io_bytes)
        
        st.write(f"<h3 style='text-align:center;'>{text_description}</h3>", unsafe_allow_html=True)
        st.image(image_io_bytes, caption="image to text", use_column_width="auto")
        image_io_bytes.close()


