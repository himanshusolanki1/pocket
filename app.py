from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/script-endpoint", methods=["POST"])
def send_combined_script():
    scripts = [
        "script1_ai_button.js",
        "script2_load_svg.js",
        "script3_demo_to_real.js"
    ]
    combined = ""
    for s in scripts:
        with open(f"static/js/{s}", encoding='utf-8') as f:
            combined += f.read() + "\n"
    return Response(combined, mimetype="application/javascript")

@app.route("/")
def home():
    return "✅ Server is Live - POST to /script-endpoint"
