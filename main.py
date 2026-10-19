from pyscript import document, display

members = ["Joshua Ortiz", "Maria Santos", "John Cruz"]

from pyscript import document

def check_member(event):
    first = document.getElementById("first").value
    last = document.getElementById("last").value

    fullname = first + " " + last

    message = f"Congratulations {fullname}! You are now part of the Glee Club."

    document.getElementById("result").innerText = message
