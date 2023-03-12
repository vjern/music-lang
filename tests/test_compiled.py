# import os
# from functools import partial
# from midi import expecto, compile


# origin = 'mm'


# class TestCompiled:
#     pass


# def populate():

#     def f(name):
#         # open .m file
#         with open(origin + '/' + name + '.m') as fi:
#             data = compile(fi.read())
#         # # compare to .mc file
#         print(name)
#         with open(origin + '/' + name + '.csv') as fi:
#             expected = expecto.read(fi)

#         assert data == expected

#     for file in os.listdir(origin):
#         name, ext = os.path.splitext(file)
#         print(name, ext)
#         if name != 'basic':
#             continue
#         if ext != '.m':
#             continue
#         setattr(TestCompiled, 'test_' + name, partial(f, name=name))


# populate()