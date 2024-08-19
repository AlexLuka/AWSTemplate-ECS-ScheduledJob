from time import time, sleep


def main():
    print(f"Starting the main application")

    n = 0
    n_max = 60
    delay_sec = 1

    t = time()
    while n < n_max:
        sleep(delay_sec)
        n += delay_sec

    t = time() - t
    print(f"Application took {t:.3f} seconds to complete")
    print(f"Application supposed to run for {n_max:.3f} seconds")
    print(f"Delta: {t - n_max:.3f}")


if __name__ == "__main__":
    main()
