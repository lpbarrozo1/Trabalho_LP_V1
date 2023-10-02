from flask import Flask, render_template, request, redirect, url_for

meu_site = Flask(__name__, template_folder='templates') 

@meu_site.route("/")
@meu_site.route("/index")  
def index():
    return render_template ("t_index.html") 

@meu_site.route("/usuarios/<nome_usuario>;<nome_profissao>")

@meu_site.route("/usuarios", defaults={"nome_usuario":"usuário?","nome_profissao":""})  
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  

#new
@meu_site.route("/login")
def login():
    return render_template("t_login.html") 

@meu_site.route("/autenticar", methods=['GET', 'POST']) 
def autenticar():
    usuario = request.form.get('nome')
    senha = request.form.get('password')
    return f"usuario: {usuario} e senha: {senha}"
    

@meu_site.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cofemail = request.form['confEmail']
        password = request.form['password']
        confpassword = request.form['confpassword']
        dn=request.form['dn']
        cpf=request.form['cpf']
        endereco = request.form['endereco']
        tel = request.form['tel']
        genero = request.form['genero']
        return redirect(url_for('t_index'))
    return render_template('cadastro.html')

@meu_site.route('/sucesso')
def sucesso():
    return f"Parabéns! Cadastro realizado com sucesso!"

if __name__ == "__main__":
    meu_site.run(port=8080, debug=True)

