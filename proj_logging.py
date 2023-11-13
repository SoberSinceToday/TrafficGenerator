from links import Links


class Logger:
    def __init__(self):
        self.logs = {}
        for x in Links().get_links_as_arr():
            self.logs[x] = {"connected": 0, "failed": 0}
        self.result = 'no logs written'

    def write_log(self, success, rec):
        self.logs[rec]["connected" if success else "failed"] += 1

    def return_logs(self):
        self.result = ''
        for x in self.logs:
            self.result += f"{x}:"
            self.result += f'\nSuccessfully {self.logs[x]["connected"]} times, Failed {self.logs[x]["failed"]} times.\n'
        return self.result
