from flask import Flask, render_template, request, redirect, session, flash, url_for


app = Flask(__name__)
app.secret_key = 'alura'
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
ljogos = [jogo1, jogo2, jogo3]        

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=ljogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', ptoxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    ljogos.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['ususario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash(request.form['usuario'] + ' Não logado, tente novamente!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado!')
    return redirect(url_for('index'))


app.run(debug=True)
