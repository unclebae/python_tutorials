def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        print("Input Value : %s" %ok)
        if ok in ('y', 'ye', 'yes', 'Y'):
            print("Input Yes")
            return True

        if ok in ('n', 'no', 'N'):
            print("Input No")
            return False

        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')

        print(reminder)

    print ("Close Program...")

if __name__ == '__main__':
    ask_ok('Do you really want to quit?')
    ask_ok('OK  to overwrite the file?', 2)
    ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
