import argparse
from database import Database

def delete_tour(args):
    db = Database()
    query = "DELETE FROM tours WHERE tour_id=?"
    db.execute(query, (args.tour_id,))
    db.close()

def main():
    parser = argparse.ArgumentParser(description="Delete a tour")
    parser.add_argument("--tour_id", required=True, type=int, help="Tour ID to delete")
    args = parser.parse_args()
    delete_tour(args)

if __name__ == "__main__":
    main()
