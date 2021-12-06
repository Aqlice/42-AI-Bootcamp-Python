def ft_reduce(function_to_apply, list_of_inputs):
    res = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for elem in list_of_inputs[2:]:
        res = function_to_apply(res, elem)
    return res