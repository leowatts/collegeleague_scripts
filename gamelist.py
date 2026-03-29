import random
random.seed(5)

oxford_weeks = ["MT3","MT4","MT5","MT6","HT1","HT2","HT3","HT4","HT5","HT6","TT1"]

def rotate(arr):
    return arr[:1]+arr[-1:]+arr[1:-1]

teams = ["Baliol","Five Seas","Jahns","Merton","Spades","Turl St","Brasenose","Wolfson/Hughs","Worcester","Hildas","Hertford","[bye]"]
random.shuffle(teams)
rounds = []

num_rounds = len(teams)-1
assert num_rounds == 11
assert len(oxford_weeks) == 11

for i in range(num_rounds):
    oxford_week = oxford_weeks[i]
    # print(f"=== GAMEWEEK {i+1} (end of {oxford_week}) ===")
    games = []
    bye = None
    for a,b in zip(teams[:len(teams)//2],teams[-1:len(teams)//2-1:-1]):
        if a!="[bye]" and b!="[bye]":
            games.append((a,b))
        elif a=="[bye]":
            bye=b
        elif b=="[bye]":
            bye=a
        else:
            assert False
    assert bye != None
    for a,b in games:
        print(f"[GW{i+1} {oxford_week}] {a} vs {b}")
    teams = rotate(teams)