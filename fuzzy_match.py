import pandas as pd
from fuzzywuzzy import process

# Load dataset
df = pd.read_csv("data/sample_data.csv")

# Define threshold for matching (e.g., 90%)
THRESHOLD = 90

# Function to find fuzzy matches
def fuzzy_match(df, column):
    matched_results = []
    seen = set()
    
    for idx, value in enumerate(df[column]):
        if value not in seen:
            matches = process.extract(value, df[column], limit=5)
            for match, score in matches:
                if score >= THRESHOLD and match != value:
                    matched_results.append([value, match, score])
                    seen.add(match)
    
    return pd.DataFrame(matched_results, columns=["Original", "Matched", "Similarity"])

# Run fuzzy matching
result_df = fuzzy_match(df, "Name")

# Save the results
result_df.to_csv("data/matched_results.csv", index=False)

print("Matching complete. Results saved to 'data/matched_results.csv'")
