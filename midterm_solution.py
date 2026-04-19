heroes = [
    ("Layla", "Marksman"),
    ("Tigreal", "Tank"),
    ("Gusion", "Assassin"),
    ("Kagura", "Mage"),
    ("Chou", "Fighter")
]

ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

print("\n==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")

for i in range(len(heroes)):
    print(str(i + 1) + ". " + heroes[i][0] + " [" + heroes[i][1] + "]")

print("==========================================")

matches = []
highest_kda = -1
best_match_index = -1

for i in range(1, 5):
    print("\n---MATCH " + str(i) + "---")

    hero_num = int(input("Hero number (1-5) or 0 to skip: "))

    if hero_num == 0:
        print("Match skipped.")
        continue

    if hero_num < 1 or hero_num > 5:
        print("Invalid hero number. Skipping match.")
        continue

    kills = int(input("Kills: "))
    deaths = int(input("Deaths: "))
    assists = int(input("Assists: "))
    result = input("Result (W/L): ").upper()

    kda = (kills + assists) / max(1, deaths)

    if kda >= 5:
        tag = "DOMINATION!"
    else:
        tag = "Better Luck Next Game"

    matches.append({
        "hero": heroes[hero_num - 1][0],
        "kda": kda,
        "result": result,
        "tag": tag
    })

    if kda > highest_kda:
        highest_kda = kda
        best_match_index = len(matches) - 1

wins = 0

for m in matches:
    if m["result"] == "W":
        wins += 1

total = len(matches)
losses = total - wins

if total > 0:
    win_rate = int((wins / total) * 100)
else:
    win_rate = 0

print("\n=============================================")
print("     " + ign + " -- MATCH LOG (" + rank + ")")
print("=============================================")

for i in range(len(matches)):
    m = matches[i]

    if m["result"] == "W":
        res = "WIN"
    else:
        res = "LOSS"

    print("[" + str(i + 1) + "] " + m["hero"] +
          " | KDA: " + str(round(m["kda"], 2)) +
          " | " + res +
          " | " + m["tag"])

print("---------------------------------------------")
print("Matches Played : " + str(total))
print("Wins : " + str(wins) + "  |  Losses : " + str(losses))
print("Win Rate       : " + str(win_rate) + "%")

if best_match_index != -1:
    best = matches[best_match_index]
    print("Best Match     : [" + str(best_match_index + 1) + "] " +
          best["hero"] + " (KDA: " + str(round(best["kda"], 2)) + ")")

print("=============================================")
