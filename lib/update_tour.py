import argparse
from database import Database

def update_tour(args):
    db = Database()
    query = "UPDATE tours SET name=?, description=?, duration=?, cost=? WHERE tour_id=?"
    db.execute(query, (args.name, args.description, args.duration, args.cost, args.tour_id))
    db.close()

def main():
    parser = argparse.ArgumentParser(description="Update tour details")
    parser.add_argument("--tour_id", required=True, type=int, help="Tour ID")
    parser.add_argument("--name", required=True, help="New Tour Name")
    parser.add_argument("--description", required=True, help="New Tour Description")
    parser.add_argument("--duration", required=True, help="New Tour Duration")
    parser.add_argument("--cost", required=True, help="New Tour Cost")
    args = parser.parse_args()
    update_tour(args)

if __name__ == "__main__":
    main()
