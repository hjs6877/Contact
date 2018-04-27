class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def print_info(self):
        print("name : ", self.name)
        print("phone_number : ",  self.phone_number)
        print("email : ", self.email)
        print("address : ", self.address)


def set_contact():
    name = input('Name: ')
    phone_number = input('Phone Number: ')
    email = input('Email: ')
    address = input('Address: ')
    print(name, phone_number, email, address)


def run():
    set_contact()


if __name__ == '__main__':
    run()
