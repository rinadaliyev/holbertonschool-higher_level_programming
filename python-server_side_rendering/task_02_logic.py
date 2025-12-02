from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/items")
def show_items():
    # Read JSON file
    try:
        with open("items.json", "r") as f:
            data = json.load(f)
            items = data.get("items", [])
    except FileNotFoundError:
        items = []
    except json.JSONDecodeError:
        items = []

    return render_template("items.html", items=items)

if __name__ == "__main__":
    app.run()
