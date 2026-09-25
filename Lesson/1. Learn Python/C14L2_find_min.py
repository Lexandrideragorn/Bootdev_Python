def find_min(nums: list[int]) -> int | float:
    MAX=float("inf")

    for num in nums:
        if num < MAX:
            MAX = num

    return MAX
