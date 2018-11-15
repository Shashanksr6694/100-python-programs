"""

Question:
    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function

Hints:
    The built-in document method is __doc__

"""
print(abs.__doc__)
print(sorted.__doc__)

def sampleDef():
    """

    This is a sample of the document/comment for method

    :return:
    """
    print("sampleDef Called")

sampleDef()
print(sampleDef.__doc__)
