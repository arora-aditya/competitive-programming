class Solution(object):
    def trimBST(self, root, L, R):
        """
        https://leetcode.com/problems/trim-a-binary-search-tree/description/
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        li = []
        for i in ans:
            li.extend(i)

        class searchtree:

              def __init__(self): #constructor of class
                  self.root = None


              def create(self,val):  #create binary search tree nodes
                  if self.root == None:
                     self.root = TreeNode(val)
                  else:
                     current = self.root
                     while 1:
                         if val < current.val:
                           if current.left:
                              current = current.left
                           else:
                              current.left = TreeNode(val)
                              break;
                         elif val > current.val:
                            if current.right:
                               current = current.right
                            else:
                               current.right = TreeNode(val)
                               break;
                         else:
                            break
        T = searchtree()
        # print(li)
        for i in li:
            if i >= L and i <= R and i != None:
                T.create(i)
        return T.root
