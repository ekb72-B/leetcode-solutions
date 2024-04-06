class Solution:
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        
        self.floodFillHelper(image,sr,sc,color, image[sr][sc])
        return image
    
    def floodFillHelper(self,image,sr,sc,color, current):
        if sr < 0 or sr >= len(image) or sc<0 or sc>= len(image[0]):
            return

        if current != image[sr][sc]:
            return
        
        image[sr][sc] = color
        
        self.floodFillHelper(image, sr -1, sc, color,current) 
        self.floodFillHelper(image, sr, sc-1, color,current) 
        self.floodFillHelper(image, sr+1, sc, color,current) 
        self.floodFillHelper(image, sr, sc+1, color,current) 
      