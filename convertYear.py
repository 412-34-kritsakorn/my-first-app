import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. ค.ศ.")

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง",value=2569)
ce_yeae=bh_year-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
