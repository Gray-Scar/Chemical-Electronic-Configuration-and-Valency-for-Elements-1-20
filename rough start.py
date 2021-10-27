atomic_num = int(input("What's the atomic number? Has to be from 1-20 btw. "))
ato = atomic_num

if ato == 2 or ato < 2:
    k = ato

if ato > 2:
    k = 2

L = ato - k
if L == 0:
    if k == 2:
        electronic_config = 2
        valency = "+2-"
        print(f"Electronic Configuration is {electronic_config}. Valency is {valency}.")
        quit()

    if k == 1:
        electronic_config = 1
        valency = "-1"
        print(f"Electronic Configuration is {electronic_config}. Valency is {valency}.")
        quit()

if L == 8 or L < 8:
    L = L

if L > 8:
    L = 8

m = ato - (L + k)
if k == ato - L:
    electronic_config = f"2, {L}"
    if ato > 4 or ato == 4 and ato < 9:
        if L != 4:
            if ato != 4:
                val1 = 8 - L
                valency = f"-{val1}"
            if ato == 4:
                valency = "+2"
        if L == 4:
            valency = "+4-"
    if ato == 3:
        valency = "+1"
    if ato == 10:
        valency = "shared"
    print(f"Electronic Configuration is {electronic_config}. and the Valency is {valency}.")
    quit()

if m == 18 or m < 18:
    m = m

if m > 18:
    m = 8

if m < 9:
    valency = f"+{m}"
if m == 9:
    valency = "+9-"
if m > 9:
    val1 = 18 - m
    valency = f"-{val1}"

print(f"Electronic Configuration is {k}, {L}, {m}. And the valency is {valency}")
