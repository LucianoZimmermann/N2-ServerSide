from flask import Flask, jsonify, render_template
from Database import get_db_connection, insert_values, create_all_tables, select_table
import random
import time

app = Flask(__name__)

conn = get_db_connection()
create_all_tables(conn)

vector = None

def initialize_vector():
    global vector
    vector = list(range(1, 50001))
    return vector

def fisher_yates_shuffle(vector):
    for i in range(len(vector) - 1, 0, -1):
        j = random.randint(0, i)
        vector[i], vector[j] = vector[j], vector[i]

def merge_sort(vector):
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
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def merge_sort_recursive(array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = merge_sort_recursive(array[:mid])
        right = merge_sort_recursive(array[mid:])
        return merge(left, right)

    sorted_vector = merge_sort_recursive(vector)
    vector[:] = sorted_vector

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/create', methods=['GET', 'POST'])
def create_vector():
    start = time.time()
    initialize_vector()
    insert_values(conn, "ordered", vector)
    end = time.time()
    final_Time = (end - start) * 1000
    return jsonify(Vetor=vector, Tempo=final_Time)

@app.route('/random', methods=['GET', 'POST'])
def random_vector():
    start = time.time()
    vector = select_table(conn, "ordered")

    if not vector:
        return jsonify(message="Vetor ordenado ainda está vazio. Crie um vetor primeiro."), 404

    fisher_yates_shuffle(vector)
    insert_values(conn, "randomized", vector)
    end = time.time()
    final_Time = (end - start) * 1000
    return jsonify(Vetor=vector, Tempo=final_Time)

@app.route('/reorder', methods=['GET', 'POST'])
def reorder():
    start = time.time()
    vector = select_table(conn, "randomized")

    if not vector:
        return jsonify(message="Vetor aleatório ainda está vazio. Crie um vetor primeiro."), 404

    merge_sort(vector)
    insert_values(conn, "reordered", vector)
    end = time.time()
    final_Time = (end - start) * 1000
    return jsonify(Vetor=vector, Tempo=final_Time)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
