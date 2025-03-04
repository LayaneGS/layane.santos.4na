from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize

wine = load_wine() #Load Dataset

dataFrame = pd.DataFrame(wine.data, columns=wine.feature_names) # caracteristicas e classe das amostras
dataFrame['target'] = wine.target


df.head()# Visualizando as primeiras linhas dos dados

# Dividindo os dados em treino e teste (80% treino, 20% teste)
X_treino, X_teste, y_treino, y_teste = treino_teste_split(wine.data, wine.target, test_size=0.2, random_state=42)

scaler = StandardScaler() #Normalizando dados
X_treino_scaled = scaler.fit_transform(X_treino)
X_teste_scaled = scaler.transform(X_teste)


knn = KNeighborsClassifier()#Inicializando classificador knn

k_values = [1, 3, 5, 7, 9] #Testando diferentes valores de K
scores = []


for k in k_values: #Usando validação cruzada para escolher melhor K
    knn = KNeighborsClassifier(n_neighbors=k)
    cv_scores = cross_val_score(knn, X_treino_scaled, y_treino, cv=5, scoring='accuracy')
    scores.append(cv_scores.mean())


best_k = k_values[scores.index(max(scores))] #K q teve o melhor desempenho
best_k, max(scores)

knn = KNeighborsClassifier(n_neighbors=best_k) #Treinando modelo com melhor K
knn.fit(X_treino_scaled, y_treino)


y_predicoes = knn.predict(X_teste_scaled) #Realizando predições no conjunto de teste

##Calculando a acurácia##
accuracy = accuracy_score(y_teste, y_predicoes)
print(f'Acurácia: {accuracy:.4f}')


cm = confusion_matrix(y_teste, y_predicoes)# Calculando a matriz de confusão

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names)
plt.xlabel('Predito')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

##Calculando as métricas##
precision = precision_score(y_teste, y_predicoes, average='weighted')
recall = recall_score(y_teste, y_predicoes, average='weighted')
f1 = f1_score(y_teste, y_predicoes, average='weighted')

print(f'Precisão: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1-Score: {f1:.4f}')


##Binarizando as classes para o cálculo da ROC (one vs rest)##
y_teste_bin = label_binarize(y_teste, classes=[0, 1, 2])
y_predicoes_bin = label_binarize(y_predicoes, classes=[0, 1, 2])

##Calculando a Curva ROC e AUC para cada classe##
fpr, tpr, roc_auc = {}, {}, {}

for i in range(3):
    fpr[i], tpr[i], _ = roc_curve(y_teste_bin[:, i], y_predicoes_bin[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

##Plotando a Curva ROC##
plt.figure()
for i in range(3):
    plt.plot(fpr[i], tpr[i], lw=2, label=f'Classe {wine.target_names[i]} (AUC = {roc_auc[i]:.2f})')

plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Curva ROC para cada classe')
plt.legend(loc='lower right')
plt.show()






