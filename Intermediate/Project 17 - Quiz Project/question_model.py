class Question:

    def __init__(self, question_text : str, answer : str) -> None:
        self.text = question_text
        self.answer = answer
    
    def __str__(self):
        return f"{self.text} ---> {self.answer}"
