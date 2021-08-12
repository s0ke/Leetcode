for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    summ=nums[i]+nums[j]
    if summ==target:
      return([i,j])
