from flask import Flask, render_template

site = Flask(__name__)
# criar a página do site

#rota -> site.com/home
#função -> o que exibir
#template
@site.route("/")
def home():
    return render_template("index.html")

@site.route("/contatos")
def contatos():
    return render_template("contatos.html")

@site.route("/central")
def central():
    return render_template("central.html")

@site.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)
#site no ar = provisório
if __name__ == "__main__":
    site.run(debug=True) #atualiza automaticamente as alterações