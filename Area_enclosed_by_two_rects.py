class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        ini_areas = (ay2-ay1)*(ax2-ax1) + (by2-by1)*(bx2-bx1)
        if bx2 >= ax2: 
            if bx1 >= ax2: #no overlap in axis
                return ini_areas
            else:
                width = ax2 - max(ax1,bx1) #ax2 as it has already been calculated
        else:
            ax1,bx1 = bx1,ax1
            ax2,bx2 = bx2,ax2
            if bx1 >= ax2: #no overlap in axis
                return ini_areas
            else:
                width = ax2 - max(ax1,bx1) #ax2 as it has already been calculated
            #SWAP AND SEARCH
        if by2 >= ay2: 
            if by1 >= ay2: #no overlap in axis
                return ini_areas
            else:
                length = ay2 - max(ay1,by1) #ax2 as it has already been calculated
        else:
            ay1,by1 = by1,ay1
            ay2,by2 = by2,ay2
            if by1 >= ay2: #no overlap in axis
                return ini_areas
            else:
                length = ay2 - max(ay1,by1) #ax2 as it has already been calculated
        return ini_areas - length*width
