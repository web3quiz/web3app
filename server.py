from flask import Flask, request, jsonify

app = Flask(__name__)

# Пример данных пользователей (можно заменить на базу данных)
users_data = {
    123456789: {"balance": 100},
    987654321: {"balance": 200},
}

@app.route('/api/get_balance', methods=['POST'])
def get_balance():
    data = request.get_json()  # Получаем данные в формате JSON
    user_id = data.get('user_id')  # Извлекаем ID пользователя

    if user_id in users_data:
        return jsonify({"balance": users_data[user_id]["balance"]})  # Возвращаем баланс
    else:
        return jsonify({"balance": 0})  # Если пользователя нет, возвращаем 0

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
