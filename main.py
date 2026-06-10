import os
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
    nome = data.get('nome')
    empresa = data.get('empresa')
    telefone = data.get('telefone')
    mensagem = data.get('mensagem')
    
    with open('leads.txt', 'a', encoding='utf-8') as f:
        f.write(f"Nome: {nome} | Empresa: {empresa} | Tel: {telefone} | Msg: {mensagem}\n")
        
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
