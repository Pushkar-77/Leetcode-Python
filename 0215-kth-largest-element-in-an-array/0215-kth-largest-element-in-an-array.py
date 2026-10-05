class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        c = len(nums) - k

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            pivot = nums[mid]

            p = left
            i = left
            q = right

            while i <= q:
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[q] = nums[q], nums[i]
                    q -= 1

                else:
                    i += 1

            if c < p:
                right = p - 1

            elif c > q:
                left = q + 1

            else:
                return pivot