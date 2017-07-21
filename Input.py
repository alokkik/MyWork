
class Enter:

    def __init__(self):
        self.value = []
        self.size = []
        self.items_list = []

    def get_input_from_file(self, file_name):
        _list = []
        f = open(file_name)
        for x in f:
            _list.append(int(x))
        return _list

    def get_input(self):

        self.value = self.get_input_from_file("item_values.txt")
        self.size = self.get_input_from_file("item_size.txt")

        for i in range(0, len(self.value), 1):
            self.items_list.append((self.value[i], self.size[i]))
        return self.items_list

    def show_item(self):
        for x in self.items_list:
            print(x)

