class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = []
        p_product = 1
        for i in range(len(nums)):
            if i != 0:
                p_product *= nums[i - 1]
            products.append(p_product)
        
        s_product = 1
        for j in range(len(nums) -1, -1, -1):
            if j != len(nums) - 1:
                s_product *= nums[j + 1]
            products[j] *= s_product

        return products