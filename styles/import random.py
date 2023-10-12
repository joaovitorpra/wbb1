import random
def main():
    def get_determiner(quantity):
        if quantity == 1:
            words = ["a", "one", "the"]
        else:
            words = ["some", "many", "the"]
 # Randomly choose and return a determiner.
            word = random.choice(words)
            word = word.capitalize()
            return word

    def get_noun(quantity):
        if quantity == 1:
            nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", 
            "man", "rabbit", "woman"]
        else:
            nouns = ["birds", "boys", "cars", "cats", "children","dogs", 
            "girls", "men", "rabbits", "women"]
 # Randomly choose and return a noun.
            noun = random.choice(nouns)
            return noun
    def get_verb(quantity, tense):
        if tense == "past":
            verbs = ["drank", "ate", "grew", "laughed", "thought","ran", 
        "slept", "talked", "walked", "wrote"]
        if tense == "present"and quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", 
            "sleeps", "talks", "walks", "writes"]
        if tense == "present" and quantity != 1:
            verbs = ["drink", "eat", "grow", "laugh", "think", "run", 
            "sleep", "talk", "walk", "write"]
        if tense == "future":
            verbs == ["will drink", "will eat", "will grow", "will laugh", 
            "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
 # Randomly choose and return a verb.
            verb = random.choice(verbs)
            return verb
 
 
    def get_preposition():
        prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",]
    def get_prepositional_phrase(quantity):
        preposition=get_preposition()
        determiner=get_determiner(quantity)
        noun=get_noun(quantity)
        prepositional_phrase= preposition+" "+determiner+" "+noun
        return prepositional_phrase
    def make_sentence(quantity, tense):
        sentence = get_determiner() + get_noun() + get_verb() + get_preposition() + get_prepositional_phrase()
        print(make_sentence)
main()