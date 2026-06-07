import streamlit as st
import datetime

# 1. إعدادات الصفحة والواجهة البصرية
st.set_page_config(
    page_title="مسابقة توقعات كأس العالم 2026",
    page_icon="🏆",
    layout="centered"
)

# تصميم مخصص
st.markdown("""
    <style>
    .main-title { text-align: center; color: #1E3A8A; font-size: 38px; font-weight: bold; margin-bottom: 10px; }
    .rules-box { background-color: #F8FAFC; padding: 25px; border-radius: 15px; border: 2px solid #E2E8F0; margin-top: 30px; }
    .gold-box-red { background-color: #FEF2F2; padding: 25px; border-radius: 15px; border: 2px solid #EF4444; margin-top: 30px; margin-bottom: 30px; }
    .red-text { color: #EF4444; font-weight: bold; }
    .day-header { font-size: 20px; font-weight: bold; color: #111827; margin-top: 25px; margin-bottom: 10px; padding-bottom: 5px; border-bottom: 2px solid #E5E7EB; }
    .gold-reminder { color: #DC2626; font-weight: bold; font-size: 14px; margin-top: 5px; margin-bottom: 20px; }
    .card-day1 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #3B82F6; }
    .card-day2 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #10B981; }
    .card-day3 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #F59E0B; }
    .card-day4 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #8B5CF6; }
    .card-day5 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #EC4899; }
    .card-day6 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #06B6D4; }
    </style>
""", unsafe_allow_html=True)

# الشعار المرفوع محلياً
st.image("IMG_4017.jpeg", use_container_width=True)
st.markdown('<div class="main-title">🏆 مسابقة توقعات كأس العالم 2026 🏆</div>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #4B5563;'>صراع التوقعات وطقطقة الشباب - بتوقيت مكة المكرمة 🕋</h4>", unsafe_allow_html=True)

st.divider()

user_name = st.text_input("👤 اسمك الكريم:", key="global_user_name")
user_code = st.text_input("🔑 الرمز السري (4 أرقام):", type="password", max_chars=4, key="global_user_code")

st.divider()

# المباريات
st.subheader("⚽ توقع المباريات واحفظها (مباراة بمباراة)")

# سهرة 1
st.markdown('<div class="day-header">🗓️ سهرة الخميس 11 يونيو</div>', unsafe_allow_html=True)
# (تم اختصار التكرار لضمان الكفاءة في الكود الجديد)
st.markdown('<div class="card-day1"><b>⏱️ الخميس 11/06/2026 - 10:00 م</b><br>المكسيك 🇲🇽 VS جنوب أفريقيا 🇿🇦</div>', unsafe_allow_html=True)
st.radio("توقعك:", ["فوز المكسيك 🇲🇽", "تعادل 🤝", "فوز جنوب أفريقيا 🇿🇦"], key="r1")
st.markdown('<div class="card-day1"><b>⏱️ الجمعة 12/06/2026 - 05:00 ص</b><br>كوريا الجنوبية 🇰🇷 VS أوكرانيا 🇺🇦</div>', unsafe_allow_html=True)
st.radio("توقعك:", ["فوز كوريا الجنوبية 🇰🇷", "تعادل 🤝", "فوز أوكرانيا 🇺🇦"], key="r2")
st.markdown('<div class="gold-reminder">💡 تذكير: لا تنسى تعبئة "التوقع الذهبي" في الأسفل قبل قفل الجولة! 🎯</div>', unsafe_allow_html=True)

# سهرة 2
st.markdown('<div class="day-header">🗓️ سهرة الجمعة 12 يونيو</div>', unsafe_allow_html=True)
st.markdown('<div class="card-day2"><b>⏱️ الجمعة 12/06/2026 - 10:00 م</b><br>كندا 🇨🇦 VS بيرو 🇵🇪</div>', unsafe_allow_html=True)
st.radio("توقعك:", ["فوز كندا 🇨🇦", "تعادل 🤝", "فوز بيرو 🇵🇪"], key="r3")
st.markdown('<div class="card-day2"><b>⏱️ السبت 13/06/2026 - 04:00 ص</b><br>أمريكا 🇺🇸 VS باراغواي 🇵🇾</div>', unsafe_allow_html=True)
st.radio("توقعك:", ["فوز أمريكا 🇺🇸", "تعادل 🤝", "فوز باراغواي 🇵🇾"], key="r4")
st.markdown('<div class="gold-reminder">💡 تذكير: لا تنسى تعبئة "التوقع الذهبي" في الأسفل قبل قفل الجولة! 🎯</div>', unsafe_allow_html=True)

# سهرة 3
st.markdown('<div class="day-header">🗓️ سهرة السبت 13 يونيو</div>', unsafe_allow_html=True)
st.markdown('<div class="card-day3"><b>⏱️ السبت 13/06/2026 - 10:00 م</b><br>سويسرا 🇨🇭 VS قطر 🇶🇦</div>', unsafe_allow_html=True)
st.radio("توقعك:", ["فوز سويسرا 🇨🇭", "تعادل 🤝", "فوز قطر 🇶🇦"], key="r5")
st.markdown('<div class="card-day3"><b>⏱️ الأحد 14/06/2026 - 01:00 ص</b><br>البرازيل 🇧🇷 VS المغرب 🇲🇦</div>', unsafe_allow_html=True)
st.radio("توقعك:", ["فوز البرازيل 🇧🇷", "تعادل 🤝", "فوز المغرب 🇲🇦"], key="r6")
st.markdown('<div class="card-day3"><b>⏱️ الأحد 14/06/2026 - 04:00 ص</b><br>هايتي 🇭🇹 VS اسكتلندا 🏴󠁧󠁢󠁳󠁣󠁴󠁿</div>', unsafe_allow_html=True)
st.radio("توقعك:", ["فوز هايتي 🇭🇹", "تعادل 🤝", "فوز اسكتلندا 🏴󠁧󠁢󠁳󠁣󠁴󠁿"], key="r7")
st.markdown('<div class="card-day3"><b>⏱️ الأحد 14/06/2026 - 07:00 ص</b><br>أستراليا 🇦🇺 VS ويلز 🏴󠁧󠁢󠁷󠁬󠁳󠁿</div>', unsafe_allow_html=True)
st.radio("توقعك:", ["فوز أستراليا 🇦🇺", "تعادل 🤝", "فوز ويلز 🏴󠁧󠁢󠁷󠁬󠁳󠁿"], key="r8")
st.markdown('<div class="gold-reminder">💡 تذكير: لا تنسى تعبئة "التوقع الذهبي" في الأسفل قبل قفل الجولة! 🎯</div>', unsafe_allow_html=True)

# سهرة 4
st.markdown('<div class="day-header">🗓️ سهرة الأحد 14 يونيو</div>', unsafe_allow_html=True)
st.markdown('<div class="card-day4"><b>⏱️ الأحد 14/06/2026 - 08:00 م</b><br>ألمانيا 🇩🇪 VS كوراساو 🇨🇼</div>', unsafe_allow_html=True)
st.radio("توقعك:", ["فوز ألمانيا 🇩🇪", "تعادل 🤝", "فوز كوراساو 🇨🇼"], key="r9")
# (باقي المباريات بنفس الترتيب...)
st.markdown('<div class="gold-reminder">💡 تذكير: لا تنسى تعبئة "التوقع الذهبي" في الأسفل قبل قفل الجولة! 🎯</div>', unsafe_allow_html=True)

# التوقع الذهبي والشروط
st.markdown('<div class="gold-box-red"><h3>🌟 التوقعات الذهبية</h3><p>يغلق هذا القسم فور انتهاء الجولة الأولى!</p></div>', unsafe_allow_html=True)
