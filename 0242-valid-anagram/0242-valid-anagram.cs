public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;
        if (s == t) return true;
        
        List<char> list = new List<char>(s);
        for(int i=0; i<t.Length; i++)
        {
            if(list.Contains(t[i]))
            {
                list.Remove(t[i]);
            }
            else
            {
                return false;
            }
        }
        return list.Count > 0 ? false : true;
    }
}