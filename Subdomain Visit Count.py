class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for domain in cpdomains:
            num, string = domain.split()
            num = int(num)
            subdomains = string.split(".")

            if len(subdomains) == 2:
                d[subdomains[-1]] += num
                d[subdomains[0]+ "." + subdomains[-1]] += num
            elif len(subdomains) == 3:
                d[subdomains[-1]] += num
                d[subdomains[-2]+ "." + subdomains[-1]] += num
                d[subdomains[-3]+ "." + subdomains[-2]+ "." + subdomains[-1]] += num


        return [f"{v} {k}" for k,v in d.items()]

        
