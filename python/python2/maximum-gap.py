class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        max_item = nums[0]
        min_item = nums[0]

        for i in nums:
            max_item = max(max_item, i)
            min_item = min(min_item, i)

        bucket_gap = (max_item - min_item) / (len(nums) - 1)

        # [1, 1, 1, 1]
        if bucket_gap == 0:
            bucket_gap = 1

        bucket_count = (max_item - min_item) / bucket_gap + 1

        bucket = []
        for i in range(bucket_count):
            bucket.append([None, None])

        for i in nums:
            index = (i - min_item) / bucket_gap

            if bucket[index][0] is None:
                bucket[index][0] = bucket[index][1] = i
            else:
                bucket[index][0] = min(bucket[index][0], i)
                bucket[index][1] = max(bucket[index][1], i)

        bucket = [b for b in bucket if b[0] is not None]

        if len(bucket) == 1:
            return 0

        return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))


if __name__ == '__main__':
    # Bucket Sort
    print Solution().maximumGap([1, 1, 1, 1])