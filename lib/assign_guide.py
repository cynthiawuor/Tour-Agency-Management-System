import argparse
from database import Database

def assign_guide(args):
    db = Database()
    query = "INSERT INTO guide_assignments (guide_id, tour_id, assignment_date) VALUES (?, ?, ?)"
    db.execute(query, (args.guide_id, args.tour_id, args.date))
    db.close()

def main():
    parser = argparse.ArgumentParser(description="Assign a guide to a tour")
    parser.add_argument("--guide_id", required=True, type=int, help="Guide ID")
    parser.add_argument("--tour_id", required=True, type=int, help="Tour ID")
    parser.add_argument("--date", required=True, help="Assignment Date")
    args = parser.parse_args()
    assign_guide(args)

if __name__ == "__main__":
    main()
