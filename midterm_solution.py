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
