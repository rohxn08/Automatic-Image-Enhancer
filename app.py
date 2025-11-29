import streamlit as st
import cv2
import numpy as np
from main1 import enhance_image
from PIL import Image
import io

st.set_page_config(page_title="Automatic Image Enhancer", layout="wide")

# Center the title using Markdown/HTML, but keep default font/colors
st.markdown("<h1 style='text-align: center;'>Automatic Image Enhancer</h1>", unsafe_allow_html=True)

# Custom CSS to ensure equal height cards
st.markdown("""
<style>
    /* Make the columns equal height */
    [data-testid="stHorizontalBlock"] {
        align-items: stretch;
    }
    
    [data-testid="stColumn"] {
        display: flex;
        flex-direction: column;
    }
    
    /* This is the internal wrapper for the column content */
    [data-testid="stVerticalBlock"] {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }
    
    /* This is the border container */
    [data-testid="stVerticalBlockBorderWrapper"] {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        /* Ensure it takes up the full height available from the flex stretch */
        height: 100%; 
        min-height: 600px;
    }
    
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        width: 100%;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

# Add some vertical spacing
st.write("")
st.write("")

# Create two columns for the card layout
col1, col2 = st.columns(2)

with col1:
    # Use a container with a border to create the "Card" look
    with st.container(border=True):
        st.markdown("<h3 style='text-align: center;'>Upload Image</h3>", unsafe_allow_html=True)
        
        # File uploader
        uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'], label_visibility="collapsed")
        
        if uploaded_file is not None:
            # Convert the file to an opencv image.
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, 1)
            
            # Display uploaded image
            st.image(opencv_image, channels="BGR", use_container_width=True)
        else:
            # Placeholder content if no image is uploaded
            st.markdown(
                """
                <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; height: 300px; color: gray;'>
                    <p>Select an image to enhance</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            opencv_image = None

with col2:
    with st.container(border=True):
        st.markdown("<h3 style='text-align: center;'>Enhanced Image</h3>", unsafe_allow_html=True)
        
        if opencv_image is not None:
            # Enhance image
            enhanced_image = enhance_image(opencv_image)
            
            # Display enhanced image
            st.image(enhanced_image, channels="BGR", use_container_width=True)
            
            # Prepare download
            enhanced_rgb = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(enhanced_rgb)
            buf = io.BytesIO()
            im_pil.save(buf, format="JPEG")
            byte_im = buf.getvalue()
            
            # Center the download button
            st.markdown("<div style='text-align: center; margin-top: 20px;'>", unsafe_allow_html=True)
            st.download_button(
                label="Download Enhanced Image",
                data=byte_im,
                file_name="enhanced_image.jpg",
                mime="image/jpeg"
            )
            st.markdown("</div>", unsafe_allow_html=True)
            
        else:
            # Placeholder content
            st.markdown(
                """
                <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; height: 300px; color: gray;'>
                    <p>Enhanced image will appear here</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
