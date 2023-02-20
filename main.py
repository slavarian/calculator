from flask import Flask, render_template, request

app: Flask = Flask(__name__)


@app.route('/')
def main() -> str:
    return render_template('index.html')


@app.route("/calculate", methods=['POST'])
def calculate():
    try:
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            result = float(num1) + float(num2)
            return render_template('index.html', result=result)

        elif operation == 'subtract':
            result = float(num1) - float(num2)
            return render_template('index.html', result=result)

        elif operation == 'multiply':
            result = float(num1) * float(num2)
            return render_template('index.html', result=result)

        elif operation == 'divide':
            result = float(num1) / float(num2)
            return render_template('index.html', result=result)
    except ValueError:
        return render_template('index.html', result="Вы не корректно ввели число")


if __name__ == "__main__":
    app.run(
        port=8800,
        debug=True
    )
