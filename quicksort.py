# Implementation of quick sort algorithm for visualization

import time

def partition(data, head, tail, draw_d, time_t):
    border = head
    pivot = data[tail]

    draw_d(data, getColorArray(len(data), head,
                               tail, border, border))
    time.sleep(time_t)

    for j in range(head, tail):
        if data[j] < pivot:
            draw_d(data, getColorArray(len(data),
                                       head, tail, border, j, True))
            time.sleep(time_t)

            data[border], data[j] = data[j], data[border]
            border += 1
        draw_d(data, getColorArray(len(data), head,
                                   tail, border, j))
        time.sleep(time_t)

    draw_d(data, getColorArray(len(data), head,
                               tail, border, tail, True))
    time.sleep(time_t)

    data[border], data[tail] = data[tail], data[border]

    return border

def quick_sort(data, head, tail,
               draw_d, time_t):
       if head < tail:
            partition_index = partition(data, head,
                                        tail, draw_d, time_t)
            
            quick_sort(data, head, partition_index - 1, draw_d, time_t)

            quick_sort(data, partition_index + 1, tail, draw_d, time_t)


def getColorArray(data_l, head, tail, border, curr_index, swapping = False):
     color_array = []
     for i in range(data_l):
        if i >= head and i <= tail:
            color_array.append('grey')
        else:
            color_array.append('white')

        if i == tail:
            color_array[i] = 'blue'
        elif i == border:
            color_array[i] = 'red'
        elif i == curr_index:
            color_array[i] = 'yellow'
        
        if swapping:
            if i == border or i == curr_index:
                color_array[i] = 'green'
     return color_array
        
                    
            
            
