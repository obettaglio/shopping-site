"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<Customer: %s, %s, %s, %s>" % (
            self.first_name, self.last_name, self.email, self.password)

customers = {}


def read_customers_from_file(filepath):

    for line in open(filepath):
        (first_name,
         last_name,
         email,
         password) = line.strip().split("|")

        customers[email] = Customer(first_name,
                                    last_name,
                                    email,
                                    password)

    return customers


def get_by_email(email):
    return customers[email]


read_customers_from_file('customers.txt')
