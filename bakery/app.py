import streamlit as st

col1, col2 = st.columns(2)

st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background-color: #d4a373;
    }

    /* Titles */
    h1, h2, h3 {
        color: #000000 !important;
    }

    /* Normal text */
    p {
        color: #000000 !important;
    }

    /* Cake pop text (markdown text fixes) */
    .stMarkdown, .stMarkdown p {
        color: #000000 !important;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #f7e6c4 !important;
        color: #000000 !important;
        border-radius: 8px;
        border: 1px solid #d9c7a3;
    }

    div.stButton > button:hover {
        background-color: #f2d9a6 !important;
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
with col1:
    st.image("pop.jpg", width=250)
    st.subheader('red velvet cake pop')
    st.write('price: $3.00')


with col2:
    st.image('coffee.webp', width=250)
    st.subheader('macciato')
    st.write('price: $3.00')


rating = st.slider('rate our cake pops')
if rating >=10:
    st.balloons()
    st.success('Wow! You loved it')
else:
    st.write("we'll make it better next time")

