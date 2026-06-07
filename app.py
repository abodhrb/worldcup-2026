import streamlit as st

# 1. إعدادات الصفحة والتنسيق
st.set_page_config(page_title="مسابقة توقعات كأس العالم 2026", page_icon="🏆", layout="centered")

st.markdown("""
    <style>
    .main-title { text-align: center; color: #1E3A8A; font-size: 38px; font-weight: bold; margin-bottom: 10px; }
    .rules-box { background-color: #F8FAFC; padding: 25px; border-radius: 15px; border: 2px solid #E2E8F0; margin-top: 30px; }
    .gold-box-red { background-color: #FEF2F2; padding: 25px; border-radius: 15px; border: 2px solid #EF4444; margin-top: 30px; margin-bottom: 30px; }
    .red-text { color: #EF4444; font-weight: bold; }
    .day-header { font-size: 20px; font-weight: bold; color: #111827; margin-top: 25px; margin-bottom: 10px; border-bottom: 2px solid #E5E7EB; }
    .gold-reminder { color: #DC2626; font-weight: bold; font-size: 14px; margin-bottom: 20px; }
    .lock-alert { color: #4B5563; font-size: 12px; font-style: italic; margin-bottom: 10px; }
    .card { background-color: #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 10px; border-right: 5px solid #3B82F6; }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.image("IMG_4017.jpeg", use_container_width=True)
st.markdown('<div class="main-title">🏆 مسابقة توقعات كأس العالم 2026 🏆</div>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #4B5563;'>بتوقيت مكة المكرمة 🕋</h4>", unsafe_allow_html=True)

# التسجيل
user_name = st.text_input("👤 اسمك الكريم:")
user_code = st.text_input("🔑 الرمز السري (4 أرقام):", type="password")

st.markdown('<p class="lock-alert">⚠️ تُقفل التوقعات تلقائياً مع صافرة البداية (بتوقيت مكة).</p>', unsafe_allow_html=True)

# دالة مساعدة لحفظ المباراة
def save_match(match_key):
    if user_name and user_code:
        st.success("✔️ تم حفظ توقعك!")
    else:
        st.error("⚠️ يرجى إدخال الاسم والرمز أولاً.")

# قائمة المباريات (مثال لعدة مباريات مع أزرار الحفظ)
matches_data = [
    ("سهرة الخميس 11 يونيو", [("الخميس 11/06 - 10:00 م", "المكسيك", "جنوب أفريقيا", "m1")]),
    ("سهرة الثلاثاء 16 يونيو", [("الأربعاء 17/06 - 11:00 م", "إنجلترا", "كرواتيا", "m22")])
]

for day, matches in matches_data:
    st.markdown(f'<div class="day-header">{day}</div>', unsafe_allow_html=True)
    for time, t1, t2, key in matches:
        st.markdown(f'<div class="card"><b>⏱️ {time}</b><br>{t1} VS {t2}</div>', unsafe_allow_html=True)
        st.radio("توقعك:", [f"فوز {t1}", "تعادل", f"فوز {t2}"], key=f"radio_{key}")
        if st.button("💾 حفظ التوقع", key=f"btn_{key}"):
            save_match(key)
    st.markdown('<div class="gold-reminder">💡 تذكير: لا تنسى تعبئة "التوقع الذهبي" في الأسفل قبل قفل الجولة! 🎯</div>', unsafe_allow_html=True)

# التوقع الذهبي
st.markdown('<div class="gold-box-red"><h3>🌟 التوقعات الذهبية</h3><p>يغلق هذا القسم فور انتهاء الجولة الأولى!</p></div>', unsafe_allow_html=True)
if st.button("💾 حفظ التوقعات الذهبية"):
    save_match("gold")

# الشروط
st.markdown("""
    <div class="rules-box">
        <h3>📜 شروط وقوانين المسابقة</h3>
        <ul>
            <li>توقعات المجموعات (نقطة واحدة).</li>
            <li>التوقعات الذهبية (بونص كبير).</li>
            <li>يغلق التوقع مع بداية المباراة.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)
