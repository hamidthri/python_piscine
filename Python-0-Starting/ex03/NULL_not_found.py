def NULL_not_found(object: any) -> int:
    """
    Prints the object type of all types of "Null".

    Args:
        object: Any Python object

    Returns:
        int: 0 if a null type is found, 1 otherwise
    """
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif isinstance(object, float) and str(object) == "nan":
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif object == 0 and not isinstance(object, bool):
        print(f"Zero: {object} {type(object)}")
        return 0
    elif object == "":
        print(f"Empty: {type(object)}")
        return 0
    elif object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1
