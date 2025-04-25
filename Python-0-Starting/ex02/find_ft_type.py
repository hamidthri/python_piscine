def all_thing_is_obj(object: any) -> int:
    """
    Prints the type of the object and returns 42.

    Args:
        object: Any Python object

    Returns:
        int: Always returns 42
    """
    type_map = {list: "List", tuple: "Tuple", set: "Set", dict: "Dict"}

    obj_type = type(object)

    if obj_type in type_map:
        print(f"{type_map[obj_type]} : {obj_type}")
    elif obj_type is str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")

    return 42
