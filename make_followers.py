import re

def remove_substring(string, suffix):
    if string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string

class HTMLAltSearcher:
    def __init__(self, html_file):
        self.html_file = html_file


    def search_alt_occurrences(self):
        with open(self.html_file, 'r') as f:
            html_content = f.read()

        search_pattern = r'alt\s*=\s*"(.*?)"'
        alt_occurrences = re.findall(search_pattern, html_content)
        result = []
        for item in alt_occurrences:
            result.append(remove_substring(item, "'s profile picture"))
        return result


# Example usage
html_file = './data/cd_007.html'
alt_searcher = HTMLAltSearcher(html_file)
alt_occurrences = alt_searcher.search_alt_occurrences()
print("Leads gerados:")
print(alt_occurrences)
print(len(alt_occurrences))


with open("./data/make_followers_007.py", "w", encoding="utf-8") as file:
    file.write("followers = " + str(alt_occurrences))
