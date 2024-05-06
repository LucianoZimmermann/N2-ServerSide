from flask import Flask, render_template

app = Flask(__name__)

# Variável global para armazenar o vetor
vector = None

# Função para inicializar o vetor com valores de 1 a 50000
def initialize_vector():
    global vector
    vector = list(range(1, 50001))
    return vector

# Função para embaralhar o vetor usando Fisher-Yates shuffle
def fisher_yates_shuffle(vector):
    import random
    # Percorre o vetor de trás para frente
    for i in range(len(vector) - 1, 0, -1):
        # Gera um índice aleatório de 0 a i
        j = random.randint(0, i)
        # Troca os elementos nas posições i e j
        vector[i], vector[j] = vector[j], vector[i]

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('home.html')

# Rota para criar um vetor ordenado
@app.route('/create', methods=['GET'])
def create_vector():
    # Inicializa o vetor com valores de 1 a 50000
    initialize_vector()
    # Renderiza o vetor como está
    return render_template('create_vector.html', vector=vector)

# Rota para criar um vetor embaralhado
@app.route('/random', methods=['GET'])
def random_vector():
    # Inicializa o vetor com valores de 1 a 50000
    initialize_vector()
    # Embaralha o vetor
    fisher_yates_shuffle(vector)
    # Renderiza o vetor embaralhado
    return render_template('create_vector.html', vector=vector)

# Rota para reordenar o vetor
@app.route('/reorder', methods=['GET'])
def reorder():
    # Inicializa o vetor com valores de 1 a 50000
    initialize_vector()
    # Função para ordenar o vetor (usando merge sort ou outro método)
    merge_sort(vector)
    # Renderiza o vetor ordenado
    return render_template('create_vector.html', vector=vector)

# Função para ordenar o vetor usando merge sort
def merge_sort(vector):
    # Função auxiliar para combinar duas metades ordenadas
    def merge(left, right):
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # Adiciona o restante dos elementos de left ou right
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    # Função de recursão para dividir e combinar
    def merge_sort_recursive(array):
        if len(array) <= 1:
            return array
        # Divide a lista ao meio
        mid = len(array) // 2
        left = merge_sort_recursive(array[:mid])
        right = merge_sort_recursive(array[mid:])
        # Combina as duas metades ordenadas
        return merge(left, right)

    # Ordena o vetor usando merge sort
    sorted_vector = merge_sort_recursive(vector)
    # Atualiza o vetor original com os elementos ordenados
    vector[:] = sorted_vector

# Executa o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)
