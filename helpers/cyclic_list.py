class CyclicList(list):
    def __getitem__(self, i):
        try:
            return super().__getitem__(i)
        except IndexError:
            corrected_i = i % len(self)
            return self[corrected_i]

    def get_item_k_left_of(self, item, k=1):
        return self[self.index(item) - k]

    def get_item_k_right_of(self, item, k=1):
        return self[self.index(item) + k]
