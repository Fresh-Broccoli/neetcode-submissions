class Solution:
    def trap(self, height: List[int]) -> int:
        height_l, height_r = 0, 0
        i, j = 0, len(height) - 1
        water = [0 for _ in height]

        # Update the side with lower highest
        while i <= j:
            #print("i:", i)
            #print("j:", j)
            #print("height_l:", height_l)
            #print("height_r:", height_r)
            if height_r > height_l:
                #print("Processing left...")
                # If the right is higher, we'll work on the left
                water[i] = min(height_l, height_r) - height[i]
                water[i] = water[i] if water[i] >= 0 else 0
                #print(f"water[{i}]:", water[i])
                # Update highest left:
                height_l = height[i] if height[i] > height_l else height_l
                #print(f"Updated height[{i}]:", height[i])
                # Update left pointer
                i += 1
            else:
                #print("Processing right...")
                # If the left is higher, we'll work on the right
                water[j] = min(height_l, height_r) - height[j]
                water[j] = water[j] if water[j] >= 0 else 0
                #print(f"water[{j}]:", water[j])
                # Update highest right:
                height_r = height[j] if height[j] > height_r else height_r
                #print(f"Updated height[{j}]:", height[j])
                # Update left pointer
                j -= 1
        #print("water:", water)
        return sum(water)