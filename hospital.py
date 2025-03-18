import mysql.connector
import pandas as pd
import streamlit as st

mysql = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="city_hospitals")
mycursor = mysql.cursor()

def fetch_and_display(query):
    mycursor.execute(query)
    rows = mycursor.fetchall()
    df = pd.DataFrame(rows)
    st.dataframe(df)

def main_page():
    st.title("Hospital Management System")

    main_menu_option = st.sidebar.selectbox("Select an option:", ["Administration", "Patient Details"])

    if main_menu_option == "Administration":
        administration_page()
    elif main_menu_option == "Patient Details":
        patient_details_page()

def administration_page():
    admin_option = st.sidebar.selectbox("Select an option:", ["Display Details", "Add Doctor Details", "Add Nurse Details", "Add Workers Details", "Update Doctor Detail", "Update Nurse Detail", "Update Worker Detail", "Delete Doctor Detail", "Delete Nurse Detail", "Delete Worker Detail"])

    if admin_option == "Display Details":
        display_details()
    elif admin_option == "Add Doctor Details":
        add_doctor_details()
    elif admin_option == "Add Nurse Details":
        add_nurse_details()
    elif admin_option == "Add Workers Details":
        add_workers_details()
    elif admin_option == "Delete Doctor Detail":
        delete_doctor()
    elif admin_option == "Delete Nurse Detail":
        delete_nurse()
    elif admin_option == "Delete Worker Detail":
        delete_worker()
    elif admin_option == "Update Doctor Detail":
        update_doctor()
    elif admin_option == "Update Nurse Detail":
        update_nurse()
    elif admin_option == "Update Worker Detail":
        update_worker()

def display_details():
    st.subheader("Doctor Details")
    mycursor.execute("select * from doctor_details")
    rows = mycursor.fetchall()
    df1 = pd.DataFrame(rows, columns=["DoctorId", "Name", "Specialization", "Age", "Address", "Contact", "Fees", "MonthlySalary", "PatientId"])
    st.dataframe(df1)
    st.subheader("Nurse Details")
    mycursor.execute("select * from nurse_details")
    rows = mycursor.fetchall()
    df2 = pd.DataFrame(rows, columns=["NurseId", "Name", "Age", "Address", "Contact", "MonthlySalary", "PatientId"])
    st.dataframe(df2)
    st.subheader("Workers Details")
    mycursor.execute("select * from other_workers_details")
    rows = mycursor.fetchall()
    df3 = pd.DataFrame(rows, columns=["WorkerId", "Name", "Age", "Address", "Contact", "MonthlySalary", "PatientId"])
    st.dataframe(df3)

def patient_details_page():
    st.subheader("Patient Details")

    patient_option = st.sidebar.selectbox("Select an option:", ["Show Patients Info", "Add New Patient", "Update Patient Detail","Discharge Summary"])

    if patient_option == "Show Patients Info":
        mycursor.execute("select * from patient_detail")
        rows = mycursor.fetchall()
        df = pd.DataFrame(rows, columns=["PatientId", "Name", "Gender", "Age", "Address", "Contact"])
        st.dataframe(df)
    elif patient_option == "Add New Patient":
        add_new_patient()
    elif patient_option == "Update Patient Detail":
        update_patient()
    elif patient_option == "Discharge Summary":
        discharge_patient()

def update_doctor():
    mycursor.execute("select * from doctor_details")
    rows = mycursor.fetchall()
    df1 = pd.DataFrame(rows, columns=["DoctorId", "Name", "Specialization", "Age", "Address", "Contact", "Fees", "MonthlySalary", "PatientId"])
    st.dataframe(df1)
    st.subheader("Update Doctor Detail")
    id = st.text_input("Doctor ID:")
    name = st.text_input("Doctor's name:")
    spe = st.text_input("Specialization:")
    age = st.text_input("Age:")
    add = st.text_input("Address:")
    cont = st.text_input("Contact Details:")
    fees = st.text_input("Fees:")
    ms = st.text_input("Monthly Salary:")
    pid = st.text_input("Patient Id:")
    if st.button("Update Doctor"):
        mycursor.execute("update doctor_details set name=%s, specialisation=%s, age=%s, address=%s, contact=%s, fees=%s, monthly_salary=%s, patient_id=%s where doctor_id=%s", (name, spe, age, add, cont, fees, ms, pid, id))
        mysql.commit()
        st.success("Doctor details updated successfully")

def update_nurse():
    mycursor.execute("select * from nurse_details")
    rows = mycursor.fetchall()
    df2 = pd.DataFrame(rows, columns=["NurseId", "Name", "Age", "Address", "Contact", "MonthlySalary", "PatientId"])
    st.dataframe(df2)
    st.subheader("Update Nurse Details")
    id = st.text_input("Nurse ID:")
    name = st.text_input("Nurse name:")
    age = st.text_input("Age:")
    add = st.text_input("Address:")
    cont = st.text_input("Contact No:")
    ms = st.text_input("Monthly Salary:")
    pid = st.text_input("Patient Id:")
    if st.button("Update Nurse"):
        mycursor.execute("update nurse_details set name=%s, age=%s, address=%s, contact=%s, monthly_salary=%s, patient_id=%s where nurse_id=%s", (name, age, add, cont, ms, pid, id))
        mysql.commit()
        st.success("Nurse details updated successfully")

def update_worker():
    mycursor.execute("select * from other_workers_details")
    rows = mycursor.fetchall()
    df3 = pd.DataFrame(rows, columns=["WorkerId", "Name", "Age", "Address", "Contact", "MonthlySalary", "PatientId"])
    st.dataframe(df3)
    st.subheader("Update Worker Details")
    id = st.text_input("Worker ID:")
    name = st.text_input("Worker name:")
    age = st.text_input("Age:")
    add = st.text_input("Address:")
    cont = st.text_input("Contact No:")
    ms = st.text_input("Monthly Salary:")
    pid = st.text_input("Patient Id:")
    if st.button("Update Nurse"):
        mycursor.execute("update other_workers_details set name=%s, age=%s, address=%s, contact=%s, monthly_salary=%s, patient_id=%s where other_worker_id=%s", (name, age, add, cont, ms, pid, id))
        mysql.commit()
        st.success("Worker details updated successfully")

def update_patient():
    mycursor.execute("select * from patient_detail")
    rows = mycursor.fetchall()
    df = pd.DataFrame(rows, columns=["PatientId", "Name", "Gender", "Age", "Address", "Contact"])
    st.dataframe(df)
    st.subheader("Update Patient Details")
    id = st.text_input("Patient ID:")
    name = st.text_input("Patient name:")
    sex = st.text_input("Gender:")
    age = st.text_input("Age:")
    address = st.text_input("Address:")
    contact = st.text_input("Contact Details:")
    if st.button("Update Pateint"):
        mycursor.execute("update patient_detail set name=%s, sex=%s, age=%s, address=%s, contact=%s where patient_id=%s", (name, sex, age, address, contact, id))
        mysql.commit()
        st.success("Patient details updated successfully")

def add_doctor_details():
    st.subheader("Add Doctor Details")
    id = st.text_input("Doctor ID:")
    name = st.text_input("Doctor's name:")
    spe = st.text_input("Specialization:")
    age = st.text_input("Age:")
    add = st.text_input("Address:")
    cont = st.text_input("Contact Details:")
    fees = st.text_input("Fees:")
    ms = st.text_input("Monthly Salary:")
    pid = st.text_input("Patient Id:")
    if st.button("Add Doctor"):
        mycursor.execute("INSERT INTO doctor_details VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, name, spe, age, add, cont, fees, ms, pid))
        mysql.commit()
        st.success("Doctor details added successfully")

def delete_doctor():
    st.subheader("Delete Doctor")
    id = st.text_input("Doctor ID to delete:")
    if st.button("Delete Doctor"):
        mycursor.execute("DELETE FROM doctor_details WHERE doctor_id=%s", (id,))
        mysql.commit()
        st.success("Doctor deleted successfully")

def add_nurse_details():
    st.subheader("Add Nurse Details")
    id = st.text_input("Nurse ID:")
    name = st.text_input("Nurse name:")
    age = st.text_input("Age:")
    add = st.text_input("Address:")
    cont = st.text_input("Contact No:")
    ms = st.text_input("Monthly Salary:")
    pid = st.text_input("Patient Id:")
    if st.button("Add Nurse"):
        mycursor.execute("INSERT INTO nurse_details VALUES(%s, %s, %s, %s, %s, %s, %s)", (id, name, age, add, cont, ms, pid))
        mysql.commit()
        st.success("Nurse details added successfully")

def delete_nurse():
    st.subheader("Delete Nurse")
    id = st.text_input("Nurse ID to delete:")
    if st.button("Delete Nurse"):
        mycursor.execute("DELETE FROM nurse_details WHERE nurse_id=%s", (id,))
        mysql.commit()
        st.success("Nurse deleted successfully")

def add_workers_details():
    st.subheader("Add Workers Details")
    id = st.text_input("Worker ID:")
    name = st.text_input("Worker name:")
    age = st.text_input("Age:")
    add = st.text_input("Address:")
    cont = st.text_input("Contact No:")
    ms = st.text_input("Monthly Salary:")
    pid = st.text_input("Patient Id:")
    if st.button("Add Worker"):
        mycursor.execute("INSERT INTO other_workers_details VALUES(%s, %s, %s, %s, %s, %s, %s)", (id, name, age, add, cont, ms, pid))
        mysql.commit()
        st.success("Workers details added successfully")

def delete_worker():
    st.subheader("Delete Worker")
    id = st.text_input("Worker ID to delete:")
    if st.button("Delete Worker"):
        mycursor.execute("DELETE FROM other_workers_details WHERE other_worker_id=%s", (id,))
        mysql.commit()
        st.success("Nurse deleted successfully")

def add_new_patient():
    st.subheader("Add New Patient")
    id = st.text_input("Patient ID:")
    name = st.text_input("Patient name:")
    sex = st.text_input("Gender:")
    age = st.text_input("Age:")
    address = st.text_input("Address:")
    contact = st.text_input("Contact Details:")
    if st.button("Add Patient"):
        mycursor.execute("INSERT INTO patient_detail (patient_id, name, sex, age, address, contact) VALUES (%s, %s, %s, %s, %s, %s)", (id, name, sex, age, address, contact))
        mysql.commit()
        st.success("Patient details added successfully")

def discharge_patient():
    st.subheader("Discharge Patient")
    id = st.text_input("Patient ID to discharge:")
    if st.button("Discharge"):
        mycursor.execute("DELETE FROM patient_detail WHERE patient_id=%s", (id,))
        mysql.commit()
        st.success("Patient discharged successfully")

main_page()
