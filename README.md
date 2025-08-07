# Recipe-Insights-Sentiment-Analysis-Python

This project explores recipe and review data to uncover trends in cooking patterns and user sentiment. Using Python for data analysis and a Hugging Face transformer model for sentiment classification, we draw insights from both the recipes and the text of user reviews.

---

## 🔍 What this project covers

- 🧾 Analysis of recipe data: ingredients, categories, cooking time, and ratings
- 💬 Sentiment analysis of user reviews using a pre-trained NLP model
- 📈 Visualizations to highlight popular ingredients, categories, and recipe ratings
- 📊 Comparison of user ratings with inferred sentiment from review text

---

## ⚙️ Tools & Libraries

- **Python**: pandas, matplotlib, tqdm
- **NLP**: Hugging Face `transformers`, `distilbert-base-uncased-finetuned-sst-2-english`
- **Data Source**: Recipe and review dataset with metadata like ratings, ingredients, and instructions

---

## 📊 Key Highlights

### 🥘 Recipe Trends
- Most frequent category: `Dessert`
- Common ingredients: `salt`, `sugar`, `butter`, `onion`
- High-rated recipes usually have at least 10+ reviews

### 💡 Sentiment Insights
- Used Hugging Face sentiment pipeline on 500+ user reviews
- Added `sentiment_label` and `sentiment_score` for each review
- Found strong alignment between review sentiment and star ratings
