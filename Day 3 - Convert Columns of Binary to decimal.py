from collections import Counter

class Binary_Counter:

    def __init__(self, binary_file):

        with open(binary_file, 'r') as bin_file:
            self.file = bin_file.readlines()
        self.count = {key:Counter({'0':0, '1':0}) for key in range(12)}
        self.gamma = [0 for _ in range(12)]
        self.epsilon = [0 for _ in range(12)]
        # self.file = file - Day 3 Part 1

    def main(self):
        ### For Day 3 Part 1 ###
        # with open(self.file, 'r') as file:
        #     for line in file.readlines():
        #         lst = [char for char in line.strip()]
        #         self.counter(lst)
        #     return self.result(self.count)  # for Day 3 Part 1

        ### For Day 3 Part 2 ###
        for line in self.file:
            lst = [char for char in line.strip()]
            self.counter(lst)

    def counter(self, lst):
        for key,num in enumerate(lst):
            self.count[key][num] += 1

    def result(self, count):
        for counter in count.items():
            try:
                self.gamma[counter[0]] = 1 if counter[1].most_common(1)[0][0] == '1' else 0
                self.epsilon[counter[0]] = 1 if not counter[1].most_common(1)[0][0] == '1' else 0
            except IndexError:
                continue

        self.gamma, self.epsilon = "".join([str(num) for num in self.gamma]), "".join([str(num) for num in self.epsilon])
        return (int(self.gamma, 2) * (int(self.epsilon, 2)))

    def get_rating(self):

        # On every iteration here, we must REDO the counter
        for idex in range(12):
            self.main()
            most_common = [c.most_common(1)[0][0] if c.most_common(2)[0][1] > c.most_common(2)[1][1] else '1' for c in self.count.values()]   # Oxygen Rating
            least_common = ['1' if char == '0' else '0' for char in most_common]  # CO2 Rating
            if len(self.file) == 1:
                break
            self.file = list(filter(lambda binary_num: binary_num[idex] == least_common[idex], self.file)) # Modifies self.file to the new list
            self.count = {key:Counter({'0':0, '1':0}) for key in range(12)}                                # Reset Counter

        # For each num in our list, check the first digit only. If no match, then remove.
        # Move to second digit and repeat


if __name__ == '__main__':
    Binary1 = Binary_Counter("Day 3 - Binary Codes")
    print(Binary1.get_rating())