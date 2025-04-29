import requests
import joblib
import os
import streamlit as st
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from numerize import numerize


def prediksi():
    # Gunakan model
    data_actor = pd.read_csv('data.csv', sep=',')

    st.write('\n')
    st.write('\n')
    st.write('\n')

    imdb_joblib = joblib.load('imdb_joblib')

    with st.form("Prediction Form"): 
        st.title('Customer Churn Prediction')
        st.write('\n')
        st.write('\n')

        st.write('**INFORMASI UMUM**')

        # Gender
        gender = st.radio("Gender", ("Male", "Female"))
        if gender == "Male":
            gender = 1
        else: gender = 0

        # Senior Citizen
        senior_citizen = st.radio("Apakah Anda berusia 65 tahun atau lebih?", ("Ya", "Tidak"))
        if senior_citizen == "Ya":
            senior_citizen = 1
        else: senior_citizen = 0

        # Partner
        partner = st.radio("Apakah Anda memiliki pasangan (menikah)?", ("Ya", "Tidak"))
        if partner == "Ya":
            partner = 1
        else: partner = 0

        # Dependent
        dependent = st.radio("Apakah Anda tinggal bersama tanggungan (anak, orang tua, kakek-nenek, dll)?", ("Ya", "Tidak"))
        if dependent == "Ya":
            dependent = 1
        else: dependent = 0

        # Tenure
        tenure = st.number_input("Berapa bulan Anda telah menjadi pelanggan kami?", min_value=0, max_value=240, value=0)
        tenure = pd.to_numeric(tenure)

        st.write('\n')
        st.write('\n')

        st.write('**LANGGANAN LAYANAN**')

        # Phone Service
        phone_service = st.radio("Apakah Anda berlangganan layanan telepon rumah dari kami?", ("Ya", "Tidak"))
        if phone_service == "Ya":
            phone_service = 1
        else: phone_service = 0

        # Multiple Lines
        multiple_lines = st.radio("Apakah Anda berlangganan lebih dari satu saluran telepon?", ("Ya", "Tidak"))
        if multiple_lines == "Ya":
            multiple_lines = 1
        else: multiple_lines = 0

        # Internet Service
        internet_service = st.radio("Apa layanan internet yang anda gunakan?", ("DSL", "Fiber Optic", "No"))
        if internet_service == "DSL":
            InternetService_FiberOptic = 0
            InternetService_No = 0
        elif internet_service == "Fiber Optic":
            InternetService_FiberOptic = 1
            InternetService_No = 0
        else:
            InternetService_FiberOptic = 0
            InternetService_No = 1
        
        # Online Security
        online_security = st.radio("Apakah Anda berlangganan layanan keamanan online tambahan?", ("Ya", "Tidak"))
        if online_security == "Ya":
            online_security = 1
        else: online_security = 0

        # Online Backup
        online_backup = st.radio("Apakah Anda berlangganan layanan backup online tambahan?", ("Ya", "Tidak"))
        if online_backup == "Ya":
            online_backup = 1
        else: online_backup = 0

        # Device Protection
        device_protection = st.radio("Apakah Anda berlangganan perlindungan perangkat untuk peralatan internet Anda?", ("Ya", "Tidak"))
        if device_protection == "Ya":
            device_protection = 1
        else: device_protection = 0

        # Tech Support
        tech_support = st.radio("Apakah Anda berlangganan paket dukungan teknis tambahan?", ("Ya", "Tidak"))
        if tech_support == "Ya":
            tech_support = 1
        else: tech_support = 0

        # Streaming TV
        streaming_tv = st.radio("Apakah Anda menggunakan layanan internet kami untuk streaming TV?", ("Ya", "Tidak"))
        if streaming_tv == "Ya":
            streaming_tv = 1
        else: streaming_tv = 0

        # Streaming Film
        streaming_film = st.radio("Apakah Anda menggunakan layanan internet kami untuk streaming film?", ("Ya", "Tidak"))
        if streaming_film == "Ya":
            streaming_film = 1
        else: streaming_film = 0

        st.write('\n')
        st.write('\n')

        st.write('**PAYMENT INFO**')

        # Contract
        contract = st.radio("Apa tipe kontrak Anda saat ini?", ("Month-to-Month", "One Year", "Two Year"))
        if contract == "Month-to-Month":
            Contract_OneYear = 0
            Contract_TwoYear = 0
        elif contract == "One Year":
            Contract_OneYear = 1
            Contract_TwoYear = 0
        else:
            Contract_OneYear = 0
            Contract_TwoYear = 1
        
        # Paperless Billing
        paperless_billing = st.radio("Apakah Anda menggunakan metode tagihan tanpa kertas?", ("Ya", "Tidak"))
        if paperless_billing == "Ya":
            paperless_billing = 1
        else: paperless_billing = 0

        # Payment Method
        payment_method = st.radio("Bagaimana Anda membayar tagihan?", ("Bank Transfer (Automatic)", "Credit Card (Automatic)", "Electronic Check", "Mailed Check"))
        if payment_method == "Bank transfer (automatic)":
            PaymentMethod_CreditCardAutomatic = 0
            PaymentMethod_ElectronicCheck = 0
            PaymentMethod_MailedCheck = 0
        elif payment_method == "Credit Card (Automatic)":
            PaymentMethod_CreditCardAutomatic = 1
            PaymentMethod_ElectronicCheck = 0
            PaymentMethod_MailedCheck = 0
        elif payment_method == "Electronic check":
            PaymentMethod_CreditCardAutomatic = 0
            PaymentMethod_ElectronicCheck = 1
            PaymentMethod_MailedCheck = 0
        else:
            PaymentMethod_CreditCardAutomatic = 0
            PaymentMethod_ElectronicCheck = 0
            PaymentMethod_MailedCheck = 1
        
        # Monthly Charges
        monthly_charges = st.number_input("Berapa total biaya bulanan Anda saat ini?", min_value=0.0, max_value=99999999.0, value=0.0)
        monthly_charges = pd.to_numeric(monthly_charges)

        # Total Charges
        total_charges = st.number_input("Berapa total biaya Anda hingga saat ini?", min_value=0.0, max_value=99999999.0, value=0.0)
        total_charges = pd.to_numeric(total_charges)


        data_predict = {'SeniorCitizen': senior_citizen,
                        'Partner': partner,
                        'Dependents': dependent,
                        'tenure': tenure,
                        'PhoneService': phone_service,
                        'MultipleLines': multiple_lines,
                        'OnlineSecurity': online_security,
                        'OnlineBackup': online_backup,
                        'DeviceProtection': device_protection,
                        'TechSupport': tech_support,
                        'StreamingTV': streaming_tv,
                        'StreamingMovies': streaming_film,
                        'PaperlessBilling': paperless_billing,
                        'MonthlyCharges': monthly_charges,
                        'TotalCharges': total_charges,
                        'GenderMale': gender,
                        'InternetService_FiberOptic': InternetService_FiberOptic,
                        'InternetService_No': InternetService_No,
                        'Contract_OneYear': Contract_OneYear,
                        'Contract_TwoYear': Contract_TwoYear,
                        'PaymentMethod_CreditCardAutomatic': PaymentMethod_CreditCardAutomatic,
                        'PaymentMethod_ElectronicCheck': PaymentMethod_ElectronicCheck,
                        'PaymentMethod_MailedCheck': PaymentMethod_MailedCheck}
        data_predict= pd.DataFrame(data_predict, index=[0])

        submitted = st.form_submit_button("Predict")
        if submitted:
            res1, res2, res3 = st.columns(3)
            with res1:
                predict = imdb_joblib.predict(data_predict)
                label = "Churn" if predict[0] == 1 else "Tidak Churn"
                st.write('**Customer Churn Prediction :**')
                st.info(label)
