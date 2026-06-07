import streamlit as st
import pandas as pd
from datetime import datetime, timezone

# إعدادات الصفحة والعنوان
st.set_page_config(page_title="مسابقة كأس العالم 2026", page_icon="⚽", layout="centered")

# رابط الجدول الخاص بك (صيغة التصدير التلقائي لقرائته برمجياً)
SHEET_ID = "1-iWn7SyOML2bGPTIIAQj2nZm7Cx7zDMwAP8XV_gcGP4"
URL_USERS = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=%D8%A7%D9%84%D9%85%D8%B4%D8%AA%D8%B1%D9%83%D9%8A%D9%86"
URL_MATCHES = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA"

st.title("🏆 مسابقة توقعات كأس العالم 2026")
st.write("أهلاً بك في منصة التحدي الخاصة بالأصدقاء!")

# دالة لقراءة البيانات من قوقل شيتس
def load_data(url):
    try:
        return pd.read_csv(url)
    except:
        return pd.DataFrame()

df_users = load_data(URL_USERS)
df_matches = load_data(URL_MATCHES)

st.success("🟢 النظام الآن متصل بجداول قوقل شيتس الخاصة بك بنجاح!")
st.info("الخطوة القادمة هي إطلاق الموقع على منصة Streamlit لتبدأ الطقطقة والحماس بين الشباب!")
