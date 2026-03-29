import json
def load_league():
    with open("league.json","r") as f:
        return json.load(f)
    
def save_league(league):
    with open("league.json","w+") as f:
        return json.dump(league,f)
    
def match_has_result(match):
    return "score1" in match

league = load_league()
matches_played = len([m for m in league["matches"] if match_has_result(m)])
matches_total = len(league["matches"])
print(f"League loaded, {matches_played}/{matches_total} games played")
while True:
    print("1. Enter match results")
    action = input()
    if action == "1":
        gameweek = input("Gameweek? ")
        week_matches = [match for match in league["matches"] if match["gameweek"]==gameweek]
        for match in week_matches:
            team1 = match["team1"]
            team2 = match["team2"]
            print(f"{team1} vs {team2}")
            score1_input = input(f"{team1} score? ")
            if score1_input:
                score1 = int(score1_input)
                score2 = int(input(f"{team2} score? "))
                for m in league["matches"]:
                    if m["id"]==match["id"]:
                        m.update({"score1":score1, "score2":score2})
                save_league(league)
                print("Saved.")