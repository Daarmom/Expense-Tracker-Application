class Expense:
    def __init__(self, amount, date, category, description=""):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def __repr__(self):
        return f"Expense(amount={self.amount}, date={self.date}, category={self.category}, description={self.description})"