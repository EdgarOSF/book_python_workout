def run_timing():
    numbers_of_runs = 0
    total_time = 0

    while True:
        one_run  = input('Enter 10k run time ')

        if not one_run:
            break

        numbers_of_runs += 1
        total_time += float(one_run)

        average = total_time / numbers_of_runs

    print(f'Average is {average:.1f} of {numbers_of_runs} of runs.')


run_timing()