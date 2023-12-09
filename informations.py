import datetime

def measuring(winner, start_time):
    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    with open("informations.txt", "a+") as file:
        file.write(f"Total time: {total_time}, End time: {end_time.strftime('%H:%M:%S %d.%m.%Y')}, Start time: {start_time.strftime('%H:%M:%S %d.%m.%Y')}, Winner: {winner}\n")