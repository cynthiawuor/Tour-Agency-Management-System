import argparse
from database import Database
from models import Customer

def add_customer(args):
    db = Database()
    customer = Customer(args.name, args.contact, args.preferences)
    query = "INSERT INTO customers (name, contact, preferences) VALUES (?, ?, ?)"
    db.execute(query, (customer.name, customer.contact, customer.preferences))
    db.close()

def main():
    parser = argparse.ArgumentParser(description="Add a new customer")
    parser.add_argument("--name", required=True, help="Customer Name")
    parser.add_argument("--contact", required=True, help="Customer Contact")
    parser.add_argument("--preferences", required=True, help="Customer Preferences")
    args = parser.parse_args()
    add_customer(args)

if __name__ == "__main__":
    main()
