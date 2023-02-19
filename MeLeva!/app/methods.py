from app import app
from flask import request, render_template

users = {}


# home page
@app.route("/", methods=['GET'])
def inicio():
    return render_template('index.html')


# Home do usuario
@app.route("/home", methods=['GET', 'POST'])
def home_passageiro():
    return render_template('home.html')


@app.route("/atividade", methods=['GET', 'POST'])
def atividade_passageiro():
    return render_template('atividade.html')


# Home do motorista
@app.route("/home_motorista", methods=['GET', 'POST'])
def home_motorista():
    return render_template('home_motorista.html')


@app.route("/atividade_motorista", methods=['GET'])
def atividade_motorista():
    return render_template('atividade_motorista.html')

@app.route("/iniciando_viagem", methods=['GET', 'POST'])
def iniciando_viagem():
    return render_template('iniciando_viagem.html')

@app.route("/perfil", methods=['GET'])
def perfil():
    return render_template('perfil.html')


@app.route("/mensagens", methods=['GET'])
def mensagens():
    return render_template('mensagens.html')


@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')


# login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get form
        usuario = request.form['usuario']
        senha = request.form['senha']

        # autenticar usuario
        if usuario in users and users[usuario] == senha:
            return render_template('selectRole.html')

        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html', error='Invalid username or password')


# signin

@app.route("/signin", methods=['GET'])
def cadastro():
    return render_template('signin.html')


@app.route("/configuracoes", methods=['GET'])
def configuracoes():
    return render_template('configuracoes.html')


@app.route("/ajuda", methods=['GET'])
def ajuda():
    return render_template('ajuda.html')


@app.route("/signin", methods=['POST'])
def user():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    usuario = request.form['usuario']
    senha = request.form['senha']
    n_matricula = request.form['nMatricula']
    bday = request.form['bday']

    users[usuario] = senha

    return render_template('usuario.html', nome=nome, cpf=cpf, email=email, usuario=usuario, senha=senha,
                           nMatricula=n_matricula, bday=bday)
