import torch
import torch.nn as nn
import torch.optim as optim
import syft as sy
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

hook = sy.TorchHook(torch)
clients = []
for _ in range(3):  
    client = sy.VirtualWorker(hook, id=f"client_{_}")
    clients.append(client)


data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


client_datasets = []
for client in clients:
    X_client = torch.tensor(X_train).send(client)
    y_client = torch.tensor(y_train).send(client)
    client_datasets.append((X_client, y_client))