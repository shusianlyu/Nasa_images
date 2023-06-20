import streamlit as st
import requests

# Prepare the API key and API url
api_key = "AyBLBPhYlYE2Qba8KySgBRPzPm4MZtcnmDeD4Ez6"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get the response data as a dictionary
response = requests.get(url)
data = response.json()

# Get the title, url, and explanation of the image
image_title = data["title"]
image_url = data["url"]
image_explanation = data["explanation"]

# Get the binary data of the image and download the image
output_filepath = "img.png"
image_content = requests.get(image_url).content
with open(output_filepath, "wb") as file:
    file.write(image_content)

st.set_page_config(layout="wide")
st.title(image_title)
st.image(output_filepath)
st.write(image_explanation)
