import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="مسابقة توقعات كأس العالم 2026", page_icon="🏆", layout="centered")

# التصميم والتنسيق
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

# الصورة والعنوان
st.image("IMG_4017.jpeg", use_container_width=True)
st.markdown('<div class="main-title">🏆 مسابقة توقعات كأس العالم 2026 🏆</div>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #4B5563;'>بتوقيت مكة المكرمة 🕋</h4>", unsafe_allow_html=True)

# تسجيل المشارك
user_name = st.text_input("👤 اسمك الكريم:")
user_code = st.text_input("🔑 الرمز السري (4 أرقام):", type="password")

st.markdown('<p class="lock-alert">⚠️ تُقفل التوقعات تلقائياً مع صافرة البداية (بتوقيت مكة).</p>', unsafe_allow_html=True)

# قائمة المباريات كاملة
matches_list = [
    ("سهرة الخميس 11 يونيو", [("الخميس 11/06 - 10:00 م", "المكسيك", "جنوب أفريقيا"), ("الجمعة 12/06 - 05:00 ص", "كوريا الجنوبية", "أوكرانيا")]),
    ("سهرة الجمعة 12 يونيو", [("الجمعة 12/06 - 10:00 م", "كندا", "بيرو"), ("السبت 13/06 - 04:00 ص", "أمريكا", "باراغواي")]),
    ("سهرة السبت 13 يونيو", [("السبت 13/06 - 10:00 م", "سويسرا", "قطر"), ("الأحد 14/06 - 01:00 ص", "البرازيل", "المغرب"), ("الأحد 14/06 - 04:00 ص", "هايتي", "اسكتلندا 🏴󠁧󠁢󠁳󠁣󠁴󠁿"), ("الأحد 14/06 - 07:00 ص", "أستراليا", "ويلز")]),
    ("سهرة الأحد 14 يونيو", [("الأحد 14/06 - 08:00 م", "ألمانيا", "كوراساو"), ("الأحد 14/06 - 11:00 م", "هولندا", "اليابان"), ("الاثنين 15/06 - 01:00 ص", "إسبانيا", "الرأس الأخضر"), ("الاثنين 15/06 - 02:00 ص", "ساحل العاج", "الإكوادور"), ("الاثنين 15/06 - 05:00 ص", "بولندا", "تونس")]),
    ("سهرة الاثنين 15 يونيو", [("الاثنين 15/06 - 10:00 م", "بلجيكا", "مصر"), ("الثلاثاء 16/06 - 01:00 ص", "السعودية", "أوروغواي"), ("الثلاثاء 16/06 - 04:00 ص", "إيران", "نيوزيلندا")]),
    ("سهرة الثلاثاء 16 يونيو", [("الثلاثاء 16/06 - 10:00 م", "فرنسا", "السنغال"), ("الأربعاء 17/06 - 01:00 ص", "تشيلي", "النرويج"), ("الأربعاء 17/06 - 04:00 ص", "الأرجنتين", "الجزائر"), ("الأربعاء 17/06 - 07:00 ص", "النمسا", "الأردن"), ("الأربعاء 17/06 - 08:00 م", "البرتغال", "غانا"), ("الأربعاء 17/06 - 11:00 م", "إنجلترا", "كرواتيا"), ("الخميس 18/06 - 02:00 ص", "الكاميرون", "بنما"), ("الخميس 18/06 - 05:00 ص", "أوزبكستان", "كولومبيا")])
]

# عرض المباريات
for day, matches in matches_list:
    st.markdown(f'<div class="day-header">{day}</div>', unsafe_allow_html=True)
    for time, t1, t2 in matches:
        st.markdown(f'<div class="card"><b>⏱️ {time}</b><br>{t1} VS {t2}</div>', unsafe_allow_html=True)
        st.radio("توقعك:", [f"فوز {t1}", "تعادل", f"فوز {t2}"], key=f"{time}")
        if st.button("💾 حفظ التوقع", key=f"btn_{time}"):
            if user_name and user_code: st.success("✔️ تم حفظ توقعك!")
            else: st.error("⚠️ يرجى إدخال الاسم والرمز أولاً.")
    st.markdown('<div class="gold-reminder">💡 تذكير: لا تنسى تعبئة "التوقع الذهبي" في الأسفل قبل قفل الجولة! 🎯</div>', unsafe_allow_html=True)

# التوقع الذهبي
st.markdown('<div class="gold-box-red"><h3>🌟 التوقعات الذهبية</h3><p>فرصة البونص الكبير! يغلق هذا القسم فور انتهاء الجولة الأولى.</p></div>', unsafe_allow_html=True)
st.text_input("🏳️ توقع طرف النهائي الأول:")
st.text_input("🏳️ توقع طرف النهائي الثاني:")
st.text_input("👑 توقع بطل كأس العالم 2026:")
if st.button("💾 حفظ التوقعات الذهبية"):
    st.success("🔥 تم تثبيت توقعاتك الذهبية!")

# الشروط والجوائز كاملة
st.markdown("""
    <div class="rules-box">
        <h3>📜 شروط وقوانين المسابقة والجوائز</h3>
        <p><b>🎁 جوائز التحدي والمنافسة للثلاثة الأوائل:</b></p>
        <ul>
            <li><b>🥇 صاحب المركز الأول:</b> يحصل على (هدية قيمة وخاصة) تليق ببطل المونديال الرسمي! 🏆</li>
            <li><b>🥈 صاحب المركز الثاني:</b> يحصل على (هدية بسيطة وترضية) تقديراً للمنافسة الشرسة! 🎉</li>
            <li><b>🥉 صاحب المركز الثالث:</b> يحصل على (هدية ترضية لطيفة) لوصوله لمنصة التتويج! 🏅</li>
        </ul>
        <hr>
        <p><b>1️⃣ نظام النقاط:</b></p>
        <ul>
            <li><b>مباريات المجموعات:</b> التوقع الصحيح للمباراة يمنحك (نقطة واحدة).</li>
            <li><b>التوقعات الذهبية:</b>
                <ul>
                    <li>توقع طرف نهائي صحيح يمنحك <b>(10 نقاط)</b> عن كل طرف.</li>
                    <li>توقع بطل كأس العالم الصحيح يمنحك <b>(20 نقطة)</b> كاملة.</li>
                </ul>
            </li>
        </ul>
        <hr>
        <p><b>2️⃣ نظام القفل الآلي:</b></p>
        <ul>
            <li>التوقعات للمباريات تغلق تلقائياً مع صافرة بداية كل مباراة.</li>
            <li>قسم التوقعات الذهبية يغلق تلقائياً فور انتهاء الجولة الأولى.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)
