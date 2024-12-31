from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Página inicial

@app.route("/gerar_senha", methods=["POST"])
def gerar_senha():
    # Captura o valor da chave enviado pelo formulário
    chave = request.form.get("chave", "")  # Valor padrão é uma string vazia

    # Inicializa a senha
    senha = ""
    for letra in chave:
        if letra in "Aa":
            senha = senha + "@"
        elif letra in "Bb":
            senha = senha + "8"
        elif letra in "Cc":
            senha = senha + "1"
        elif letra in "Dd":
            senha = senha + "2"
        elif letra in "Ee":
            senha = senha + "3"
        elif letra in "Ff":
            senha = senha + "7"
        elif letra in "Gg":
            senha = senha + "6"
        elif letra in "Hh":
            senha = senha + "4"
        elif letra in "Ii":
            senha = senha + "!"
        elif letra in "Jj":
            senha = senha + "%"
        elif letra in "Kk":
            senha = senha + "5"
        elif letra in "Ll":
            senha = senha + "|"
        elif letra in "Mm":
            senha = senha + "#"
        elif letra in "Nn":
            senha = senha + letra
        elif letra in "Oo":
            senha = senha + "0"
        elif letra in "Pp":
            senha = senha + "9"
        elif letra in "Qq":
            senha = senha + letra
        elif letra in "Rr":
            senha = senha + "/"
        elif letra in "Ss":
            senha = senha + "$"
        elif letra in "Tt":
            senha = senha + "+"
        elif letra in "Uu":
            senha = senha + ")"
        elif letra in "Vv":
            senha = senha + "^"
        elif letra in "Ww":
            senha = senha + "}"
        elif letra in "Xx":
            senha = senha + letra
        elif letra in "Yy":
            senha = senha + letra
        elif letra in "Zz":
            senha = senha + letra
        elif letra in "0":
            senha = senha + "o"
        elif letra in "1":
            senha = senha + "I"
        elif letra in "2":
            senha = senha + "B"
        elif letra in "3":
            senha = senha + "E"
        elif letra in "4":
            senha = senha + "A"
        elif letra in "5":
            senha = senha + "H"
        elif letra in "6":
            senha = senha + "G"
        elif letra in "7":
            senha = senha + "T"
        elif letra in "8":
            senha = senha + "&"
        elif letra in "9":
            senha = senha + "P"
    
    # Renderiza o HTML com a senha gerada
    return render_template("index.html", senha=senha)

if __name__ == "__main__":
    app.run(debug=True)