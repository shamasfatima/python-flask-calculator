
from flask import Flask, request, render_template_string

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["number1"])
            op = request.form["operation"]

            if op == "square":
                result = a ** 2
            else:
                b = float(request.form["number2"])

                if op == "+":
                    result = a + b
                elif op == "-":
                    result = a - b
                elif op == "*":
                    result = a * b
                elif op == "/":
                    if b == 0:
                        raise ValueError("Cannot divide by zero.")
                    result = a / b
                elif op == "%":
                    result = a % b
                else:
                    raise ValueError("Invalid operation.")

            result = round(result, 10)

        except ValueError as e:
            error = str(e) or "Please enter valid numbers."
        except (KeyError, TypeError):
            error = "Please enter all required numbers."

    with open("index.html", encoding="utf-8") as file:
        html = file.read()

    return render_template_string(
        html,
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
