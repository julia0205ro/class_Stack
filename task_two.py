from task_one import Stack


def parentheses_balance(parentheses_str: str):
    parentheses_list = ['[', ']', '{', '}', '(', ')']
    parentheses_dict = {'[': ']', '{': '}', '(': ')'}
    example = Stack()
    try:
        for i in parentheses_str:
            if i not in parentheses_list:
                return f'Expecting a string of parentheses as input'
    except TypeError:
        return f'Expecting a string of parentheses as input'
    for i in parentheses_str:
        if len(parentheses_str) % 2 != 0:
            return f'Unbalanced'
        if i in list(parentheses_dict.keys()):
            Stack.push(example, i)
        else:
            target_key = [key for key, value in parentheses_dict.items()
                          if value == i]
            if ''.join(target_key) in example.get_list():
                Stack.remove(example, ''.join(target_key))
            else:
                return f'Unbalanced'
    if Stack.is_empty(example):
        return f'Balanced'
    else:
        return f'Unbalanced'


if __name__ == '__main__':
    print(parentheses_balance('(((([{}]))))'))
    print(parentheses_balance('[([])((([[[]]])))]{()}'))
    print(parentheses_balance('{{[()]}}'))
    print(parentheses_balance('}{}'))
    print(parentheses_balance('{{[(])]}}'))
    print(parentheses_balance('[[{())}]'))
    print(parentheses_balance(9))
    print(parentheses_balance('[][]66'))
    print(parentheses_balance('[][]6'))
    print(parentheses_balance('[[{())}'))
    print(parentheses_balance('9'))
    print(parentheses_balance('['))
