from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Bienvenue sur l'application Flask ! 🎉</h1>"

@app.route("/hello")
def hello():
    html = """
    <html>
      <head>
        <title>Bienvenue !</title>
        <style>
          body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f8ff;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
          }
          .container {
            text-align: center;
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
          }
          h1 {
            color: #007acc;
            margin-bottom: 10px;
          }
          p {
            font-size: 18px;
            color: #333;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>👋 Bonjour et bienvenue !</h1>
          <p>Cette page a été déployée automatiquement via GitHub Actions 🚀</p>
        </div>
      </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
