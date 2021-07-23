import json
import random
from random import randint
from typing import List, Dict, Tuple, Any

class Quiz:

    def __init__(self, json_path: str):
        self.quiz_dict = self.parse_json(json_path=json_path)
        self.quiz_key = [key for key in self.quiz_dict]
        
    def parse_json(self, json_path: str) -> dict[str, str]:
        """Return data structure from JSON file"""
        f = open(json_path,)
        data = json.load(f)
        f.close()
        return data

    def set_answer(self) -> Tuple[int, ...]:
        """Create answer tuple"""
        self.quiz_nubmer = randint(0, len(self.quiz_key)-1)
        self.quiz_answer = self.quiz_key[self.quiz_nubmer]
        self.quiz_question = self.quiz_dict[self.quiz_key[self.quiz_nubmer]]
        return (self.quiz_nubmer, self.quiz_answer, self.quiz_question)

    def print_question(self, quiz_tuple: Tuple[Any]) -> List[Any]:
        question = quiz_tuple[0][2]
        answers = []
        answers.append(quiz_tuple[0][1])
        for ans in quiz_tuple[1]:
            answers.append(ans)
        random.shuffle(answers)
        for i in range(0, len(answers)):
            answers[i] = f"{i}. {answers[i]}"
        
        return (question, answers, quiz_tuple[0])
        

    def set_question(self) -> List[List[Any]]:
        """Create answer key"""
        quiz_answer = self.set_answer()
        wrong_answers = [self.quiz_key[randint(0, len(self.quiz_key)-1)] for x in range(3)]
        format_question = self.print_question(quiz_tuple=(quiz_answer, wrong_answers))
        return format_question


if __name__ == "__main__":
    quiz = Quiz("dictionaries/dict.json")

    while True:
        next_question = input("Next question? (y/n)\n")
        if next_question.lower() == "y":
            quiz_setup = quiz.set_question()

            print(f"Question:\n{quiz_setup[0].capitalize()}")
            print("\n".join(quiz_setup[1]))
            answer = input(">>>")

            for answers in quiz_setup[1]:
                if int(answer) == int(answers[0:1]):
                    if answers[3:] == quiz_setup[2][1]:
                        print("correct")
                    else:
                        print("incorrect")
        else:
            break
            



    