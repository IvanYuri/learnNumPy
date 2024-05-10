import numpy as np

def simple_space():
    simple_space = np.linspace(start=2, stop=10)
    print("shape: ", simple_space.shape)
    # print(simple_space)
    print("type: ", type(simple_space))
simple_space()

def space_10():
    space_10 = np.linspace(start=2, stop=10, num=10)
    print(space_10)
space_10()

def space_no_end():
    space_no_end = np.linspace(start=2, stop=10, num=10, endpoint=False)
    print(space_no_end)
space_no_end()

def space_between():
    space_no_end, retstep = np.linspace(start=2, stop=10, num=10, endpoint=False, retstep=True)
    print(f'{space_no_end}\nThe space between is: {retstep}')
space_between()

def simple_space_int():
    simple_space_int = np.linspace(start=2, stop=10, num=10, dtype=int)
    print(simple_space_int)
simple_space_int()

def simple_array_space():
    simple_array_space, retstep = np.linspace(start=[2, 10, 5], stop=[10, 20, 4], num=20, endpoint=False, retstep=True)
    print(simple_array_space, "\n\nThe retstep is: ", retstep)
    print("\nThe shape is: ", simple_array_space.shape)
simple_array_space()

def simple_array_axis():
    simple_array_axis, retstep = np.linspace(start=[20, 7, 13], stop=[50, 1, 250], num=100, retstep=True)
    print("\n", simple_array_axis, "\n\nThe retstep is: ", retstep)
    print("\nThe shape is: ", simple_array_axis.shape)
simple_array_axis()
