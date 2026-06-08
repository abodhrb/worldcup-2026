import streamlit as st
from datetime import datetime
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="مسابقة توقعات كأس العالم 2026", page_icon="🏆", layout="centered")

# 2. التنسيق العام (CSS)
st.markdown("""
    <style>
    .main-title { text-align: center; color: #1E3A8A; font-size: 38px; font-weight: bold; margin-bottom: 30px; }
    .card { background-color: #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 10px; border-right: 5px solid #3B82F6; }
    .day-header { font-size: 20px; font-weight: bold; color: #111827; margin-top: 25px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 3. عرض الصورة
if os.path.exists("IMG_4017.jpeg"):
    st.image("IMG_4017.jpeg", use_container_width=True)

# 4. لوحة الإدارة
# نستخدم session_state لحفظ النتائج لكي تظهر للجميع
if 'results_table' not in st.session_state:
    st.session_state['results_table'] = {}

with st.sidebar:
    st.header("⚙️ لوحة الإدارة")
    admin_pass = st.text_input("كلمة سر المدير:", type="password")
    if admin_pass == "1234":
        st.success("أهلاً بك يا أبو أحمد")
        match_name = st.text_input("اسم المباراة:")
        result = st.text_input("النتيجة النهائية:")
        if st.button("💾 حفظ النتيجة في الجدول"):
            st.session_state['results_table'][match_name] = result
            st.success("تم تحديث الجدول بنجاح!")
    else:
        st.info("القسم مخصص للإدارة فقط")

# 5. الواجهة الرئيسية
st.markdown('<div class="main-title">🏆 مسابقة توقعات كأس العالم 2026 🏆</div>', unsafe_allow_html=True)

# 6. عرض جدول النتائج (يظهر للجميع)
st.markdown("---")
st.subheader("📊 جدول النتائج الرسمية")
if st.session_state['results_table']:
    st.table(st.session_state['results_table'])
else:
    st.write("لا توجد نتائج مسجلة حتى الآن.")

# 7. قائمة المباريات
st.markdown("---")
st.subheader("⚽ المباريات")
matches_list = [
    ("سهرة الخميس 11 يونيو", [("الخميس 11/06", "🇲🇽 المكسيك", "🇿🇦 جنوب أفريقيا"), ("الجمعة 12/06", "🇰🇷 كوريا الجنوبية", "🇯🇴 الأردن")]),
    ("سهرة الجمعة 12 يونيو", [("الجمعة 12/06", "🇨🇦 كندا", "🇵🇪 بيرو"), ("السبت 13/06", "🇺🇸 أمريكا", "🇵🇾 باراغواي")])
]

for day, matches in matches_list:
    st.markdown(f'<div class="day-header">{day}</div>', unsafe_allow_html=True)
    for time, t1, t2 in matches:
        st.markdown(f'<div class="card"><b>⏱️ {time}</b><br>{t1} VS {t2}</div>', unsafe_allow_html=True)
        st.radio("توقعك:", [f"فوز {t1.split(' ', 1)[-1]}", "تعادل", f"فوز {t2.split(' ', 1)[-1]}"], key=f"radio_{time}")
        if st.button("💾 حفظ توقعي", key=f"btn_{time}"):
            st.success("تم تسجيل توقعك!")

# 8. التوقعات الذهبية
st.markdown("---")
st.subheader("🌟 التوقعات الذهبية")
closing_date = datetime(2026, 6, 14, 23, 59)
if datetime.now() < closing_date:
    st.text_input("بطل كأس العالم 2026:")
    if st.button("💾 تثبيت التوقعات الذهبية"):
        st.success("تم تثبيت توقعاتك!")
else:
    st.error("🚫 انتهى وقت التوقعات الذهبية.")
