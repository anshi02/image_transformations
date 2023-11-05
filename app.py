import streamlit as st
import cv2
import numpy as np
# from matplotlib import pyplot as plt

# Function to display images using Streamlit
def st_display_image(image, caption=''):
    st.image(image, caption=caption, use_column_width=True)

# Function to read an image from the uploaded file
def read_uploaded_image(uploaded_image):
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
    return image

# Main Streamlit app
def main():
  st.title("AFFINE-IMAGE TRANSFORMATION ")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(image, caption="Original Image", use_column_width=True)

    transformation_type = st.selectbox("Select Transformation", ["Translation", "Rotation", "Scaling", "Shearing"])

    if transformation_type == "Translation":
        x_translation = st.slider("X-Translation", -50, 50, 0)
        y_translation = st.slider("Y-Translation", -50, 50, 0)
        M = np.float32([[1, 0, x_translation], [0, 1, y_translation]])
        transformed_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    
    elif transformation_type == "Rotation":
        angle = st.slider("Rotation Angle", -180, 180, 0)
        M = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)
        transformed_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    elif transformation_type == "Scaling":
        scale_factor = st.slider("Scaling Factor", 0.1, 2.0, 1.0)
        M = np.float32([[scale_factor, 0, 0], [0, scale_factor, 0]])
        transformed_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    elif transformation_type == "Shearing":
        shear_factor_x = st.slider("Shear Factor X", -1.0, 1.0, 0.0)
        shear_factor_y = st.slider("Shear Factor Y", -1.0, 1.0, 0.0)
        M = np.float32([[1, shear_factor_x, 0], [shear_factor_y, 1, 0]])
        transformed_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    st.image(transformed_image, caption="Transformed Image", use_column_width=True)
if __name__ == '__main__':
    main()