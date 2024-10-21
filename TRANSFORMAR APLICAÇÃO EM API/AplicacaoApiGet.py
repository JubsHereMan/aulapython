#instalando o framework: Flask !!
#pip intall flask

from flask import Flask

#o objetivo do flask é de: fazer com que a minha aplicação se aplique via WEB

app = Flask(__name__)#framework
#         __name__  vai fazer rodar no servidor: quero que o as coisas rodem baseadas no nome da minha aplicação 

@app.route('/') #rota 
def hello(): #metodo GET
    return {"message": "Hello, JUBS"}

if __name__ == '__main__':
    app.run(debug='True')