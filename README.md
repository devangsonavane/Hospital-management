# 🏥 Hospital Management System  

A **web-based Hospital Management System** built using **Python (Streamlit) and MySQL** to help hospitals efficiently manage patient records, doctor details, and appointments.  

![Hospital Management System](https://via.placeholder.com/800x400?text=Hospital+Management+System)

---

## 🚀 Features  

✅ **Patient Management** – Add, update, and delete patient records  
✅ **Doctor Management** – Store doctor details and specializations  
✅ **Appointment Scheduling** – Manage patient-doctor appointments  
✅ **Database Integration** – Uses **MySQL** for data storage  
✅ **User-Friendly UI** – Built with **Streamlit** for an intuitive interface  

---

## 📌 Tech Stack  

- **Frontend:** Streamlit (Python-based UI)  
- **Backend:** Python  
- **Database:** MySQL  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure  

```
Hospital_management_sql/
│— hospitals.sql           # SQL file to set up the database
│— hospital.py             # Main Python script with Streamlit interface
│— requirements.txt        # Required Python libraries
│— README.md               # Project documentation
│— .gitignore              # Files to ignore in Git
```

---

## 📦 Installation & Setup  

### **1⃣ Clone the Repository**  
First, clone the project from GitHub:  
```bash
git clone https://github.com/devangsonavane/Hospital-management.git
cd Hospital-management
```

### **2⃣ Install Dependencies**  
Ensure you have Python **3.11+** installed, then run:  
```bash
pip install -r requirements.txt
```

### **3⃣ Set Up MySQL Database**  
Start MySQL and create the database:  
```sql
CREATE DATABASE city_hospitals;
USE city_hospitals;
SOURCE hospitals.sql;
```
If necessary, update **MySQL credentials** inside `hospital.py`.

---

## ▶️ **Run the Application**  
Start the Streamlit web app using:  
```bash
streamlit run hospital.py
```
It will open automatically in your default browser.

---

## 🛠 Troubleshooting  

### 🔹 **MySQL Connection Error?**  
- Ensure MySQL is running:  
  ```bash
  brew services start mysql
  ```
- Check credentials in `hospital.py`  

### 🔹 **Streamlit Not Found?**  
- Install it using:  
  ```bash
  pip install streamlit
  ```

---

## 👥 Contributors  
- **Devang Sonavane** - [GitHub](https://github.com/devangsonavane)  
- **Kapil (kap007)** - [GitHub](https://github.com/kap007)  

---

## 📝 License  
This project is open-source and available under the **MIT License**.

---

🌟 **Feel free to contribute and star this repo!** 🌟
