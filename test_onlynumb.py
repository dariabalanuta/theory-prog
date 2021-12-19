def onlynumb(lines):
    l = list(string.ascii_letters)

    for element in lines:
        if element in l:
            print('Mistake - there is a letter!')
            break
    else:
        print('no latters')

def test_onlynumb()
    lines = ['1', '4', '2', '3', '002']
    assert(lines) == 'no latters'
    lines = ['1', '4', 's', '3', '002']
    assert(lines) == 'Mistake - there is a letter!'
