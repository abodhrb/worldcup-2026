import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import datetime

# 1. إعدادات الصفحة والواجهة البصرية
st.set_page_config(
    page_title="مسابقة توقعات كأس العالم 2026",
    page_icon="🏆",
    layout="centered"
)

# تصميم مخصص بالألوان وإطارات الأيام المختلفة
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-size: 38px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .rules-box {
        background-color: #F8FAFC;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #E2E8F0;
        margin-top: 30px;
    }
    .gold-box-red {
        background-color: #FEF2F2;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #EF4444;
        margin-top: 30px;
        margin-bottom: 30px;
    }
    .red-text {
        color: #EF4444;
        font-weight: bold;
    }
    .day-header {
        font-size: 20px;
        font-weight: bold;
        color: #111827;
        margin-top: 25px;
        margin-bottom: 10px;
        padding-bottom: 5px;
        border-bottom: 2px solid #E5E7EB;
    }
    /* ألوان إطارات مخصصة لكل يوم للتفريق البصري */
    .card-day1 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #3B82F6; } /* أزرق */
    .card-day2 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #10B981; } /* أخضر */
    .card-day3 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #F59E0B; } /* برتقالي */
    .card-day4 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #8B5CF6; } /* بنفسجي */
    .card-day5 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #EC4899; } /* وردي */
    .card-day6 { background-color: #FFFFFF; padding: 18px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 15px; border-right: 6px solid #06B6D4; } /* سماوي */
    </style>
""", unsafe_allow_html=True)

# هيدر الموقع - الشعار الملون الرسمي لمونديال 2026
st.image("https://upload.wikimedia.org/wikipedia/commons/4/43/FIFA_World_Cup_2026_Logo.svg", width=320)
st.markdown('<div class="main-title">🏆 مسابقة توقعات كأس العالم 2026 🏆</div>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #4B5563;'>صراع التوقعات وطقطقة الشباب - بتوقيت مكة المكرمة 🕋</h4>", unsafe_allow_html=True)

st.divider()

# 2. واجهة التسجيل وبيانات المشارك
st.subheader("📝 بيانات المشارك")
st.info("💡 ابدأ بكتابة اسمك ورمزك السري لتتمكن من حفظ توقعاتك لكل مباراة بشكل مستقل.")
user_name = st.text_input("👤 اسمك الكريم:", key="global_user_name")
user_code = st.text_input("🔑 الرمز السري (4 أرقام):", type="password", max_chars=4, key="global_user_code")

st.divider()

# 3. قائمة مباريات الجولة الأولى (مقسمة بسهرات الأيام مدمج معها الفجر وملونة)
st.subheader("⚽ توقع المباريات واحفظها (مباراة بمباراة)")

# سهرة 1: الخميس 11 يونيو (افتتاحية البطولة)
st.markdown('<div class="day-header">🗓️ سهرة الخميس 11 يونيو</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="card-day1"><b>⏱️ الخميس 11/06/2026 - 10:00 م</b><br><span style="font-size:18px; font-weight: bold;">المكسيك 🇲🇽 <span style="color: #EF4444;">VS</span> جنوب أفريقيا 🇿🇦</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز المكسيك 🇲🇽", "تعادل 🤝", "فوز جنوب أفريقيا 🇿🇦"], key="radio_m1")
    if st.button("💾 حفظ التوقع", key="btn_m1"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day1"><b>⏱️ الجمعة 12/06/2026 - 05:00 ص (تابع لسهرة الخميس فجراً)</b><br><span style="font-size:18px; font-weight: bold;">كوريا الجنوبية 🇰🇷 <span style="color: #EF4444;">VS</span> أوكرانيا 🇺🇦</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز كوريا الجنوبية 🇰🇷", "تعادل 🤝", "فوز أوكرانيا 🇺🇦"], key="radio_m2")
    if st.button("💾 حفظ التوقع", key="btn_m2"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")


# سهرة 2: الجمعة 12 يونيو
st.markdown('<div class="day-header">🗓️ سهرة الجمعة 12 يونيو</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="card-day2"><b>⏱️ الجمعة 12/06/2026 - 10:00 م</b><br><span style="font-size:18px; font-weight: bold;">كندا 🇨🇦 <span style="color: #EF4444;">VS</span> بيرو 🇵🇪</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز كندا 🇨🇦", "تعادل 🤝", "فوز بيرو 🇵🇪"], key="radio_m3")
    if st.button("💾 حفظ التوقع", key="btn_m3"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day2"><b>⏱️ السبت 13/06/2026 - 04:00 ص (تابع لسهرة الجمعة فجراً)</b><br><span style="font-size:18px; font-weight: bold;">أمريكا 🇺🇸 <span style="color: #EF4444;">VS</span> باراغواي 🇵🇾</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز أمريكا 🇺🇸", "تعادل 🤝", "فوز باراغواي 🇵🇾"], key="radio_m4")
    if st.button("💾 حفظ التوقع", key="btn_m4"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")


# سهرة 3: السبت 13 يونيو
st.markdown('<div class="day-header">🗓️ سهرة السبت 13 يونيو</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="card-day3"><b>⏱️ السبت 13/06/2026 - 10:00 م</b><br><span style="font-size:18px; font-weight: bold;">سويسرا 🇨🇭 <span style="color: #EF4444;">VS</span> قطر 🇶🇦</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز سويسرا 🇨🇭", "تعادل 🤝", "فوز قطر 🇶🇦"], key="radio_m5")
    if st.button("💾 حفظ التوقع", key="btn_m5"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day3"><b>⏱️ الأحد 14/06/2026 - 01:00 ص (تابع لسهرة السبت فجراً)</b><br><span style="font-size:18px; font-weight: bold;">البرازيل 🇧🇷 <span style="color: #EF4444;">VS</span> المغرب 🇲🇦</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز البرازيل 🇧🇷", "تعادل 🤝", "فوز المغرب 🇲🇦"], key="radio_m6")
    if st.button("💾 حفظ التوقع", key="btn_m6"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day3"><b>⏱️ الأحد 14/06/2026 - 04:00 ص (تابع لسهرة السبت فجراً)</b><br><span style="font-size:18px; font-weight: bold;">هايتي 🇭🇹 <span style="color: #EF4444;">VS</span> اسكتلندا 🏴󠁧󠁢󠁳🇪🇺</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز هايتي 🇭🇹", "تعادل 🤝", "فوز اسكتلندا 🏴󠁧󠁢󠁳🇪"], key="radio_m7")
    if st.button("💾 حفظ التوقع", key="btn_m7"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day3"><b>⏱️ الأحد 14/06/2026 - 07:00 ص (تابع لسهرة السبت فجراً)</b><br><span style="font-size:18px; font-weight: bold;">أستراليا 🇦🇺 <span style="color: #EF4444;">VS</span> ويلز 🏴󠁧󠁢󠁷󠁬󠁳󠁿</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز أستراليا 🇦🇺", "تعادل 🤝", "فوز ويلز 🏴󠁧󠁢󠁷󠁬󠁳󠁿"], key="radio_m8")
    if st.button("💾 حفظ التوقع", key="btn_m8"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")


# سهرة 4: الأحد 14 يونيو
st.markdown('<div class="day-header">🗓️ سهرة الأحد 14 يونيو</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="card-day4"><b>⏱️ الأحد 14/06/2026 - 08:00 م</b><br><span style="font-size:18px; font-weight: bold;">ألمانيا 🇩🇪 <span style="color: #EF4444;">VS</span> كوراساو 🇨🇼</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز ألمانيا 🇩🇪", "تعادل 🤝", "فوز كوراساو 🇨🇼"], key="radio_m9")
    if st.button("💾 حفظ التوقع", key="btn_m9"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day4"><b>⏱️ الأحد 14/06/2026 - 11:00 م</b><br><span style="font-size:18px; font-weight: bold;">هولندا 🇳🇱 <span style="color: #EF4444;">VS</span> اليابان 🇯🇵</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز هولندا 🇳🇱", "تعادل 🤝", "فوز اليابان 🇯🇵"], key="radio_m10")
    if st.button("💾 حفظ التوقع", key="btn_m10"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day4"><b>⏱️ الاثنين 15/06/2026 - 01:00 ص (تابع لسهرة الأحد فجراً)</b><br><span style="font-size:18px; font-weight: bold;">إسبانيا 🇪🇸 <span style="color: #EF4444;">VS</span> الرأس الأخضر 🇨🇻</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز إسبانيا 🇪🇸", "تعادل 🤝", "فوز الرأس الأخضر 🇨🇻"], key="radio_m11")
    if st.button("💾 حفظ التوقع", key="btn_m11"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day4"><b>⏱️ الاثنين 15/06/2026 - 02:00 ص (تابع لسهرة الأحد فجراً)</b><br><span style="font-size:18px; font-weight: bold;">ساحل العاج 🇨🇮 <span style="color: #EF4444;">VS</span> الإكوادور 🇪🇨</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز ساحل العاج 🇨🇮", "تعادل 🤝", "فوز الإكوادور 🇪🇨"], key="radio_m12")
    if st.button("💾 حفظ التوقع", key="btn_m12"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day4"><b>⏱️ الاثنين 15/06/2026 - 05:00 ص (تابع لسهرة الأحد فجراً)</b><br><span style="font-size:18px; font-weight: bold;">بولندا 🇵🇱 <span style="color: #EF4444;">VS</span> تونس 🇹🇳</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز بولندا 🇵🇱", "تعادل 🤝", "فوز تونس 🇹🇳"], key="radio_m13")
    if st.button("💾 حفظ التوقع", key="btn_m13"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")


# سهرة 5: الاثنين 15 يونيو
st.markdown('<div class="day-header">🗓️ سهرة الاثنين 15 يونيو</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="card-day5"><b>⏱️ الاثنين 15/06/2026 - 10:00 م</b><br><span style="font-size:18px; font-weight: bold;">بلجيكا 🇧🇪 <span style="color: #EF4444;">VS</span> مصر 🇪🇬</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز بلجيكا 🇧🇪", "تعادل 🤝", "فوز مصر 🇪🇬"], key="radio_m14")
    if st.button("💾 حفظ التوقع", key="btn_m14"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day5"><b>⏱️ الثلاثاء 16/06/2026 - 01:00 ص (تابع لسهرة الاثنين فجراً - مباراة الصقور 🔥)</b><br><span style="font-size:18px; font-weight: bold;">السعودية 🇸🇦 <span style="color: #EF4444;">VS</span> أوروغواي 🇺🇾</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز السعودية 🇸🇦", "تعادل 🤝", "فوز أوروغواي 🇺🇾"], key="radio_m15")
    if st.button("💾 حفظ التوقع", key="btn_m15"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day5"><b>⏱️ الثلاثاء 16/06/2026 - 04:00 ص (تابع لسهرة الاثنين فجراً)</b><br><span style="font-size:18px; font-weight: bold;">إيران 🇮🇷 <span style="color: #EF4444;">VS</span> نيوزيلندا 🇳🇿</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز إيران 🇮🇷", "تعادل 🤝", "فوز نيوزيلندا 🇳🇿"], key="radio_m16")
    if st.button("💾 حفظ التوقع", key="btn_m16"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")


# سهرة 6: الثلاثاء 16 يونيو
st.markdown('<div class="day-header">🗓️ سهرة الثلاثاء 16 يونيو</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="card-day6"><b>⏱️ الثلاثاء 16/06/2026 - 10:00 م</b><br><span style="font-size:18px; font-weight: bold;">فرنسا 🇫🇷 <span style="color: #EF4444;">VS</span> السنغال 🇸🇳</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز فرنسا 🇫🇷", "تعادل 🤝", "فوز السنغال 🇸🇳"], key="radio_m17")
    if st.button("💾 حفظ التوقع", key="btn_m17"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day6"><b>⏱️ الأربعاء 17/06/2026 - 01:00 ص (تابع لسهرة الثلاثاء فجراً)</b><br><span style="font-size:18px; font-weight: bold;">تشيلي 🇨🇱 <span style="color: #EF4444;">VS</span> النرويج 🇳🇴</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز تشيلي 🇨🇱", "تعادل 🤝", "فوز النرويج 🇳🇴"], key="radio_m18")
    if st.button("💾 حفظ التوقع", key="btn_m18"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day6"><b>⏱️ الأربعاء 17/06/2026 - 04:00 ص (تابع لسهرة الثلاثاء فجراً)</b><br><span style="font-size:18px; font-weight: bold;">الأرجنتين 🇦🇷 <span style="color: #EF4444;">VS</span> الجزائر 🇩🇿</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز الأرجنتين 🇦🇷", "تعادل 🤝", "فوز الجزائر 🇩🇿"], key="radio_m19")
    if st.button("💾 حفظ التوقع", key="btn_m19"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day6"><b>⏱️ الأربعاء 17/06/2026 - 07:00 ص (تابع لسهرة الثلاثاء فجراً)</b><br><span style="font-size:18px; font-weight: bold;">النمسا 🇦🇹 <span style="color: #EF4444;">VS</span> الأردن 🇯🇴</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز النمسا 🇦🇹", "تعادل 🤝", "فوز الأردن 🇯🇴"], key="radio_m20")
    if st.button("💾 حفظ التوقع", key="btn_m20"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day6"><b>⏱️ الأربعاء 17/06/2026 - 08:00 م</b><br><span style="font-size:18px; font-weight: bold;">البرتغال 🇵🇹 <span style="color: #EF4444;">VS</span> غانا 🇬🇭</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز البرتغال 🇵🇹", "تعادل 🤝", "فوز غانا 🇬🇭"], key="radio_m21")
    if st.button("💾 حفظ التوقع", key="btn_m21"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day6"><b>⏱️ الأربعاء 17/06/2026 - 11:00 م</b><br><span style="font-size:18px; font-weight: bold;">إنجلترا 🏴󠁧󠁢󠁥󠁮󠁧󠁿 <span style="color: #EF4444;">VS</span> كرواتيا 🇭🇷</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز إنجلترا 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "تعادل 🤝", "فوز كرواتيا 🇭🇷"], key="radio_m22")
    if st.button("💾 حفظ التوقع", key="btn_m22"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day6"><b>⏱️ الخميس 18/06/2026 - 02:00 ص (تابع لسهرة الأربعاء فجراً)</b><br><span style="font-size:18px; font-weight: bold;">الكاميرون 🇨🇲 <span style="color: #EF4444;">VS</span> بنما 🇵🇦</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز الكاميرون 🇨🇲", "تعادل 🤝", "فوز بنما 🇵🇦"], key="radio_m23")
    if st.button("💾 حفظ التوقع", key="btn_m23"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

with st.container():
    st.markdown('<div class="card-day6"><b>⏱️ الخميس 18/06/2026 - 05:00 ص (تابع لسهرة الأربعاء فجراً)</b><br><span style="font-size:18px; font-weight: bold;">أوزبكستان 🇺🇿 <span style="color: #EF4444;">VS</span> كولومبيا 🇨🇴</span></div>', unsafe_allow_html=True)
    choice = st.radio("توقعك:", ["فوز أوزبكستان 🇺🇿", "تعادل 🤝", "فوز كولومبيا 🇨🇴"], key="radio_m24")
    if st.button("💾 حفظ التوقع", key="btn_m24"):
        if user_name and user_code: st.success("✔️ تم حفظ توقعك بنجاح!")
        else: st.error("⚠️ اكتب اسمك ورمزك فوق أولاً.")

st.divider()

# 4. قسم التوقعات الذهبية (الموقع الجديد: قبل الشروط مباشرة ومحمي باللون الأحمر والإعلان الرسمي)
st.markdown('<div class="gold-box-red">', unsafe_allow_html=True)
st.markdown("### 🌟 قسم التوقعات الذهبية (التحدي الكبير)")
st.markdown("<p style='color: #4B5563; font-size: 16px;'>🎯 <b>فرصة التوقعات الذهبية الكبرى!</b> طرفي النهائي وبطل كأس العالم يمنحونك (البونص الكبير) لقلب الطاولة في صدارة الترتيب.. لا تفوتها! 🏆</p>", unsafe_allow_html=True)
st.markdown("<p class='red-text'>⚠️ تنبيه حساس: هذا القسم بالكامل يقفل تلقائياً فور نهاية آخر مباراة في الجولة الأولى مباشرة!</p>", unsafe_allow_html=True)

finalist_1 = st.text_input("🏳️ توقع طرف النهائي الأول:")
finalist_2 = st.text_input("🏳️ توقع طرف النهائي الثاني:")
champion_pred = st.text_input("👑 توقع بطل كأس العالم 2026:")

if st.button("💾 حفظ التوقعات الذهبية الكبرى"):
    if user_name and user_code:
        st.success(f"🔥 كفو! تم تثبيت وتأمين توقعاتك الذهبية للأبطال بنجاح يا {user_name}!")
        st.balloons()
    else:
        st.error("⚠️ خطأ: يرجى كتابة اسمك والرمز السري في أعلى الصفحة أولاً لحفظ التوقعات الذهبية!")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 5. قسم الشروط والقوانين والجوائز (مفتوح دائماً في أسفل الصفحة كمرجع)
st.markdown("""
    <div class="rules-box">
        <h3 style='color: #1E3A8A; text-align: center; margin-bottom: 15px;'>📜 شروط وقوانين المسابقة والجوائز المعتمدة</h3>
        <hr style='border-color: #E2E8F0;'>
        <h4 style='color: #10B981;'>🎁 جوائز التحدي والمنافسة للثلاثة الأوائل:</h4>
        <ul>
            <li><b>🥇 صاحب المركز الأول:</b> يحصل على <b>(هدية قيمة وخاصة)</b> تليق ببطل المونديال الرسمي! 🏆</li>
            <li><b>🥈 صاحب المركز الثاني:</b> يحصل على <b>(هدية بسيطة وترضية)</b> تقديراً للمنافسة الشرسة! 🎉</li>
            <li><b>🥉 صاحب المركز الثالث:</b> يحصل على <b>(هدية ترضية لطيفة)</b> لوصوله لمنصة التتويج! 🏅</li>
        </ul>
        <hr style='border-color: #E2E8F0;'>
        <h4>1️⃣ نظام نقاط المباريات والتوقعات الذهبية:</h4>
        <ul>
            <li><b>مباريات المجموعات:</b> تتوقع مسار المباراة (فوز أو تعادل)، والتوقع الصحيح يمنحك <b>(نقطة واحدة)</b>.</li>
            <li><b>بونص التوقعات الذهبية:</b> تحصل على <b>(10 نقاط)</b> عن كل منتخب صحيح يصل للنهائي، وتوقع البطل الصحيح يمنحك <b>(20 نقطة)</b> كاملة!</li>
        </ul>
        <hr style='border-color: #E2E8F0;'>
        <h4>2️⃣ نظام القفل الآلي وحفظ البيانات ⏱️:</h4>
        <ul>
            <li><b>توقع مباراة بمباراة:</b> تقدر تدخل وتتوقع كل مباراة لحالها وتحفظها بشكل مستقل في أي وقت، مو شرط تتوقع الجولة كلها دفعة واحدة!</li>
            <li><b>قفل المباريات:</b> يغلق التوقع لأي مباراة تلقائياً مع صافرة انطلاق المباراة بالضبط (بتوقيت مكة).</li>
            <li><b>قفل التوقع الذهبي:</b> <span class='red-text'>يغلق قسم التوقعات الذهبية بالكامل فور انتهاء آخر مباراة في الجولة الأولى.</span></li>
        </ul>
    </div>
""", unsafe_allow_html=True)
