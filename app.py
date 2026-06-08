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
        result = st.text_input("النتيجة:")
        if st.button("💾 حفظ النتيجة"):
            with open("results.txt", "a", encoding="utf-8") as f:
                f.write(f"{match_name} | {result}\n")
            st.success("تم الحفظ في الجدول!")
    else:
        st.info("القسم مخصص للإدارة")

# 4. الواجهة الرئيسية
st.title("🏆 مسابقة توقعات كأس العالم 2026")

# جدول النتائج
st.subheader("📊 جدول النتائج الرسمية")
if os.path.exists("results.txt"):
    with open("results.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            st.write(f"📢 {line.strip()}")
else:
    st.write("بانتظار بدء المباريات...")

# قائمة المباريات
st.markdown("---")
st.subheader("⚽ المباريات")
matches = [
    ("المكسيك vs جنوب أفريقيا", "11/06"),
    ("كوريا الجنوبية vs الأردن", "12/06"),
    ("كندا vs بيرو", "12/06"),
    ("أمريكا vs باراغواي", "13/06")
]

for match, date in matches:
    st.write(f"**{match}** ({date})")
    st.radio("توقعك:", ["فوز الأول", "تعادل", "فوز الثاني"], key=match)

# التوقعات الذهبية
st.markdown("---")
st.subheader("🌟 التوقعات الذهبية")
if datetime.now() < datetime(2026, 6, 14, 23, 59):
    champion = st.text_input("بطل كأس العالم 2026:")
    if st.button("💾 تثبيت التوقعات الذهبية"):
        st.success("تم تثبيت التوقعات!")
else:
    st.error("🚫 انتهى وقت التوقعات الذهبية.")
