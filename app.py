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

# تصميم مخصص بالألوان
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
        margin-top: 50px;
    }
    .gold-box-red {
        background-color: #FEF2F2;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #EF4444;
        margin-bottom: 30px;
    }
    .match-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-right: 6px solid #1E3A8A;
    }
    .red-text {
        color: #EF4444;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# هيدر الموقع - شعار كأس العالم 2026
st.image("https://upload.wikimedia.org/wikipedia/en/4/42/2026_FIFA_World_Cup_logo.svg", width=300)
st.markdown('<div class="main-title">🏆 مسابقة توقعات كأس العالم 2026 🏆</div>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #4B5563;'>صراع التوقعات - بتوقيت مكة المكرمة 🕋</h4>", unsafe_allow_html=True)

st.divider()

# 2. واجهة التسجيل وبيانات المشارك
st.subheader("📝 بيانات المشارك")
st.info("💡 ابدأ بكتابة اسمك ورمزك السري لتتمكن من حفظ توقعاتك لكل مباراة.")
user_name = st.text_input("👤 اسمك الكريم:", key="global_user_name")
user_code = st.text_input("🔑 الرمز السري (4 أرقام):", type="password", max_chars=4, key="global_user_code")

st.divider()

# 3. قسم التوقعات الذهبية (باللون الأحمر وتنبيه القفل)
st.markdown('<div class="gold-box-red">', unsafe_allow_html=True)
st.markdown("### 🌟 التوقعات الذهبية (بونص الأبطال)")
st.markdown("<p class='red-text'>⚠️ تنبيه: هذا القسم يغلق تماماً فور نهاية آخر مباراة في الجولة الأولى!</p>", unsafe_allow_html=True)

finalist_1 = st.text_input("🏳️ توقع طرف النهائي الأول:")
finalist_2 = st.text_input("🏳️ توقع طرف النهائي الثاني:")
champion_pred = st.text_input("👑 توقع بطل كأس العالم 2026:")

if st.button("💾 حفظ التوقعات الذهبية"):
    if user_name and user_code:
        st.success(f"🔥 تم تأمين توقعاتك للأبطال يا {user_name}!")
        st.balloons()
    else:
        st.error("⚠️ يرجى كتابة الاسم والرمز السري بالأعلى أولاً.")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 4. قائمة مباريات الجولة الأولى بالأعلام وتوقيت مكة
st.subheader("⚽ توقع المباريات واحفظها (مباراة بمباراة)")

matches_round_1 = [
    {"id": "m1", "date": "الخميس 11/06/2026 - 10:00 م", "team1": "المكسيك 🇲🇽", "team2": "جنوب أفريقيا 🇿🇦"},
    {"id": "m2", "date": "الجمعة 12/06/2026 - 05:00 ص", "team1": "كوريا الجنوبية 🇰🇷", "team2": "أوكرانيا 🇺🇦"},
    {"id": "m3", "date": "الجمعة 12/06/2026 - 10:00 م", "team1": "كندا 🇨🇦", "team2": "بيرو 🇵🇪"},
    {"id": "m4", "date": "السبت 13/06/2026 - 04:00 ص", "team1": "أمريكا 🇺🇸", "team2": "باراغواي 🇵🇾"},
    {"id": "m5", "date": "السبت 13/06/2026 - 10:00 م", "team1": "سويسرا 🇨🇭", "team2": "قطر 🇶🇦"},
    {"id": "m6", "date": "الأحد 14/06/2026 - 01:00 ص", "team1": "البرازيل 🇧🇷", "team2": "المغرب 🇲🇦"},
    {"id": "m7", "date": "الأحد 14/06/2026 - 04:00 ص", "team1": "هايتي 🇭🇹", "team2": "اسكتلندا 🏴󠁧󠁢󠁳🇪"}, # علم اسكتلندا مضبوط
    {"id": "m8", "date": "الأحد 14/06/2026 - 07:00 ص", "team1": "أستراليا 🇦🇺", "team2": "ويلز 🏴󠁧󠁢󠁷󠁬󠁳󠁿"},
    {"id": "m9", "date": "الأحد 14/06/2026 - 08:00 م", "team1": "ألمانيا 🇩🇪", "team2": "كوراساو 🇨🇼"},
    {"id": "m10", "date": "الأحد 14/06/2026 - 11:00 م", "team1": "هولندا 🇳🇱", "team2": "اليابان 🇯🇵"},
    {"id": "m11", "date": "الاثنين 15/06/2026 - 01:00 ص", "team1": "إسبانيا 🇪🇸", "team2": "الرأس الأخضر 🇨🇻"},
    {"id": "m12", "date": "الاثنين 15/06/2026 - 02:00 ص", "team1": "ساحل العاج 🇨🇮", "team2": "الإكوادور 🇪🇨"},
    {"id": "m13", "date": "الاثنين 15/06/2026 - 05:00 ص", "team1": "بولندا 🇵🇱", "team2": "تونس 🇹🇳"},
    {"id": "m14", "date": "الاثنين 15/06/2026 - 10:00 م", "team1": "بلجيكا 🇧🇪", "team2": "مصر 🇪🇬"},
    {"id": "m15", "date": "الثلاثاء 16/06/2026 - 01:00 ص (فجراً)", "team1": "السعودية 🇸🇦", "team2": "أوروغواي 🇺🇾"},
    {"id": "m16", "date": "الثلاثاء 16/06/2026 - 04:00 ص", "team1": "إيران 🇮🇷", "team2": "نيوزيلندا 🇳🇿"},
    {"id": "m17", "date": "الثلاثاء 16/06/2026 - 10:00 م", "team1": "فرنسا 🇫🇷", "team2": "السنغال 🇸🇳"},
    {"id": "m18", "date": "الأربعاء 17/06/2026 - 01:00 ص", "team1": "تشيلي 🇨🇱", "team2": "النرويج 🇳🇴"},
    {"id": "m19", "date": "الأربعاء 17/06/2026 - 04:00 ص", "team1": "الأرجنتين 🇦🇷", "team2": "الجزائر 🇩🇿"},
    {"id": "m20", "date": "الأربعاء 17/06/2026 - 07:00 ص", "team1": "النمسا 🇦🇹", "team2": "الأردن 🇯🇴"},
    {"id": "m21", "date": "الأربعاء 17/06/2026 - 08:00 م", "team1": "البرتغال 🇵🇹", "team2": "غانا 🇬🇭"},
    {"id": "m22", "date": "الأربعاء 17/06/2026 - 11:00 م", "team1": "إنجلترا 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "team2": "كرواتيا 🇭🇷"},
    {"id": "m23", "date": "الخميس 18/06/2026 - 02:00 ص", "team1": "الكاميرون 🇨🇲", "team2": "بنما 🇵🇦"},
    {"id": "m24", "date": "الخميس 18/06/2026 - 05:00 ص", "team1": "أوزبكستان 🇺🇿", "team2": "كولومبيا 🇨🇴"}
]

for match in matches_round_1:
    with st.container():
        st.markdown(f"""
            <div class="match-card">
                <b style='color: #64748B;'>🗓️ {match['date']}</b><br>
                <span style='font-size:18px; font-weight: bold;'>{match['team1']} <span style='color: #EF4444;'>VS</span> {match['team2']}</span>
            </div>
        """, unsafe_allow_html=True)
        
        options = [f"فوز {match['team1']}", "تعادل 🤝", f"فوز {match['team2']}"]
        choice = st.radio(f"توقعك:", options, key=f"radio_{match['id']}")
        
        if st.button(f"💾 حفظ التوقع", key=f"btn_{match['id']}"):
            if user_name and user_code:
                st.success(f"✔️ حفظنا توقعك يا بطل!")
            else:
                st.error("⚠️ اكتب اسمك ورمزك فوق.")
        st.write("---")

# 5. قسم الشروط والقوانين (مفتوح دائماً في الأسفل)
st.markdown("""
    <div class="rules-box">
        <h3 style='color: #1E3A8A; text-align: center;'>📜 قوانين المسابقة والجوائز</h3>
        <hr>
        <h4 style='color: #10B981;'>🎁 الجوائز المعتمدة:</h4>
        <ul>
            <li><b>🥇 المركز الأول:</b> هدية قيمة وخاصة تليق بالبطل!</li>
            <li><b>🥈 المركز الثاني:</b> هدية بسيطة وترضية للمنافس.</li>
            <li><b>🥉 المركز الثالث:</b> هدية ترضية لطيفة.</li>
        </ul>
        <hr>
        <h4>1️⃣ نظام النقاط:</h4>
        <ul>
            <li><b>توقع المباراة:</b> (نقطة واحدة) لكل توقع صحيح لمسار المباراة.</li>
            <li><b>التوقع الذهبي:</b> (10 نقاط) لكل طرف نهائي صحيح + (20 نقطة) لتوقع البطل الصحيح.</li>
        </ul>
        <hr>
        <h4>2️⃣ نظام القفل:</h4>
        <ul>
            <li><b>المباريات:</b> يقفل التوقع تلقائياً عند صافرة بداية كل مباراة.</li>
            <li><b>التوقع الذهبي:</b> <span class='red-text'>يقفل نهائياً بعد انتهاء مباريات الجولة الأولى.</span></li>
        </ul>
    </div>
""", unsafe_allow_html=True)
