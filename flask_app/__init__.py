from flask import Flask, request

from .lib_model import predict

def create_app():

    app = Flask(__name__)

    '''
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
    '''
    @app.route('/')
    def index():
        return f"""
            <!doctype html>
            <html>
            <head>
                <title>Project 3</title>
            </head>
            <body>

                <form name="frm" id="frm" method="get" target="_self" action="">
                    <input type="number" name="age" min="1" max="89" placeholder="Age" />
                    <fieldset>
                        <legend>Graduated</legend>
                        <label>
                            <input type="radio" name="graduated" value="Yes" />
                            <span>Yes</span>
                        </label>
                        <label>
                            <input type="radio" name="graduated" value="No" />
                            <span>No</span>
                        </label>
                    </fieldset>
                    <select name="profession">
                        <option value="">- Profession -</option>
                        <option value="Homemaker">Homemaker</option>
                        <option value="Artist">Artist</option>
                        <option value="Healthcare">Healthcare</option>
                        <option value="Lawyer">Lawyer</option>
                        <option value="Entertainment">Entertainment</option>
                        <option value="Executive">Executive</option>
                        <option value="Marketing">Marketing</option>
                        <option value="Doctor">Doctor</option>
                        <option value="Engineer">Engineer</option>
                    </select>
                    <fieldset>
                        <legend>Spending Score</legend>
                        <label>
                            <input type="radio" name="spending_score" value="Low" />
                            <span>Low</span>
                        </label>
                        <label>
                            <input type="radio" name="spending_score" value="Average" />
                            <span>Average</span>
                        </label>
                        <label>
                            <input type="radio" name="spending_score" value="High" />
                            <span>High</span>
                        </label>
                    </fieldset>
                    <input type="submit" value="Submit" />
                </form>
                
                <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
                <script type="text/javascript">
                var frm = document.forms.frm;
                frm.onsubmit = function(e){{
                    e.preventDefault();

                    axios.get("/predict", {{
                        params: {{
                            age: frm.age.value,
                            graduated: frm.graduated.value,
                            profession: frm.profession.value,
                            spending_score: frm.spending_score.value
                        }}
                    }}).then(function(response){{
                        alert(response.data);
                    }});
                }}
                </script>
            </body>
            </html>
            """

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

    return app