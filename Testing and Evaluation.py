
X_test_tensor = torch.tensor(X_test).float()
y_test_tensor = torch.tensor(y_test).float().unsqueeze(1)

with torch.no_grad():
    predictions = global_model(X_test_tensor)
    accuracy = ((predictions > 0.5).float() == y_test_tensor).float().mean()
print(f"Test Accuracy: {accuracy.item() * 100:.2f}%")