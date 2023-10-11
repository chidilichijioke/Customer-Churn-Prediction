import json
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# find more emojis at: streamlit emoji
st.set_page_config(page_title="Telco Churn", page_icon=":telephone_receiver:", layout="wide")

# .....load asset lottiefiles.....
lottie_file = load_lottiefile("/Users/apple/Downloads/analysis lottie.json")

# .....Header section....
with st.container():
    st.subheader("Welcome, User :telephone_receiver:")
    st.title("Telco Customer Churn")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            "Customer churn is a significant concern for businesses, as it can lead to decreased revenue and profitability. It is more cost-effective to retain existing customers than acquire new ones. Predicting customer churn allows companies to implement targeted strategies to retain valuable customers, such as offering discounts, improving customer service, or personalizing marketing campaigns.")
        # create divider ----
        st.write("___")

    with right_column:
        st_lottie(
            lottie_file, speed=1, reverse=False, loop=True, quality="high", height=None, width=None, key=None
        )
