# 🏡 House Price Prediction App

An interactive web application built with **Streamlit** that predicts house prices based on various real-world factors such as crime rate, number of rooms, air quality, proximity to public transport, and more. Powered by a **Linear Regression** model trained on real housing data, this app offers instant predictions and serves as a compact demonstration of deploying machine learning models on the web.

---
### APP IS DEPLOYED AT THE SITE : [WEBSITE LINK](https://house-pricing-predict-using-linear-regression.streamlit.app/)

---

## 🚀 Features

- ✅ **User-friendly UI** – Intuitive sliders, dropdowns, and number inputs for seamless user interaction.
- 🧠 **Real-time Predictions** – Instantaneous output using a trained **Linear Regression** model.
- 📈 **Multi-feature Input** – Factors include:
  - Crime rate in the area  
  - Number of rooms  
  - Tax rate  
  - Nitric Oxide concentration (NOx level – air quality)  
  - Distance to employment centers / public transport  
  - Pupil-teacher ratio (school quality proxy)  
  - Property age
- ☁️ **Deployed on Streamlit Community Cloud** – Free, easy access without setup for users.
- ⚙️ **Extensible** – Easily extendable to more complex models (e.g., Random Forest, Gradient Boosting) and additional features.

---

## 🛠️ Technologies Used

### 🔧 Backend
- **Python 3.x**
- **Pandas** & **NumPy** – Data manipulation and analysis
- **Scikit-learn** – Model training, evaluation, and regression algorithm
- **Joblib** – Model serialization

### 🎨 Frontend
- **Streamlit** – Fast UI development and web deployment

---

## 🧪 Model Training Process

1. **Dataset Preparation**
   - Imported a housing dataset (e.g., Boston Housing or a similar dataset).
   - Performed preprocessing: handling missing values, normalization, and feature selection.

2. **Model Training**
   - Used `LinearRegression` from **scikit-learn**.
   - Dataset split into training and test sets (e.g., 80/20).
   - Model trained on features such as:
     - `CRIM` – Crime rate
     - `RM` – Average rooms
     - `NOX` – Air quality
     - `DIS` – Distance to employment centers
     - `TAX` – Tax rate
     - `PTRATIO` – Pupil-teacher ratio
     - `AGE` – House age
   - Evaluated using **Mean Squared Error (MSE)** and **R² Score**.

3. **Model Saving**
   ```python
   import joblib
   joblib.dump(model, 'house_price_model.pkl')

## 📦 Installation & Setup

Ensure Python is installed, then clone and install dependencies:

```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
pip install -r requirements.txt
```
## ▶️ Run the App Locally

To run the app locally, use the following command:

```bash
streamlit run app.py
```
## 🌐 Deployment

This app is deployed on **Streamlit Community Cloud**.

To deploy your own:

1. Push the code to a public GitHub repository.
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo and deploy in a few clicks.

---

## 📌 Future Improvements

- Display model performance metrics within the app  
- Add support for multiple regression algorithms  
- Include interactive charts for better insights  
- Enable CSV upload for bulk prediction  

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---



 
