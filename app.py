import streamlit as st
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="مسابقة توقعات كأس العالم 2026", page_icon="🏆", layout="centered")

# التنسيق العام
st.markdown("""
    <style>
    .main-title { text-align: center; color: #1E3A8A; font-size: 38px; font-weight: bold; margin-bottom: 10px; }
    .card { background-color: #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 10px; border-right: 5px solid #3B82F6; }
    .day-header { font-size: 20px; font-weight: bold; color: #111827; margin-top: 25px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 1. لوحة تحكم المدير (القائمة الجانبية) ---
with st.sidebar:
    st.header("⚙️ لوحة الإدارة")
    admin_pass = st.text_input("كلمة سر المدير:", type="password")
    if admin_pass == "1234": # يمكنك تغيير الرقم
        st.success("أهلاً بك يا أبو أحمد")
        st.subheader("إضافة/تعديل نتائج")
        match_name = st.text_input("اسم المباراة (مثل: المكسيك ضد جنوب أفريقيا):")
        result = st.text_input("النتيجة (مثل: 2-1):")
        if st.button("💾 حفظ النتيجة"):
            st.write(f"تم حفظ نتيجة {match_name} بـ {result}")
    else:
        st.info("القسم مخصص للإدارة فقط")

# --- 2. الواجهة الرئيسية (للمشاركين) ---
st.markdown('<div class="main-title">🏆 مسابقة توقعات كأس العالم 2026 🏆</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("👤 اسمك:")
with col2:
    user_code = st.text_input("🔑 رمز سري (آخر 4 أرقام):", type="password")

# المباريات
matches_list = [
    ("سهرة الخميس 11 يونيو", [("الخميس 11/06 - 10:00 م", "🇲🇽 المكسيك", "🇿🇦 جنوب أفريقيا"), ("الجمعة 12/06 - 05:00 ص", "🇰🇷 كوريا الجنوبية", "🇯🇴 الأردن")]),
    ("سهرة الجمعة 12 يونيو", [("الجمعة 12/06 - 10:00 م", "🇨🇦 كندا", "🇵🇪 بيرو"), ("السبت 13/06 - 04:00 ص", "🇺🇸 أمريكا", "🇵🇾 باراغواي")]),
    ("سهرة السبت 13 يونيو", [("السبت 13/06 - 10:00 م", "🇨🇭 سويسرا", "🇶🇦 قطر"), ("الأحد 14/06 - 01:00 ص", "🇧🇷 البرازيل", "🇲🇦 المغرب"), ("الأحد 14/06 - 04:00 ص", "🇭🇹 هايتي", "🏴󠁧󠁢󠁳󠁣󠁴󠁿 اسكتلندا"), ("الأحد 14/06 - 07:00 ص", "🇦🇺 أستراليا", "🏴󠁧󠁢󠁷󠁬󠁳󠁿 ويلز")]),
    ("سهرة الأحد 14 يونيو", [("الأحد 14/06 - 08:00 م", "🇩🇪 ألمانيا", "🇨🇼 كوراساو"), ("الأحد 14/06 - 11:00 م", "🇳🇱 هولندا", "🇯🇵 اليابان"), ("الاثنين 15/06 - 01:00 ص", "🇪🇸 إسبانيا", "🇨🇻 الرأس الأخضر"), ("الاثنين 15/06 - 02:00 ص", "🇨🇮 ساحل العاج", "🇪🇨 الإكوادور"), ("الاثنين 15/06 - 05:00 ص", "🇵🇱 بولندا", "🇹🇳 تونس")]),
    ("سهرة الاثنين 15 يونيو", [("الاثنين 15/06 - 10:00 م", "🇧🇪 بلجيكا", "🇪🇬 مصر"), ("الثلاثاء 16/06 - 01:00 ص", "🇸🇦 السعودية", "🇺🇾 أوروغواي"), ("الثلاثاء 16/06 - 04:00 ص", "🇮🇷 إيران", "🇳🇿 نيوزيلندا")]),
    ("سهرة الثلاثاء 16 يونيو", [("الثلاثاء 16/06 - 10:00 م", "🇫🇷 فرنسا", "🇸🇳 السنغال"), ("الأربعاء 17/06 - 01:00 ص", "🇨🇱 تشيلي", "🇳🇴 النرويج"), ("الأربعاء 17/06 - 04:00 ص", "🇦🇷 الأرجنتين", "🇩🇿 الجزائر"), ("الأربعاء 17/06 - 07:00 ص", "🇦🇹 النمسا", "🇺🇿 أوزبكستان"), ("الأربعاء 17/06 - 08:00 م", "🇵🇹 البرتغال", "🇬🇭 غانا"), ("الأربعاء 17/06 - 11:00 م", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 إنجلترا", "🇭🇷 كرواتيا"), ("الخميس 18/06 - 02:00 ص", "🇨🇲 الكاميرون", "🇵🇦 بنما"), ("الخميس 18/06 - 05:00 ص", "🇨🇴 كولومبيا", "🇩🇿 الجزائر")])
]

for day, matches in matches_list:
    st.markdown(f'<div class="day-header">{day}</div>', unsafe_allow_html=True)
    for time, t1, t2 in matches:
        st.markdown(f'<div class="card"><b>⏱️ {time}</b><br>{t1} VS {t2}</div>', unsafe_allow_html=True)
        st.radio("توقعك:", [f"فوز {t1.split(' ', 1)[1]}", "تعادل", f"فوز {t2.split(' ', 1)[1]}"], key=f"radio_{time}")
        if st.button("💾 حفظ توقعي", key=f"btn_{time}"):
            st.success("تم تسجيل توقعك!")

# --- 3. التوقع الذهبي (مع عداد زمني) ---
st.markdown("---")
st.subheader("🌟 التوقعات الذهبية")
closing_date = datetime(2026, 6, 14, 23, 59)
if datetime.now() < closing_date:
    st.text_input("طرف النهائي الأول:")
    st.text_input("طرف النهائي الثاني:")
    st.text_input("بطل كأس العالم 2026:")
    if st.button("💾 تثبيت التوقعات الذهبية"):
        st.success("تم تثبيت توقعاتك الذهبية بنجاح!")
else:
    st.error("🚫 عذراً، تم إغلاق باب التوقعات الذهبية.")
