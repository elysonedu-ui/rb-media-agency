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

@app.route('/secret-leads-rb')
def secret_leads():
    leads_html = """
    <html>
    <head>
        <title>RB Media | Controle de Leads</title>
        <style>
            body { background: #020202; color: #fff; font-family: Arial, sans-serif; padding: 40px; }
            h1 { color: #1c6ff8; text-align: center; }
            table { width: 100%; max-width: 800px; margin: 0 auto; border-collapse: collapse; background: #111; }
            th, td { padding: 15px; text-align: left; border-bottom: 1px solid #333; }
            th { background: #1c6ff8; color: #fff; }
            tr:hover { background: #222; }
        </style>
    </head>
    <body>
        <h1>📋 DADOS CRIPTOGRAFADOS DE LEADS</h1>
        <table>
            <tr><th>Nome</th><th>Empresa</th><th>WhatsApp</th><th>Status</th></tr>
    """
    
    if os.path.isfile('leads.csv'):
        with open('leads.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                leads_html += f"<tr><td>{row.get('Nome','')}</td><td>{row.get('Empresa','')}</td><td>{row.get('Telefone','')}</td><td style='color: #25d366;'>NOVO</td></tr>"
    else:
        leads_html += "<tr><td colspan='4' style='text-align:center;'>Nenhum lead registrado ainda.</td></tr>"
        
    leads_html += """
        </table>
        <div style="text-align: center; margin-top: 30px;">
            <a href="/" style="color: #1c6ff8;">Voltar para o site</a>
        </div>
    </body>
    </html>
    """
    return leads_html

if __name__ == '__main__':
    app.run(debug=True, port=5001)
