class QuiezModle:
    def __init__(self,question,answers,correct_index):
        self.question=question
        self.answers=answers
        self.correct_index=correct_index
    def fromJson(map):
        return QuiezModle(question=map['question'],answers=map['answers'],correct_index=map['index_of_the_correct_answer'])
        