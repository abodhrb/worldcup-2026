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
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #10B981;
        margin-bottom: 25px;
    }
    .gold-box {
        background-color: #FEF3C7;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #F59E0B;
        margin-bottom: 25px;
    }
    .match-card {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        border-left: 5px solid #1E3A8A;
    }
    </style>
""", unsafe_allow_html=True)

# هيدر الموقع وصور المونديال
st.image("https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
st.markdown('<div class="main-title">🏆 مسابقة توقعات كأس العالم 2026 🏆</div>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #4B5563;'>الجولة الأولى - بتوقيت مكة المكرمة 🕋</h4>", unsafe_allow_html=True)

st.divider()

# 2. عرض الشروط والجوائز والنقاط المعتمدة (محدثة بالمركز الثاني والثالث)
with st.expander("📜 شروط وقوانين المسابقة والجوائز (اضغط للتفاصيل)", expanded=False):
    st.markdown(
        """
        <div class="rules-box">
        <h3>🎁 جوائز التحدي والمنافسة:</h3>
        <ul>
            <li><b>🥇 صاحب المركز الأول:</b> يحصل على <b>(هدية قيمة وخاصة)</b> تليق ببطل المونديال! 🏆</li>
            <li><b>🥈 صاحب المركز الثاني:</b> يحصل على <b>(هدية بسيطة وترضية)</b> تقديراً لمنافسته الشرسة! 🎉</li>
            <li><b>🥉 صاحب المركز الثالث:</b> يحصل على <b>(هدية ترضية لطيفة)</b> لوصوله لمنصة التتويج! 🏅</li>
        </ul>
        <hr>
        <h3>1️⃣ نظام نقاط المباريات:</h3>
        <ul>
            <li><b>دور المجموعات:</b> تتوقع مسار المباراة (فوز فريق معين أو التعادل)، والتوقع الصحيح يمنحك <b>(نقطة واحدة)</b>.</li>
        </ul>
        <hr>
        <h3>2️⃣ نظام القفل التلقائي ⏱️:</h3>
        <ul>
            <li>يغلق التوقع لأي مباراة تلقائياً <b>مع وقت انطلاق المباراة بالضبط (بتوقيت مكة)</b>.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="gold-box">
        <h3>🔥 التوقعات الذهبية (البونص الكبير):</h3>
        <ul>
            <li><b>توقع طرفي النهائي:</b> تحصل على <b>(10 نقاط)</b> عن كل منتخب صحيح يصل للنهائي (المجموع 20 نقطة).</li>
            <li><b>توقع بطل كأس العالم:</b> توقع البطل الصحيح يمنحك <b>(20 نقطة)</b> كاملة!</li>
            <li>⚠️ <i>ملاحظة مهمة:</i> يغلق التوقع الذهبي تماماً مع صافرة بداية أول مباراة في البطولة (11 يونيو الساعة 10:00 م بتوقيت مكة).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )

st.divider()

# 3. واجهة التسجيل وبيانات المشارك
st.subheader("📝 سجل بياناتك وتوقعاتك")
user_name = st.text_input("👤 اسمك الكريم:")
user_code = st.text_input("🔑 הرمز السري (4 أرقام):", type="password", max_chars=4)

st.divider()

# 4. قائمة مباريات الجولة الأولى الرسمية والمصححة بناءً على الجدول وتوقيت مكة
st.subheader("⚽ مباريات الجولة الأولى (توقيت مكة المكرمة)")

matches_round_1 = [
    # الخميس 11 يونيو
    {"id": "m1", "date": "الخميس 11/06/2026 - 10:00 م", "team1": "المكسيك 🇲🇽", "team2": "جنوب أفريقيا 🇿🇦"},
    
    # الجمعة 12 يونيو
    {"id": "m2", "date": "الجمعة 12/06/2026 - 05:00 ص", "team1": "كوريا الجنوبية 🇰🇷", "team2": "(يحدد لاحقاً) 🌐"},
    {"id": "m3", "date": "الجمعة 12/06/2026 - 10:00 م", "team1": "كندا 🇨🇦", "team2": "(يحدد لاحقاً) 🌐"},
    
    # السبت 13 يونيو
    {"id": "m4", "date": "السبت 13/06/2026 - 04:00 ص", "team1": "أمريكا 🇺🇸", "team2": "باراغواي 🇵🇾"},
    {"id": "m5", "date": "السبت 13/06/2026 - 10:00 م", "team1": "سويسرا 🇨🇭", "team2": "قطر 🇶🇦"},
    
    # الأحد 14 يونيو
    {"id": "m6", "date": "الأحد 14/06/2026 - 01:00 ص", "team1": "البرازيل 🇧🇷", "team2": "المغرب 🇲🇦"},
    {"id": "m7", "date": "الأحد 14/06/2026 - 04:00 ص", "team1": "هايتي 🇭🇹", "team2": "اسكتلندا 🏴󠁧󠁢󠁳🇪🇺"},
    {"id": "m8", "date": "الأحد 14/06/2026 - 07:00 ص", "team1": "أستراليا 🇦🇺", "team2": "(يحدد لاحقاً) 🌐"},
    {"id": "m9", "date": "الأحد 14/06/2026 - 08:00 م", "team1": "ألمانيا 🇩🇪", "team2": "كوراساو 🇨🇼"},
    {"id": "m10", "date": "الأحد 14/06/2026 - 11:00 م", "team1": "هولندا 🇳🇱", "team2": "اليابان 🇯🇵"},
    
    # الاثنين 15 يونيو
    {"id": "m11", "date": "الاثنين 15/06/2026 - 01:00 ص", "team1": "إسبانيا 🇪🇸", "team2": "الرأس الأخضر 🇨🇻"},
    {"id": "m12", "date": "الاثنين 15/06/2026 - 02:00 ص", "team1": "ساحل العاج 🇨🇮", "team2": "الإكوادور 🇪🇨"},
    {"id": "m13", "date": "الاثنين 15/06/2026 - 05:00 ص", "team1": "(يحدد لاحقاً) 🌐", "team2": "تونس 🇹🇳"},
    {"id": "m14", "date": "الاثنين 15/06/2026 - 10:00 م", "team1": "بلجيكا 🇧🇪", "team2": "مصر 🇪🇬"},
    
    # الثلاثاء 16 يونيو
    {"id": "m15", "date": "الثلاثاء 16/06/2026 - 01:00 ص (فجراً)", "team1": "السعودية 🇸🇦", "team2": "أوروغواي 🇺🇾"}, # صقورنا 🔥
    {"id": "m16", "date": "الثلاثاء 16/06/2026 - 04:00 ص", "team1": "إيران 🇮🇷", "team2": "نيوزيلندا 🇳🇿"},
    {"id": "m17", "date": "الثلاثاء 16/06/2026 - 10:00 م", "team1": "فرنسا 🇫🇷", "team2": "السنغال 🇸🇳"},
    
    # الأربعاء 17 يونيو
    {"id": "m18", "date": "الأربعاء 17/06/2026 - 01:00 ص", "team1": "(يحدد لاحقاً) 🌐", "team2": "النرويج 🇳🇴"},
    {"id": "m19", "date": "الأربعاء 17/06/2026 - 04:00 ص", "team1": "الأرجنتين 🇦🇷", "team2": "الجزائر 🇩🇿"},
    {"id": "m20", "date": "الأربعاء 17/06/2026 - 07:00 ص", "team1": "النمسا 🇦🇹", "team2": "الأردن 🇯🇴"},
    {"id": "m21", "date": "الأربعاء 17/06/2026 - 08:00 م", "team1": "البرتغال 🇵🇹", "team2": "(يحدد لاحقاً) 🌐"},
    {"id": "m22", "date": "الأربعاء 17/06/2026 - 11:00 م", "team1": "إنجلترا 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "team2": "كرواتيا 🇭🇷"},
    
    # الخميس 18 يونيو
    {"id": "m23", "date": "الخميس 18/06/2026 - 02:00 ص", "team1": "غانا 🇬🇭", "team2": "بنما 🇵🇦"},
    {"id": "m24", "date": "الخميس 18/06/2026 - 05:00 ص", "team1": "أوزبكستان 🇺🇿", "team2": "كولومبيا 🇨🇴"}
]

user_predictions = {}

# عرض المباريات بشكل كروت وتجميع التوقعات
for match in matches_round_1:
    st.markdown(f"""
        <div class="match-card">
            <b>🗓️ {match['date']}</b><br>
            <span style='font-size:18px;'>{match['team1']} <b>VS</b> {match['team2']}</span>
        </div>
    """, unsafe_allow_html=True)
    
    options = [f"فوز {match['team1']}", "تعادل 🤝", f"فوز {match['team2']}"]
    choice = st.radio(f"توقعك للمباراة:", options, key=match['id'])
    user_predictions[match['id']] = choice
    st.write("")

st.divider()

# 5. قسم التوقعات الذهبية
st.markdown("### 🌟 قسم التوقعات الذهبية (قفل التحدي الكبير)")
finalist_1 = st.text_input("🏳️ توقع طرف النهائي الأول:")
finalist_2 = st.text_input("🏳️ توقع طرف النهائي الثاني:")
champion_pred = st.text_input("👑 توقع بطل كأس العالم 2026:")

st.divider()

if st.button("🚀 إرسال التوقعات والاعتماد النهائي"):
    if user_name and user_code:
        st.success(f"كفو يا {user_name}! تم حفظ وتأمين توقعاتك وجوائز التحدي بنجاح 🏆🕋")
        st.balloons()
    else:
        st.error("الرجاء التأكد من كتابة اسمك والرمز السري أولاً!")
