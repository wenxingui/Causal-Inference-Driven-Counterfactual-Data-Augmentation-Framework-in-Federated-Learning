class SimpleMLP(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_dim, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        return self.layers(x)

def federated_training(clients, model, epochs=10):

    opt = optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.BCELoss()
    
    for epoch in range(epochs):
        for client in clients:

            X, y = client_datasets[clients.index(client)]
            
     
            cf_samples = torch.randn(10, X.shape[1])  
            X_aug = torch.cat([X, cf_samples], dim=0)
            y_aug = torch.cat([y, torch.ones(10)], dim=0)
            

            model.send(client)
            opt.zero_grad()
            pred = model(X_aug.float())
            loss = criterion(pred.squeeze(), y_aug.float())
            loss.backward()
            opt.step()
            model.get()
            
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")


global_model = SimpleMLP(X_train.shape[1])
federated_training(clients, global_model)