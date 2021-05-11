data = []
idx = 0

def ni():
    global data, idx
    ret = data[idx]
    idx += 1
    return ret

def main():

    from sys import stdin
    global data, idx
    data = map(int, stdin.read().split())
    idx = 0

    T = ni()
    for t in xrange(T):
        N = ni()
        speed = [ni() for n in xrange(N)]
        free = 1        #First car is always free, no kidding!
        for n in xrange(1, N):
            if speed[n] > speed[n-1]:
                # If this car is faster than previous car, it has to wait
                # decreasing its net speed
                speed[n] = speed[n-1]

            else:
                # Else, it's free to go :)
                free += 1
        print free

main()
