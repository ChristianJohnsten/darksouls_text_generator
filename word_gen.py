from random import randint

class WordGen:
    def __init__(self):
        self.adjectives_list = "word_lists/adjectives.txt"
        self.nouns_list = "word_lists/nouns.txt"
        self.verbs_list = "word_lists/verbs_past_tense.txt"
        self.adjectives = []
        self.nouns = []
        self.verbs = []

        # Load and format adjectives
        with open(self.adjectives_list, "r") as f:
            self.adjectives = f.readlines()

        for i in range(len(self.adjectives)):
            self.adjectives[i] = self.adjectives[i].rstrip()

        # Load and format nouns
        with open(self.nouns_list, "r") as f:
            self.nouns = f.readlines()

        for i in range(len(self.nouns)):
            self.nouns[i] = self.nouns[i].rstrip()

        # Load and format verbs
        with open(self.verbs_list, "r") as f:
            self.verbs = f.readlines()

        for i in range(len(self.verbs)):
            self.verbs[i] = self.verbs[i].rstrip()

    def get_adjective(self):
        return self.adjectives[randint(0, len(self.adjectives)-1)]

    def get_noun(self):
        return self.nouns[randint(0, len(self.nouns)-1)]

    def get_verb(self):
        return self.verbs[randint(0, len(self.verbs)-1)]

    def gen_anv(self):
        return self.get_adjective() + " " + self.get_noun() + " " + self.get_verb()

    def gen_nv(self):
        return self.get_noun() + " " + self.get_verb()


if __name__ == "__main__":
    wg = WordGen()

    running = True
    print('Press [Enter] for new "adj noun verb"\nType "quit" or "q" to exit.\n')
    while running == True:
        print(wg.gen_anv())
        user_in = input()
        if user_in.lower() in ["quit", "q", "close", "stop", "exit"]:
            running = False


# with open("verbs_past_tense.txt", "r") as f:
#     verbs = f.readlines()
#
# for i in range(len(verbs)):
#     try:
#         word = verbs[i].rstrip().split("\t")[2]
#         if "/" in word:
#             word = word.split("/")
#             print(word[0].strip())
#             print(word[1].strip())
#         else:
#             print(word)
#
#     except IndexError:
#         pass
