import sys
def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    t_len = int(input_data[1])

    events = []

    for i in range(2, 2 * n + 1, 2):
        a_i = int(input_data[i])
        b_i = int(input_data[i + 1])
        events.append((a_i, 0))
        events.append((b_i, 1))

    events.sort()
    akutalny_snieg=0
    max_snieg=0
    index=0
    for snieg,czy in events:
        if czy == 1:
            akutalny_snieg-=1
        else:
            akutalny_snieg+=1
        if akutalny_snieg>max_snieg:
            max_snieg=akutalny_snieg
            index=snieg
    print(f"{max_snieg} {index}")

if __name__ == "__main__":
    main()

