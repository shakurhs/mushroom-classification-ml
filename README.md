# Survival Guide: "Is this Shroom Edible?"

## Repository Outline

Explanation about the content of each file and folder:

1. best_rf_model.pkl - The best ML model used for Data Inference.
2. model_building.ipynb - Notebook containing data processing with Python, starting from loading dataset to ML model evaluation.
3. model_inf.ipynb - Data Inference notebook containing activities from loading the model to making predictions.
4. secondary_data.csv - File sourced from a website used as the dataset for this ML project.
5. url.txt - File containing the Dataset URL and Deployment URL.
6. Deployment - Folder containing related files to perform deployment to HuggingFace.


## Problem Background

This Machine Learning model is a guide to help identify if a mushroom species is safe to eat or dangerous.
In survival situations, experienced explorers usually know how to find food in the wild. However, many people do not have this experience. It is very dangerous if someone tries to survive but eats the wrong mushroom. Eating toxic mushrooms can cause symptoms from mild nausea and vomiting to severe paralysis or even death.
This project aims to prevent these accidents by providing a reliable way to check mushroom safety.

## Project Output

The product generated from this project is a Machine Learning model displayed using a basic Python web app (Streamlit) as the user interface.

## Data

The dataset I obtained comes from the UC Irvine Machine Learning Repository website, which contains specifications and attributes of mushroom species. The data consists of 61,069 rows and 21 columns. When loaded into a data frame, it shows that the dataset has many missing values. For cases where the number of missing values reached more than 80% in a column, I decided to drop those columns. The remaining missing values were handled using SimpleImputer.

## Method

This project is a Supervised Machine Learning Classification Problem to determine the class division of mushroom species. The model used in this project is Random Forest Classification that has gone through a Hyperparameter Tuning process. The Random Forest model was chosen based on the best performance compared to other models like Support Vector Machine, K-Nearest Neighbors, Decision Tree, and AdaBoost. These five models were tested using Cross Validation to produce the best Recall value.

## Stacks

1. Programming Language : Python
2. Tools                : Visual Studio Code, HuggingFace, GitHub
3. Library              : pandas, numpy, scipy, seaborn, matplotlib, scikit-learn, feature_engine, phik, pickle, streamlit,plotly, pillow

## Reference

URL Dataset   : https://archive.ics.uci.edu/dataset/848/secondary+mushroom+dataset
URL Deployment: https://huggingface.co/spaces/shakurhs/Predict_Edible_Mushroom

---