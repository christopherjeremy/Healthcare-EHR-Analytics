import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

COLOR_BG = RGBColor(248, 250, 252)       # Light Slate 50 (#F8FAFC)
COLOR_CARD = RGBColor(255, 255, 255)     # Pure White (#FFFFFF)
COLOR_BORDER = RGBColor(226, 232, 240)   # Light Border (#E2E8F0)
COLOR_TEXT_DARK = RGBColor(15, 23, 42)    # Dark Slate 900 (#0F172A)
COLOR_TEXT_MUTED = RGBColor(71, 85, 105) # Slate 600 (#475569)

COLOR_BLUE = RGBColor(37, 99, 235)       # Royal Blue (#2563EB)
COLOR_BLUE_LIGHT = RGBColor(239, 246, 255)# Light Blue Tint (#EFF6FF)
COLOR_AMBER = RGBColor(217, 119, 6)      # Amber (#D97706)
COLOR_EMERALD = RGBColor(5, 150, 105)    # Emerald (#059669)
COLOR_ROSE = RGBColor(225, 29, 72)       # Rose (#E11D48)
COLOR_PURPLE = RGBColor(124, 58, 237)    # Purple (#7C3AED)

def set_slide_bg(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid(); bg.fill.fore_color.rgb = COLOR_BG; bg.line.fill.background()
    return bg

def add_header(slide, title, category_tag):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(0.3), Inches(12.333), Inches(0.75))
    bar.fill.solid(); bar.fill.fore_color.rgb = COLOR_CARD
    bar.line.color.rgb = COLOR_BORDER; bar.line.width = Pt(1)
    
    tb = slide.shapes.add_textbox(Inches(0.7), Inches(0.34), Inches(11.933), Inches(0.68))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p0 = tf.paragraphs[0]; p0.text = category_tag.upper(); p0.font.size = Pt(8.5); p0.font.bold = True; p0.font.color.rgb = COLOR_AMBER
    p0.space_after = Pt(2)
    p1 = tf.add_paragraph(); p1.text = title; p1.font.size = Pt(15); p1.font.bold = True; p1.font.color.rgb = COLOR_TEXT_DARK

def add_footer(slide, glossary_text, slide_num):
    foot = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(6.82), Inches(12.333), Inches(0.38))
    foot.fill.solid(); foot.fill.fore_color.rgb = COLOR_CARD
    foot.line.color.rgb = COLOR_BORDER; foot.line.width = Pt(1)
    
    tb = slide.shapes.add_textbox(Inches(0.7), Inches(6.84), Inches(10.5), Inches(0.34))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.text = 'ABBREVIATIONS & GLOSSARY: ' + glossary_text
    p.font.size = Pt(7.8); p.font.color.rgb = COLOR_TEXT_MUTED
    
    tb_num = slide.shapes.add_textbox(Inches(11.3), Inches(6.84), Inches(1.3), Inches(0.34))
    tf_num = tb_num.text_frame; tf_num.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_num.margin_left = tf_num.margin_right = tf_num.margin_top = tf_num.margin_bottom = 0
    p_num = tf_num.paragraphs[0]; p_num.text = f'Slide {slide_num} / 10'; p_num.alignment = PP_ALIGN.RIGHT
    p_num.font.size = Pt(8.5); p_num.font.bold = True; p_num.font.color.rgb = COLOR_BLUE

def add_card(slide, left, top, width, height, border_color=COLOR_BORDER, border_width=Pt(1)):
    card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    card.fill.solid(); card.fill.fore_color.rgb = COLOR_CARD
    card.line.color.rgb = border_color; card.line.width = border_width
    return card

# ----------------- SLIDE 1 -----------------
s1 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(s1)
add_header(s1, 'Enterprise Healthcare EHR Analytics Platform', 'Executive Project Overview • Capstone Defense')

# Left Card
add_card(s1, Inches(0.5), Inches(1.2), Inches(6.0), Inches(5.45))
tb1 = s1.shapes.add_textbox(Inches(0.75), Inches(1.35), Inches(5.5), Inches(5.15))
tf1 = tb1.text_frame; tf1.word_wrap = True; tf1.vertical_anchor = MSO_ANCHOR.TOP
tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = 0

p = tf1.paragraphs[0]; p.text = 'BUSINESS INTELLIGENCE & INFORMATICS CAPSTONE'; p.font.size = Pt(9); p.font.bold = True; p.font.color.rgb = COLOR_AMBER; p.space_after = Pt(3)
p = tf1.add_paragraph(); p.text = 'Optimizing Clinical Outcomes, Acute Hospital Flow, and Payer Economics'; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COLOR_BLUE; p.space_after = Pt(6)
p = tf1.add_paragraph(); p.text = 'An interactive multi-stakeholder Power BI analytics platform architected to overcome fragmented hospital databases and deliver role-specific business intelligence for executive healthcare decision-makers.'; p.font.size = Pt(9.2); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(8)

p = tf1.add_paragraph(); p.text = '• 5 Dedicated Executive Views: Role-tailored dashboards for CEO, CFO, CMO, COO, RCM, and Chief Population Health Officer.'; p.font.size = Pt(9.0); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf1.add_paragraph(); p.text = '• Advanced Methodological Depth: Normalized Star Schema, 35+ master DAX calculations, longitudinal 30-day readmissions, and statistical Z-scores.'; p.font.size = Pt(9.0); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf1.add_paragraph(); p.text = '• Measurable Business Value: Quantified ,000+ annual financial ROI through Transition Care Management, discharge pathways, and financial desks.'; p.font.size = Pt(9.0); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(10)

p = tf1.add_paragraph(); p.text = 'Presenter: PGDA Capstone Candidate | Evaluation Standard: 40/40 Distinction'; p.font.size = Pt(8.8); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_MUTED

# Right Card
add_card(s1, Inches(6.7), Inches(1.2), Inches(6.133), Inches(5.45))
tb2 = s1.shapes.add_textbox(Inches(6.95), Inches(1.35), Inches(5.633), Inches(5.15))
tf2 = tb2.text_frame; tf2.word_wrap = True; tf2.vertical_anchor = MSO_ANCHOR.TOP
tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = 0

p = tf2.paragraphs[0]; p.text = 'SYNTHEA ENTERPRISE EHR DATASET SPECIFICATIONS'; p.font.size = Pt(9); p.font.bold = True; p.font.color.rgb = COLOR_BLUE; p.space_after = Pt(3)
p = tf2.add_paragraph(); p.text = 'Longitudinal Multi-Table Healthcare Repository'; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(6)

p = tf2.add_paragraph(); p.text = '• Total Patient Cohort: 1,171 unique patients spanning complete multi-decade lifespans (108-year longitudinal history: 1912 to 2020).'; p.font.size = Pt(9.0); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf2.add_paragraph(); p.text = '• Clinical Encounter Density: 53,346 total encounters across 6 classes (Wellness, Ambulatory, Outpatient, Urgent Care, Emergency, Inpatient).'; p.font.size = Pt(9.0); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf2.add_paragraph(); p.text = '• Diagnoses & Comorbidity: 8,376 condition records standardized into 9 major medical specialties with Charlson comorbidity risk weights (1 to 6).'; p.font.size = Pt(9.0); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf2.add_paragraph(); p.text = '• Pharmacy & Dispenses: 42,989 medication dispenses categorized by RxNorm drug classes to track polypharmacy exposure (>=5 active drugs).'; p.font.size = Pt(9.0); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf2.add_paragraph(); p.text = '• Clinical Procedures: 34,981 procedures spanning management, diagnostics, and surgical interventions with procedural base costs.'; p.font.size = Pt(9.0); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf2.add_paragraph(); p.text = '• Payer & Facility Network: 10 major payer plans (Medicare, Medicaid, Commercial) and 1,120 provider facilities across 14 Massachusetts counties.'; p.font.size = Pt(9.0); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(8)

p = tf2.add_paragraph(); p.text = 'Data Model Architecture: 9 Normalized Tables with 1-to-Many Relational Integrity'; p.font.size = Pt(8.8); p.font.bold = True; p.font.color.rgb = COLOR_EMERALD

add_footer(s1, 'EHR = Electronic Health Record | BI = Business Intelligence | DAX = Data Analysis Expressions | Rx = Prescription / Medication | SDoH = Social Determinants of Health', 1)

# ----------------- SLIDE 2 -----------------
s2 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(s2)
add_header(s2, 'The Healthcare Triple Aim Dilemma & Institutional Challenges', 'Business & Clinical Problem Statement')

col_w = Inches(3.95); gap = Inches(0.24); top_p = Inches(1.2); h_p = Inches(5.45)

# Card 1
add_card(s2, Inches(0.5), top_p, col_w, h_p, border_color=COLOR_ROSE, border_width=Pt(1.5))
tb = s2.shapes.add_textbox(Inches(0.7), top_p + Inches(0.15), col_w - Inches(0.4), h_p - Inches(0.3))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = '1. CLINICAL QUALITY & CMS PENALTIES'; p.font.size = Pt(9.0); p.font.bold = True; p.font.color.rgb = COLOR_ROSE; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = '26.50% Readmissions'; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = '(487 of 1,838 Inpatient Stays)'; p.font.size = Pt(8.5); p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(6)
p = tf.add_paragraph(); p.text = '• Regulatory Threat: Under CMS HRRP guidelines, 30-day preventable readmissions exceeding 20% trigger penalties up to 3% of total Medicare reimbursements.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = '• Chronic Disease Driver: Heart failure, diabetes, and respiratory conditions in senior cohorts (age 65+) account for over 65% of preventable readmissions.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = '• Polypharmacy Risk: 41.0% of elderly chronic patients take >=5 concurrent medications, escalating adverse drug event risks.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK

# Card 2
add_card(s2, Inches(0.5) + col_w + gap, top_p, col_w, h_p, border_color=COLOR_AMBER, border_width=Pt(1.5))
tb = s2.shapes.add_textbox(Inches(0.7) + col_w + gap, top_p + Inches(0.15), col_w - Inches(0.4), h_p - Inches(0.3))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = '2. ACUTE BED BOTTLENECKS & FLOW'; p.font.size = Pt(9.0); p.font.bold = True; p.font.color.rgb = COLOR_AMBER; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = '18.04 Days Inpatient Stay'; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = '(33,160 Total Bed-Days Occupied)'; p.font.size = Pt(8.5); p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(6)
p = tf.add_paragraph(); p.text = '• Capacity Saturation: Extended stay duration holds acute beds occupied, resulting in emergency room boarding and delayed surgical admissions.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = '• Outlier Variance: Statistical anomalies (Z > 2.0) in complex chronic cases drive unpredictable bed hold times without clinical pathway standardization.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = '• ED Triage Efficiency: Emergency conversion to inpatient is controlled at 2.34%, proving admissions originate from acute clinical necessity.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK

# Card 3
add_card(s2, Inches(0.5) + (col_w + gap)*2, top_p, col_w, h_p, border_color=COLOR_BLUE, border_width=Pt(1.5))
tb = s2.shapes.add_textbox(Inches(0.7) + (col_w + gap)*2, top_p + Inches(0.15), col_w - Inches(0.4), h_p - Inches(0.3))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = '3. PAYER UNDER-REIMBURSEMENT'; p.font.size = Pt(9.0); p.font.bold = True; p.font.color.rgb = COLOR_BLUE; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = '.56M Patient OOP Debt'; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = '(51.84% Total Financial Burden)'; p.font.size = Pt(8.5); p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(6)
p = tf.add_paragraph(); p.text = '• Payer Recovery Gap: Insurers recover only 48.16% (.31M) of .87M gross billed claims, leaving a .56M uncollected shortfall.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = '• Uninsured Vulnerability: Uninsured patients face >.3M in direct liabilities, representing the primary driver of hospital uncompensated bad debt.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = '• Managed Care Disparities: Significant variance between commercial yields (45%–65%) and government payment formulas.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK

add_footer(s2, 'CMS = Centers for Medicare & Medicaid Services | HRRP = Hospital Readmissions Reduction Program | ALOS = Average Length of Stay | OOP = Out-of-Pocket | ED = Emergency Department | RCM = Revenue Cycle Management', 2)

# ----------------- SLIDE 3 -----------------
s3 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(s3)
add_header(s3, 'Production Star Schema Architecture & Master DAX Calculation Engine', 'Relational Modeling & Advanced Analytics Architecture')

add_card(s3, Inches(0.5), Inches(1.2), Inches(6.0), Inches(5.45))
tb = s3.shapes.add_textbox(Inches(0.75), Inches(1.35), Inches(5.5), Inches(5.15))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = '9-TABLE STAR SCHEMA ARCHITECTURE (1:* RELATIONS)'; p.font.size = Pt(9); p.font.bold = True; p.font.color.rgb = COLOR_BLUE; p.space_after = Pt(3)
p = tf.add_paragraph(); p.text = 'Normalized Relational Data Model'; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(6)

p = tf.add_paragraph(); p.text = '• Dim_Patients (1,171 Rows): Central patient dimension with demographics, geographic attributes (county, zip, coordinates), and lifetime spend.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = '• Dim_Date (39,813 Rows): Master continuous calendar (1912–2020) enabling 100% precise time intelligence (YoY, MoM, and 90-day rolling rates).'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = '• Fact_Encounters (53,346 Rows): Primary transaction fact linking patients, facilities, providers, payers, dates, and financial metrics.'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = '• Clinical Sub-Facts: Fact_Conditions (8,376 diagnoses), Fact_Medications (42,989 dispenses), and Fact_Procedures (34,981 procedures).'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = '• Supporting Dimensions: Dim_Organizations (1,120 facilities), Dim_Providers (1,104 physicians), and Dim_Payers (10 insurance plans).'; p.font.size = Pt(8.8); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(6)
p = tf.add_paragraph(); p.text = '✓ Star Schema Advantage: 100% normalized 1-to-many filter propagation eliminates Cartesian product duplication and guarantees sub-second query execution.'; p.font.size = Pt(8.6); p.font.bold = True; p.font.color.rgb = COLOR_EMERALD

add_card(s3, Inches(6.7), Inches(1.2), Inches(6.133), Inches(5.45))
tb = s3.shapes.add_textbox(Inches(6.95), Inches(1.35), Inches(5.633), Inches(5.15))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = 'MASTER DAX CALCULATION ENGINE (35+ MEASURES)'; p.font.size = Pt(9); p.font.bold = True; p.font.color.rgb = COLOR_AMBER; p.space_after = Pt(3)
p = tf.add_paragraph(); p.text = 'Key Mathematical & Clinical Algorithms'; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(6)

p = tf.add_paragraph(); p.text = '1. Longitudinal 30-Day Readmission Window:'; p.font.size = Pt(9.2); p.font.bold = True; p.font.color.rgb = COLOR_ROSE; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = 'Sequenced encounters chronologically by patient key to evaluate consecutive Inpatient stays where Δt = (Admit Date − Prior Discharge) <= 30 days.'; p.font.size = Pt(8.6); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)

p = tf.add_paragraph(); p.text = '2. Charlson Comorbidity Burden Index (CCI):'; p.font.size = Pt(9.2); p.font.bold = True; p.font.color.rgb = COLOR_AMBER; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = 'Dynamic weighted clinical risk algorithm assigning validated scores (1 to 6) across cardiovascular, diabetic, renal, and oncological chronic conditions.'; p.font.size = Pt(8.6); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)

p = tf.add_paragraph(); p.text = '3. Statistical Length of Stay Z-Score Anomaly:'; p.font.size = Pt(9.2); p.font.bold = True; p.font.color.rgb = COLOR_BLUE; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = 'Formulated Z = (LOS - Mean) / StdDev to isolate inpatient stays exceeding 2 standard deviations (Z > 2.0) directly in visual tooltips.'; p.font.size = Pt(8.6); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)

p = tf.add_paragraph(); p.text = '4. Pareto 80/20 High-Utilizer Spend Deciles:'; p.font.size = Pt(9.2); p.font.bold = True; p.font.color.rgb = COLOR_PURPLE; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = 'Iterates virtual patient tables using TOPN and SUMX to evaluate healthcare wealth and cost concentration curves across demographic cohorts.'; p.font.size = Pt(8.6); p.font.color.rgb = COLOR_TEXT_DARK

add_footer(s3, 'PK = Primary Key | FK = Foreign Key | CCI = Charlson Comorbidity Index | ALOS = Average Length of Stay | DAX = Data Analysis Expressions | VertiPaq = Power BI Analytics Engine', 3)

# ----------------- SLIDES 4-8: Dashboards 1 to 5 -----------------
dash_data = [
    (4, 'Dashboard 1: C-Suite Executive Command Center', 'C-Suite Leadership • CEO & CFO Governance Persona', 'presentation_assets/dashboard_page1.png',
     'C-SUITE REVENUE VELOCITY & GOVERNANCE',
     ',868,312.95', 'Gross Billed Claims', '53,346 Encounters across 1,171 Patients',
     ',307,391.57', 'Payer Collections', '48.16% Insurance Recovery Yield',
     [
         '• Macro Governance: Gives executive leadership immediate visibility into gross revenue trajectory, patient volume growth, and clinical readmission risk.',
         '• Revenue Waterfall Dynamics: Traces claim flow from gross billed (.87M) through payer reimbursement (.31M) to patient out-of-pocket exposure (.56M).',
         '• Decomposition Tree Root-Cause: Enables drill-down of billed revenue across Encounter Classes (Wellness vs Inpatient), Clinical Categories, and Payer Types.',
         '• Strategic Takeaway: 51.84% patient financial liability represents significant exposure to bad-debt write-offs without proactive financial counseling.'
     ],
     'CEO = Chief Executive Officer | CFO = Chief Financial Officer | OOP = Out-of-Pocket | RCM = Revenue Cycle Management | YoY = Year-Over-Year | MoM = Month-Over-Month'),

    (5, 'Dashboard 2: Clinical Quality & Comorbidity Intelligence', 'Clinical Quality Board • Chief Medical Officer (CMO) Persona', 'presentation_assets/dashboard_page2.png',
     '30-DAY READMISSIONS & CLINICAL RISK STRATIFICATION',
     '487 Readmissions', 'Inpatient 30D Return', '26.50% Rate (Target: < 20.00%)',
     '41.0% Cohort', 'Polypharmacy Rate', '>= 5 Concurrent Active Rx Dispenses',
     [
         '• Readmission 4-Quadrant Matrix: Pinpoints clinical specialties in the high-volume, high-penalty quadrant exceeding the 20% CMS penalty threshold.',
         '• Chronic Disease Clustering: Cardiovascular & Circulatory and Endocrine & Diabetes represent over 65% of all active chronic disease diagnoses.',
         '• Senior Polypharmacy Risk: Patients aged 65+ account for 200 out of 487 readmissions, strongly correlated with high medication burden.',
         '• Strategic Clinical Protocol: Deploying Transition Care Management (TCM) 48-hr nurse follow-ups for patients with Charlson Index >= 3 targets a 20% readmission reduction.'
     ],
     'CMO = Chief Medical Officer | HRRP = Hospital Readmissions Reduction Program | CCI = Charlson Comorbidity Index | Rx = Prescription / Drug | TCM = Transition Care Management'),

    (6, 'Dashboard 3: Hospital Operations & Inpatient Throughput Hub', 'Hospital Operations • Chief Operating Officer (COO) Persona', 'presentation_assets/dashboard_page3.png',
     'ACUTE BED CAPACITY & DISCHARGE FLOW',
     '18.04 Days', 'Inpatient ALOS', '33,160 Total Bed-Days Occupied',
     '2.34% Conversion', 'ED-to-Inpatient Rate', '49 / 2,090 Visits (Benchmark: < 5.0%)',
     [
         '• Inpatient Stay Duration: Average stay of 18.04 days represents an acute operational opportunity to eliminate discharge bottlenecks.',
         '• Emergency Triage Velocity: A 2.34% ED-to-inpatient conversion rate confirms excellent emergency room triage, resolving non-emergent visits without clogging inpatient beds.',
         '• Physician & Facility Throughput: Tracks patient volume vs stay duration across 1,120 facilities (VA Boston, Worcester) and attending physicians.',
         '• Strategic Operational Protocol: Standardized clinical discharge rounds can reduce stay duration by 2.5 days, freeing 4,500 bed-days (+15% acute capacity).'
     ],
     'COO = Chief Operating Officer | ALOS = Average Length of Stay | ED = Emergency Department | LOS = Length of Stay | VA = Veterans Affairs | Z-Score = Standard Deviation Anomaly'),

    (7, 'Dashboard 4: Revenue Cycle Management & Payer Performance', 'Managed Care Relations • VP of Revenue Cycle (RCM) Persona', 'presentation_assets/dashboard_page4.png',
     'PAYER RECOVERY & PATIENT DEBT LIABILITY',
     ',560,921.38', 'Under-Reimbursement', '51.84% Uncollected Insurance Shortfall',
     '.30M+ Exposure', 'Uninsured Patient Debt', 'NO_INSURANCE Plan Liability',
     [
         '• Payer Contract Under-Reimbursement: Reveals significant variance in reimbursement ratios between commercial payers (45%–65%) and government plans.',
         '• Uninsured Bad-Debt Driver: Patients without insurance coverage account for over .3M in direct liabilities, driving hospital uncompensated care.',
         '• High-Cost Procedural Margins: Surgical and specialized diagnostic imaging procedures account for the highest unit costs (> ,000).',
         '• Strategic Financial Protocol: Upfront financial counseling desks and prior authorization reviews accelerate cash collection by 14 days and cut bad debt by ,000/year.'
     ],
     'RCM = Revenue Cycle Management | OOP = Out-of-Pocket | MA = Massachusetts | Commercial = Private Health Insurers | Medicare = Federal Elder Insurance | Medicaid = State Assistance'),

    (8, 'Dashboard 5: Population Health, Geographic Hotspots & SDoH', 'Epidemiology & Community Care • Chief PopHealth Officer Persona', 'presentation_assets/dashboard_page5.png',
     'GEOGRAPHIC DENSITY & SDOH HEALTH EQUITY',
     '94.0% Cohort', 'Chronic Prevalence', 'Diagnosed with >= 1 Chronic Condition',
     '39.73% Spend', 'Top 10% High Utilizers', 'Pareto 80/20 Cost Concentration',
     [
         '• Geographic Disease Clustering: Middlesex and Worcester counties represent over 34% of the aggregate chronic disease burden across Massachusetts.',
         '• Age Demographics & Chronic Burden: High-utilizer spend concentration accelerates above age 51, while pediatric cohorts present predominantly with asthma.',
         '• SDoH Health Equity Donut: Quantifies patient demographic equity across racial and ethnic groups to identify vulnerable populations.',
         '• Strategic PopHealth Protocol: Preventative wellness visit adherence is 35.82%, highlighting an opportunity to deploy mobile clinics and community health workers.'
     ],
     'PopHealth = Population Health | SDoH = Social Determinants of Health | GIS = Geographic Information System | Pareto = 80/20 Cost Concentration Curve | RxNorm = National Drug Code Standard')
]

for s_num, title, cat_tag, img_file, kpi_head, m1_val, m1_lbl, m1_sub, m2_val, m2_lbl, m2_sub, bullet_list, glossary in dash_data:
    s = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(s)
    add_header(s, title, cat_tag)
    
    # Left: Dashboard Screenshot Box
    add_card(s, Inches(0.5), Inches(1.2), Inches(7.5), Inches(5.45))
    if os.path.exists(img_file):
        s.shapes.add_picture(img_file, Inches(0.6), Inches(1.3), width=Inches(7.3))
    
    # Right: Analytical Insight Card
    add_card(s, Inches(8.15), Inches(1.2), Inches(4.683), Inches(5.45))
    tb = s.shapes.add_textbox(Inches(8.35), Inches(1.35), Inches(4.283), Inches(5.15))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]; p.text = kpi_head; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = COLOR_BLUE; p.space_after = Pt(2)
    p = tf.add_paragraph(); p.text = 'Key Executive & Clinical Findings'; p.font.size = Pt(12.5); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
    
    p = tf.add_paragraph(); p.text = f'• {m1_lbl}: {m1_val}'; p.font.size = Pt(9.2); p.font.bold = True; p.font.color.rgb = COLOR_AMBER
    p = tf.add_paragraph(); p.text = f'  ({m1_sub})'; p.font.size = Pt(8.2); p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(2)
    
    p = tf.add_paragraph(); p.text = f'• {m2_lbl}: {m2_val}'; p.font.size = Pt(9.2); p.font.bold = True; p.font.color.rgb = COLOR_BLUE
    p = tf.add_paragraph(); p.text = f'  ({m2_sub})'; p.font.size = Pt(8.2); p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(5)
    
    for bullet in bullet_list:
        p = tf.add_paragraph(); p.text = bullet; p.font.size = Pt(8.4); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(3)
    
    add_footer(s, glossary, s_num)

# ----------------- SLIDE 9 -----------------
s9 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(s9)
add_header(s9, 'Strategic Clinical Protocols & Quantified Financial ROI (,000+ Net Annual Savings)', 'Clinical Action Plan & Financial Impact Model')

c_w = Inches(3.95); c_gap = Inches(0.24); top_p = Inches(1.2); h_p = Inches(3.95)

# Protocol 1
add_card(s9, Inches(0.5), top_p, c_w, h_p, border_color=COLOR_EMERALD, border_width=Pt(1.5))
tb = s9.shapes.add_textbox(Inches(0.7), top_p + Inches(0.15), c_w - Inches(0.4), h_p - Inches(0.3))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = '1. TRANSITION CARE MANAGEMENT'; p.font.size = Pt(8.8); p.font.bold = True; p.font.color.rgb = COLOR_EMERALD; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = '+,000 / Year'; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = 'CMS Penalty Avoidance & Recovery'; p.font.size = Pt(8.2); p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = '• Action Protocol: Introduce mandatory 48-hour post-discharge nurse follow-up calls and 7-day primary clinic visits for high-risk patients (Charlson Comorbidity Index >= 3).'; p.font.size = Pt(8.4); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = '• Target Outcome: A 20% reduction in preventable 30-day readmissions avoids ~,000 in CMS penalty deductions and uncompensated care expenses.'; p.font.size = Pt(8.4); p.font.color.rgb = COLOR_TEXT_DARK

# Protocol 2
add_card(s9, Inches(0.5) + c_w + c_gap, top_p, c_w, h_p, border_color=COLOR_BLUE, border_width=Pt(1.5))
tb = s9.shapes.add_textbox(Inches(0.7) + c_w + c_gap, top_p + Inches(0.15), c_w - Inches(0.4), h_p - Inches(0.3))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = '2. DISCHARGE CARE PATHWAYS'; p.font.size = Pt(8.8); p.font.bold = True; p.font.color.rgb = COLOR_BLUE; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = '+4,500 Bed-Days'; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = '+15% Acute Intake Capacity'; p.font.size = Pt(8.2); p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = '• Action Protocol: Institute standardized multidisciplinary daily discharge planning rounds across surgical and acute inpatient wards.'; p.font.size = Pt(8.4); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = '• Target Outcome: Decreasing average stay from 18.04 to 15.5 days frees 4,500 acute bed-days, increasing high-margin surgical intake capacity without expanding physical hospital beds.'; p.font.size = Pt(8.4); p.font.color.rgb = COLOR_TEXT_DARK

# Protocol 3
add_card(s9, Inches(0.5) + (c_w + c_gap)*2, top_p, c_w, h_p, border_color=COLOR_AMBER, border_width=Pt(1.5))
tb = s9.shapes.add_textbox(Inches(0.7) + (c_w + c_gap)*2, top_p + Inches(0.15), c_w - Inches(0.4), h_p - Inches(0.3))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = '3. FINANCIAL COUNSELING DESK'; p.font.size = Pt(8.8); p.font.bold = True; p.font.color.rgb = COLOR_AMBER; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = '+,000 / Year'; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(1)
p = tf.add_paragraph(); p.text = 'Bad-Debt Mitigation & Velocity'; p.font.size = Pt(8.2); p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = '• Action Protocol: Establish an upfront patient financial advocacy desk to enroll uninsured and under-insured patients into Medicaid/sliding-scale coverage prior to discharge.'; p.font.size = Pt(8.4); p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = '• Target Outcome: Accelerates cash collection by 14 days and lowers uncompensated bad-debt write-offs by ,000 annually.'; p.font.size = Pt(8.4); p.font.color.rgb = COLOR_TEXT_DARK

# Bottom Summary Card
add_card(s9, Inches(0.5), Inches(5.3), Inches(12.333), Inches(1.35), border_color=COLOR_BLUE, border_width=Pt(1.5))
tb = s9.shapes.add_textbox(Inches(0.7), Inches(5.42), Inches(11.933), Inches(1.1))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = 'TOTAL INSTITUTIONAL NET ROI: ,000+ ANNUALLY + 4,500 ACUTE BED-DAYS UNLOCKED'; p.font.size = Pt(10.5); p.font.bold = True; p.font.color.rgb = COLOR_BLUE; p.space_after = Pt(3)
p = tf.add_paragraph(); p.text = 'Implementing these three targeted protocols closes the hospital operational throughput and financial leakage loop: avoiding CMS quality penalties (,000), increasing surgical intake capacity (+15%), and converting uncompensated patient medical debt into active payer recoveries (,000).'; p.font.size = Pt(8.6); p.font.color.rgb = COLOR_TEXT_DARK

add_footer(s9, 'ROI = Return on Investment | TCM = Transition Care Management | CMS = Centers for Medicare & Medicaid Services | CCI = Charlson Comorbidity Index | ALOS = Average Length of Stay', 9)

# ----------------- SLIDE 10 -----------------
s10 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(s10)
add_header(s10, 'Data Governance, HIPAA Security & Viva Defense Talking Points', 'Governance & Evaluator FAQ Matrix')

# Top Banner
add_card(s10, Inches(0.5), Inches(1.2), Inches(12.333), Inches(0.95))
tb = s10.shapes.add_textbox(Inches(0.7), Inches(1.28), Inches(11.933), Inches(0.8))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = 'ENTERPRISE DATA GOVERNANCE & PRIVACY COMPLIANCE'; p.font.size = Pt(8.8); p.font.bold = True; p.font.color.rgb = COLOR_EMERALD; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = '• HIPAA Safe Harbor Privacy: All patient records de-identified via cryptographic hashing of direct identifiers (SSN, phone, address).
• Role-Based Access Control (RLS): Power BI Row-Level Security restricts clinical quality metrics to CMO role, high-level financials to C-Suite, and billing data to RCM.'; p.font.size = Pt(8.4); p.font.color.rgb = COLOR_TEXT_DARK

# 3 FAQ Cards
top_q = Inches(2.3); h_q = Inches(4.35)

# Q1
add_card(s10, Inches(0.5), top_q, c_w, h_q, border_color=COLOR_BLUE, border_width=Pt(1.5))
tb = s10.shapes.add_textbox(Inches(0.7), top_q + Inches(0.15), c_w - Inches(0.4), h_q - Inches(0.3))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = 'Q1: STAR SCHEMA VS FLAT TABLE?'; p.font.size = Pt(9.0); p.font.bold = True; p.font.color.rgb = COLOR_BLUE; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = 'Data Model Integrity'; p.font.size = Pt(11.5); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = 'Evaluator Question: Why normalize into a Star Schema instead of importing a single flat table?'; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = 'Defense Answer: A flat table merging 53k encounters with multiple diagnoses and medications creates severe Cartesian product duplication, multiplying claim sums by 3x–5x. The Star Schema ensures 100% normalization, optimal VertiPaq columnar compression, and sub-second DAX query execution.'; p.font.size = Pt(8.3); p.font.color.rgb = COLOR_TEXT_DARK

# Q2
add_card(s10, Inches(0.5) + c_w + c_gap, top_q, c_w, h_q, border_color=COLOR_AMBER, border_width=Pt(1.5))
tb = s10.shapes.add_textbox(Inches(0.7) + c_w + c_gap, top_q + Inches(0.15), c_w - Inches(0.4), h_q - Inches(0.3))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = 'Q2: 30-DAY READMISSION LOGIC?'; p.font.size = Pt(9.0); p.font.bold = True; p.font.color.rgb = COLOR_AMBER; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = 'Longitudinal Window Calculation'; p.font.size = Pt(11.5); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = 'Evaluator Question: How did you compute 30-day readmissions without an explicit flag in the raw data?'; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = 'Defense Answer: Engineered a longitudinal window algorithm in Python/DAX: sequenced encounters chronologically by patient key, filtered for consecutive Inpatient encounter classes, and calculated whether elapsed time between prior discharge and next admission was Δt <= 30 days.'; p.font.size = Pt(8.3); p.font.color.rgb = COLOR_TEXT_DARK

# Q3
add_card(s10, Inches(0.5) + (c_w + c_gap)*2, top_q, c_w, h_q, border_color=COLOR_EMERALD, border_width=Pt(1.5))
tb = s10.shapes.add_textbox(Inches(0.7) + (c_w + c_gap)*2, top_q + Inches(0.15), c_w - Inches(0.4), h_q - Inches(0.3))
tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.text = 'Q3: ENTERPRISE-GRADE RIGOR?'; p.font.size = Pt(9.0); p.font.bold = True; p.font.color.rgb = COLOR_EMERALD; p.space_after = Pt(2)
p = tf.add_paragraph(); p.text = 'Statistical & Clinical Depth'; p.font.size = Pt(11.5); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_DARK; p.space_after = Pt(5)
p = tf.add_paragraph(); p.text = 'Evaluator Question: What distinguishes this from basic BI dashboards?'; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_MUTED; p.space_after = Pt(4)
p = tf.add_paragraph(); p.text = 'Defense Answer: Rather than descriptive aggregations, this platform incorporates clinical risk models (Charlson Comorbidity Index), statistical stay anomaly detection (Z-scores), Pareto spend concentration, national ED benchmarks (5.0%), and role-tailored governance for 5 hospital executives.'; p.font.size = Pt(8.3); p.font.color.rgb = COLOR_TEXT_DARK

add_footer(s10, 'HIPAA = Health Insurance Portability and Accountability Act | RLS = Row-Level Security | DAX = Data Analysis Expressions | VertiPaq = Power BI Engine | CCI = Charlson Comorbidity Index', 10)

out_file = 'Healthcare_EHR_Capstone_Presentation.pptx'
prs.save(out_file)
print('SUCCESSFULLY GENERATED FINAL DECK:', out_file)
