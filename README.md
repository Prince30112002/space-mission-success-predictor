

---

# 🚀 Space Mission Success Predictor

Predicting the **success or failure of space missions** using Machine Learning models with Python and Streamlit.

---

## 📌 Table of Contents

* <a href="#overview">Overview</a>
* <a href="#business-problem">Business Problem</a>
* <a href="#dataset">Dataset</a>
* <a href="#tools--technologies">Tools & Technologies</a>
* <a href="#project-structure">Project Structure</a>
* <a href="#data-cleaning--preprocessing">Data Cleaning & Preprocessing</a>
* <a href="#model-training">Model Training</a>
* <a href="#deployment">Deployment</a>
* <a href="#how-to-run-this-project">How to Run This Project</a>
* <a href="#final-recommendations">Final Recommendations</a>
* <a href="#author--contact">Author & Contact</a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>  

This project predicts whether a **space mission** will be successful or not.
It uses historical data of space launches, including **launch site, rocket type, payload mass, cost, and country**.
The final model is deployed using **Streamlit** for interactive predictions.

---

<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>  

Space missions involve **huge costs and risks**. This project aims to:

* Predict probability of mission **success or failure**
* Identify **key factors** affecting mission outcomes
* Help researchers and organizations optimize future launches
* Provide a **simple interface** for predictions and analysis

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>  

* `space_missions.csv` file containing columns:

  * `Organisation`, `Location`, `Date`, `Detail`, `Rocket_Status`, `Price`, `Mission_Status`
* Label values: **Success**, **Failure**, **Partial Failure**
* Located in `/data/raw/` folder

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>  

* Python (Pandas, NumPy, scikit-learn, Matplotlib, Seaborn)
* Machine Learning (Logistic Regression, Random Forest, XGBoost)
* Streamlit (Web Deployment)
* GitHub (Version Control)

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>  

```
space-mission-success-predictor/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── space_missions.csv
│   └── processed/
│
├── src/
│   ├── data_preprocessing.py
│   └── model_training.py
│
├── models/
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   └── feature_scaler.pkl
│
└── deployment/
    └── app.py
```

---

<h2><a class="anchor" id="data-cleaning--preprocessing"></a>Data Cleaning & Preprocessing</h2>  

* Removed null/empty values
* Converted dates into proper datetime format
* Extracted features: year, rocket status, organisation type
* Encoded categorical columns (OneHot / Label Encoding)
* Normalized numerical features like cost & payload
* Saved processed data in `/data/processed/`

---

<h2><a class="anchor" id="model-training"></a>Model Training</h2>  

* **Features:** Rocket type, cost, organisation, location, payload, year
* **Models trained:**

  * Logistic Regression
  * Random Forest
  * XGBoost
* **Train/Test split:** 80/20
* Best accuracy achieved with **XGBoost (~88%)**
* Models saved as `.pkl` files for deployment

---

<h2><a class="anchor" id="deployment"></a>Deployment</h2>  

* Streamlit web app allows users to input **mission details**
* Predicts **Success / Failure probability**
* Provides feature importance visualization
* Simple and interactive interface

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>  

1. Clone the repository:

```bash
git clone https://github.com/yourusername/space-mission-success-predictor.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run Streamlit app:

```bash
"C:/Program Files/Python313/python.exe" -m streamlit run deployment/app.py
```

4. Input mission details in browser → get prediction ✅

---

<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>  

* Integrate with real-time space mission APIs for live predictions
* Continuously retrain model as new missions are added
* Use Deep Learning or Graph Neural Networks for complex patterns
* Extend dashboard with **mission cost vs success** analytics

---

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>  

*Prince Rajak*
Computer Science Student / ML Enthusiast
📧 Email: [rajakprince30112002@gmail.com](mailto:rajakprince30112002@gmail.com)


---


