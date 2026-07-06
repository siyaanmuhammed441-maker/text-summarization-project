# 📝 Text Summarization using T5 Transformer

## 📌 Project Overview

This project is an AI-powered Text Summarization system built using the **T5 (Text-to-Text Transfer Transformer)** model from Hugging Face Transformers. It generates concise and meaningful summaries from long news articles while preserving the key information.

The model is trained on the **CNN/DailyMail** dataset and provides high-quality abstractive summaries.

---

## 🚀 Features

- Automatic text summarization
- Uses Google's pre-trained T5-Small model
- CNN/DailyMail dataset
- Text preprocessing and cleaning
- ROUGE evaluation
- Interactive Streamlit Web Application
- Fast and accurate summary generation

---

## 📂 Dataset

**Dataset:** CNN/DailyMail 3.0.0

Contains:
- News Articles
- Human-written Summaries

Dataset Columns:

- article
- highlights
- id

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Regular Expressions (re)
- Hugging Face Transformers
- PyTorch
- Datasets
- Evaluate
- ROUGE Score
- Streamlit

---

## 📊 Project Workflow

1. Import Libraries
2. Load CNN/DailyMail Dataset
3. Exploratory Data Analysis (EDA)
4. Data Cleaning & Preprocessing
5. Load T5 Tokenizer
6. Load Pre-trained T5 Model
7. Generate Summary
8. Compare with Human Summary
9. Evaluate using ROUGE
10. Deploy with Streamlit

---

## 📈 Model Evaluation

Evaluation Metric:

- ROUGE-1
- ROUGE-2
- ROUGE-L
- ROUGE-Lsum

### Results

| Metric | Score |
|---------|-------|
| ROUGE-1 | **0.48** |
| ROUGE-2 | **0.27** |
| ROUGE-L | **0.45** |
| ROUGE-Lsum | **0.45** |

These scores indicate that the generated summaries closely match the human-written summaries.

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/text-summarization-t5.git
```

Go to the project folder

```bash
cd text-summarization-t5
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Text-Summarization/
│
├── app.py
├── text_summarization_project.ipynb
├── requirements.txt
├── README.md
├── cnn_dailymail_train.csv
└── images/
```

---

## 📝 Example

### Input

```
Daniel Radcliffe gains access to his £20 million fortune as he turns 18. The Harry Potter actor says he has no plans to spend his money on luxury cars or celebrity parties.
```

### Generated Summary

```
Daniel Radcliffe says he has no plans to waste his money on expensive cars or celebrity parties and intends to stay grounded.
```

---

## 🎯 Future Improvements

- Fine-tune T5 on custom datasets
- Support multiple languages
- Upload PDF and DOCX files
- Adjustable summary length
- Batch summarization
- Deploy on cloud platforms

---

## 👨‍💻 Author

**Siyan**

AI & Data Science Student

---

## ⭐ If you found this project useful, give it a Star!
