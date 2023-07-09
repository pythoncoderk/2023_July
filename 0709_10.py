import itertools
for value, group in itertools.groupby("aaaaaavvvvbgtttthssssseeegggggaaaasgdgfskkfghdgsdgaerga"):
    print(f"{value}: {list(group)}")