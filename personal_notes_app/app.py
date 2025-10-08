from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
        return redirect(url_for("home"))
    return render_template("index.html",notes=notes)

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect(url_for("home"))
    
if __name__ == "__main__":

        app.run(debug= True)
