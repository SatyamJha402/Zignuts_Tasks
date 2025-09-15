import json
from contact import ContactManager

with open("contact_details.json") as f:
    data = json.load(f)

cm = ContactManager()
for c in data["contacts"]:
    cm.add_contact(c["name"], c["phones"], c["emails"])

cm.show_all()
