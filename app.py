import streamlit as st
from datetime import datetime
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="مسابقة توقعات كأس العالم 2026", page_icon="🏆", layout="centered")

# 2. عرض الصورة
if os.path.exists("IMG_4017.jpeg"):
    st.image("IMG_4017.jpeg", use_container_width=True)

# 3. لوحة الإدارة
with st.sidebar:
    st.header("⚙️ لوحة الإدارة")
    admin_pass = st.text_input("كلمة سر المدير:", type="password")
    if admin_pass == "1234":
        st.success("أهلاً بك يا أبو أحمد")
        match_name = st.text_input("اسم المباراة:")
        result = st.text_input("النتيجة (مثل: 1-0):")
        if st.button("💾 حفظ"):
            # هنا سنحفظ النتيجة في ملف بسيط
            with open("results.txt", "a") as f:
                f.write(f"{match_name}: {result}\n")
            st.success("تم الحفظ!")
    else:
        st.info("القسم مخصص للإدارة فقط")

# 4. الواجهة الرئيسية
st.title("🏆 مسابقة توقعات كأس العالم 2026")

# عرض النتائج من الملف
st.subheader("📊 جدول النتائج الرسمية")
if os.path.exists("results.txt"):
    with open("results.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            st.write(f"✅ {line}")
else:
    st.write("لم يتم تسجيل نتائج بعد.")

# المباريات
st.markdown("---")
st.subheader("⚽ المباريات")
st.write("المكسيك ضد جنوب أفريقيا | كوريا ضد الأردن")
st.radio("توقعك للمباراة الأولى:", ["فوز المكسيك", "تعادل", "فوز جنوب أفريقيا"], key="match1")

if st.button("💾 حفظ توقعي"):
    st.success("تم حفظ توقعك!")
