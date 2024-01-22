# Dataset
weather = ['Sunny', 'Overcast', 'Rainy', 'Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy']
play = ['No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']

# Convert lists to dictionary format for easier counting
data = [(weather[i], play[i]) for i in range(len(weather))]

# Calculate Prior Probabilities
def calculate_prior_probabilities(labels):
    total = len(labels)
    return {label: labels.count(label) / total for label in set(labels)}

# Calculate Likelihood
def calculate_likelihood(data, feature, label, feature_index):
    feature_label_count = sum(1 for item in data if item[feature_index] == feature and item[1] == label)
    label_count = sum(1 for item in data if item[1] == label)
    return feature_label_count / label_count

# Naive Bayes Prediction
def naive_bayes_predict(data, new_feature):
    labels = [item[1] for item in data]
    features = set(item[0] for item in data)
    prior_probabilities = calculate_prior_probabilities(labels)
    likelihoods = {label: calculate_likelihood(data, new_feature, label, 0) for label in set(labels)}
    
    # Apply Bayes' Theorem to calculate posterior probabilities
    posteriors = {}
    for label in set(labels):
        posteriors[label] = likelihoods[label] * prior_probabilities[label]
    
    # Prediction based on the highest posterior probability
    return max(posteriors, key=posteriors.get)

# Example Prediction
new_weather = 'Sunny'
prediction = naive_bayes_predict(data, new_weather)
print(f"Prediction for weather {new_weather}: Play = {prediction}")
