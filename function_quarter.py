def function_quarter(x,y):
    # x,y = input(), input()
    if x > 0:
        if y > 0:
            print("I quarter")
        else:
            print("IV quarter")
    else:
        if y > 0:
            print("II quarter")
        else:
            print("III quarter")

function_quarter(3, 4)
function_quarter(-3.5, 8)
function_quarter(-3.5, -8)
function_quarter(3, -4)