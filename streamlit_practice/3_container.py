import streamlit as st
con1 = st.container(border=True)
con2 = st.container(border=True)
with con1 :
    btn = st.button("눌러보세요")
    if btn:
        st.markdown("아무것도 안 일어나요")

with con2 :
    btn = st.button("누르면 큰일나요!")
    if btn:
        st.markdown("큰일난다고 했잖아요")