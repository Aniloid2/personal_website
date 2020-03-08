from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def index():
	return render_template("profile.html")

@app.route('/eye')
def eyecam_demo():
	return render_template("eyecam_demo.html")

@app.route('/asv')
def asv_demo():
	return render_template("asv_demo.html")

if __name__ == "__main__":
	app.run(debug=True)