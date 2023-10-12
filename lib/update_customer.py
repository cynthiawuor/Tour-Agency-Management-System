import argparse
from database import Database

def update_customer(args):
    db = Database()
    query = "UPDATE customers SET name=?, contact=?, preferences=? WHERE customer_id=?"
    db.execute(query, (args.name, args.contact, args.preferences, args.customer_id))
    db.close()

def main():
    parser = argparse.ArgumentParser(description="Update customer information")
    parser.add_argument("--customer_id", required=True, type=int, help="Customer ID")
    parser.add_argument("--name", required=True, help="New Customer Name")
    parser.add_argument("--contact", required=True, help="New Customer Contact")
    parser.add_argument("--preferences", required=True, help="New Customer Preferences")
    args = parser.parse_args()
    update_customer(args)

if __name__ == "__main__":
    main()
