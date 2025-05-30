# Semantic equivalence detection

## Method 1: Pre-trained Cross Encoder

The file cross_encoder_final.ipynb contains all code need to load the pre-trained model, finetune it, and run it on the test set. \n The resulting model from our fine-tuning can be loaded in the notebook as, simply by running the relevant cell. \n Make sure to follow the steps to unzip the dataset below. If there are issues with loading data, you might have to adjust the "path" variable for the dataset. 

## Method 2: Logistic Regression with TF-IDF

This method implements a simple and effective non-neural baseline for duplicate question detection using logistic regression and lexical similarity features.

### Data Preparation

* The input data is a cleaned version of the Quora Question Pairs dataset: `question_pairs_cleaned.csv.zip`
* It contains the fields: `id`, `qid1`, `qid2`, `question1`, `question2`, and `is_duplicate`
* Label `1` indicates the questions are duplicates; `0` indicates they are not

### Steps

1. **Load and Clean Data**

   * Unzip the dataset and load it using pandas
   * Drop rows with missing values
   * Convert the `is_duplicate` label to integer

2. **TF-IDF Feature Extraction**

   * Use `TfidfVectorizer` to convert each question into a sparse vector
   * Fit on the combined text of `question1` and `question2`
   * Use both unigrams and bigrams with a vocabulary limit of 10,000 features

3. **Similarity Feature**

   * For each question pair, compute the row-wise dot product between TF-IDF vectors as an approximation of cosine similarity
   * This produces a single numeric feature per pair

4. **Feature Combination**

   * Concatenate TF-IDF vectors of `question1` and `question2` and the similarity score into a single sparse feature matrix

5. **Model Training**

   * Use `LogisticRegression` with the `saga` solver
   * Enable `class_weight='balanced'` to handle class imbalance
   * Use `n_jobs=-1` and `verbose=1` to parallelize and monitor progress

6. **Evaluation**

   * Split the dataset into training and testing sets (80/20)
   * Evaluate using accuracy, precision, recall, F1-score, and confusion matrix

### Output Example

```
Accuracy: 0.771
F1-score (duplicates): ~0.71
Confusion Matrix:
[[39310 11585]
 [ 6900 22940]]
```

This method provides a strong lexical baseline and helps measure the value added by more advanced semantic or neural approaches.

The full implementation can be found in the notebook: `TF-IDF.ipynb`.
