# sentiment_analysis_product_review
Sentiment Analysis Amazon Product Review using LSTM and DistilBERT

This application is designed to analyze sentiment from Amazon product reviews using LSTM and DistilBERT models.
<img width="1918" height="821" alt="image" src="https://github.com/user-attachments/assets/1fc6a4d5-23f1-4159-a2da-1941a6278463" />

Terdapat 2 fungsi utama dalam aplikasi ini yaitu:
1. Dataset Overview
The dataset used for *fine-tuning* the model is the Amazon Product dataset from <a href="https://www.kaggle.com/datasets/mahmudulhaqueshawon/amazon-product-reviews/data" target="_blank">Kaggle</a>. To prepare the data for our model, we first apply a comprehensive preprocessing pipeline to clean and standardize the information. Recognizing the inherent class imbalance within the dataset, we have strategically applied the random oversampling method to mitigate potential biases and improve model performance on minority classes.
<img width="1918" height="822" alt="image" src="https://github.com/user-attachments/assets/e3202752-f84d-4367-b543-ae16e444a7c1" />

3. Model Implementation
The models used in this application are **Long Short-Term Memory (LSTM)** and **DistilBERT**.
- Long Short-Term Memory (LSTM)
<img width="1918" height="818" alt="image" src="https://github.com/user-attachments/assets/9e63739d-d0ae-4b57-9b6f-2232b96a57e2" />

- DistilBERT
<img width="1918" height="817" alt="image" src="https://github.com/user-attachments/assets/3f38e238-47e3-41fc-80f5-fb3135573aba" />
