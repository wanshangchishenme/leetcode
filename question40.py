class Solution:
    # It's a DP(Dynamic Programming) soluction.
    # Split the question target into (i + (target - i)) and then drop the invalid results.
    # It's not a very good soluction because we must filter the invalid results.
    # A better solution is Traversing the list candidates and use the element to calculate the table.
    # For example, a number x which is little than target should be put the tables from table[x] to table[target].
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res_dict = dict()

        # used to filter the invalid values.
        def valid(candidates, res_raw):
            """
            :type candidates: List[int]
            :type res_raw: set(tuple(int))
            :rtype: set(tuple(int))
            """
            res = set()
            for i in res_raw:
                list_i = list(i)
                list_i.sort()
                k = 0
                flag = True
                for j in list_i:
                    if k >= len(candidates) or j < candidates[k]:
                        flag = False
                        break

                    while j > candidates[k]:
                        k += 1
                    if j == candidates[k]:
                        k += 1

                if flag:
                    res.add(tuple(list_i))
            return res

        # use recursion to find the result and store the temporary in a dictionary.
        def combinationSum2_helper(candidates, target):
            """
            :type candidates: List[int]
            :type res_raw: set(tuple(int))
            :rtype: set(tuple(int))
            """
            res = set()
            if target in candidates:
                res.add((target,))
            if str(target) in res_dict:
                return res_dict[str(target)]

            for i in range(1, ((target // 2) + 1)):
                for j in combinationSum2_helper(candidates,i):
                    for k in combinationSum2_helper(candidates,target - i):
                        res.add(j + k)
            
            res_dict[str(target)] = valid(candidates, res);
            return res_dict[str(target)]

        res_raw = combinationSum2_helper(candidates,target)
        res_raw = list(res_raw)
        res = map(list, res_raw)
        return res

    # Another method to solve this problem and it's much faster than the upper one.
    # it's a solution in the leetcode.
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        temporary_table = [set() for i in range(0, target + 1)]
        temporary_table[0].add(())
        candidates.sort()
        for num in candidates:
            if num > target:
                break
            for index in range(target, num - 1, -1):
                for temp in temporary_table[index - num]:
                    temporary_table[index].add(temp + (num,))
        return list(map(list, temporary_table[-1]))
