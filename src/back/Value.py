class Value:
    def __init__(self):
        self._total = 0
        self._positive = 0

    def result(self):
        if self._total:
            return round(self._positive/self._total*100)
        else:
            return 0

    def add_review(self, is_positive):
        self._total += 1
        if is_positive:
            self._positive += 1
        return self

    def remove_review(self, was_positive):
        self._total -= 1
        if was_positive and self._positive:
            self._positive -= 1
        return self

    def __str__(self):
        return str(self.result()) + '%'

    def __bool__(self):
        return self.result() >= 50
