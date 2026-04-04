# 🚀 A/B Testing Decision System: Landing Page Experiment

**Built by Nihar Nandala**

---

## 🌐 Live Application

👉 https://ab-testing-decision-system.streamlit.app/

---

## 📌 What this project is

Most A/B testing projects stop at statistical testing.  
This one doesn’t.

This system answers:

> “Should the business actually ship this change?”

It combines:
- Experiment validation  
- Statistical inference  
- Business decision logic  

To produce a **decision, not just analysis**.

---

## ⭐ Why this project stands out

- Not just a test → full pipeline + deployment  
- Not just p-values → CI + MDE + business thresholds  
- Not just results → clear decision framework  

Built like something a product team can trust.

---

## 🧠 Core Idea

Instead of just reporting:

p-value = 0.905

This system answers:

No meaningful uplift → Do NOT deploy

---

## ⚙️ System Overview

### Pipeline

- Data cleaning & validation  
- Experiment integrity checks  
- Statistical testing  
- Confidence interval analysis  
- Decision logic  
- Deployment via Streamlit  

---

### Key Components

| Component              | Role                          |
|-----------------------|-------------------------------|
| Data Cleaning         | Removes contamination         |
| Statistical Testing   | Measures significance         |
| Confidence Intervals  | Quantifies uncertainty        |
| MDE Analysis          | Evaluates experiment power    |
| Decision Logic        | Converts results → action     |

---

## ⚠️ Critical Insight (Most people miss this)

~1.32% of data was invalid

- Group ≠ Page mismatch  
- Breaks randomization  
- Leads to wrong conclusions  

### Fix:

- Removed contaminated rows  
- Enforced one user per observation  

---

## 📈 Results

| Metric        | Control | Treatment |
|--------------|--------|----------|
| Conversion   | 12.04% | 11.88%   |

Observed effect:

-0.16 percentage points (treatment performs worse)

---

## 📉 Statistical Outcome

- Two-proportion z-test  
- p-value ≈ 0.905  

No evidence of improvement  

---

## 🎯 Decision System (Not Just Stats)

### Confidence Interval

(-0.00394, 0.00078)

- Could be worse  
- Could be slightly better  
- Either way → impact is negligible  

---

### Business Threshold

Minimum meaningful uplift:

+0.12 percentage points

Reality:

Not reached  

---

### Experiment Sensitivity (MDE)

Detectable uplift ≈ 0.30 percentage points  

Meaning:

- Experiment was strong  
- Result is reliable  

---

## 💼 Final Decision

Do NOT deploy the new landing page

Why:

- No statistical improvement  
- No practical impact  
- Experiment is valid  

---

## 🖥️ Streamlit App

### What you see

- Clean experiment summary  
- Conversion comparison  
- Confidence intervals  
- Final decision output  

### What it represents

This is NOT a dashboard.

This is a decision interface built on:

- validated data  
- correct inference  
- business logic  

---

## 📁 Project Structure

ab_testing_project/
├── app/                # Streamlit app
├── data/               # raw + processed data
├── notebooks/          # analysis
├── src/                # cleaning + inference + logic
├── tests/              # unit tests
├── outputs/            # results

---

## ▶️ Running the Project

pip install -r requirements.txt  
python src/pipeline.py  
streamlit run app/app.py  

---

## ⚠️ Important Design Decisions

- Contaminated data removed → ensures validity  
- CI + MDE used → avoids misleading conclusions  
- Business threshold defined → avoids useless wins  

---

## 📌 What this project demonstrates

- Real-world experiment validation  
- Clean statistical thinking  
- Decision-focused analysis  
- End-to-end pipeline design  
- Deployment-ready system  

---

## 🧠 Final Note

This project is not about running a test.

It is about answering:

Should the business act?

---

## 👤 Author

**Nihar Nandala**

Focused on building decision-driven data systems, not just analysis.