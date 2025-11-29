import streamlit as st
import cv2
import numpy as np
from main1 import enhance_image
from PIL import Image

st.set_page_config(page_title="Automatic Image Enhancer", layout="wide")

st.title("Automatic Image Enhancer")
st.write("Upload an image to automatically enhance its brightness and contrast.")

col1, col2 = st.columns(2)

with col1:
    st.header("Input Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    
    # Display original image
    with col1:
        st.image(opencv_image, channels="BGR", caption="Original Image", use_container_width=True)

    # Enhance image
    enhanced_image = enhance_image(opencv_image)

    # Display enhanced image
    with col2:
        st.header("Enhanced Output")
        st.image(enhanced_image, channels="BGR", caption="Enhanced Image", use_container_width=True)
        
        # Convert for download (BGR to RGB for PIL)
        enhanced_rgb = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(enhanced_rgb)
        
        # Save to buffer for download button
        import io
        buf = io.BytesIO()
        im_pil.save(buf, format="JPEG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="Download Enhanced Image",
            data=byte_im,
            file_name="enhanced_image.jpg",
            mime="image/jpeg"
        )
