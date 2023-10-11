import streamlit as st
import pickle
import numpy as np
import pandas as pd
import json
from streamlit_lottie import st_lottie

# create load funtion for model
def load_model():
    with open('model.rfc', 'rb') as file:
        model=pickle.load(file)
    return model

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
# load model
model=load_model()

# load data for packing inputs
df1 = pd.read_csv("telco_datapack.csv")

# create function for predict page 
def show_predict_page():
    #st.title("Telco Customer Churn Prediction")

    #st.write("""### Information required for predicting churn""")


    # find more emojis at: streamlit emoji
    # st.set_page_config(page_title="Telco Churn", page_icon=":telephone_receiver:", layout="wide")
    # st.title("Telco Customer Churn", ":telephone_receiver:")
    st.subheader("Welcome, User :telephone_receiver:")
    st.title("Telco Customer Churn")
    
     # create divider ----
    st.write("___")


    # .....load asset lottiefiles.....
    lottie_file = load_lottiefile("/Users/apple/Downloads/analysis lottie.json")

    # .....Header section....
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write(
                "Customer churn is a significant concern for businesses, as it can lead to decreased revenue and profitability. It is more cost-effective to retain existing customers than acquire new ones. Predicting customer churn allows companies to implement targeted strategies to retain valuable customers, such as offering discounts, improving customer service, or personalizing marketing campaigns.")
           

            gender=("Male", "Female")
            SeniorCitizen=("0", "1")
            Partner=("Yes", "No")	
            Dependents=("Yes", "No")	
            #tenure=("")	
            PhoneService=("Yes", "No")	
            MultipleLines=("Yes", "No", "No phone service")
            InternetService=("Fiber optic", "DSL", "No")	
            OnlineSecurity=("Yes", "No")
            OnlineBackup=("Yes", "No")
            DeviceProtection=("Yes", "No")
            TechSupport=("Yes", "No")
            StreamingTV=("Yes", "No")
            StreamingMovies=("Yes", "No")
            Contract=("Month-to-month", "One year", "Two year")
            PaperlessBilling=("Yes", "No")
            PaymentMethod=("Bank transfer (automatic)", "Electronic check", "Mailed check", "Credit card (automatic)")
            #MonthlyCharges=("")
            #TotalCharges=("")

            tenures=st.slider("Tenure", 0, 80, 1)
            monthly_charges=st.number_input("Monthly Charges", min_value=0, max_value=1000)
            total_charges=st.number_input("Total Charges", min_value=0, max_value=10000)
            genders=st.selectbox("Gender", gender)
            seniorcitizen=st.selectbox("Senior Citizen", SeniorCitizen)
            partner=st.selectbox("Partner", Partner)
            dependents=st.selectbox("Dependents", Dependents)
            phone_service=st.selectbox("Phone Service", PhoneService)
            multiple_lines=st.selectbox("Multiple Lines", MultipleLines)
            internet_service=st.selectbox("Internet Service", InternetService)
            online_security=st.selectbox("Security", OnlineSecurity)
            online_backup=st.selectbox("Backup", OnlineBackup)
            device_protection=st.selectbox("Device Protection", DeviceProtection)
            tech_support=st.selectbox("Tech Support", TechSupport)
            streamingtv=st.selectbox("StreamingTv", StreamingTV)
            streamingmovies=st.selectbox("StreamingMovies", StreamingMovies)
            contract=st.selectbox("Contract", Contract)
            paperlessbilling=st.selectbox("Paperless Billing", PaperlessBilling)
            paymentmethod=st.selectbox("Payment Method", PaymentMethod)

            ok = st.button("Predict Churn")
            if ok:
                data=[[tenures, monthly_charges, total_charges, genders, seniorcitizen, partner, dependents, phone_service, multiple_lines,
                       internet_service, online_security, online_backup, device_protection, tech_support, streamingtv, streamingmovies, 
                       contract, paperlessbilling, paymentmethod]]
                df2=pd.DataFrame(data, columns = [
                    'tenure', 'MonthlyCharges', 'TotalCharges', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
                    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                    'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',])
                
                # join both df1 and df2(inputs) to create new dataframe
                df=pd.concat([df1, df2], ignore_index=True)

                # group tenure into bins of 12months
                labels=["{0}-{1}".format(i,i+11) for i in range(1, df['tenure'].max(), 12)]
                df["tenure_grp"]=pd.cut(df.tenure, range(1, 80, 12), right=False, labels=labels)

                # drop tenure
                df.drop(["tenure", "Unnamed: 0"], axis=1, inplace=True)

                # convert total charges col to numeric
                df.TotalCharges=pd.to_numeric(df.TotalCharges, errors='coerce')
                df.SeniorCitizen=pd.to_numeric(df.SeniorCitizen, errors='coerce')
                df=df.dropna()

                # get dummies
                df_dummies=pd.get_dummies(df)
                
                pred = model.predict(df_dummies.tail(1))
                probability=model.predict_proba(df_dummies.tail(1))[:,1]

                if pred == 1:
                    st.subheader(f"This customer is likely to churn!!!")
                    st.subheader(f"Confidence: {probability * 100}%")
                else:
                    st.subheader(f"This customer is likely to continue!!!")
                    st.subheader(f"Confidence: {probability * 100}%")


        with right_column:
            st_lottie(
                lottie_file, speed=1, reverse=False, loop=True, quality="high", height=None, width=None, key=None
            )
