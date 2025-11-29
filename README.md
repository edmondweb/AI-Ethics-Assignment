COMPAS Recidivism Fairness Audit
================================

Overview
--------

This repository contains an analysis of racial bias in the **COMPAS recidivism risk scores** using fairness metrics. The analysis is conducted using the **COMPAS recidivism dataset** to examine the disparities in how different racial groups are assessed in terms of their likelihood to reoffend. The analysis includes key fairness metrics such as **false positive rate**, **true positive rate**, and **disparity in impact** across different racial groups.

The goal of this project is to explore potential bias in AI systems, specifically focusing on the **risk prediction model** used by COMPAS, which is widely used in criminal justice systems to assess the likelihood of recidivism.

## Dataset

The dataset used for this analysis is the **COMPAS recidivism dataset**, which contains information about individuals who were assessed using the COMPAS tool, including demographic information such as race, sex, and age, as well as risk scores for **recidivism** and **violence**.

### Key columns used in the analysis:

* **race**: The race of the individual.

* **decile_score.1**: The recidivism risk score assigned by the COMPAS tool (1-10 scale).

* **label**: A binary label indicating whether an individual is classified as "high risk" (decile score >= 5).

Fairness Metrics
----------------

The analysis includes the following fairness metrics:

1. **Average Recidivism Risk Score**: The average **decile score** for each racial group, indicating the average recidivism risk for each race.

2. **False Positive Rate**: The proportion of low-risk individuals (decile score < 5) who are misclassified as high-risk.

3. **True Positive Rate (TPR)**: The proportion of high-risk individuals (decile score >= 5) correctly classified as high-risk.

4. **Disparity in Impact**: The ratio of false positive rates between different racial groups, measuring potential bias in the model's predictions.

Steps for Analysis
------------------

### 1. Data Preparation

* **Data Loading**: The dataset is loaded using `pandas`.

* **Data Cleaning**: Any missing or NaN values are removed to ensure accurate analysis.

* **Race Mapping**: The race column is mapped to numeric values for easier analysis.

### 2. Fairness Metric Calculation

* **Average Decile Score by Race**: The average recidivism risk scores (decile scores) are computed for each racial group.

* **False Positive Rates**: The false positive rate is calculated for each group by identifying low-risk individuals (decile score < 5) who are misclassified as high-risk (label = 1).

* **True Positive Rates**: The true positive rate is calculated by identifying high-risk individuals (decile score >= 5) who are correctly classified as high-risk.

* **Disparity in Impact**: The disparity in false positive rates between privileged and unprivileged racial groups is computed.

### 3. Visualization

* **Bar Plots**: The analysis includes several bar plots to visualize:
  
  * Average recidivism risk scores by race.
  
  * False positive rates by race.
  
  * True positive rates by race.
  
  * Disparity in impact (false positive rate ratio).

Requirements
------------

To run the analysis, you will need the following Python libraries:

* `pandas` – for data manipulation.

* `matplotlib` – for plotting visualizations.

Install the required libraries with the following command:

```bash
pip install pandas matplotlib
```

How to Run the Analysis
-----------------------

1. **Clone the Repository**:

```bash
git clone https://github.com/your-username/compas-fairness-audit.git
cd compas-fairness-audit
```

1. **Download the Dataset**:  
   Ensure that you have the COMPAS recidivism dataset files in the same directory as the notebook or script.

2. **Run the Analysis**:  
   Open the Python script or Jupyter notebook (`compare.py`  and run the code blocks to perform the fairness audit.

3. **View the Results**:  
   The script will generate various visualizations (bar plots) to help you assess the fairness of the COMPAS tool in predicting recidivism based on race.

Example Output
--------------

### 1. **Average Recidivism Risk Score by Race**:

* A bar chart showing the average recidivism risk score for each racial group, highlighting potential racial disparities.

### 2. **False Positive Rate by Race**:

* A bar chart illustrating the false positive rate for each racial group, showing how often low-risk individuals are misclassified as high-risk.

### 3. **True Positive Rate by Race**:

* A bar chart displaying the true positive rate for each racial group, indicating how well the model identifies high-risk individuals.

### 4. **Disparity in False Positive Rates**:

* A bar chart comparing the false positive rates of different racial groups, highlighting any disparities in treatment.

Further Exploration
-------------------

This project focuses on basic fairness analysis, but there are several opportunities for further exploration:

* **Bias Mitigation**: Implement fairness-enhancing algorithms (e.g., **reweighing**, **adversarial debiasing**) to reduce bias in the model.

* **Additional Metrics**: Explore other fairness metrics, such as **statistical parity**, **equal opportunity**, and **disparate treatment**.

* **External Audits**: Use the **AI Fairness 360** library for more advanced audits and debiasing.


