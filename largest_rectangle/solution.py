# https://www.hackerrank.com/challenges/largest-rectangle

N = int(raw_input().strip())
height_list = [int(x) for x in raw_input().strip().split()]


def largest_rect(height_list):
    '''
    Create an empty stack. The stack holds indexes of hist[] array
    The bars stored in stack are always in increasing order of their
    heights.
    '''
    stack = list()
    max_area = -1

    i = 0
    while i < len(height_list):
        # If this bar is higher than the bar on top stack, push it to stack
        if len(stack) == 0 or height_list[stack[-1]] <= height_list[i]:
            stack.append(i)
            i += 1
            '''
            If this bar is lower than top of stack, then calculate area of rectangle 
            with stack top as the smallest (or minimum height) bar. 'i' is 
            'right index' for the top and element before top in stack is 'left index'
            '''
        else:
            tp = stack.pop()
            # Calculate the area with hist[tp] stack as smallest bar
            if len(stack) == 0:
                area_with_top = height_list[tp] * i
            else:
                area_with_top = height_list[tp] * (i - stack[-1] - 1)

            if max_area < area_with_top:
                max_area = area_with_top

    '''
    Now pop the remaining bars from stack and calculate area with every
    popped bar as the smallest bar
    '''
    while len(stack) != 0:
        tp = stack.pop()
        if len(stack) == 0:
            area_with_top = height_list[tp] * i
        else:
            area_with_top = height_list[tp] * (i - stack[-1] - 1)
        if max_area < area_with_top:
            max_area = area_with_top

    return max_area


print largest_rect(height_list)
