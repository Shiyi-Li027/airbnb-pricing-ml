# Airbnb Pricing Prediction & Market Intelligence in New York City

A machine learning and geospatial analytics project investigating how spatial, socioeconomic, and listing-level factors influence Airbnb pricing behavior across New York City.

This project combines exploratory data analysis (EDA), statistical inference, geospatial visualization, census demographic integration, feature engineering, and predictive modeling to better understand pricing dynamics in short-term rental markets.

---

# Project Overview

Airbnb pricing in large metropolitan areas is influenced by a complex combination of:

* geographic location,
* neighborhood characteristics,
* room and property attributes,
* market demand,
* and local socioeconomic conditions.

This project builds an interpretable machine learning workflow for NYC Airbnb pricing analysis using:

* geospatial data,
* zipcode-level demographic indicators,
* engineered listing features,
* and statistical learning techniques.

The project aims not only to improve predictive performance, but also to generate interpretable and data-driven pricing insights for marketplace participants.

---

# Research Questions

This project investigates several key questions:

* How does Airbnb pricing vary across NYC boroughs and ZIP-code regions?
* Which listing characteristics most strongly influence price?
* How do neighborhood-level socioeconomic conditions relate to Airbnb pricing?
* Can machine learning models effectively predict Airbnb prices?
* Which features contribute most to predictive performance?
* What practical pricing insights can be extracted from the analysis?

---

# Dataset and Data Sources

## Main Data Sources

* Inside Airbnb NYC Listings Dataset
* U.S. Census ACS Demographic Data
* NYC ZIP-code and ZCTA Shapefiles

## Data Scale

The project analyzes:

* 150K+ NYC Airbnb listings
* 70+ engineered variables
* spatial, demographic, and listing-level attributes

## Feature Categories

The workflow integrates multiple feature groups.

### Listing Features

* room type
* property type
* bathrooms
* bedrooms
* accommodates
* amenities
* availability
* review statistics

### Spatial Features

* borough
* ZIP-code
* latitude / longitude
* neighborhood aggregation
* spatial density metrics

### Socioeconomic Features

* median household income
* population density
* demographic indicators
* zipcode-level census statistics

### Textual Features

* sentiment-related listing variables
* description-length variables
* subjectivity-related features

---

# Feature Engineering Pipeline

A substantial portion of the project focused on preprocessing and feature engineering to transform raw Airbnb listing data into a structured machine learning dataset.

The workflow included:

* extracting structured bathroom information from semi-structured text fields,
* generating zipcode variables using official ZCTA shapefiles,
* integrating ACS socioeconomic indicators,
* constructing sentiment and subjectivity variables from listing descriptions,
* engineering host-level and listing-level aggregate variables,
* and generating neighborhood-level spatial metrics.

Additional engineered variables included:

* account age,
* amenities count,
* host verification count,
* listing text-length variables,
* review recency features,
* and zipcode-level listing density statistics.

These preprocessing steps enabled the integration of spatial, demographic, textual, and listing-level information into a unified predictive modeling pipeline.

---

# Methods

## Exploratory Data Analysis (EDA)

The project includes:

* pricing distribution analysis,
* borough-level comparisons,
* ZIP-code heatmaps,
* geospatial visualization,
* correlation analysis,
* and regression diagnostics.

The EDA process was used to identify pricing heterogeneity, spatial clustering behavior, and potential nonlinear relationships between predictors and Airbnb prices.

---

## Statistical Inference and Diagnostics

The project combines predictive modeling with statistical inference to better understand both pricing prediction performance and the statistical significance of pricing drivers.

Statistical analyses include:

* ANOVA,
* Tukey HSD,
* variance analysis,
* multicollinearity diagnostics (VIF),
* residual diagnostics,
* and Q-Q plot analysis.

These methods were used to evaluate statistically significant pricing differences across neighborhoods and property categories.

---

## Machine Learning Models

The predictive modeling pipeline compares:

* OLS Regression
* Ridge Regression
* Lasso Regression
* Elastic Net
* XGBoost

Models were evaluated using:

* R²
* RMSE
* residual diagnostics
* prediction error analysis
* and feature importance analysis

The comparison between Multiple Linear Regression and XGBoost highlights how nonlinear interactions and complex spatial relationships significantly influence Airbnb pricing behavior.

---

# Key Findings

## Spatial Pricing Patterns

The analysis reveals strong geographic heterogeneity in Airbnb pricing across NYC.

* Manhattan listings consistently exhibit the highest average prices.
* Brooklyn and Queens show larger intra-neighborhood variation.
* ZIP-code-level analysis reveals substantial local pricing differences even within the same borough.

These findings suggest that micro-location effects play an important role in short-term rental pricing behavior.

---

## Statistical Findings

The log(price) transformation substantially improves distribution stability and regression behavior.

Statistical inference results show that:

* room type,
* borough,
* and neighborhood characteristics

are statistically significant pricing drivers.

Socioeconomic indicators such as income and population density also demonstrate measurable relationships with Airbnb prices.

---

## Machine Learning Findings

XGBoost substantially outperformed traditional linear regression models by capturing nonlinear feature interactions and complex pricing relationships.

The predictive pipeline improved:

* R² from approximately 0.41 to 0.89
* RMSE to approximately $72

Feature importance analysis highlights several major pricing drivers:

* Manhattan location
* room type
* bathrooms
* accommodates
* neighborhood-level variables
* socioeconomic conditions

Unlike black-box prediction pipelines, this project emphasizes interpretable pricing analysis through statistical diagnostics, regression interpretation, and feature importance analysis.

---

# Business and Market Insights

The analysis suggests that Airbnb pricing behavior is influenced by both local spatial dynamics and broader socioeconomic conditions.

Several practical insights emerge from the results:

* Entire-home listings command substantial price premiums relative to shared or private rooms.
* Manhattan neighborhoods consistently maintain higher pricing power.
* Outer-borough regions exhibit larger pricing dispersion, suggesting stronger neighborhood-level differentiation.
* Socioeconomic and demographic indicators contribute meaningful predictive value beyond simple geographic location.

From a marketplace perspective, these findings may help:

* hosts better understand pricing competitiveness,
* travelers interpret regional pricing variation,
* and urban researchers analyze short-term rental market dynamics.

The project demonstrates how interpretable machine learning and geospatial analytics can support pricing strategy and market intelligence applications.

---

# Repository Structure

```text
airbnb-pricing-ml/
│
│
├── presentation/
│   ├── results/
│   ├── apa.csl
│   ├── presentation_slides.pdf 
│   ├── presentation_slides.qmd
│   ├── references.bib
│   └── styles.css
│
│
└── proposal/
│   ├── apa.csl
│   ├── proposal.pdf
│   ├── proposal.qmd
│   └── references.bib
│
├── sample_data/
│   └── sample_listings.csv
│
├── src/
│   ├── create_sample_data.py
│   └── Unpacking_Airbnb_Pricing.qmd
│
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Reproducibility

The full raw datasets are not included in this public repository due to file size limitations.

A small sample dataset is provided in:

```text
sample_data/sample_listings.csv
```

to demonstrate the dataset structure.

The script below can be used to generate the sample dataset:

```text
src/create_sample_data.py
```

---

# Sample Outputs

The repository includes:

* geospatial heatmaps
* borough-level pricing analysis
* ZIP-code visualizations
* regression diagnostics
* residual analysis
* feature importance plots
* machine learning evaluation outputs

---

# Technologies Used

## Programming and Data Processing

* Python
* pandas
* numpy

## Visualization and Spatial Analytics

* matplotlib
* seaborn
* geopandas
* shapely

## Machine Learning and Statistical Modeling

* scikit-learn
* statsmodels
* xgboost

## Spatial and Demographic Data Integration

* U.S. Census ACS
* ZCTA Shapefiles

## Reproducible Research and Reporting

* Quarto

---

# Author

Shiyi Li

M.S. Candidate in Data Science  
New York University
