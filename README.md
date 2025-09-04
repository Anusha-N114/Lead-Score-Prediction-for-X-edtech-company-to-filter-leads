# 🎯 Lead Score Prediction for X Education

This project was completed as part of a capstone analysis for **X Education**, an online learning platform.  
The goal was to build a **Lead Scoring Model** using Logistic Regression to identify **Hot Leads** most likely to convert,  
enabling the sales team to prioritize resources and improve efficiency.

---

## 📊 Business Problem
- X Education’s lead-to-conversion rate stood at **~30%**, despite strong inbound traffic from campaigns.  
- Sales teams spent equal effort on all leads → **low efficiency and wasted resources**.  
- Goal: Build a **data-driven lead scoring system** to raise the conversion rate to **~80%** by focusing on high-quality leads.

---

## 🔎 Process Overview
1. **Data Understanding & Cleaning**
   - Dataset: ~9,200 leads, 37 features.  
   - Dropped high-missing columns (Lead Quality, Asymmetrique scores).  
   - Treated placeholders like `"Select"` as missing values.  
   - Removed redundant IDs (Prospect ID, Lead Number).  

2. **Feature Engineering**
   - Created **Engagement Score** = Total Time Spent + Page Views + Visits.  
   - Derived **Visit_Page_Ratio** = TotalVisits ÷ Page Views Per Visit.  
   - One-hot encoded categorical variables, scaled numeric features.  

3. **EDA & Insights**
   - **Tags** and **Last Activities** were highly predictive:  
     - “Will revert after reading the email” → strong intent.  
     - “SMS Sent” → strong conversion signal.  
   - High-converting sources: Google, Referral Sites, Direct Traffic.  

4. **Modeling**
   - Logistic Regression with **Recursive Feature Elimination (RFE)**.  
   - Refined using p-values and VIF to retain only significant, stable predictors.  
   - Final model retained 12 interpretable features.  

---

## 🚀 Results
- **Pseudo R² ≈ 0.59** → strong explanatory power.  
- **ROC AUC ≈ 0.96** → excellent discriminatory ability.  
- **Test Set Performance** (cutoff = 0.3):  
  - Accuracy: **92%**  
  - Recall: **87%**  
  - Precision: **91%**  

✅ Clear, interpretable coefficients → easy to explain to sales & marketing teams.  
✅ Focused outreach → simulated efficiency gain of ~30% in lead conversions.  

---

## 📑 Business Recommendations
- Prioritize campaigns from **Google, Referral, and Direct Traffic**.  
- Use **SMS + Email** campaigns more actively (high impact).  
- Focus on **working professionals** and **Finance specialization** leads.  
- During peak sales (e.g., intern cycles): lower threshold to target more leads.  
- When targets are already met: raise threshold (≥0.7) to minimize low-value calls.  

---

## 🛠️ Tech Stack
- **Languages:** Python, SQL  
- **Libraries:** Pandas, NumPy, Scikit-learn, Statsmodels, Matplotlib, Seaborn  
- **Techniques:** Logistic Regression, RFE, Feature Engineering, VIF, ROC-AUC  

---

## 📂 Repository Structure
Lead-Score-Prediction-for-X-edtech-company-to-filter-leads/
├── data/raw/ # Raw datasets
├── notebooks/ # Jupyter notebooks (EDA & modeling)
├── src/ # Python scripts for cleaning & modeling
├── reports/figures/ # Plots & visualizations
├── report/ # Final deliverables
│ ├── Lead_Score_Summary_Report_AnushaN.pdf
│ ├── Lead_Score_Analysis_AnushaN_Presentation.pdf
│ ├── Lead Score Analysis Subjective questions.pdf
├── requirements.txt # Dependencies
└── README.md # Project documentation
