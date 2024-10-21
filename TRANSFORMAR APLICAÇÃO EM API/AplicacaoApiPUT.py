from flask import Flask, request

app = Flask(__name__)

#estou declarando que essa função é um GET
@app.route('/',methods=['GET'])
def home():
    return {"message": "Bem vindo Jubs, esta é a sua API"}

#estou declarando que esta função é um POST 
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() # vai me devolver um arquivo JSON
    #lógica para criar um usuario com  os dados recebidos
    return{"message": "Usuário cirado com sucesso!"}

if __name__ == '__main__':
    app.run(debug='True')