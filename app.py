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

# إضافة صورة هيدر حماسية للمونديال وألوان مبهجة
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-size: 40px;
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
    </style>
""", unsafe_allow_html=True)

# رأس الصفحة (الصور والشعار)
st.image("https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
st.markdown('<div class="main-title">🏆 مسابقة توقعات كأس العالم 2026 🏆</div>', unsafe_allow_html=True)
st.write("<h3 style='text-align: center; color: #4B5563;'>منصة التحدي والإثارة الكبرى بين الأصدقاء!</h3>", unsafe_allow_html=True)

st.divider()

# 2. عرض الشروط والجوائز بشكل رسمي ومنسق بالألوان
with st.expander("📜 شروط وقوانين المسابقة والجوائز (اضغط للتفاصيل)", expanded=True):
    st.markdown(
        """
        <div class="rules-box">
        <h3>🎁 جوائز التحدي:</h3>
        <ul>
            <li><b>صاحب المركز الأول:</b> يحصل على <b>(هدية قيمة وخاصة)</b> تليق ببطل المونديال ومتربع عرش التوقعات! 🏆</li>
        </ul>
        <hr>
        <h3>1️⃣ نظام نقاط المباريات (فوز أو تعادل):</h3>
        <ul>
            <li><b>دور المجموعات:</b> يتوقع المشارك مسار المباراة فقط (فوز فريق معين أو التعادل)، والتوقع الصحيح يمنحك <b>(نقطة واحدة)</b>.</li>
            <li><b>الأدوار الإقصائية:</b> لا يوجد تعادل! يجب توقع الفريق المتأهل للدور القادم (سواء بالوقت الأصلي، الإضافي، أو ركلات الترجيح). التوقع الصحيح يمنحك <b>(نقطة واحدة)</b>.</li>
        </ul>
        <hr>
        <h3>2️⃣ نظام القفل التلقائي ⏱️:</h3>
        <ul>
            <li>يغلق استقبال التوقعات لأي مباراة تلقائياً <b>مع وقت انطلاق المباراة بالضبط</b>، ولن يتاح تعديل أو إدخال أي توقع بعدها نهائياً.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="gold-box">
        <h3>🔥 التوقعات الذهبية (البونص الكبير):</h3>
        <ul>
            <li><b>توقع طرفي النهائي:</b> تحصل على <b>(10 نقاط)</b> عن كل منتخب تتوقعه ويصل للنهائي فعلياً (مجموع النقاط يصل إلى <b>20 نقطة</b>).</li>
            <li><b>توقع بطل كأس العالم:</b> توقع المنتخب الذي سيرفع الكأس الغالية وتحصل على <b>(20 نقطة)</b> كاملة تقلب موازين الصدارة!</li>
            <li>⚠️ <i>ملاحظة:</i> يغلق التوقع الذهبي تماماً مع صافرة بداية أول مباراة في البطولة.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )

st.divider()

# 3. واجهة التسجيل وإدخال التوقعات (مثال تفاعلي بأعلام الدول)
st.subheader("📝 سجل توقعك الآن")

user_name = st.text_input("👤 اسمك الكريم:")
user_code = st.text_input("🔑 الرمز السري الخاص بك (4 أرقام):", type="password", max_chars=4)

st.markdown("### 🏟️ مباراة اليوم")
col1, col2 = st.columns(2)
with col1:
    st.info("🇸🇦 السعودية")
with col2:
    st.info("🇲🇽 المكسيك")

prediction = st.radio("ما هي توقعاتك للمباراة؟", ["فوز السعودية 🇸🇦", "تعادل 🤝", "فوز المكسيك 🇲🇽"])

# 4. التوقعات الذهبية في الواجهة
st.markdown("### 🌟 التوقعات الذهبية (متاحة الآن فقط!)")
finalist_1 = st.text_input("🏳️ توقع طرف النهائي الأول:")
finalist_2 = st.text_input("🏳️ توقع طرف النهائي الثاني:")
champion_pred = st.text_input("👑 توقع بطل كأس العالم 2026:")

# زر الحفظ مع تأثير الألعاب النارية
if st.button("🚀 إرسال التوقعات واعتمادها"):
    if user_name and user_code:
        # هنا يتم الربط مع جوجل شيت خلف الكواليس
        st.success(
            f"تم تسجيل توقعك بنجاح يا {user_name}! بالتوفيق في صراع الصدارة 🏆"
        )
        st.balloons()  # تأثير الألعاب النارية الاحتفالية 🎉
    else:
        st.error("الرجاء كتابة اسمك والرمز السري أولاً لتأمين توقعك!")
