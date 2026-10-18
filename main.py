from pyscript import document, display


from flask import Flask, render_template, request, redirect, url_for

app

# Initial club members
members = [
    ("Alice", "Blue"),
    ("Anita", "Bath"),
    ("Billy", "Sparks"),
    ("Eileen", "Dover"),
    ("Ella", "Vator"),
    ("Francisco", "Portero"),
    ("Joe", "Kerr"),
    ("Juanito", "Lakarin"),
    ("Justin", "Case"),
    ("Ligaya", "Anonuevo"),
    ("Paige", "Turner"),
    ("Restituto", "Fruto"),
    ("Sheldon", "Cooper"),
    ("Tam", "Nguyen"),
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name", "").strip()
        last_name = request.form.get("last_name", "").strip()

        if first_name and last_name:
            new_member = (first_name.title(), last_name.title())

            # Prevent duplicate members
            if new_member not in members:
                members.append(new_member)

        return redirect(url_for("index"))

    # Sort by first name, then last name
    sorted_members = sorted(
        members,
        key=lambda member: (member[0].lower(), member[1].lower())
    )

    return render_template(
        "index.html",
        members=sorted_members,
        total=len(sorted_members)
    )


if __name__ == "__main__":
    app.run(debug=True)