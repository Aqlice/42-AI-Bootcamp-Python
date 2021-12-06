def ft_map(function_to_apply, list_of_inputs):
    newlist = []
    for elem in list_of_inputs:
        newlist.append(function_to_apply(elem))
    return newlist