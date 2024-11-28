""" 22. Compute Accuracy, Error rate, Precision, Recall for the following
confusion matrix.
Actual Class\Predicted
class
cancer =
yes
cancer = no Total
cancer = yes 90 210 300
cancer = no 140 9560 9700
Total 230 9770 10000 """
# Confusion matrix values
TP = 90  # True Positives
FN = 210 # False Negatives
FP = 140 # False Positives
TN = 9560 # True Negatives

# Compute metrics
accuracy = (TP + TN) / (TP + TN + FP + FN)
error_rate = 1 - accuracy
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0

# Print the results
print(f"Accuracy: {accuracy:.4f}")
print(f"Error Rate: {error_rate:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
