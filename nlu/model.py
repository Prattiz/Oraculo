import yaml
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


# Carregar os dados do arquivo YAML
data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [], []

# Preparando os inputs e outputs
for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append(f"{command['entity']}|{command['action']}" if command['action'] else f"{command['entity']}\\{command['entity']}")

# Processar o texto e rótulos
vectorizer = CountVectorizer(analyzer='char')
X = vectorizer.fit_transform(inputs)

# Codificar os rótulos com LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(outputs)

# Criar um modelo simples de Naive Bayes
model = make_pipeline(CountVectorizer(analyzer='char'), MultinomialNB())

# Treinar o modelo
model.fit(inputs, outputs)

# Salvar o modelo e os rótulos
with open('labels.txt', 'w', encoding='utf-8') as fwrite:
    for label in label_encoder.classes_:
        fwrite.write(label + '\n')

# Função para classificar um novo texto
def classify(text):
    prediction = model.predict([text.lower()])
    print(f'Predição: {prediction[0]}')

# Exemplo de uso