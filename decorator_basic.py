user = {"username": "ricky", "level": "admin"}
def user_has_permission(fn):
    def wrapper_user_has_permission():
        if user["level"] == "admin":
            return fn
        else:
            return None

    return wrapper_user_has_permission()

def show_pass():
    return "acbdnfdroeke@123"

my_function = user_has_permission(show_pass)
if my_function != None:
    print(my_function())
else:
    print("No access!")


