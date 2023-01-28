def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    s=list1[0::3]
    return s
print(main([1,2,3,4,5,6,7]))