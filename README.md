# Recipe Analysis | Python

I worked on this project to explore **recipe and review data** to uncover patterns in cooking trends, popular ingredients, and user ratings.  



## 📖 Project Overview
- Cleaned & transformed raw recipe and review data.  
- Classified missing categories using **Zero-Shot Classification (BART)**.  
- Performed **EDA**: category distribution, calorie trends, ingredient frequency.  
- Visualised patterns like review timelines and ratings vs. cook time.  


## 📂 Dataset
- **Original Source:** [Food.com Recipes & Reviews](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews)  
- **My Cleaned Dataset:** [Recipe Data (Kaggle Notebook)](https://www.kaggle.com/code/praneetharao/recipe-data)  



## 🔑 Features  
✔ Cleaned and structured data (removed R-style vectors, formatted times).  
✔ Grouped 311 categories → **17 major categories**.  
✔ Predicted missing categories with HuggingFace **BART model**.  
✔ Visualised:  
  - Recipe distribution by category  
  - Average calories by category  
  - Cook time vs. rating  
  - Ingredient frequency (Bar & Word Cloud)  
✔ Identified top contributors and interesting recipes.


## 🛠 Tech Stack  
- **Python:** Pandas, NumPy
- **Visualization:** Matplotlib, WordCloud
- **NLP:** HuggingFace Transformers (BART)
- 

## 📊 Results

### 🔹 Top Ingredients  
Most frequent ingredients found across recipes are:

- **Salt**
- **Sugar**
- **Butter**
- **Onion**

### 🔹 Distribution of Recipes by Category  
A pie chart shows the distribution of recipes, with top categories like Meal, Dessert, and Meat leading.

*Insert Pie Chart Image here*

### 🔹 Average Calories by Category  
Pie recipes have the highest average calories (~740.5), followed by Bread (~668.6) and Dessert (~616.9).

*Insert Bar Chart here*

### 🔹 Cook Time vs Rating Correlation  
Scatterplots show no strong relationship between total cook time and average rating across recipes.

*Insert Scatterplot Image here*

### 🔹 Ingredient Frequency (Word Cloud)  
The top ingredients by usage count include salt, butter, sugar, onion, and water.

A Word Cloud visualisation highlights the most common ingredients aesthetically.

*Insert Word Cloud Image here*
