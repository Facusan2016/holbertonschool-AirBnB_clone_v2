#!/usr/bin/python3
"""
    Main program for Flask application.
"""
if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def helloBnb():
        """
            Function to retun "Hello HBNB!".
        """
        return "Hello HBNB!"

    @app.route("/hbnb")
    def hbnb():
        """
            Function to retun "HBNB".
        """
        return "HBNB"

    @app.route("/c/<text>")
    def cName(text):
        """
            Function to return the text variable with a C.
        """
        formatted_text = text.replace('_', ' ')
        return f'C {formatted_text}'

    @app.route('/python/', defaults={'text': 'is_cool'})
    @app.route("/python/<text>")
    def PythonName(text):
        """
            Function to return the text variable with a C.
        """

        formatted_text = text.replace('_', ' ')
        return f'Python {formatted_text}'

    @app.route("/number/<int:n>")
    def routeNum(n):
        """
            Route that returns the number if it's an integer
        """
        return f"{n} is a number"

    @app.route("/number_template/<int:n>")
    def routeNumTemplate(n):
        """
            Route that returns a html if n is an integer
        """
        from flask import render_template
        return render_template('5-number.html', n=n)

    @app.route("/number_odd_or_even/<int:n>")
    def routeNumTemplateOddOrEven(n):
        """
            Route that returns a html if n is an integer
        """
        from flask import render_template
        return render_template('6-number_odd_or_even.html', num=n)

    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
