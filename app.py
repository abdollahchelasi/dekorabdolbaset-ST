import streamlit as st
from bs4 import BeautifulSoup
import pathlib

# تنظیمات سئو و متا تگ‌های شبکه اجتماعی
seo_tags = {
    'title': 'World Marathons Planner',
    'meta_description': 'Best Marathon Planner! Browse through the event selection and discover your next Marathon challenge.',
    'meta_keywords': 'marathon, running, event, training',
    'og_title': 'World Marathons Planner',
    'og_description': 'Join us to find the best marathons and personalized training plans.',
    'og_image': 'https://example.com/image.jpg',
    'og_url': 'https://example.com'
}

def load_index_file():
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    with open(index_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_index_file(content):
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    with open(index_path, 'w', encoding='utf-8') as file:
        file.write(content)

def inject_seo_tags(html_content):
    soup = BeautifulSoup(html_content, features="html.parser")
    # ... (کد تگ‌های سئو همانند قبلی)
    return str(soup)

def modify_seo_tags():
    html_content = load_index_file()
    updated_content = inject_seo_tags(html_content)
    save_index_file(updated_content)
    st.success("SEO tags updated successfully.")
    st.write("Updated HTML content:")
    st.code(updated_content, language='html')

# اپلیکیشن Streamlit
st.title("SEO Tag Modifier")

if st.button("Update SEO Tags"):
    modify_seo_tags()

st.write("Current SEO tags will be added to the index.html file.")
