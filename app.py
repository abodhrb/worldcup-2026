import streamlit as st
import os

# --- نسخة الإصدار: V3 ---

st.set_page_config(page_title="مسابقة توقعات كأس العالم 2026 (V3)", page_icon="🏆", layout="centered")

# التنسيق للألوان والأجزاء
st.markdown("""
    <style>
    .day-box { padding: 15px; border-radius: 10px; margin-bottom: 10px; color: white; }
    .rules-box { background-color: #f9f9f9; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-top: 30px; color: black; }
    .gold-reminder { color: red; font-weight: bold; margin-top: 10px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

if os.path.exists("IMG_4017.jpeg"):
    st.image("IMG_4017.jpeg", use_container_width=True)

# لوحة الإدارة
with st.sidebar:
    st.header("⚙️ لوحة الإدارة (V3)")
    admin_pass = st.text_input("كلمة سر المدير:", type="password")
    if admin_pass == "1234":
        st.success("أهلاً بك يا أبو أحمد")
        match_name = st.text_input("اسم المباراة:")
        result = st.text_input("النتيجة:")
        if st.button("💾 حفظ النتيجة"):
            st.write(f"✅ تم حفظ نتيجة {match_name} بـ {result}")
    else:
        st.info("للإدارة فقط")

st.markdown("<h1 style='text-align: center;'>🏆 مسابقة توقعات كأس العالم 2026</h1>", unsafe_allow_html=True)

# قائمة المباريات
matches_data = [
    ("سهرة الخميس 11 يونيو", [("🇲🇽 المكسيك", "🇿🇦 جنوب أفريقيا"), ("🇰🇷 كوريا الجنوبية", "🇯🇴 الأردن")], "#1E3A8A"),
    ("سهرة الجمعة 12 يونيو", [("🇨🇦 كندا", "🇵🇪 بيرو"), ("🇺🇸 أمريكا", "🇵🇾 باراغواي")], "#059669"),
    ("سهرة السبت 13 يونيو", [("🇨🇭 سويسرا", "🇶🇦 قطر"), ("🇧🇷 البرازيل", "🇲🇦 المغرب"), ("🇭🇹 هايتي", "🏴󠁧󠁢󠁳󠁣󠁴󠁿 اسكتلندا"), ("🇦🇺 أستراليا", "🏴󠁧󠁢󠁷󠁬󠁳󠁿 ويلز")], "#DC2626"),
    ("سهرة الأحد 14 يونيو", [("🇩🇪 ألمانيا", "🇨🇼 كوراساو"), ("🇳🇱 هولندا", "🇯🇵 اليابان"), ("🇪🇸 إسبانيا", "🇨🇻 الرأس الأخضر"), ("🇨🇮 ساحل العاج", "🇪🇨 الإكوادور"), ("🇵🇱 بولندا", "🇹🇳 تونس")], "#D97706"),
    ("سهرة الاثنين 15 يونيو", [("🇧🇪 بلجيكا", "🇪🇬 مصر"), ("🇸🇦 السعودية", "🇺🇾 أوروغواي"), ("🇮🇷 إيران", "🇳🇿 نيوزيلندا")], "#7C3AED"),
    ("سهرة الثلاثاء 16 يونيو", [("🇫🇷 فرنسا", "🇸🇳 السنغال"), ("🇨🇱 تشيلي", "🇳🇴 النرويج"), ("🇦🇷 الأرجنتين", "🇩🇿 الجزائر"), ("🇦🇹 النمسا", "🇺🇿 أوزبكستان"), ("🇵🇹 البرتغال", "🇬🇭 غانا"), ("🏴󠁧󠁢󠁥󠁮󠁧󠁿 إنجلترا", "🇭🇷 كرواتيا"), ("🇨🇲 الكاميرون", "🇵🇦 بنما"), ("🇨🇴 كولومبيا", "🇩🇿 الجزائر")], "#DB2777")
]

for day, matches, color in matches_data:
    st.markdown(f'<div class="day-box" style="background-color: {color};"><h3>{day}</h3></div>', unsafe_allow_html=True)
    for t1, t2 in matches:
        st.write(f"**{t1} vs {t2}**")
        st.radio("اختر توقعك:", [f"فوز {t1}", "تعادل", f"فوز {t2}"], key=f"radio_{t1}_{t2}")
        if st.button("💾 حفظ توقعي", key=f"btn_{t1}_{t2}"):
            st.success(f"تم حفظ توقعك لـ {t1} vs {t2}")
        st.markdown("---")
    # تذكير التوقع الذهبي بالأحمر بعد كل يوم
    st.markdown('<p class="gold-reminder">⚠️ تذكير: ينتهي التوقع الذهبي يوم 18 يونيو الساعة 11:59 مساءً.</p>', unsafe_allow_html=True)

# التوقعات الذهبية
st.subheader("🌟 التوقعات الذهبية")
final1 = st.text_input("طرف النهائي الأول:")
final2 = st.text_input("طرف النهائي الثاني:")
champion = st.text_input("بطل كأس العالم 2026:")
if st.button("💾 تثبيت التوقعات الذهبية"):
    st.success("تم تثبيت توقعاتك الذهبية بنجاح!")

# الشروط والقوانين
st.markdown("""
<div class="rules-box">
<h3>📜 شروط وقوانين المسابقة والجوائز</h3>
<ul>
<li><b>🥇 المركز الأول:</b> هدية المركز الأول (قيمة وخاصة).</li>
<li><b>🥈 المركز الثاني:</b> هدية المركز الثاني (هدية ترضية مميزة).</li>
<li><b>🥉 المركز الثالث:</b> هدية المركز الثالث (هدية ترضية لطيفة).</li>
<li><b>نظام النقاط:</b> (10) نقاط لكل طرف نهائي صحيح، و(20) نقطة لتوقع البطل.</li>
<li><b>القفل:</b> التوقعات تغلق تلقائياً مع بداية المباراة، والذهبي يغلق بعد الجولة الأولى.</li>
</ul>
</div>
""", unsafe_allow_html=True)
