import collections


def capitalize():
    s = "this is test"
    s = s.capitalize()
    assert s == 'This is test'

def center():
    s = "test"
    s = s.center(20,'|')
    assert s == '||||||||test||||||||'

def count():
    # counts substrings in the string
    s = "abcabcabcabcabc"
    cnt = s.count('abc',0,len(s))
    assert cnt == 5

def encode():
    s = "test"
    '''
    The default is 'strict' meaning that encoding errors raise a
    UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that can handle UnicodeEncodeErrors.
    '''
    es = s.encode('utf-8', errors='strict')
    assert es == b'test'
    es = s.encode('ascii', errors='strict')
    assert es == b'test'

def endswith():
    s  = 'this is test'
    assert s.endswith('test',0,len(s))

def expandtabs():
    s = '01\t012\t0123\t01234'.expandtabs()
    # default tabsize is 8 and it starts from 0
    # so tab \t is replaced by whitespaces starting from 0
    # 01 takes 2 chars and there are also 6 whitespaces followed by 012, so in total 8 chars
    # 012 takes 3 chars and there are also 5 whitespaces followed by 0123, so in total 8 chars
    # 0123 takes 4 chars and there are also 4 whitespaces followed by 01234, so in total 8 chars
    assert s == '01      012     0123    01234'

def find():
    s = 'this is a test'
    index = s.find('is')
    assert index == 2
    # NOTE: this version returns the original index in the string
    index = s.find('es', 10, len(s))
    assert index == 11

def format():
    s = "The sum of 1 + 2 is {0}".format(1 + 2)
    assert s == "The sum of 1 + 2 is 3"
    s = "The sum of 1 + 2 is {0}, {1}".format(2.567, 'dsf')
    assert s == "The sum of 1 + 2 is 2.567, dsf"

def index():
    # the same as find but but raises ValueError when the substring is not found.
    pass

def isalnum():
    '''
    Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise.
    A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
    '''
    pass


def isalpha():
    s = 't'
    assert s.isalpha() == True

def isascii():
    '''
    Return True if the string is empty or all characters in the string are ASCII, False otherwise.
    ASCII characters have code points in the range U+0000-U+007F.
    '''
    pass


def isdecimal():
    '''
    method supports only Decimal Numbers.
    '''
    s = '1'
    assert s.isdecimal() == True
    s = '12.5'
    assert s.isdecimal() == False
    s = '10'
    assert s.isdecimal() == True
    s = '12'
    assert s.isdecimal() == True
    s = '1000'
    assert s.isdecimal() == True
    s = '46572115'
    assert s.isdecimal() == True
    s = '-5'
    assert s.isdecimal() == False

def isdigit():
    '''
    Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.
    method supports Decimals, Subscripts, Superscripts.
    '''
    s = '1'
    assert s.isdigit() == True
    s = '12.5'
    assert s.isdigit() == False
    s = '10'
    assert s.isdigit() == True
    s = '12'
    assert s.isdigit() == True
    s = '1000'
    assert s.isdigit() == True
    s = '46572115'
    assert s.isdigit() == True
    s = '-5'
    assert s.isdigit() == False

def isnumeric():
    '''
     Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric
     method supports Digits, Vulgar Fractions, Subscripts, Superscripts, Roman Numerals, Currency Numerators.
    '''
    s = '1'
    assert s.isnumeric() == True
    s = '12.5'
    assert s.isnumeric() == False
    s = '10'
    assert s.isnumeric() == True
    s = '12'
    assert s.isnumeric() == True
    s = '1000'
    assert s.isnumeric() == True
    s = '46572115'
    assert s.isnumeric() == True
    s = '-5'
    assert s.isnumeric() == False

def isidentifier():
    from keyword import iskeyword
    id, kw = 'hello'.isidentifier(), iskeyword('hello')
    assert id == True, False
    id, kw = 'def'.isidentifier(), iskeyword('def')
    assert id == True, True

def isspace():
    s = ''
    assert s.isspace() == False
    s = '  '
    assert s.isspace() == True
    s = ' s'
    assert s.isspace() == False

def istitle():
    s = 'This is test'
    assert s.istitle() == False
    s = 'This Is Test'
    assert s.istitle() == True
    s = 'This Is test'
    assert s.istitle() == False
    s = "There're Some Items"
    assert s.istitle() == False
    s = 'THIS IS TEST'
    assert s.istitle() == False

def ljust():
    s = 'test'
    s = s.ljust(10, '|')
    assert s == 'test||||||'

def lstrip():
    '''
    The chars argument is a string specifying the set of characters to be removed.
    If omitted or None, the chars argument defaults to removing whitespace.
    The chars argument is not a prefix; rather, all combinations of its values are stripped:
    '''
    s = '   spacious   '.lstrip()
    assert s == 'spacious   '
    s = 'www.example.com'.lstrip('cmowz.')
    assert s == 'example.com'
    s = 'Arthur: three!'.lstrip('Arthur: ')
    assert s == 'ee!' # so it removed any combination of chars 'Arthur: '
    # this is from 3.9 version of Python
    # s = 'Arthur: three!'.removeprefix('Arthur: ')
    # assert s == 'three!' # remove prefix removes the pointed prefix


def maketrans():
    str = "this is string example....wow!!!"
    intab = "aeiou"
    outtab = "12345"
    trantab = "".maketrans(intab, outtab)
    # chars that are in aeiou are replaced by 12345
    # the rest of the chars are not changed

    assert str.translate(trantab) == 'th3s 3s str3ng 2x1mpl2....w4w!!!'

# starting from Python 3.9
def removeprefix():
    pass
#     s = 'BaseTestCase'.removeprefix('Test')
#     assert s == 'BaseTestCase'
#     s = 'TestHook'.removeprefix('Test')
#     assert s == 'Hook'

# starting from Python 3.9
def removesuffix():
    pass

def replace():
    s = 'teeest'
    assert s.replace('e', '') == 'tst'
    assert s.replace('e','',2) == 'test'

def rfind():
    s = 'this is a test'
    index = s.rfind('is')
    assert index == 5
    # NOTE: this version returns the original index in the string
    index = s.rfind('t', 0, len(s))
    assert index == 13

def rjust():
    s = 'test'
    assert s.rjust(10,'|') == '||||||test'

def rindex():
    pass
    # the same as rfind but raises exception if sub is not found

def partition():
    s = 'this - is a - test'
    # always returns tuple of three parts
    assert s.partition('-') == ('this ', '-', ' is a - test')

def rpartition():
    s = 'this - is a - test'
    assert s.rpartition('-') == ('this - is a ', '-', ' test')

def rsplit():
    s = 'this - is a - test - test - lll'
    assert s.rsplit('-', 3) == ['this - is a ', ' test ', ' test ', ' lll']

def rstrip():
    s = 'hello world'
    assert s.rstrip('ldr') == 'hello wo'
    assert  'Monty Python'.rstrip(' Python') == 'M'

def split():
    s = 'this - is a - test - test - lll'
    assert s.split('-', 3) == ['this ',' is a ', ' test ', ' test - lll']

def splitlines():
    '''
    split symbols
        \n Line Feed
        \r Carriage Return
        \r\n Carriage Return + Line Feed
        \v or \x0b Line Tabulation
        \f or \x0c Form Feed
        \x1c File Separator
        \x1d Group Separator
        \x1e Record Separator
        \x85 Next Line (C1 Control Code)
        \u2028 Line Separator
        \u2029 Paragraph Separator
    '''
    s = 'this\nis\r\ntest\r\n!'
    assert s.splitlines() == ['this','is','test','!']
    assert s.splitlines(keepends=True) == ['this\n', 'is\r\n', 'test\r\n', '!']

def startswith():
    s = 'this is test'
    assert s.startswith('this') == True
    assert s.startswith('test',8, len(s)) == True

def strip():
    s = 'www.example.com'
    assert s.strip('cmowz.') == 'example'

def swapcase():
    s = 'This Is Test'
    assert s.swapcase() == 'tHIS iS tEST'

def title():
    s = 'hello world'
    assert s.title() ==  'Hello World'

def zfill():
    s = '42'
    assert s.zfill(5) == '00042'
    s = '-42'
    assert s.zfill(5) == '-0042'

if __name__ == '__main__':
    capitalize()
    center()
    count()
    encode()
    endswith()
    expandtabs()
    find()
    format()
    isdigit()
    isdecimal()
    isidentifier()
    isnumeric()
    isspace()
    istitle()
    ljust()
    lstrip()
    maketrans()
    replace()
    rfind()
    rjust()
    partition()
    rpartition()
    rsplit()
    rstrip()
    split()
    splitlines()
    startswith()
    swapcase()
    title()
    zfill()