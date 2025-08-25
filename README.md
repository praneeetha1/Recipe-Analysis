# Recipe-Insights-Sentiment-Analysis-Python

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
- **Python**: Pandas, NumPy  
- **Visualization**: Matplotlib, WordCloud  
- **NLP**: HuggingFace `transformers` (BART)  


## 📊 Results## 📊 Results  

### 🔹 Top Ingredients  
Most frequent: `salt`, `sugar`, `butter`, `onion`.  

### 🔹 Distribution of Recipes by Category  
*Add image or chart here (e.g., Bar Chart)*  

### 🔹 Average Calories by Category  
*Add chart here*  

### 🔹 Cook Time vs Rating Correlation  
*Add scatterplot or heatmap*  

### 🔹 Ingredient Frequency (Word Cloud)  
*Add Word Cloud image*  
