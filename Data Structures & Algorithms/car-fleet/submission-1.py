class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position,speed))
        pairs.sort(reverse=True)
        
        stack = []

        for pair in pairs:
            if not stack:
                stack.append(pair)
                continue
            
            current = float((target - pair[0]) / pair[1])
            previous = float((target - stack[-1][0]) / stack[-1][1])

            if current > previous:
                stack.append(pair)
        
        return len(stack)