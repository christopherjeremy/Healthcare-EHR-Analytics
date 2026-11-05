# Power BI Step-by-Step Data Model & Dashboard Construction Guide (V2 Refined)

This comprehensive guide details how to import the processed Star-Schema dataset into **Power BI Desktop**, configure relationships without ambiguity, mark the date table, load the master DAX measures, and assemble all 5 stakeholder dashboard pages.

---

## Step 1: Loading Data into Power BI Desktop

1. Launch **Power BI Desktop**.
2. Click **Get Data** -> **Folder** (or **Text/CSV**).
3. Browse to your processed data directory:
   `C:\Users\krish\OneDrive\Documents\PGDA\Capstone project 1\processed_data`
4. Load the following **9 Star-Schema CSV files**:
   - `Dim_Patients.csv`
   - `Dim_Organizations.csv`
   - `Dim_Providers.csv`
   - `Dim_Payers.csv`
   - `Dim_Date.csv`
   - `Fact_Encounters.csv`
   - `Fact_Conditions.csv`
   - `Fact_Medications.csv`
   - `Fact_Procedures.csv`
5. Click **Load** (or Transform Data in Power Query to verify column data types).

---

## Step 2: Mark Date Table for Time Intelligence

To ensure 100% precision for Time Intelligence measures (`SAMEPERIODLASTYEAR`, `DATEADD`, `DATESINPERIOD`):
1. In the **Fields / Data** pane, right-click on the `Dim_Date` table.
2. Select **Mark as Date Table** -> **Mark as Date Table**.
3. In the dialog, select the `Date` column (DataType: Date) and click **OK**.

---

## Step 3: Configuring the Star-Schema Relationships (Model View)

Navigate to **Model View** in Power BI Desktop. Configure the following **1-to-Many ($1:*$)** active relationships:

### Core Star Schema Relationships (Active, Single Cross-Filter):

| Dimension Table (1) | Primary Key | Fact Table (*) | Foreign Key | Cardinality | Cross Filter | State |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Dim_Patients` | `PATIENT_KEY` | `Fact_Encounters` | `PATIENT_KEY` | 1 to Many ($1:*$) | Single | Active |
| `Dim_Patients` | `PATIENT_KEY` | `Fact_Conditions` | `PATIENT_KEY` | 1 to Many ($1:*$) | Single | Active |
| `Dim_Patients` | `PATIENT_KEY` | `Fact_Medications` | `PATIENT_KEY` | 1 to Many ($1:*$) | Single | Active |
| `Dim_Patients` | `PATIENT_KEY` | `Fact_Procedures` | `PATIENT_KEY` | 1 to Many ($1:*$) | Single | Active |
| `Dim_Organizations` | `ORGANIZATION_KEY` | `Fact_Encounters` | `ORGANIZATION_KEY` | 1 to Many ($1:*$) | Single | Active |
| `Dim_Providers` | `PROVIDER_KEY` | `Fact_Encounters` | `PROVIDER_KEY` | 1 to Many ($1:*$) | Single | Active |
| `Dim_Payers` | `PAYER_KEY` | `Fact_Encounters` | `PAYER_KEY` | 1 to Many ($1:*$) | Single | Active |
| `Dim_Payers` | `PAYER_KEY` | `Fact_Medications` | `PAYER_KEY` | 1 to Many ($1:*$) | Single | Active |
| `Dim_Date` | `DateFormatted` | `Fact_Encounters` | `ENCOUNTER_DATE` | 1 to Many ($1:*$) | Single | Active |

> [!NOTE]
> To prevent relationship loops or diamond ambiguities, keep the direct relationships from `Fact_Encounters` to `Fact_Conditions`, `Fact_Medications`, and `Fact_Procedures` on `ENCOUNTER_KEY` as **Inactive** or utilize the primary `PATIENT_KEY` star-dimension filter propagation.

---

## Step 4: Loading Master `_Measures` Table

1. On the **Home** ribbon, click **Enter Data**.
2. Name the table `_Measures` and click **Load**.
3. Open [`Healthcare_EHR_DAX_Measures.dax`](Healthcare_EHR_DAX_Measures.dax).
4. Create each DAX measure (Right-click `_Measures` -> **New Measure**).
5. In Model view, group them into the 6 designated display folders:
   - `01_Executive_KPIs`
   - `02_Clinical_Quality`
   - `03_Hospital_Operations`
   - `04_Revenue_Cycle_Management`
   - `05_Population_Health_SDoH`
   - `06_Time_Intelligence`

---

## Step 5: Assembling the 5 Stakeholder Dashboard Pages

Create 5 interactive report pages at the bottom of Power BI Desktop:

### Page 1: C-Suite Executive Command Center (CEO & CFO)
- **Top KPI Ribbon**: `[Total_Unique_Patients]`, `[Total_Billed_Revenue]`, `[Net_Collection_Rate_Pct]`, `[Inpatient_Readmission_Rate_30D]`.
- **Visual 1 (Trend)**: Line & Clustered Column (`Dim_Date[YearMonth]` on Shared Axis, `[Total_Encounters]` on Column, `[Total_Billed_Revenue]` on Line).
- **Visual 2 (Waterfall)**: Waterfall Chart (`[Total_Billed_Revenue]` $\rightarrow$ `[Total_Payer_Reimbursement]` $\rightarrow$ `[Total_Patient_OOP_Burden]`).
- **Visual 3 (Donut)**: Encounter Class Distribution (`Fact_Encounters[ENCOUNTERCLASS]`, Values: `[Total_Encounters]`).
- **Visual 4 (Decomposition Tree)**: Analyze `[Total_Billed_Revenue]`, Explain By `ENCOUNTERCLASS`, `CLINICAL_CATEGORY`, `PAYER_TYPE`.

### Page 2: Clinical Quality & Comorbidity Intelligence (CMO & Board)
- **Top KPI Ribbon**: `[Inpatient_Encounters]`, `[Inpatient_Readmissions_30D]`, `[Charlson_Comorbidity_Index_Avg]`, `[Polypharmacy_Prevalence_Pct]`.
- **Visual 1 (Scatter Quadrant)**: `Fact_Conditions[CLINICAL_CATEGORY]` on Details, `[Inpatient_Encounters]` on X-Axis, `[Inpatient_Readmission_Rate_30D]` on Y-Axis, `[Total_Billed_Revenue]` on Size. Add reference lines at median volume and 20% readmission rate.
- **Visual 2 (Horizontal Bar)**: `Fact_Conditions[CLINICAL_CATEGORY]` on Y-Axis, `[Active_Chronic_Conditions_Count]` on X-Axis.
- **Visual 3 (100% Stacked Bar)**: `Fact_Medications[DRUG_CLASS]` on Y-Axis, `[Total_Patient_OOP_Burden]` on X-Axis, `Dim_Patients[AGE_GROUP]` on Legend.

### Page 3: Hospital Operations & Bed Throughput Hub (COO)
- **Top KPI Ribbon**: `[Average_LOS_Inpatient_Days]`, `[Total_Bed_Days_Occupied]`, `[Bed_Turnover_Rate]`, `[LOS_Outlier_Encounter_Count]`.
- **Visual 1 (Column Chart)**: `Fact_Encounters[ENCOUNTERCLASS]` on X-Axis, `[Average_LOS_Days]` on Y-Axis, Tooltip = `[LOS_Z_Score_Inpatient]`.
- **Visual 2 (Facility Bar Chart)**: `Dim_Organizations[NAME]` on Y-Axis, `[Total_Encounters]` on X-Axis.
- **Visual 3 (Physician Matrix)**: Rows = `Dim_Providers[NAME]`, `Dim_Providers[SPECIALITY]`, Values = `[Total_Encounters]`, `[Average_LOS_Days]`, `[Total_Billed_Revenue]`.
- **Visual 4 (Conversion Card / Gauge)**: `[ED_to_Inpatient_Conversion_Rate]` (2.34% Sequential ED conversions within 24h).

### Page 4: Revenue Cycle Management & Payer Analytics (RCM)
- **Top KPI Ribbon**: `[Total_Billed_Revenue]`, `[Net_Collection_Rate_Pct]`, `[Under_Reimbursement_Gap]`, `[Patient_Financial_Burden_Ratio]`.
- **Visual 1 (Payer Comparison Bar)**: `Dim_Payers[NAME]` on Y-Axis, `[Total_Payer_Reimbursement]` & `[Total_Patient_OOP_Burden]` on X-Axis.
- **Visual 2 (High-Cost Procedures Bubble)**: `Fact_Procedures[PROCEDURE_CATEGORY]` on Details, `[Total_Procedures]` on X-Axis, `[High_Cost_Procedure_Count]` on Y-Axis, `[Total_Procedure_Cost]` on Size.
- **Visual 3 (Demographic Burden Column)**: `Dim_Patients[RACE]` on X-Axis, `[Total_Patient_OOP_Burden]` on Y-Axis, `Dim_Patients[GENDER_DESC]` on Legend.

### Page 5: Population Health & SDoH Geographic Hub (PopHealth)
- **Top KPI Ribbon**: `[Chronic_Disease_Prevalence_Rate]`, `[Top10Pct_High_Utilizer_Cost_Share_Pct]`, `[Preventative_Care_Visit_Rate]`, `[Patient_Concentration_By_County]`.
- **Visual 1 (Shape / Filled Map)**: Location = `Dim_Patients[COUNTY]`, Color = `[Total_Unique_Patients]`, Tooltip = `[Chronic_Disease_Prevalence_Rate]`.
- **Visual 2 (Pareto Curve)**: X-Axis = Spend Decile, Y-Axis = `[Top10Pct_High_Utilizer_Cost_Share_Pct]`.
- **Visual 3 (100% Stacked Column)**: `Dim_Patients[AGE_GROUP]` on X-Axis, `[Active_Chronic_Conditions_Count]` on Y-Axis, Legend = `Fact_Conditions[CLINICAL_CATEGORY]`.

---

## Step 6: Save and Publish
Save the file as `Healthcare_EHR_Analytics.pbix`.
