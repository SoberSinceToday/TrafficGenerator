from browserDriver import createDriver
from links import Links
import time
from proj_logging import Logger


class TrafficGenerator:

    def __init__(self):
        self.driver = createDriver()
        self.links = Links()
        self.link_num = 0
        self.logger = Logger()

    def startGen(self, exec_time):
        self.link_num = 0
        start_time = time.time()
        links_data = self.links.get_links_as_arr()
        while int(time.time()) - int(start_time) < exec_time:
            try:
                self.driver.get(links_data[self.link_num % self.links.__len__()])
                print(
                    f'Successfully connected to {links_data[self.link_num % self.links.__len__()]}')
                self.logger.write_log(True, links_data[self.link_num % self.links.__len__()])
            except:
                print(f'Failed to load the page {links_data[self.link_num % self.links.__len__()]}.')
                self.logger.write_log(False, links_data[self.link_num % self.links.__len__()])
            self.link_num += 1

    def driverDisconnect(self):
        print(self.logger.return_logs())
        self.driver.quit()

    def driverConnect(self):
        self.driver = createDriver()


if __name__ == "__main__":
    TrafGen = TrafficGenerator()
    TrafGen.startGen(100)
    TrafGen.driverDisconnect()
