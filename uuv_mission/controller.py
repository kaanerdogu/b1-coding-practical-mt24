#controller function to be called
def controller(reference_t, reference_t_1, depts_t, depts_t_1):
    Kp = 0.15
    Kd = 0.6
    err = reference_t - depts_t
    err_1 = reference_t_1 - depts_t_1
    action = Kp*err + Kd*(err - err_1)
    return action