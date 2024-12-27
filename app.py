import streamlit as st
import streamlit.components.v1 as components

# عنوان اپلیکیشن
st.title("SEO Tags Example for Streamlit")

# نمایش تگ‌های متا در قسمت <head>
components.html("""
<head>
    <meta property="og:title" content="Your Streamlit Project Title">
    <meta property="og:description" content="Describe your Streamlit project here.">
    <meta property="og:image" content="URL to an image for social sharing">
    <meta property="og:url" content="https://yourcustomdomain.com">
    <meta name="twitter:card" content="summary_large_image">
</head>
""", height=0)

# محتوای اصلی اپلیکیشن
st.write("This is a simple Streamlit application to demonstrate how to set SEO tags for social sharing.")
