#PhishGuard AI: Phishing Email Detection

PhishGuard AI is a lightweight machine learning application designed to identify potentially malicious emails based on behavioral patterns. Using a **Bernoulli Naive Bayes classifier** and a custom dataset, the tool evaluates key risk factors like link presence and domain trust to provide real-time security analysis.

##Project Overview

**Core Objective:**
Provide a simple, accessible tool for non-technical users to verify email legitimacy without requiring deep cybersecurity knowledge.

**Target Features:**
The system evaluates four primary indicators:

* Hyperlinks
* Attachments
* Urgent Tone
* Domain Trust

**Interface:**
Built using **Tkinter**, the GUI offers a straightforward checkbox system for quick input and instant visual feedback.


##Project Structure
```
PlaintextML_MINI/
├── data/
│   └── phishing.csv         # Custom dataset with categorical features
├── model/
│   ├── label_encoder.pkl    # Serialized preprocessing encoder
│   └── model.pkl            # Trained Bernoulli Naive Bayes model
├── app.py                   # Main GUI application logic
└── train.py                 # Model training and evaluation script
```

## Technical Implementation

### Machine Learning Pipeline

**Preprocessing:**
Categorical "Yes/No" inputs are converted into binary numerical format (1 and 0) for model compatibility.

**Algorithm:**
Bernoulli Naive Bayes was chosen due to its efficiency with binary features and strong performance on smaller datasets.

**Training:**
The model is trained using an 80/20 train-test split and achieves high accuracy in detecting patterns within the dataset.


##Tech Stack
* **Language:** Python
* **Libraries:**
  * Pandas (Data Handling)
  * Scikit-learn (Machine Learning)
  * Pickle (Model Storage)
* **GUI:** Tkinter

##Getting Started

**1. Install Requirements**
```bash
pip install pandas scikit-learn
```
**2. Train the Model**
```bash
python train.py
```
**3. Run the Application**
```bash
python app.py
```

##Observations & Future Scope

**Current State:**

* Provides instant predictions
* Low computational overhead
* Relies on manual feature selection instead of raw email content

**Future Improvements:**

* Integrate NLP for direct email content analysis
* Develop a browser extension for real-world usage
* Enhance dataset for better generalization
