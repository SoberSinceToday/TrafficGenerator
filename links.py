class Links:
    def __init__(self):
        with open("utils/links.txt", 'r') as file:
            self.data = [x.strip().lower() for x in file.readlines()]
        self.all_links = ""

    def get_links(self) -> str:
        self.all_links = ""
        for x in self.data:
            self.all_links += x + '\n'
        return self.all_links

    def add_link(self, added_link):
        self.data.append(added_link)

    def del_link(self, del_link):
        self.data.remove(del_link)

    def add_links(self, links):
        for link in links:
            self.add_link(link)

    def get_links_as_arr(self):
        return self.data

    def __len__(self):
        return len(self.data)

# Можно добавить clear_all
