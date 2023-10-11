import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick
#%matplotlib inline


@st.cache_data

def load_dataset2():
    t_data=pd.read_csv("/Users/apple/Downloads/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    t_data.TotalCharges=pd.to_numeric(t_data.TotalCharges, errors='coerce')
    t_data.dropna(how='any', inplace=True)
    labels=["{0}-{1}".format(i,i+11) for i in range(1, t_data['tenure'].max(), 12)]
    t_data["tenure_grp"]=pd.cut(t_data.tenure, range(1, 80, 12), right=False, labels=labels)
    t_data.drop(["customerID","tenure"], axis=1, inplace=True)
    t_data["Churn"]=t_data["Churn"].map({"Yes":1, "No":0 })
    return t_data

df1=load_dataset2()

def load_dataset():
    t_data=pd.read_csv("/Users/apple/Downloads/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    t_data.TotalCharges=pd.to_numeric(t_data.TotalCharges, errors='coerce')
    t_data.dropna(how='any', inplace=True)
    labels=["{0}-{1}".format(i,i+11) for i in range(1, t_data['tenure'].max(), 12)]
    t_data["tenure_grp"]=pd.cut(t_data.tenure, range(1, 80, 12), right=False, labels=labels)
    t_data.drop(["customerID","tenure"], axis=1, inplace=True)
    t_data["Churn"]=t_data["Churn"].map({"Yes":1, "No":0 })
    t_data_dummies=pd.get_dummies(t_data)
    return t_data_dummies

df = load_dataset()


def show_explore_page():
    st.title("Explore Customer Churn")
    st.write("""
             #### Telco Customer Charges Survey""")
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    

    def kdeplot(feature):
        plt.figure(figsize=(9, 4))
        plt.title("Density Plot For {}".format(feature))
        ax0 = sns.kdeplot(df[df['Churn'] == 0][feature], color= 'navy', label= 'Churn: No')
        ax1 = sns.kdeplot(df[df['Churn'] == 1][feature], color= 'orange', label= 'Churn: Yes')
        plt.legend()
        
    st.pyplot(kdeplot('MonthlyCharges'))
    st.pyplot(kdeplot('TotalCharges'))

    st.write("""
             #### Services for Customer with Internet""")
    
    cols = ["OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies"]

    df2 = pd.melt(df1[df1["InternetService"] != "No"][cols]).rename({'value': 'Has service'}, axis=1)
    plt.figure(figsize=(15, 5))
    ax = sns.countplot(data=df2, x='variable', hue='Has service')
    ax.set(xlabel='Additional service', ylabel='Num of customers')
    st.pyplot(plt.show())

    plt.figure(figsize=(15, 5))
    df3 = df1[(df1.InternetService != 0) & (df1.Churn == 1)]
    df3 = pd.melt(df3[cols]).rename({'value': 'Has service'}, axis=1)
    ax = sns.countplot(data=df3, x='variable', hue='Has service', hue_order=['No', 'Yes'])
    ax.set(xlabel='Additional service', ylabel='Num of churns')
    st.pyplot(plt.show())

    
    