def get_short_time(m_dict, member, follows, path=[], time=0, durations=[]):
    path = path + [member]
    if follows in m_dict[member].keys():
        durations.append(time + m_dict[member][follows])
    
    for i in m_dict[member]:
        if i not in path:
            time = time + m_dict[member][i]
            durations = get_short_time(m_dict, i, follows, path, time, durations)
    return durations
            
def main():
    members_dict = dict()
    n = int(input("No. of Vertices: "))
    for i in range(n):
        in_member = input()
        if in_member not in members_dict.keys():
            members_dict[in_member] = dict()
    n = int(input("No. of Edges: "))
    for i in range(n):
        in_member, follow, time = list(input().split())
        members_dict[in_member][follow] = int(time)

    members_dict = {'2': {'9': 2}, '5': {}, '7': {'2': 3, '9': 7}, '9': {'5': 1}}

    member = input("member: ")
    follow = input("following: ")

    print(members_dict)
    print(min(get_short_time(members_dict, member, follow)))

if __name__ == "__main__":
    main()