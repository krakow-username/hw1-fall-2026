# trip_stats.py: summary of trip durations in a Bike Share Toronto trips file

filename = "trips.csv"


def main():
    infile = open(filename)
    header = infile.readline()
    duration = []

    for line in infile:
        line.removesuffix("\n")
        row = line.split(",")
        duration.append(int(row[0]))
    infile.close()

    ordered = sorted(duration)

    print(len(duration))
    print(min(duration))
    print(max(duration))
    print(sum(duration)/ len(duration))
    print((ordered [(len(duration) //2)] + ordered[((len(duration)-1)//2)]) /2)
    
    



if __name__ == "__main__":
    main()