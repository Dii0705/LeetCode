class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set() # set doesn't allow duplicates
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.replace(".","")
            local_name = local_name.split("+")[0]
            email = local_name + "@" + domain_name
            unique_emails.add(email)
        return len(unique_emails)