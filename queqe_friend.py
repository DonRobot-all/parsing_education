# Queue time counter
queqe = [2, 5, 3, 6, 4]
len_queqe = len(queqe)
position = 1
time = 0


def queue_time(customers, n):
    tills = [0] * n

    for i in customers:
        min_till = min(tills)

        min_till_index = tills.index(min_till)
        tills[min_till_index] += i

    return max(tills) + 1

print(queue_time(queqe, position))
# [2, 5, 3, 6, 4]
# [5, 3, 6, 4, 1] 1
# [3, 6, 4, 1, 4] 2
# [6, 4, 1, 4] 3
# [4, 1, 4] 4
# [1, 4] 5
# [1, 4] 6

# for count in range(sum(queqe)):
#     if queqe[0] > 1:
#         queqe.append(queqe.pop(0) - 1)
#     else:
#         queqe.remove(1)
#     time += 1
#     position -= 1
#     if position == 0:
#         position = len(queqe)
#     # if abs(position) % len_queqe == 0 and queqe[0] == 1:
#     #     break
#     # if position < 0:
#     #     if queqe[position] == 1:
#     #         break
#     #     position = len(queqe)
#     print(queqe, time, position)

