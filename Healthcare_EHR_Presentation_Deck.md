# CAPSTONE PROJECT VIVA PRESENTATION DECK

## Enterprise Healthcare EHR Analytics: An Interactive Multi-Stakeholder Power BI Platform
**Presenter**: PGDA Capstone Candidate | **Domain**: Healthcare Informatics & BI | **Tool**: Microsoft Power BI Desktop

---

## Slide 1: Title & Project Scope
- **Project Title**: Enterprise Healthcare EHR Analytics Platform
- **Sub-title**: Optimizing Patient Outcomes, Operational Throughput, and Payer Economics in Power BI
- **Presenter**: PGDA Capstone Student
- **Key Highlight**: Full-scale multi-table EHR analysis across 53,346 encounters, 1,171 patients, and $6.87M in gross clinical claims.

---

## Slide 2: The Healthcare "Triple Aim" Problem Statement
- **Clinical Challenge**: Excess 30-day preventable readmissions trigger severe CMS regulatory penalties.
- **Operational Challenge**: Prolonged Average Length of Stay (ALOS) causes acute bed shortages and emergency department boarding.
- **Financial Challenge**: Payer reimbursement discrepancies (only 48.2% recovered from payers) shift a heavy 51.8% financial burden onto patients.
- **The Solution**: An integrated 5-stakeholder Power BI intelligence platform powered by an enterprise Star Schema and 35+ advanced DAX measures.

---

## Slide 3: Data Architecture & Star Schema Model
- **Data Source**: Synthea Multi-Table Electronic Health Records.
- **Scale**: 9 Processed Star-Schema Tables, 1 Master Continuous Calendar (`Dim_Date` with 39,813 days).
- **Core Relationships**:
  - `Dim_Patients` ($1:*$) $\rightarrow$ `Fact_Encounters`, `Fact_Conditions`, `Fact_Medications`, `Fact_Procedures`
  - `Dim_Organizations` & `Dim_Providers` ($1:*$) $\rightarrow$ `Fact_Encounters`
  - `Dim_Payers` ($1:*$) $\rightarrow$ `Fact_Encounters` & `Fact_Medications`
  - `Dim_Date` ($1:*$) $\rightarrow$ `Fact_Encounters`

---

## Slide 4: Advanced DAX & Feature Engineering Highlights
- **1. 30-Day Readmission Context Transition**:
  - Longitudinal window calculation evaluating subsequent inpatient admissions within $\le 30$ days of discharge.
- **2. Charlson Comorbidity Risk Index (CCI)**:
  - Dynamic weighted scoring algorithm evaluating cardiovascular, diabetic, renal, and oncological comorbidities.
- **3. Statistical Length of Stay Z-Score**:
  - Dynamic $Z = (\text{LOS} - \mu) / \sigma$ identifying statistical outliers ($Z > 2.0$).
- **4. Pareto 80/20 High-Utilizer Allocation**:
  - DAX virtual table iterating across patient cohorts to compute cumulative spend deciles.

---

## Slide 5: Dashboard 1 - C-Suite Executive Command Center
- **Audience**: CEO, CFO, Board of Directors.
- **Key Metrics**: Total Patients (1,171), Total Billed Revenue ($6.87M), Payer Reimbursement ($3.31M), 30D Readmission Rate (26.5%).
- **Key Visuals**: Monthly Revenue vs. Volume Dual-Axis Trend, Revenue Waterfall Flow, Executive Decomposition Tree.

---

## Slide 6: Dashboard 2 - CMO & Clinical Quality Intelligence
- **Audience**: Chief Medical Officer, Quality Review Board.
- **Key Metrics**: 1,838 Inpatient Admissions, 487 30-Day Readmissions, Charlson Comorbidity Index, Polypharmacy Prevalence ($\ge 5$ drugs).
- **Key Visuals**: 30-Day Readmission Risk 4-Quadrant Scatter Plot, Active Disease Categories Bar Chart, Drug Class vs. Age Stacked Bar.

---

## Slide 7: Dashboard 3 - COO & Hospital Operations Hub
- **Audience**: Chief Operating Officer, Bed Managers, Clinical Directors.
- **Key Metrics**: Average Inpatient LOS (18.04 Days), Total Bed Days Occupied, Bed Turnover Rate, LOS Outlier Count.
- **Key Visuals**: LOS Distribution by Service Class, Top Facility Utilization Chart, Physician Workload & Performance Matrix.

---

## Slide 8: Dashboard 4 - Revenue Cycle Management & Payer Analytics
- **Audience**: VP of Managed Care, Billing Directors.
- **Key Metrics**: Gross Billed ($6.87M), Net Collection Rate (100%), Under-Reimbursement Gap ($3.56M), Patient Out-of-Pocket Burden (51.8%).
- **Key Visuals**: Payer Reimbursement Ratio Comparison, High-Cost Clinical Procedures Bubble Chart, Demographic OOP Burden Chart.

---

## Slide 9: Dashboard 5 - Population Health & SDoH Hub
- **Audience**: Chief Population Health Officer, Care Coordinators.
- **Key Metrics**: Chronic Disease Prevalence Rate, Top 10% High-Utilizer Cost Share, Preventative Care Rate, County Density.
- **Key Visuals**: Massachusetts County GIS Heatmap, High-Utilizer Pareto 80/20 Curve, Age Group vs. Disease Distribution.

---

## Slide 10: Actionable Recommendations & Quantified ROI
1. **Transition Care Management (TCM)**: 20% reduction in readmissions via 48-hr nurse follow-up saves ~$280,000 annually.
2. **Clinical Discharge Pathways**: Reducing Inpatient ALOS by 2.5 days frees up 4,500 bed-days (+15% acute capacity).
3. **Payer Contract Renegotiation & Financial Counseling**: Accelerates cash collection by 14 days and lowers bad debt by $150,000/yr.

---

## Slide 11: Viva Anticipated Questions & Defense Talking Points
- **Q1: Why did you choose a Star Schema instead of a single flat table?**
  - *Answer*: A single flat table of 53k encounters merged with multiple diagnoses and medications results in severe cartesian product duplication, inflating financial sums and degrading DAX calculation speeds. A Star Schema ensures 100% normalization, optimal VertiPaq compression, and clean 1-to-many filter propagation.
- **Q2: How did you handle 30-day readmission logic without an explicit flag in the raw data?**
  - *Answer*: We engineered a longitudinal window algorithm in Python/DAX by sorting encounters by patient and start date, checking if the current and prior visits were inpatient admissions, and evaluating if the time elapsed between prior discharge and new admission was $\le 30$ days.
- **Q3: What makes this dashboard enterprise-grade?**
  - *Answer*: Rather than a generic single-screen summary, the platform delivers 5 role-specific dashboards designed for distinct hospital decision-makers, supported by statistical outlier detection (Z-scores) and clinical risk scoring (Charlson index).

---

## Slide 12: Conclusion & Q&A
- **Summary**: Comprehensive, end-to-end Healthcare EHR Business Intelligence platform ready for enterprise deployment.
- **Thank You! Open for Evaluator Questions.**
