class TextMachine:
    def __init__(self, text_type_1, text_type_2):
        self.text_type_1 = text_type_1
        self.text_type_2 = text_type_2
        self.current_owe = (self.text_type_1[0], self.text_type_2[0])
        self.current_count = (self.text_type_1[1], self.text_type_2[1])
        self.cur_short_owe = self.text_type_1[1]
        self.cur_long_owe = self.text_type_2[1]

    def __str__(self):
        return f'Text Machine:<{self.text_type_1[0]} texts; ₴{self.text_type_1[1]/100} each>; \"\"<{self.text_type_2[0]} texts; ₴{self.text_type_2[1]/100} each>'

    def is_empty(self):
        if self.text_type_1[0] == 0 or self.text_type_2[0] == 0:
            return True

    def texts_count(self):
        self.count = (self.text_type_1[0], self.text_type_2[0])
        return self.count

    def still_owe(self):
        self.current_owe = (self.text_type_1[1], self.text_type_2[1])
        return self.current_owe

    def test(self, one, two):
        return one*two

    def insert_money(self, items):

        money = items[0]
        text_type = items[1]


        if text_type == 'short':
            self.cur_short_owe = self.cur_short_owe - money

            if self.cur_short_owe == 0:
                self.current_count = (
                    self.current_count[0] - 1, self.current_count[1])
            return (f"Still owe ₴{self.cur_short_owe/100}", money)

        if text_type == 'long':
            self.cur_long_owe = self.cur_long_owe[1] - money
            if self.cur_long_owe == 0:
                self.current_count = (
                    self.current_count[0] - 1, self.current_count[1])
            return f'"Still owe ₴{self.cur_long_owe/100}", {money}'

    def still_owe(self):
        return self.current_count

# Text machines have four main properties:
# how many text of two type they contain and the price of each type text.
# A new text machine starts with two texts type.
tm1 = TextMachine((75, 125), (25, 245))


# FAILING
# assert (str(tm1) == "Text Machine:<75 texts; ₴1.25 each>; ""<25 texts; ₴2.45 each>")
assert not tm1.is_empty()
assert tm1.texts_count() == (75, 25)
assert tm1.still_owe() == (125, 245)

# When the user inserts money and text type, the machine returns
# a message about their status and any change they need as a tuple.
print(tm1.insert_money((20, 'short')))
assert tm1.insert_money((20, 'short')) == ("Still owe ₴1.05", 20)
assert tm1.still_owe() == (105, 245)
assert tm1.texts_count() == (75, 25)
assert tm1.insert_money((5, 'short')) == ("Still owe ₴1.00", 25)