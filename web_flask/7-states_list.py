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

    @app.route("/states_list")
    def listingStates():
        from models.state import State
        data = storage.all(State)
        """
            Function to retun "Hello HBNB!".
        """
        sortedDict = dict(sorted(data.items(), key=lambda x: x[1].name))
        from flask import render_template
        return render_template('7-states_list.html', data=sortedDict)

    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
