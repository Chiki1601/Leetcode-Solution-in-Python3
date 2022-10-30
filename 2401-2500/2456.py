class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        memo = {}
        overall_max_popular_video_count = -1
        for i in range(len(creators)):
            if creators[i] in memo:
                memo[creators[i]][0] += views[i]
                if memo[creators[i]][2] < views[i]:
                    memo[creators[i]][1] = ids[i]
                    memo[creators[i]][2] = views[i]
            
                elif memo[creators[i]][2] == views[i]:
                    memo[creators[i]][1] = min(memo[creators[i]][1],ids[i])
            else:
			
                memo[creators[i]] = [views[i],ids[i],views[i]]
		
            overall_max_popular_video_count = max(memo[creators[i]][0],overall_max_popular_video_count)
        
        result = []
        for i in memo:
            if memo[i][0] == overall_max_popular_video_count:
                result.append([i,memo[i][1]])
        return result
