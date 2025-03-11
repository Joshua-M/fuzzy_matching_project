# Fuzzy Matching Algorithm for Data Cleaning

## 📌 Project Overview
This project provides a Python-based fuzzy matching script to clean and deduplicate datasets. It is useful for handling inconsistencies in text-based data such as customer names, product descriptions, and addresses.

## 🔧 How It Works
- Uses the `fuzzywuzzy` library to compare and match similar text entries.
- Applies `pandas` for data processing and merging.
- Assigns similarity scores to potential matches and filters based on a threshold.

## 🛠️ Technologies Used
- Python
- Pandas
- FuzzyWuzzy
- RapidFuzz (optional, for better performance)

## 🚀 Installation & Usage
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR-USERNAME/fuzzy-matching-script.git
cd fuzzy-matching-script
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Script
```sh
python src/fuzzy_match.py
```

## 📊 Example Use Case
### **Input Data (`sample_data.csv`)**
| ID | Name |
|----|----------------|
| 1  | John Doe       |
| 2  | Jon Doe        |
| 3  | J. Doe         |
| 4  | Jane Smith     |
| 5  | Jne Smith      |

### **Output (After Fuzzy Matching)**
| ID | Name        | Matched To | Similarity |
|----|------------|-----------|------------|
| 1  | John Doe   | Jon Doe   | 95%        |
| 2  | Jon Doe    | John Doe  | 95%        |
| 3  | J. Doe     | John Doe  | 90%        |
| 4  | Jane Smith | Jne Smith | 92%        |
| 5  | Jne Smith  | Jane Smith| 92%        |

## 🏗️ Future Improvements
- Optimize performance using `RapidFuzz`.
- Implement ML-based entity resolution.
- Add support for large-scale data processing.

