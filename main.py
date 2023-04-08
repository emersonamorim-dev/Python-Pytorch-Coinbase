import torch
import torch.nn as nn
import pandas as pd
from sklearn.model_selection import train_test_split
import requests
import json

# dados do arquivo CSV para um dataframe do Pandas
df = pd.read_csv('coinbase_data.csv')

df['output'] = df['output'].apply(lambda x: 1 if x == 'positive' else 0)

# conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(df.drop('output', axis=1), df['output'], test_size=0.2)

# Cria um modelo de rede neural usando Pytorch
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(7, 16)
        self.fc2 = nn.Linear(16, 32)
        self.fc3 = nn.Linear(32, 1)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

net = Net()

criterion = nn.BCELoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

for epoch in range(100):
    optimizer.zero_grad()
    output = net(X_train)
    loss = criterion(output, y_train.unsqueeze(1).float())
    loss.backward()
    optimizer.step()
    
# Teste o modelo usando os dados de teste e calcule a precisão
with torch.no_grad():
    output = net(X_test)
    predicted = (output > 0.5).float()
    accuracy = (predicted == y_test.unsqueeze(1).float()).sum().item() / len(y_test)
    print(f"Accuracy: {accuracy}")

# criptomoedas de interesse
coins = ['BTC', 'ETH', 'LTC']

# Api da Coinbase
url = 'https://api.coinbase.com/v2/prices/'

# Captura os preços das criptomoedas

prices = {}
for coin in coins:
    response = requests.get(url + coin + '-USD/spot')
    data = json.loads(response.text)
    prices[coin] = float(data['data']['amount'])
print(prices)

# Adiciona os preços capturados ao dataframe do Pandas
df['BTC_price'] = prices['BTC']
df['ETH_price'] = prices['ETH']
df['LTC_price'] = prices['LTC']

# conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(df.drop('output', axis=1), df['output'], test_size=0.2)
