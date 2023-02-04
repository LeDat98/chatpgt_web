from flask import Flask, render_template, request
import openai
import requests
import numpy as np

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    openai.api_key = "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"
    question = request.args.get('text')
    if question:
        # Sử dụng hàm completions để nhận đầu ra từ OpenAI GPT-3
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        answer = response["choices"][0]["text"]
        # print(answer)
        #đổi từ chuỗi sang list ngăn cách bởi \n
        def split_string(string):
            return string.split("\n")
        answers = split_string(answer)
        print(answers)
        print(type(answers))
        return render_template('index.html', answers = answers)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
