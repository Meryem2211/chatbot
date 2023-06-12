from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")

    # Send the message to OpenAI's API and receive the response
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        ).choices[0].text.strip()

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"response": str(e)})

if __name__ == '__main__':
    app.run()
