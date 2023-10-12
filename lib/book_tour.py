import argparse
from database import Database

def book_tour(args):
    db = Database()
    query = "INSERT INTO bookings (customer_id, tour_id, booking_date) VALUES (?, ?, ?)"
    db.execute(query, (args.customer_id, args.tour_id, args.date))
    db.close()

def main():
    parser = argparse.ArgumentParser(description="Book a tour")
    parser.add_argument("--customer_id", required=True, type=int, help="Customer ID")
    parser.add_argument("--tour_id", required=True, type=int, help="Tour ID")
    parser.add_argument("--date", required=True, help="Booking Date")
    args = parser.parse_args()
    book_tour(args)

if __name__ == "__main__":
    main()
