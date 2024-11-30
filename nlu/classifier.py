import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
import yaml


# Carregar dados (o formato de entrada é o mesmo do treinamento)
data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [], []
for command in data['commands']:
    inputs.append(command['input'].lower().strip())
    action = command['action'] if command['action'] else ""
    outputs.append(f"{command['entity']}\\{action.strip()}")

# Definir comprimento máximo da sequência em bytes
max_seq = max(len(bytes(x.encode('utf-8'))) for x in inputs)
print('Maior seq:', max_seq)

# Codificar inputs usando one-hot encoding em bytes
input_data = np.zeros((len(inputs), max_seq, 256), dtype='float32')
for i, inp in enumerate(inputs):
    for k, ch in enumerate(bytes(inp.encode('utf-8'))):
        input_data[i, k, int(ch)] = 1.0

# Redimensionar os inputs para o formato que o classificador MLP aceita (flatten)
input_data = input_data.reshape(len(inputs), -1)

# Codificar outputs com LabelEncoder
label_encoder = LabelEncoder()
output_data = label_encoder.fit_transform(outputs)

# Treinar modelo MLP (sem o TensorFlow)
model = MLPClassifier(hidden_layer_sizes=(128,), max_iter=500, activation='relu', solver='adam')
model.fit(input_data, output_data)

# Salvar o modelo treinado e as labels
import joblib
joblib.dump(model, 'model.pkl')  # Salvar o modelo
joblib.dump(label_encoder, 'label_encoder.pkl')  # Salvar o LabelEncoder

# Função para classificar novo texto
def classify(text):
    # Criar array de entrada para o texto
    x = np.zeros((1, max_seq, 256), dtype='float32')
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        if k < max_seq:
            x[0, k, int(ch)] = 1.0
    x = x.reshape(1, -1)

    # Fazer previsão
    out = model.predict(x)
    label = label_encoder.inverse_transform(out)
    return label[0]

# Teste de classificação
# while True:
#     text = input('Digite algo: ')
#     print(f"Previsão: {classify(text)}")
