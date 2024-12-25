import pathlib
from bs4 import BeautifulSoup
import streamlit as st

def add_meta_tags():
    # مسیر فایل index.html در محیط ابر (Hugging Face) و همچنین بررسی در Liara
    try:
        # در Hugging Face
        index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
        index_path = index_path.resolve()  # تبدیل به مسیر مطلق
        # اگر فایل وجود ندارد، آن را ایجاد کنید
        if not index_path.exists():
            html_content = "<html><head></head><body><h1>خوش آمدید!</h1></body></html>"
            index_path.write_text(html_content, encoding='utf-8')

    except Exception as e:
        # در صورت بروز خطا، ممکن است در Liara یا تغییر مسیر در Hugging Face باشد
        index_path = pathlib.Path("index.html")  # مسیر پیش‌فرض برای Liara
        if not index_path.exists():
            html_content = "<html><head></head><body><h1>خوش آمدید!</h1></body></html>"
            index_path.write_text(html_content, encoding='utf-8')

    # خواندن محتوای HTML
    soup = BeautifulSoup(index_path.read_text(encoding='utf-8'), features="html.parser")

    # تغییر عنوان
    if soup.find('title'):
        soup.title.string = 'دکوراسیون عبدالباسط - بهترین خدمات دکوراسیون در قشم'
    else:
        title_tag = soup.new_tag('title')
        title_tag.string = 'دکوراسیون عبدالباسط - بهترین خدمات دکوراسیون در قشم'
        soup.head.append(title_tag)
    
    # افزودن متا تگ‌های Open Graph
    og_tags = [
        ('og:title', 'دکوراسیون عبدالباسط - بهترین خدمات دکوراسیون در قشم'),
        ('og:description', 'دکوراسیون عبدالباسط با نصب PVC، کناف و قرنیز در جزیره قشم.'),
        ('og:image', 'https://abdollah-dekor.hf.space/media/05d5f29d85b54442b746b17d95730097fd403c7b864b458922ef34ca.png'),
        ('og:url', 'https://abdollah-dekor.hf.space'),
        ('og:type', 'website')
    ]

    for name, content in og_tags:
        meta_tag = soup.new_tag('meta')
        meta_tag.attrs['property'] = name
        meta_tag.attrs['content'] = content
        soup.head.append(meta_tag)

    # افزودن متا تگ‌های سئو
    seo_tags = [
        ('description', 'دکوراسیون عبدالباسط با نصب PVC، کناف و قرنیز در جزیره قشم.'),
        ('keywords', 'دکوراسیون, عبدالباسط, قشم, PVC, کناف, قرنیز'),
        ('author', 'عبدالله چلاسی')
    ]

    for name, content in seo_tags:
        meta_tag = soup.new_tag('meta')
        meta_tag.attrs['name'] = name
        meta_tag.attrs['content'] = content
        soup.head.append(meta_tag)

    # اضافه کردن favicon
    favicon_tag = soup.new_tag('link')
    favicon_tag.attrs['rel'] = 'icon'
    favicon_tag.attrs['href'] = 'https://abdollah-dekor.hf.space/media/05d5f29d85b54442b746b17d95730097fd403c7b864b458922ef34ca.png'
    favicon_tag.attrs['type'] = 'image/png'
    soup.head.append(favicon_tag)

    # ذخیره تغییرات در فایل
    index_path.write_text(str(soup), encoding='utf-8')
    
# فراخوانی تابع
add_meta_tags()

st.text("hi")
