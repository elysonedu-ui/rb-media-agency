import os
import csv
from flask import Flask, request, jsonify, render_template
import logging

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato', methods=['POST'])
def contato():
    data = request.get_json()
    nome = data.get('nome', '')
    empresa = data.get('empresa', '')
    telefone = data.get('telefone', '')
    
    # Salvar em formato de Planilha (CSV)
    file_exists = os.path.isfile('leads.csv')
    with open('leads.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nome', 'Empresa', 'Telefone', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
            
        writer.writerow({
            'Nome': nome,
            'Empresa': empresa,
            'Telefone': telefone,
            'Status': 'Novo'
        })
        
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
