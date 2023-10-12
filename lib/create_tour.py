import argparse
from database import Database
from models import Tour

def create_tour(args):
    db = Database()
    tour = Tour(args.name, args.description, args.duration, args.cost)
    query = "INSERT INTO tours (name, description, duration, cost) VALUES (?, ?, ?, ?)"
    db.execute(query, (tour.name, tour.description, tour.duration, tour.cost))
    db.close()

def main():
    parser = argparse.ArgumentParser(description="Create a new tour")
    parser.add_argument("--name", required=True, help="Tour Name")
    parser.add_argument("--description", required=True, help="Tour Description")
    parser.add_argument("--duration", required=True, help="Tour Duration")
    parser.add_argument("--cost", required=True, help="Tour Cost")
    args = parser.parse_args()
    create_tour(args)

if __name__ == "__main__":
    main()
