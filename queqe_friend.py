# Queue time counter
def queue(queuers, pos, time=0):
    for count in range(sum(queuers)):
        if pos == 0:
            if queuers[pos] == 1:
                time += 1
                return time
            else:
                number = queuers.pop(0)
                queuers.append(number - 1)
                pos = len(queuers) - 1
                time += 1
        else:
            number = queuers.pop(0)
            if number != 1:
                queuers.append(number - 1)
            pos -= 1
            time += 1
        # print(queqe, time, position)


print(queue([2, 5, 3, 6, 4], 3))
