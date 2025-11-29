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
    /* Force both cards to be exactly the same height */
    [data-testid="stVerticalBlockBorderWrapper"] {
        height: 950px; /* Large fixed height to fit image + button */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        overflow-y: auto; /* Allow scrolling inside the card if content is too big */
    }
    
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        width: 100%;
        align-items: center;
    }

    /* Custom styling for the download button to match file uploader */
    .stDownloadButton button {
        background-color: transparent;
        color: inherit;
        border: 1px solid rgba(250, 250, 250, 0.2);
        border-radius: 0.5rem;
        padding: 1rem;
        text-align: left;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        width: 100%;
    }
    
    .stDownloadButton button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
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
            
            # Prepare download
            enhanced_rgb = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(enhanced_rgb)
            buf = io.BytesIO()
            im_pil.save(buf, format="JPEG")
            byte_im = buf.getvalue()
            
            # Download button at the top
            st.download_button(
                label="Download Enhanced Image",
                data=byte_im,
                file_name="enhanced_image.jpg",
                mime="image/jpeg",
                icon=":material/download:",
                use_container_width=True
            )
            
            # Display enhanced image
            st.image(enhanced_image, channels="BGR", use_container_width=True)
            
        else:
            # Disabled/Dummy download button at the top
            if st.button("Download Enhanced Image", disabled=False, icon=":material/download:", use_container_width=True):
                st.warning("Please upload an image first!")
                
            # Placeholder content
            st.markdown(
                """
                <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; height: 300px; color: gray;'>
                    <p>Enhanced image will appear here</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
