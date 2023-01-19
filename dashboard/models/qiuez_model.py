class QuiezModle:
    def __init__(self,question,answers,correct_index):
        self.question=question
        self.answers=answers
        self.correct_index=correct_index
    def toMap(self):
        return {"question":self.question,"answers":self.answers,"index_of_the_correct_answer":self.correct_index}
        