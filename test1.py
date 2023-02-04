from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    answer = '\n\n1. Hướng dẫn cách thiết lập môi trường Python và cài đặt các thư viện cần thiết\n2. Hướng dẫn cách tạo một ứng dụng web đơn giản bằng Python và Flask\n3. Hướng dẫn cách xây dựng một trò chơi đối kháng sử dụng Pygame\n4. Hướng dẫn cách xây dựng một ứng dụng di động bằng Python và Kivy\n5. Hướng dẫn cách xử lý dữ liệu bằng Python và Pandas'
    answer = answer.replace('\n', '<br>')

    return render_template('index2.html', answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
