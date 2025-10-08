# =========================================
# Deloitte Finance Insights Portal
# =========================================
# Built by Zakir Umudov, Deloitte Consulting 🧠
# Purpose: Record, view, and analyze client transactions


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In memory data (temporary)
transactions = [
    {"id":1, "client": "Apple Inc.", "amount": 25000},
    {"id":2, "client": "Microsoft", "amount": 40000}
]

# HOME PAGE

@app.route("/")
def home():
    total = sum(t["amount"] for t in transactions)
    return render_template("home.html", transactions = transactions, total = total)


# ADD TRANSACTION PAGE

@app.route("/add", methods = ["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        client = request.form.get("client")
        amount = float(request.form.get("amount"))
        new_id = len(transactions) + 1
        transactions.append({"id": new_id, "client": client, "amount": amount})
        return redirect(url_for("home"))
    return render_template("add_transaction.html")


# FEEDBACK PAGE

@app.route("/feedback", methods = ["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        comment = request.form.get("comment")
        return render_template("thankyou.html", name =name, comment = comment)
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True, port = 8080)
