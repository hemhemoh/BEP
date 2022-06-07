def gscholar(name):
    prefix = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&as_vis=1&q="
    suffix = "&btnG="
    name = name.replace(' ', '+').replace(',', '%2C').replace('–', '%E2%80%93')
    return prefix+name+suffix

def mendely(name):
    prefix = "https://www.mendeley.com/search/?query="
    suffix  = "&dgcid=md_homepage"
    name = name.replace(' ', '+').replace(',', '%2C').replace('–', '%E2%80%93')
    return prefix+name+suffix


if __name__ == '__main__':
    print("Google Scholar Link",gscholar("Aishwarya Agrawal, Dhruv Batra, and Devi Parikh. Analyzing the behavior of visual question answering models. In Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing, pages 1955–1960, Austin, Texas, November 2016. Association for Computational Linguistics."))
    print("Mendeley Link:",mendely("Aishwarya Agrawal, Dhruv Batra, and Devi Parikh. Analyzing the behavior of visual question answering models. In Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing, pages 1955–1960, Austin, Texas, November 2016. Association for Computational Linguistics."))

