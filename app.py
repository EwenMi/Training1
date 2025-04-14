from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "👋 Hello depuis ta VM Azure (Ansible + Terraform) !"

@app.route("/clement")
def hello_api():
    return {"message": "love you bebou!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
