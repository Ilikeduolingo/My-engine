import datetime
class Log:
    log_file = 'engine.log'
    enable_file_logs = True
    enable_console_logs = True
    @staticmethod
    def log(message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        if Log.enable_console_logs:
            print(log_entry)
        if Log.enable_file_logs:
            with open(Log.log_file, "a") as file:
                    file.write(log_entry)
    @staticmethod
    def initialise():
         with open(Log.log_file, "w") as file:
            file.write('Starting session\n')
    