from enum import Enum

EASY_LEVEL_QUESTION = """( 1 ) is a for-profit educational ( 2 ) founded by
Sebastian Thrun, David Stavens, and Mike Sokolsky offering massive open 
( 3 ) courses (MOOCs). According to Thrun, the origin of the name 
( 1 ) comes from the company's desire to be "audacious for you, 
the ( 4 )". While it originally focused on offering university-style 
courses, it now focuses more on vocational courses for professionals."""

EASY_LEVEL_ANSWERS = ["Udacity", "organization", "online", "student"]

MEDIUM_LEVEL_QUESTION = """A ( 1 ) language is a formal language that 
specifies a set of ( 2 ) that can be used to produce various kinds 
of output. ( 1 ) languages generally consist of ( 2 ) for a 
computer. ( 1 ) languages can be used to create ( 3 ) that ( 4 ) 
specific ( 5 )."""

MEDIUM_LEVEL_ANSWERS = ["programming", "instructions", "programs", "implement",
                        "algorithms"]

HARD_LEVEL_QUESTION = """( 1 ) is an interpreted high-level programming 
language for general-purpose programming. Created by ( 2 ) van Rossum and first 
released in ( 3 ), ( 1 ) has a design philosophy that emphasizes code 
( 4 ), notably using significant whitespace. It provides constructs 
that enable clear programming on both small and large scales. ( 1 ) features 
a dynamic type system and automatic memory management. It supports multiple 
programming paradigms, including ( 5 ), imperative, functional and 
procedural, and has a large and comprehensive standard library."""

HARD_LEVEL_ANSWERS = ["Python", "Guido", "1991", "readability",
                      "object oriented"]


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Game:
    @staticmethod
    def select_difficulty_level():
        """
        selecting level of difficulty
        :return: the level of difficulty ( easy, medium, hard )
        """
        difficulty_level = input(
            "Please enter the difficulty level, the choices "
            "of difficulty levels includes "
            "{0}, {1} and {2}: ".format(Difficulty.EASY.value,
                                        Difficulty.MEDIUM.value,
                                        Difficulty.HARD.value))

        while difficulty_level not in {Difficulty.EASY.value,
                                       Difficulty.MEDIUM.value,
                                       Difficulty.HARD.value}:
            print(
                "{} is not a valid difficulty level.".format(difficulty_level))
            difficulty_level = input(
                "Please enter the difficulty level, the choices "
                "of difficulty levels includes "
                "{0}, {1} and {2}: ".format(Difficulty.EASY.value,
                                            Difficulty.MEDIUM.value,
                                            Difficulty.HARD.value))

        return difficulty_level

    @staticmethod
    def get_number_of_retries():
        """
        getting from the user the number of retries
        :return: number of retries
        """
        number_of_retries = input("Please input a number for retries: ")
        if number_of_retries is "":
            number_of_retries = 1
            return number_of_retries
        else:
            number_of_retries = int(number_of_retries)
            if number_of_retries <= 0:
                number_of_retries = 1
        return number_of_retries

    @staticmethod
    def get_easy_question():
        """
        getting the easy question and it's answers
        :return: easy question and answers
        """
        print("You have chosen the easy level")
        return EASY_LEVEL_QUESTION, EASY_LEVEL_ANSWERS

    @staticmethod
    def get_medium_question():
        """
        getting the medium question and it's answers
        :return: medium question and answers
        """
        print("You have chosen the medium level")
        return MEDIUM_LEVEL_QUESTION, MEDIUM_LEVEL_ANSWERS

    @staticmethod
    def get_hard_question():
        """
        getting the hard question and it's answers
        :return: hard question and answers
        """
        print("You have chosen the hard level")
        return HARD_LEVEL_QUESTION, HARD_LEVEL_ANSWERS

    def select_the_question(self, difficulty_level):
        """
        selecting the question for the user depending on the level of
        difficulty
        :param difficulty_level: the level of difficulty
        :return: a question and its answers based on the level of difficulty
        """
        if difficulty_level == Difficulty.EASY.value:
            return self.get_easy_question()
        elif difficulty_level == Difficulty.MEDIUM.value:
            return self.get_medium_question()
        elif difficulty_level == Difficulty.HARD.value:
            return self.get_hard_question()

    def ask_question(self, question, blank, answers, number_of_retries):
        """
        forming the question for the user and checking his answers
        if the answer is valid it replaces the ( # ) in the question and
        he moves on to the next blank space
        :param question: the question
        :param blank: the index of the blank in the question starting 1
        :param answers: the answers of the question
        :param number_of_retries: the number of retries for the user
        :return: the updated question and the next blank index
        """
        minimum_number_of_retries = 1
        remaining_retries = number_of_retries
        blanks_to_be_replaced = "( " + str(blank) + " )"
        displayed_question = self.display_question(
            current_question=question,
            blanks_to_be_replaced=blanks_to_be_replaced,
            remaining_retries=remaining_retries,
            number_of_retries=number_of_retries)
        user_answer = input(displayed_question).lower()
        while user_answer != answers.lower() and remaining_retries > \
                minimum_number_of_retries:
            remaining_retries -= 1
            displayed_question = self.display_question(
                current_question=question,
                blanks_to_be_replaced=blanks_to_be_replaced,
                remaining_retries=remaining_retries,
                number_of_retries=number_of_retries)
            user_answer = input(displayed_question).lower()
        if remaining_retries > minimum_number_of_retries:
            print("\nGreat on to the next one!\n")
            return question.replace(
                blanks_to_be_replaced, answers.lower()), blank + 1
        return None, blank + 1

    @staticmethod
    def display_question(current_question, blanks_to_be_replaced,
                         remaining_retries, number_of_retries):
        """
        displaying the question for the user and checking if the he still has
        retries left, formats the question and replaces the blanks that were
        correctly answered
        :param current_question: the question
        :param blanks_to_be_replaced: the number of the blank
        :param remaining_retries: the user's remaining retries
        :param number_of_retries: the number of retries
        :return:
        """
        result = "\nYour question is:\n{}\n\n"
        result += "What is your guess for # {}? "
        result = result.format(current_question, blanks_to_be_replaced)
        if remaining_retries == number_of_retries:
            return result
        wrong_answer_result = "This answer is not correct! "
        if remaining_retries > number_of_retries:
            wrong_answer_result += "\n\nYou can try again but you only have " \
                                   "{} trys left!\n\n"
        else:
            wrong_answer_result += "You only have {} try left!"
        return wrong_answer_result.format(remaining_retries) + result

    def start_game(self):
        """
        asks the user to input a difficulty level and number of retries
        then displays the results
        :return: The result of the users answers
        """
        print("Welcome to our guessing game, your get to choose the level of"
              "difficulty you would like to play in, the choices of difficulty"
              " levels includes {0}, {1} and {2}.\nAfter you select the "
              "difficulty level you will then be given a paragraph with"
              " some missing words and you should guess these missing words"
              " correctly".format(Difficulty.EASY.value,
                                  Difficulty.MEDIUM.value,
                                  Difficulty.HARD.value))
        difficulty_level = self.select_difficulty_level()
        print("You can also select a number of retries that will allow you to "
              "try to answer correctly again. If you do not select a number "
              "for retries then you will only be allowed to try one time.")
        number_of_retries = self.get_number_of_retries()
        question, answers = self.select_the_question(
            difficulty_level=difficulty_level)
        first_blank = 1
        while first_blank <= len(answers):
            question, first_blank = self.ask_question(
                question=question, blank=first_blank,
                answers=answers[first_blank - 1],
                number_of_retries=number_of_retries)
            if question is None:
                return print("Ops! Looks like you have lost!")
        return print(question + "\n\nYou won, Congratulation!\n")


if __name__ == '__main__':
    Game = Game()
    Game.start_game()
