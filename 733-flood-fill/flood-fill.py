class Solution:
    def floodFill(self, image, sr, sc, color):
        # base case : current color is already what we're looking for 
        if image[sr][sc] == color:
            return image
        # otherwise, look for a recursive way to apply the changes to current 
        # and other pixels
        self.floodHelper(image,sr,sc,color, image[sr][sc])
        return image
    
    def floodHelper(self,image, sr,sc,color, current):
        if sr <0 or sr >= len(image) or sc<0 or sc>=len(image[0]):
            return 
        if current != image[sr][sc]:
            return 
        image[sr][sc] = color
        self.floodHelper(image,sr + 1,sc,color,current)
        self.floodHelper(image,sr,sc +1,color,current)
        self.floodHelper(image,sr - 1,sc,color,current)
        self.floodHelper(image,sr,sc-1,color,current)