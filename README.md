# 🏋️ Dynamic Pricing Strategy (MentorMind × CultFit)

This project was developed under a **MentorMind mentorship program in association with CultFit**.  
It applies **EDA, demand forecasting, and price elasticity modeling** to design a **dynamic pricing strategy** for fitness classes.  
The solution enables CultFit to **optimize utilization (~55% average fill rate)** and **boost revenue through data-driven pricing decisions**.

---

## 🎯 Objectives
- Analyze booking, pricing, and attendance data to uncover demand drivers.
- Forecast demand using statistical and machine learning models.
- Build a **dynamic pricing algorithm** that adapts prices in real-time based on:
  - Demand patterns  
  - Time until event  
  - Location & class popularity  
- Recommend actionable strategies for **maximizing revenue and utilization**.

---

## 📊 Dataset Overview
- **Duration:** April 1, 2018 – June 30, 2018 (3 months)  
- **Size:** 3,271 rows × 14 columns  
- **Metrics:** bookings, prices, capacities, event dates, and class metadata  
- **Data Quality:** Cleaned dataset, no missing values  

---

## 🔎 Exploratory Data Analysis (EDA)
Key findings from the data:contentReference[oaicite:2]{index=2}:
- Average Capacity: ~30 seats/event  
- Average Bookings: ~16–17 seats/event (**~55% utilization**)  
- **Price per Seat:** Mostly < ₹100 → budget-friendly strategy  
- **Peak Month:** May, with up to 1000 bookings/day on weekends  
- **Revenue Range:** ₹25,000 – ₹100,000 typical; outliers up to ₹2,00,000  
- Correlations:
  - Capacity ↔ Bookings: +0.47 (more capacity → more bookings)  
  - Price ↔ Bookings: −0.19 (weak negative, higher prices → fewer bookings)  

---

## 📈 Modeling & Forecasting
- **Demand Forecasting**
  - Models: ARIMA, Prophet  
  - Captured weekly seasonality and demand surges (e.g., Saturdays, festivals).  
  - RMSE ≈ 212 → moderate error, best for short-term stable patterns.  

- **Price Elasticity Analysis**
  - Found **budget segments** highly sensitive to price cuts (→ higher fill rates).  
  - Identified **inelastic segments** (premium classes like Zumba/HRX) where small hikes increased revenue without hurting demand.  

- **Dynamic Pricing Algorithm Inputs**
  - Current price  
  - Days until event  
  - Current bookings  
  - Max capacity  
  - Class popularity  
  - Location factor  

---

## 🚀 Business Recommendations
From the business report:contentReference[oaicite:3]{index=3}:
- **Discount low-demand days (Wednesdays, summer months)** to reduce underutilization.  
- **Premium pricing for high-demand slots (weekends, May, festivals)** to maximize revenue.  
- **Segmented strategy**:
  - Budget classes → keep prices low to maximize attendance.  
  - Premium classes → apply moderate price hikes for higher per-seat revenue.  
- **Scalable framework**: approach can extend to new cities, event types, and other subscription models.  

---

## 🛠️ Tech Stack
- **Languages:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Statsmodels, Prophet  
- **Techniques:** EDA, ARIMA forecasting, Prophet modeling, Regression, Price Elasticity, Simulation  

---

## 📂 Repository Structure
Dynamic-Pricing-Stratergy/
├── data/raw/ # Raw datasets
├── notebooks/ # Jupyter notebooks (EDA, forecasting, modeling)
├── src/ # Python scripts for preprocessing, modeling
├── reports/figures/ # Visualizations & plots
├── report/ # Documentation & deliverables
│ ├── EDA report.pdf # Exploratory Data Analysis report
│ ├── business recommendation.pptx # Business recommendation presentation
│ └── Mentorship_Certificate.pdf # (optional) certificate of completion
├── requirements.txt # Project dependencies
└── README.md # Project documentation

