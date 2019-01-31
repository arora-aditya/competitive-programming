class Solution:
    def numUniqueEmails(self, emails):
        """
        https://leetcode.com/problems/unique-email-addresses/description/
        :type emails: List[str]
        :rtype: int
        """
        unique = set()

        for email in emails:
            user, domain = email.split("@")
            user = user.split("+")[0].replace(".", "")
            unique.add(user+domain)


        return len(unique)
