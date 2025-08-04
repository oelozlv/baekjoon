public class Solution {
    public static void main(String[] args) {
        n = int(input())
        filenames = [input() for _ in range(n)]
        
        pattern = ""
        
        for i in range(len(filenames[0])):
            char_set = set(filename[i] for filename in filenames)
            if len(char_set) == 1:
                pattern += filenames[0][i]
        else:
            pattern += '?'
        
        print(pattern)
    }
}