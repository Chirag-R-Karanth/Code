import requests
import json
import datetime
import csv

# ---------- CONFIG ----------
USERNAMES = {
    "codewars": "your_codewars_username",
    "leetcode": "your_leetcode_username",
    "codeforces": "your_codeforces_handle",
}
OUTPUT_FILE = "coding_progress.csv"


# ---------- HELPERS ----------
def fetch_codewars(user):
    url = f"https://www.codewars.com/api/v1/users/{user}"
    r = requests.get(url).json()
    return {
        "platform": "Codewars",
        "rank": r["ranks"]["overall"]["name"],
        "honor": r["honor"],
        "completed_challenges": r["codeChallenges"]["totalCompleted"],
    }


def fetch_leetcode(user):
    url = "https://leetcode-stats-api.herokuapp.com/" + user
    r = requests.get(url).json()
    return {
        "platform": "LeetCode",
        "total_solved": r.get("totalSolved", 0),
        "easy_solved": r.get("easySolved", 0),
        "medium_solved": r.get("mediumSolved", 0),
        "hard_solved": r.get("hardSolved", 0),
        "ranking": r.get("ranking", None),
    }


def fetch_codeforces(user):
    url = f"https://codeforces.com/api/user.info?handles={user}"
    r = requests.get(url).json()["result"][0]
    return {
        "platform": "Codeforces",
        "rank": r.get("rank", "unrated"),
        "rating": r.get("rating", 0),
        "maxRank": r.get("maxRank", "unrated"),
        "maxRating": r.get("maxRating", 0),
    }


# ---------- MAIN ----------
def main():
    today = datetime.date.today().isoformat()
    results = []

    results.append(fetch_codewars(USERNAMES["codewars"]))
    results.append(fetch_leetcode(USERNAMES["leetcode"]))
    results.append(fetch_codeforces(USERNAMES["codeforces"]))

    # Save to CSV
    fieldnames = ["date"] + list(results[0].keys())
    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if f.tell() == 0:  # write header only once
            writer.writeheader()
        for r in results:
            r["date"] = today
            writer.writerow(r)

    print("Data saved to", OUTPUT_FILE)


if __name__ == "__main__":
    main()
