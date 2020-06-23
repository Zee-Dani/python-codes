# def my_function(param_list):
#     param_list[0] = 100
#     print(param_list)


# arg_list = [1,2,3]
# my_function(arg_list)
# print(arg_list)


def my_fun(param):
    param.append(4)
    return param

my_list = [5,6,3]
new_list = my_fun(my_list)
print(my_list,new_list)