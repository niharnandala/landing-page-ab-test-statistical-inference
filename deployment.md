# 🚀 Deployment Guide

**Nihar Nandala**

---

## 🌐 Live Application

👉 https://ab-testing-decision-system.streamlit.app/

---

## ▶️ Run Locally

streamlit run app/app.py

---

## ⚙️ First-Time Setup

pip install -r requirements.txt  
python src/pipeline.py  

---

## ☁️ Deploy on Streamlit Cloud

1. Push project to GitHub  
2. Go to https://streamlit.io/cloud  
3. Connect your repository  
4. Set entry point:  

app/app.py  

---

## ⚠️ Required Data

The app depends on:

data/processed/ab_clean.csv  

If missing, run:

python src/pipeline.py  

---

## 🧠 What This App Is

This is NOT a dashboard.

This is a decision interface built on:

- validated experiment data  
- correct statistical inference  
- business-aware conclusions  

---

## 🛠️ Common Issues

### Import errors

Run from project root.

### Missing data file

Run pipeline first.

---

## 🎯 Deployment Philosophy

- correctness > UI  
- reproducibility > complexity  
- clarity > visuals  

---

## 👤 Author

**Nihar Nandala**

Focused on building decision-driven data systems, not just analysis.