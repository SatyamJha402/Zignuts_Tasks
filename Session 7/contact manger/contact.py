class ContactManager:
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"{name} added")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} removed")
        else:
            print(f"{name} not found")

    def search_contact(self, name):
        return self.contacts.get(name, "Contact not found")

    def show_all(self):
        for name, info in self.contacts.items():
            print(f"{name}, Phone: {info['phone']}, Email: {info['email']}")


# cm = ContactManager()
# cm.add_contact("satyam", "12345", "satyam@egmail.com")
# cm.add_contact("shivam", "67890", "shivam@gmail.com")

# cm.show_all()
# print(cm.search_contact("satyam"))
