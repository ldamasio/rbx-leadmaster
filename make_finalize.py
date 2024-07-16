username_list_filename = "usernames_007.txt"
url_list_filename = "urls_007.txt"

def finalize(followers):
    for i in followers:
        with open(username_list_filename, "a", encoding="utf-8") as file:
            file.write("\n"+i)
        with open(url_list_filename, "a", encoding="utf-8") as file:
            file.write("\nhttps://instagram.com/" + i)
    print('teste')










