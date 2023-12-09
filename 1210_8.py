def clip_value(value, v_ain, v_max):
    """
    :param value:
    :param v_ain:
    :param v_max:
    :return:
    """
    if value < v_ain:
        return v_ain
    elif value > v_max:
        return v_max
    else:
        return value
help(clip_value)
print(clip_value(1,2,3))