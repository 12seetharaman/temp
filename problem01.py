def check_follows(m_dict, member, follows, path=[]):
    path = path + [member]
    
    if follows in m_dict[member]:
        return 1
    
    for i in m_dict[member]:
        if i not in path:
            if check_follows(m_dict, i, follows, path):
                return 1
    return 0
            
def main():
    members_dict = dict()
    n = int(input("No. of Vertices: "))
    for i in range(n):
        in_member = input()
        if in_member not in members_dict.keys():
            members_dict[in_member] = []
    n = int(input("No. of Edges: "))
    for i in range(n):
        in_member, follow = list(input().split())
        members_dict[in_member].append(follow)

    member = input("member: ")
    follow = input("following: ")

    print(members_dict)
    print(check_follows(members_dict, member, follow))

if __name__ == "__main__":
    main()