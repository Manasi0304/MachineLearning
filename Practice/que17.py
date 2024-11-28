""" 17. Compute Accuracy, Error rate, Precision, Recall for following confusion
matrix ( Use formula for each)
True Positives (TPs): 1 False Positives (FPs): 1
False Negatives (FNs): 8 True Negatives (TNs): 90
"""
# Given values
TP = 1  # True Positives
FP = 1  # False Positives
FN = 8  # False Negatives
TN = 90 # True Negatives

# Total samples
total = TP + FP + FN + TN

# Calculations
accuracy = (TP + TN) / total
error_rate = 1 - accuracy
precision = TP / (TP + FP) if (TP + FP) != 0 else 0
recall = TP / (TP + FN) if (TP + FN) != 0 else 0

# Display the results
print(f"Accuracy: {accuracy:.2f} (or {accuracy * 100:.2f}%)")
print(f"Error Rate: {error_rate:.2f} (or {error_rate * 100:.2f}%)")
print(f"Precision: {precision:.2f} (or {precision * 100:.2f}%)")
print(f"Recall: {recall:.2f} (or {recall * 100:.2f}%)")
