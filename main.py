from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/contato', methods=['POST'])
def contato():
    data = request.get_json()
    nome = data.get('nome')
    empresa = data.get('empresa')
    telefone = data.get('telefone')
    mensagem = data.get('mensagem')

    if not all([nome, empresa, telefone]):
        return jsonify({"error": "Preencha os campos obrigatórios."}), 400

    # Simulação de envio de e-mail / salvamento de lead no banco
    print(f"NOVO LEAD RECEBIDO: {nome} | {empresa} | {telefone}")
    print(f"Mensagem: {mensagem}")

    return jsonify({"success": "Sua solicitação foi enviada. Entraremos em contato em breve."})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Usando 5001 para não conflitar com a barbearia
