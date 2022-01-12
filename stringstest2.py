# In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are
# Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop tries to output
# these names in order. Of course, that’s not quite right because Ouack and Quack
# are misspelled. Can you fix it?

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p == "O" or p == "Q":
        print(p + "u" + suffix)
    else:
        print(p + suffix)