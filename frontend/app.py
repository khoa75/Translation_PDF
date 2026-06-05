import streamlit as st
import requests
import os
from PIL import Image
import io

# Backend API URL - in a real deployment, this would point to the actual backend
BACKEND_URL = "http://localhost:8000"

def main():
    st.title("Document Translation Benchmark Platform")
    st.write("Upload a PDF document to translate it from English to Vietnamese using either LSTM or Transformer models.")
    
    # Model selection
    model_type = st.selectbox("Select Model", ["lstm", "transformer"])
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Display uploaded file info
        st.write(f"Uploaded file: {uploaded_file.name}")
        
        # Create columns for side-by-side display
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original PDF")
            st.write("Preview of original document")
            # Display first page of original PDF
            # (This would require actual PDF rendering which is not implemented here)
            
        with col2:
            st.subheader("Translation Options")
            # For now, we'll just show a placeholder
            st.write("Translated PDF will appear here")
            
        # When the user clicks on "Translate" button
        if st.button("Translate"):
            if uploaded_file is not None:
                # Save uploaded file temporarily
                with open(f"/tmp/{uploaded_file.name}", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Call backend API to translate
                files = {"pdf_file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                data = {"model_type": model_type}
                
                try:
                    response = requests.post(f"{BACKEND_URL}/translate-pdf", files=files, data=data)
                    if response.status_code == 200:
                        st.success("Document translated successfully!")
                        # In a real implementation, we would display the translated PDF here
                        st.write("Translation completed! The translated PDF will be available for download.")
                    else:
                        st.error("Translation failed. Please try again.")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.error("Please upload a PDF file first.")

if __name__ == "__main__":
    main()