# Enterprise Healthcare EHR Analytics Platform

An Interactive Multi-Stakeholder Power BI Business Intelligence System for Clinical Outcomes, Operational Throughput, and Payer Economics.

---

## Executive Summary

Modern hospital networks navigate a persistent dilemma across three competing priorities: enhancing clinical quality, maximizing inpatient operational capacity, and preserving financial viability under complex payer reimbursement models. While healthcare systems record vast volumes of Electronic Health Record (EHR) data, clinical, operational, and billing records often remain isolated across disparate departments.

This repository presents an end-to-end, enterprise-grade healthcare analytics platform developed in **Microsoft Power BI Desktop**, supported by advanced data modeling, longitudinal clinical calculations, and statistical feature engineering. The analysis is built upon an authentic longitudinal EHR dataset encompassing **53,346 clinical encounters, 1,171 multi-decade patient histories, 8,376 condition records, 42,989 medication dispenses, and 34,981 clinical procedures**.

---

## Key Business Problems Addressed

1. **Preventable 30-Day Readmission Penalties**: Under value-based reimbursement frameworks such as the CMS Hospital Readmissions Reduction Program (HRRP), unmanaged readmission spikes incur severe financial penalties.
2. **Acute Bed Throughput and Boarding Delays**: Elevated Average Length of Stay (ALOS) and outlier hospital stays limit available staffed bed capacity and increase emergency department wait times.
3. **Payer Reimbursement Deficits**: Significant reimbursement discrepancies (with payers covering approximately 48.2% of gross charges) shift substantial financial liability (51.8%) directly to patients, elevating bad debt risk and extending Days Sales Outstanding (DSO).

---

## Data Architecture & Star Schema Model

The data pipeline standardizes transactional medical logs into a normalized **Star/Snowflake Schema**, ensuring optimal VertiPaq columnar compression, avoiding Cartesian product duplications, and enabling performant dynamic DAX calculations.

### Dimensional Model Summary

- **Dimension Tables**:
  - `Dim_Patients`: Patient demographics, geographic identifiers (county, city, zip code), age banding, and vital status.
  - `Dim_Organizations`: Healthcare facility metadata, locations, and structural capacity.
  - `Dim_Providers`: Attending and operating clinicians, specialties, and utilization volumes.
  - `Dim_Payers`: Health plans, commercial versus government coverage classification.
  - `Dim_Date`: Comprehensive corporate calendar table spanning continuous historical periods with time-intelligence attributes.

- **Fact Tables**:
  - `Fact_Encounters`: Inpatient, outpatient, emergency, ambulatory, and wellness visits with duration, financial charges, payer coverage, and patient copays.
  - `Fact_Conditions`: Clinical diagnoses coded with SNOMED-CT / ICD equivalents and mapped to primary clinical categories.
  - `Fact_Medications`: Prescription orders, dispense events, duration, and medication expenditure.
  - `Fact_Procedures`: Diagnostic and surgical interventions with standardized procedural costs.

### Relationship Architecture

- `Dim_Patients` (1:Many) -> `Fact_Encounters`, `Fact_Conditions`, `Fact_Medications`, `Fact_Procedures`
- `Dim_Organizations` (1:Many) -> `Fact_Encounters`
- `Dim_Providers` (1:Many) -> `Fact_Encounters`
- `Dim_Payers` (1:Many) -> `Fact_Encounters`, `Fact_Medications`
- `Dim_Date` (1:Many) -> `Fact_Encounters`

---

## Advanced Analytical Formulations & DAX Engine

The platform integrates over **35 production-ready DAX measures** organized into structured display folders. Key technical formulations include:

1. **Longitudinal 30-Day Readmission Window**:
   - Evaluates consecutive inpatient admissions per patient where the elapsed time between prior discharge and subsequent admission is less than or equal to 30 days.
2. **Charlson Comorbidity Risk Index (CCI)**:
   - Dynamic clinical weighting algorithm that attributes severity scores based on active cardiovascular, diabetic, renal, pulmonary, and oncological diagnoses.
3. **Statistical Length of Stay Outlier Detection**:
   - Standardized Z-Score formulation ($Z = \frac{\text{LOS} - \mu}{\sigma}$) flagging stays exceeding two standard deviations above the class mean ($Z > 2.0$).
4. **Pareto 80/20 Cost & Utilization Segmentation**:
   - Virtual DAX ranking tables segmenting patient cohorts into expenditure deciles to track top-tier resource utilization.

---

## Multi-Stakeholder Dashboard Views

The Power BI report (`Capstone Project 1.pbix`) provides five persona-specific reporting pages tailored to hospital governance:

| Page | Target Stakeholder | Primary Focus Areas | Key Visuals |
| :--- | :--- | :--- | :--- |
| **1. Executive Command Center** | Chief Executive Officer (CEO), Chief Financial Officer (CFO) | High-level organizational health, gross billed charges, payer recovery, readmission rate | Revenue trend line, payer vs. patient waterfall, service class donut, executive decomposition tree |
| **2. Clinical Quality Intelligence** | Chief Medical Officer (CMO), Quality Committee | 30-day readmissions, comorbidity burden, polypharmacy prevalence | Clinical risk quadrant scatter plot, active disease volume, drug class by age bracket |
| **3. Hospital Operations Hub** | Chief Operating Officer (COO), Capacity Directors | Bed turnover, Average Length of Stay (ALOS), physician workloads, ED-to-inpatient conversion | LOS distribution by visit class, facility volume bars, physician performance matrix |
| **4. Revenue Cycle Management** | VP of Managed Care, Billing Directors | Payer reimbursement ratios, under-reimbursement leakage, patient out-of-pocket liabilities | Payer collection comparison, procedure cost bubble chart, demographic burden distribution |
| **5. Population Health & SDoH Hub** | Chief Population Health Officer, Care Coordinators | Chronic disease prevalence, high-utilizer spend concentration, geographic disease density | County-level GIS choropleth map, high-utilizer Pareto curve, age-group disease distribution |

---

## Repository Structure

```text
├── Capstone Project 1.pbix                   # Master Microsoft Power BI report file (5 dashboard views)
├── Capstone_Presentation Christopher Jeremy A W.pptx # Executive presentation slide deck
├── Capstone Project 1 - Project Proposal Healthcare EHR Analytics... # Formal project proposal document
├── Healthcare_EHR_Capstone_Report.md        # Comprehensive technical and clinical report
├── Healthcare_EHR_Presentation_Deck.md       # Slide-by-slide viva defense presentation notes
├── Healthcare_EHR_DAX_Measures.dax          # Complete catalog of 35+ production DAX measures
├── Healthcare_EHR_Presentation.html         # Interactive HTML slide presentation companion
├── PowerBI_StepByStep_Model_Setup.md        # Data ingestion and model configuration guide
├── generate_presentation.py                 # Presentation build automation script
├── presentation_assets/                     # Dashboard previews, schema diagrams, and visuals
└── processed_data/                          # Cleaned, normalized Star Schema tables ready for BI
```

---

## Getting Started & Replication

### Prerequisites

- **Microsoft Power BI Desktop** (August 2023 release or newer recommended)
- **Python 3.10+** (optional, for slide generation scripts: `python-pptx`, `pandas`)

### Opening the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/christopherjeremy/Healthcare-EHR-Analytics.git
   cd Healthcare-EHR-Analytics
   ```
2. Open `Capstone Project 1.pbix` in **Power BI Desktop**.
3. If data source paths require updating:
   - Navigate to **Home** > **Transform Data** > **Data source settings**.
   - Update the file path to point to the local `processed_data` directory.
   - Select **Apply changes**.

---

## Actionable Business Recommendations & ROI

1. **Transition Care Management (TCM)**:
   - Deploying mandatory 48-hour post-discharge nurse outreach for patients in the high-risk readmission quadrant is projected to reduce 30-day readmissions by 20%, generating an estimated \$280,000 in annual direct savings and penalty avoidance.
2. **Clinical Care Pathway Optimization**:
   - Reducing inpatient ALOS by 2.5 days across high-variance clinical categories yields approximately 4,500 reclaimed bed-days annually, expanding acute patient capacity without capital facility expansion.
3. **Proactive Financial Clearance & Payer Renegotiation**:
   - Implementing point-of-service eligibility verification and structured payment plans addresses the 51.8% patient liability ratio, accelerating cash collections by 14 days and curtailing uncollectible debt write-offs by \$150,000 annually.

---

## Author & Project Metadata

- **Author**: Christopher Jeremy A W
- **Profile**: [github.com/christopherjeremy](https://github.com/christopherjeremy)
- **Specialization**: Business Intelligence, Healthcare Informatics, and Data Analytics
- **Primary Tools**: Microsoft Power BI Desktop, DAX, Power Query (M), Python
