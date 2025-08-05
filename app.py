from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    tip = None

    if request.method == "POST":
        crop = request.form["crop"]
        rainfall = float(request.form["rainfall"])
        temperature = float(request.form["temperature"])
        area = float(request.form["area"])
        fertilizer = float(request.form["fertilizer"])
        pesticides = float(request.form["pesticides"])
        soil_type = request.form["soil_type"]

        yield_score = (
            rainfall * 0.25 +
            temperature * 0.25 +
            fertilizer * 0.2 +
            pesticides * 0.1 +
            (10 if soil_type.lower() in ["loamy", "black", "alluvial"] else -5)
        ) * area
        if yield_score > 1000:
            result = f"🌱✨ {crop.capitalize()} is a Fantastic Choice for your Farm!"
            tip = f"💡 Tip: Make sure to rotate {crop.lower()} with legumes to maintain soil health."
        else:
            result = f"🚫 {crop.capitalize()} may not grow well in this environment."
            tip = f"📌 Try adjusting fertilizer levels or choosing crops suited for {soil_type} soil."

    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🌾 Smart Crop Buddy</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    @keyframes animateBG {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    body {
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(135deg, #d4fc79, #96e6a1, #a1c4fd, #c2e9fb);
 background-size: 300% 300%;
      animation: animateBG 15s ease infinite;
      margin: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
    }

    .glass-card {
      background: rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(15px);
      border-radius: 20px;
      padding: 30px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
      width: 100%;
      max-width: 500px;
    }

    h1 {
      text-align: center;
      color: #1e3d59;
      font-size: 28px;
      margin-bottom: 10px;
    }

    .mascot {
      font-size: 50px;
      text-align: center;
 animation: bounce 2s infinite;
    }

    @keyframes bounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
    }

    label {
      display: block;
      margin-top: 12px;
      font-weight: bold;
      color: #0b3d20;
    }

    input, select {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 10px;
    }

    button {
      width: 100%;
      margin-top: 20px;
      padding: 12px;
      font-size: 16px;
      border: none;
      border-radius: 12px;
      background-color: #2d6a4f;
      color: white;
      font-weight: bold;
      cursor: pointer;
      transition: transform 0.2s;
  }

    button:hover {
      background-color: #1b4332;
      transform: scale(1.03);
    }

    .result, .tip {
      text-align: center;
      margin-top: 20px;
      font-size: 18px;
      font-weight: bold;
      color: #003b2f;
    }

    .tip {
      font-size: 15px;
      font-style: italic;
      color: #4f772d;
    }
  </style>
</head>
<body>
  <div class="glass-card">
    <div class="mascot">👨‍🌾</div>
    <h1>Smart Crop Predictor</h1>
    <form method="POST">
      <label for="crop">Crop Name:</label>
      <input type="text" name="crop" id="crop" required>

      <label for="rainfall">Rainfall (mm):</label>
      <input type="number" step="any" name="rainfall" id="rainfall" required>
                                  
      <label for="temperature">Temperature (C):</label>
      <input type="number" step="any" name="temperature" id="temperature" required>


      <label for="area">Area (hectares):</label>
      <input type="number" step="any" name="area" id="area" required>

      <label for="fertilizer">Fertilizer Used (kg):</label>
      <input type="number" step="any" name="fertilizer" id="fertilizer" required>

      <label for="pesticides">Pesticides Used (tonnes):</label>
      <input type="number" step="any" name="pesticides" id="pesticides" required>

      <label for="soil_type">Soil Type:</label>
      <select name="soil_type" id="soil_type" required>
        <option value="" disabled selected>Select soil type</option>
        <option value="loamy">Loamy</option>
        <option value="black">Black</option>
        <option value="red">Red</option>
        <option value="alluvial">Alluvial</option>
        <option value="laterite">Laterite</option>
        <option value="desert">Desert</option>
        <option value="mountain">Mountain</option>
        <option value="peaty">Peaty</option>
        <option value="saline">Saline</option>
        <option value="sandy">Sandy</option>
        <option value="clay">Clay</option>
      </select>
<button type="submit">🚜 Predict Now</button>
    </form>

    {% if result %}
      <div class="result">{{ result }}</div>
    {% endif %}
    {% if tip %}
      <div class="tip">{{ tip }}</div>
    {% endif %}
  </div>
</body>
</html>
    """, result=result, tip=tip)

if __name__ == "__main__":
    app.run(debug=True)