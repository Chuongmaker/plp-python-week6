# unbreakable.py
import safe_tools

def run_unbreakable():
    print("--- Unbreakable Program Demo ---")
    print("Safe Divide (20 / 4):", safe_tools.safe_divide(20, 4))
    print("Safe Divide (20 / 0):", safe_tools.safe_divide(20, 0))
    print("Safe Number ('123'):", safe_tools.safe_number("123"))
    print("Safe Number ('xyz'):", safe_tools.safe_number("xyz"))

    learner_data = {"name": "John", "grade": "A"}
    print("Get Field ('grade'):", safe_tools.get_field(learner_data, "grade"))
    print("Get Field ('age'):", safe_tools.get_field(learner_data, "age"))

run_unbreakable()