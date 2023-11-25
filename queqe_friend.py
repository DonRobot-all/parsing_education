# # Queue time counter
# def queue(queuers, pos, time=0):
#     for count in range(sum(queuers)):
#         if pos == 0:
#             if queuers[pos] == 1:
#                 time += 1
#                 return time
#             else:
#                 number = queuers.pop(0)
#                 queuers.append(number - 1)
#                 pos = len(queuers) - 1
#                 time += 1
#         else:
#             number = queuers.pop(0)
#             if number != 1:
#                 queuers.append(number - 1)
#             pos -= 1
#             time += 1
#         # print(queqe, time, position)

def queue(queuers,pos):
    ticket_Need = queuers[pos]
    frontFriend = queuers[:pos+1]
    backFriend = queuers[pos+1:]
    frontFriend = [min(x, ticket_Need) for x in frontFriend]
    backFriend = [min(x, ticket_Need-1) for x in backFriend]
    return sum(frontFriend) + sum(backFriend)


print(queue([2, 5, 3, 6, 4], 2))
