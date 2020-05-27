import textwrap

def wrap(string, max_width):
    print(string,max_width)
    wrapper = textwrap.TextWrapper(width=max_width)
    result= wrapper.wrap(text=string)
    result = '\n'.join(result)

    for element in string:
        return result

if __name__ == '__main__':
    string, max_width = input("Enter string: ").upper(), int(input("Enter length: "))
    result = wrap(string, max_width)
    print(result)
