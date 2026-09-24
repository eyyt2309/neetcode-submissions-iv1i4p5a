from collections import defaultdict, deque
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        edgeSet = {}
        visited = {}

        new_accounts = [x[1:] for x in accounts]

        for edges in new_accounts:
            i = 0
            while i < len(edges) - 1:
                if edges[i] not in edgeSet:
                    edgeSet[edges[i]] = set()
                if edges[i+1] not in edgeSet:
                    edgeSet[edges[i+1]] = set()
                edgeSet[edges[i]].add(edges[i + 1])
                edgeSet[edges[i+1]].add(edges[i])
                i += 1
        
        ans = []

        for account in accounts:
            arr = []
            if account[1] not in edgeSet: # email is isolated
                arr.append(account[1])
            elif account[1] not in visited: # current email not visited yet
                queue = deque([account[1]])
                visited[account[1]] = True

                while queue:
                    curr_email = queue.popleft()
                    arr.append(curr_email)

                    for neighbor in edgeSet[curr_email]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited[neighbor] = True
            elif account[1] in visited:
                continue

            arr.sort()
            arr.insert(0, account[0])
            ans.append(arr[:])

        return ans
        
