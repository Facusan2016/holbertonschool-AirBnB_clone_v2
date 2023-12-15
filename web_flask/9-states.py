#!/usr/bin/python3
"""
    Main program for Flask application.
"""

if __name__ == "__main__":
    from flask import Flask
    from models import storage

    app = Flask(__name__)

    @app.teardown_appcontext
    def tearDownApp(self):
        storage.close()

    @app.route("/states/")
    def listingStates():
        """
            Function to retun "Hello HBNB!".
        """
        from models.state import State
        data = storage.all(State)
        from flask import render_template
        return render_template('7-states_list.html', data=data)

    @app.route("/states/<id>")
    def listingStatesById(id):
        """
            Function to retun "Hello HBNB!".
        """
        from models.state import State
        from flask import render_template

        states = storage.all(State)
        for state in states.values():
            if id == state.id:
                return render_template('9-states.html', state=state)

        return "<H1>Not found!</H1>"

    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
