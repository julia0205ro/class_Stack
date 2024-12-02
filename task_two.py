from task_one import Stack


def parentheses_balance(parentheses_str: str):
    parentheses_dict = {'[': ']', '{': '}', '(': ')'}
    example = Stack()

    if not isinstance(parentheses_str, str):
        return "Error: a string of parentheses is expected"

    for item in parentheses_str:
        if item not in parentheses_dict.values() and item not in parentheses_dict.keys():
            parentheses_str = parentheses_str.replace(item, '')

    if len(parentheses_str) == 0:
        return 'Error: the string does not contain parentheses'

    for item in parentheses_str:
        if item in parentheses_dict:
            example.push(item)
        elif item in parentheses_dict.values():
            if example.is_empty() or parentheses_dict[example.pop()] != item:
                return 'Unbalanced'

    if example.is_empty():
        return 'Balanced'
    else:
        return 'Unbalanced'


if __name__ == '__main__':
    test_cases = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}',
                  '[[{())}]', 9, '[][]66', '[][]6', '[][6]6}', '[[{())}', '9', '[', '']

    for case in test_cases:
        print(f'{case}: {parentheses_balance(case)}')
