# Thesis Project

- Author 💻✍: Diego Acosta Ugalde
- Description 🖇: This notebook contains all the implementations of my thesis project. The structure is shown in the Table of Contents.
- Date of creation 📅: 8/Feb/2024

----

MODULES

1 -> Preprocessing: text cleaning, stop words removal, lemmatization.

2 -> Initial Data Exploration: distribution analysis, correlation analysis, transformation using a threshold.

3 -> Text Representations Analysis
    3.1 -> TF-IDF analysis, WordCloud, topwords in TFIDF. Word Emeddings, demonstration of the embeddings, PCA and tSNE over the embeddings, LDA analysis.
    3.2 -> Similarity of the embeddings analysis, range of values for the cosine similarity using USE and BERT embeddings.

4 -> Pipeline ABSA: Topic Classification using the similarity of the best embeddings found in 3.2, followed by Sentiment Classification using ML, DL and Attention-based models.

5 -> Multitask ABSA: Implementation of both TC and SC using a multitask and pretrained model from Hugging Face.