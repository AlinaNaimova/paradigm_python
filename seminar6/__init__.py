import time

# ДЗ: исправить ошибки подсчета времени, добавить комментарии, описать какую парадигму использовали.

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.bool_pause_time = False
        self.pause_start_time = None
        self.total_paused_time = 0

    def start(self):
        if not self.start_time:
            self.start_time = time.time()
        elif self.bool_pause_time:
            self.total_paused_time += time.time() - self.pause_start_time
            self.bool_pause_time = False

    def pause(self):
        if self.start_time and not self.bool_pause_time:
            self.bool_pause_time = True
            self.pause_start_time = time.time()

    def resume(self):
        if self.bool_pause_time:
            self.bool_pause_time = False
            self.total_paused_time += time.time() - self.pause_start_time

    def stop(self):
        self.start_time = None
        self.bool_pause_time = False
        self.pause_start_time = None
        self.total_paused_time = 0

    def get_time(self):
        if self.start_time:
            if self.pause_start_time:
                return self.pause_start_time - self.start_time - self.total_paused_time
            else:
                return time.time() - self.start_time - self.total_paused_time

    def get_time_format(self):
        time = int(self.get_time())
        min = time // 60
        sec = time % 60
        return f"{min:02}: {sec:02}"


if __name__ == "__main__":
    name = Stopwatch()
    while True:
        print("1 - start")
        print("2 - pause")
        print("3 - continue")
        print("4 - stop")
        print("5 - exit")

        choice = input("Choose number: ")
        if choice == "1":
            name.start()
        elif choice == "2":
            name.pause()
        elif choice == "3":
            name.resume()
        elif choice == "4":
            name.stop()
        elif choice == "5":
            print("Exit")
            break

    total = name.get_time_format()
    print("time", total)








