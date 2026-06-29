class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for x in nums:
            num_dict[x] = num_dict.get(x, 0) + 1

        most_frequent = max(num_dict, key=num_dict.get)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in num_dict.items():
            buckets[count].append(num)
        
        k_values = []
        for bucket in reversed(buckets):
            if(bucket):
                for num in bucket:
                    if(k > 0):
                        k_values.append(num)
                    k = k - 1

        return k_values
