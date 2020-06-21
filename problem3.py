def get_connections(m_dict, member, follows, path=[], connections = []):
    path = path + [member]
    
    if follows in m_dict[member]:
        connections.append(member)
    
    for i in m_dict[member]:
        if i not in path:
            connections = get_connections(m_dict, i, follows, path, connections)
    return connections
            
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

    members_dict = {'2': ['9'], '5': [], '7': ['2', '9'], '9': ['5']}
    
    member = input("member: ")
    follow = input("following: ")

    print(members_dict)
    output = get_connections(members_dict, member, follow)
    output.sort()
    print(" ".join(output))

if __name__ == "__main__":
    main()