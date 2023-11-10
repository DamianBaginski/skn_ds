from typing import NamedTuple


class Columns(NamedTuple):
    id_col = 'customerID'
    gender_col = 'gender'
    senior_col = 'SeniorCitizen'
    partner_col = 'Partner'
    dependents_col = 'Dependents'
    tenure_col = 'tenure'
    phone_service_col = 'PhoneService'
    multiple_lines_col = 'MultipleLines'
    internet_col = 'InternetService'
    online_sec_col = 'OnlineSecurity'
    online_backup_col = 'OnlineBackup'
    device_prot_col = 'DeviceProtection'
    tech_support_col = 'TechSupport'
    streaming_tv_col = 'StreamingTV'
    streaming_movies_col = 'StreamingMovies'
    contract_col = 'Contract'
    paperless_billing_col = 'PaperlessBilling'
    payment_method_col = 'PaymentMethod'
    monthly_charges_col = 'MonthlyCharges'
    total_charges_col = 'TotalCharges'
    target_col = 'Churn'
    has_internet_col = 'has_internet'
    automatic_pay_col = 'automatic_pay'
    streaming_col = 'streaming'
    support_col = 'has_support'

    values_to_change = {'Yes': 1, 'Male': 1, 'Female': 0, 'No': 0, 'No internet service': None, 'No phone service': None}
    cols_to_encode = [internet_col, payment_method_col, contract_col]