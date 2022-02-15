from flask import Flask, request

from lib_model import predict

app = Flask(__name__)

@app.route('/test')
def test():
    name = request.args.get('my-param')
    if name:
        html = f"""
        <!doctype html>
        <html>
        <head>
            <title>My HTML Page</title>
        </head>
        <body>
            <button type="button" onclick="onButtonClicked('{name}')">Click Me</button>
            <script type="text/javascript">
            function onButtonClicked(message){{
                alert("My Name is " + message);
            }}
            </script>
        </body>
        </html>
        """
        return html;
    return "api test"

@app.route('/predict')
def predict_api():
    age = request.args.get('age') # 숫자 1 ~ 89
    graduated = request.args.get('graduated') # Yes / No
    '''
    Homemaker
    Artist
    Healthcare
    Lawyer
    Entertainment
    Executive
    Marketing
    Doctor
    Engineer
    '''
    profession = request.args.get('profession')
    spending_score = request.args.get('spending_score') # Low, Average, High

    prediction = predict(int(age), graduated, profession, spending_score)

    return prediction[0]

if __name__ == '__main__':
    app.run()