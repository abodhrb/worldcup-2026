import streamlit as st
import os
from datetime import datetime, timezone, timedelta

# --- نسخة الإصدار: V4 ---

st.set_page_config(page_title="مسابقة توقعات كأس العالم 2026 (V4)", page_icon="🏆", layout="centered")

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
    st.header("⚙️ لوحة الإدارة (V4)")
    admin_pass = st.text_input("كلمة سر المدير:", type="password")
    if admin_pass == "1234":
        st.success("أهلاً بك يا أبو أحمد")
    else:
        st.info("للإدارة فقط")

st.markdown("<h1 style='text-align: center;'>🏆 مسابقة توقعات كأس العالم 2026</h1>", unsafe_allow_html=True)

# استخدام التوقيت الموحد (UTC) للقفل
current_time = datetime.now(timezone.utc)

# جدول المباريات (تعديل توقيتاتك هنا)
matches_data = [
    ("سهرة الخميس 11 يونيو", [("🇲🇽 المكسيك", "🇿🇦 جنوب أفريقيا", datetime(2026, 6, 11, 20, 0, tzinfo=timezone.utc)), ("🇰🇷 كوريا الجنوبية", "🇯🇴 الأردن", datetime(2026, 6, 11, 22, 0, tzinfo=timezone.utc))], "#1E3A8A"),
    ("سهرة الجمعة 12 يونيو", [("🇨🇦 كندا", "🇵🇪 بيرو", datetime(2026, 6, 12, 20, 0, tzinfo=timezone.utc)), ("🇺🇸 أمريكا", "🇵🇾 باراغواي", datetime(2026, 6, 12, 22, 0, tzinfo=timezone.utc))], "#059669"),
    ("سهرة السبت 13 يونيو", [("🇨🇭 سويسرا", "🇶🇦 قطر", datetime(2026, 6, 13, 20, 0, tzinfo=timezone.utc)), ("🇧🇷 البرازيل", "🇲🇦 المغرب", datetime(2026, 6, 13, 22, 0, tzinfo=timezone.utc))], "#DC2626"),
]

for day, matches, color in matches_data:
    st.markdown(f'<div class="day-box" style="background-color: {color};"><h3>{day}</h3></div>', unsafe_allow_html=True)
    for t1, t2, start_time in matches:
        st.write(f"**{t1} vs {t2}**")
        
        # القفل بعد 5 دقائق من بداية المباراة
        lock_time = start_time + timedelta(minutes=5)
        
        if current_time > lock_time:
            st.error("🔒 تم إغلاق التوقع لهذه المباراة.")
        else:
            st.radio("اختر توقعك:", [f"فوز {t1}", "تعادل", f"فوز {t2}"], key=f"radio_{t1}_{t2}")
            if st.button("💾 حفظ توقعي", key=f"btn_{t1}_{t2}"):
                st.success(f"تم حفظ توقعك لـ {t1} vs {t2}")
        st.markdown("---")
    st.markdown('<p class="gold-reminder">⚠️ تذكير: ينتهي التوقع الذهبي يوم 18 يونيو الساعة 11:59 مساءً.</p>', unsafe_allow_html=True)

# التوقعات الذهبية
st.subheader("🌟 التوقعات الذهبية")
gold_lock_time = datetime(2026, 6, 18, 23, 59, tzinfo=timezone.utc)
if current_time > gold_lock_time:
    st.error("🔒 تم إغلاق التوقعات الذهبية.")
else:
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
<li><b>القفل:</b> التوقعات تغلق تلقائياً بعد 5 دقائق من بداية المباراة، والذهبي يغلق يوم 18 يونيو.</li>
</ul>
</div>
""", unsafe_allow_html=True)
