from collections import namedtuple

# Also instead of IMPORT - it can be done via CLASS
# class tuple_named:
#     def __init__(self, user_id, user_name, ..... ):
#         self._user_id = user_id
#         self._user_name = user_name


User = namedtuple('User', 'user_name, user_id')
print(User)


def named_tuple():
    pass


if __name__ == '__main__':
    named_tuple()