def my_decorator(func):
    def wrapper():
        print("До вызова функции.")
        func()
        print("После вызова функции.")
    return wrapper


def say_whee():
    print("Ура!")


say_whee = my_decorator(say_whee)

say_whee()
