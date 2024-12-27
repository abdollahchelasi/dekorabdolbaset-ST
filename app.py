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
    
    # تگ عنوان
    title_tag = soup.find('title')
    if title_tag:
        title_tag.string = seo_tags['title']
    else:
        new_title_tag = soup.new_tag('title')
        new_title_tag.string = seo_tags['title']
        if soup.head:
            soup.head.append(new_title_tag)

    # تگ متا برای توضیحات
    meta_description = soup.new_tag('meta')
    meta_description.attrs['name'] = 'description'
    meta_description.attrs['content'] = seo_tags['meta_description']
    soup.head.append(meta_description)

    # تگ متا برای کلمات کلیدی
    meta_keywords = soup.new_tag('meta')
    meta_keywords.attrs['name'] = 'keywords'
    meta_keywords.attrs['content'] = seo_tags['meta_keywords']
    soup.head.append(meta_keywords)

    # تگ‌های اوپن گراف
    og_tags = [
        ('og:title', seo_tags['og_title']),
        ('og:description', seo_tags['og_description']),
        ('og:image', seo_tags['og_image']),
        ('og:url', seo_tags['og_url']),
    ]
    
    for property_name, content in og_tags:
        og_meta = soup.new_tag('meta')
        og_meta.attrs['property'] = property_name
        og_meta.attrs['content'] = content
        soup.head.append(og_meta)

    return str(soup)

def modify_seo_tags():
    html_content = load_index_file()
    updated_content = inject_seo_tags(html_content)
    save_index_file(updated_content)
    st.success("SEO tags updated successfully.")

# اپلیکیشن Streamlit
st.title("SEO Tag Modifier")

if st.button("Update SEO Tags"):
    modify_seo_tags()

st.write("Current SEO tags will be added to the index.html file.")
    
