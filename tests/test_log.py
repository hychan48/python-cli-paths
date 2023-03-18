# PyTest
import sys
import pytest
import logging as log

log.warning('hi')  # for the user


class A:
    def run(self):
        log.warning('A')


class B:
    def run(self):
        log.warning('B')


def test_name():

    log.warning("hi")  # for framework
    a = {
        "a": 'a'
    }
    b = {
        "a": 'b'
    }
    #
    # c = {**a, **b}
    # # C = {**A,**B}
    # log.warning(c)
    # # log.warning(C)
    # log.warning(dir(A))
    # try:
    #     pass
    # except Exception as ex:
    #     # log.warning(ex)
    #     pass
    tmp = map(lambda val: val + 1, (1, 2, 3) )
    # name_keys:list=None
    # name_keys = ['a'] if name_keys is None else name_keys
    terinary_operator = "terinary_operator" if tmp is None else tmp
    def wont_warn(actual, expected='asdf'):
        pass

    def will_warn(expected='default',actual=None):
        pass


    log.warning(list(tmp))

hi = None
def test_class_tmp():
    # PyTest
    import sys
    import pytest
    import logging as log
    print(locals())
    if 1:
        print(locals())
        print('hi');
        print('hi');
        print('hi')

    def fake():
        print(locals())

    fake()

    class A:
        def local(self):
            print(locals())

            def local_a():
                print('locala')
                print(locals())

            local_a()

        def run(self):
            print(locals())
            fake()

    a = A()
    a.run()
    a.local()

if __name__ == '__main__':
    # map( val => val.tmp)

    pytest.main(sys.argv)
