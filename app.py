from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    location = request.args.get("location", "Unknown location")
    recommendations = [
        {"name": "Restaurant A", "rating": 4.5, "description": "Great food and cozy atmosphere."},
        {"name": "Restaurant B", "rating": 4.0, "description": "Nice ambiance with creative dishes."},
        {"name": "Restaurant C", "rating": 3.8, "description": "Affordable with excellent service."}
    ]
    
    return jsonify({
        "location": location,
        "recommendations": recommendations
    })

if __name__ == "__main__":
    app.run(debug=True)