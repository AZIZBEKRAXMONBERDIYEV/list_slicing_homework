def main(numbers):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    s=numbers[0::2]
    return s
print(main([1,2,3,4,5,6,7]))