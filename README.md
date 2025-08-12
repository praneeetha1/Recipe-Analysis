# Recipe-Insights-Sentiment-Analysis-Python

I worked on this project to explore **recipe and review data** and uncover patterns in cooking trends, popular ingredients, and how users feel about the recipes they try.  
It’s a mix of **data analysis** and **NLP-based sentiment classification** using a Hugging Face transformer model.


## 📖 Project Overview
I wanted to understand:
- Which recipe categories and ingredients are the most popular  
- How cooking times vary across recipes  
- How well review sentiment aligns with actual star ratings  

To do this, I:
1. Cleaned and preprocessed the dataset  
2. Performed exploratory data analysis (EDA)  
3. Used a Hugging Face `transformers` model for sentiment analysis  
4. Compared predicted sentiments with given star ratings  


## 📂 Dataset
- **Original Source:** [Food.com Recipes & Reviews](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews)  
- **My Cleaned Dataset:** [Recipe Data (Kaggle Notebook)](https://www.kaggle.com/code/praneetharao/recipe-data)  


## ⚙️ Tools & Libraries

- **Python**: `pandas`, `matplotlib`, `tqdm`  
- **NLP**: Hugging Face `transformers`, `distilbert-base-uncased-finetuned-sst-2-english`


## 📊 Results
### 🍽 Recipe Trends
- Dessert recipes came out as the most common  
- Most frequent ingredients: `salt`, `sugar`, `butter`, `onion`  
- Highly rated recipes often had **10+ reviews**  

### 💬 Sentiment Insights
- Analyzed **500+ reviews** for sentiment  
- Added `sentiment_label` and `sentiment_score` columns  
- Found strong alignment between review sentiment and star ratings  
