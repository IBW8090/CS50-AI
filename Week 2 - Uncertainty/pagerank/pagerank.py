import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probDist = {pageName : 0 for pageName in corpus}

    # This if statement will assume the same probability to every page if the page has no links as the surfer can not travel.
    if len(corpus[page]) == 0:
        for pageName in probDist:
            probDist[pageName] = 1 / len(corpus)
        return probDist

    #Probability of randomly selecting that page from the corpus while ignoring any links on the page (1-damping).
    randomProbability = (1 - damping_factor) / len(corpus)

    #Probabiity of selecting a specific link on the current page with damping factor being the chance for each link divided by the number of links.
    linkProbability = damping_factor / len(corpus[page])

    #Iterate over the dictionary adding the probability of each page to the dictionary based on if it is linked in the current page.
    for pageName in probDist:
        probDist[pageName] = probDist[pageName] + randomProbability
        if pageName in corpus[page]:
            probDist[pageName] = probDist[pageName] + linkProbability

    return probDist

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    visits = {pageName: 0 for pageName in corpus}

    #Pick a random page and start there
    currentPage = random.choice(list(visits))
    visits[currentPage] = visits[currentPage] + 1

    #For all the remaining samples of pages, pick a page based on the transition model's probabilities
    for i in range(0, n-1):
        transitionModel = transition_model(corpus, currentPage, damping_factor)

        pages = list(transitionModel.keys())
        probabilities = list(transitionModel.values())
        #Pick a random item from pages with each item having the weighted probability of the corresponding item in probabilities. Always returns as a list so [0] grabs first item.
        currentPage = random.choices(pages, probabilities)[0]

        visits[currentPage] = visits[currentPage] + 1

    #Divide the amount of time the surfer spent on each page by n to ensure that everything is a probability and is not greater than 1.
    pageRanks = {pageName: (timesVisited / n) for pageName, timesVisited in visits.items()}
    return pageRanks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    numPages = len(corpus)
    initialRank = 1 / numPages
    randomProbability = (1 - damping_factor) / numPages
    iterations = 0

    pageRanks = {pageName: initialRank for pageName in corpus}
    newRanks = {pageName : None for pageName in corpus}
    maximumRankChange = initialRank

    #Iterates through the rankings until they stop changing. Larger values will be less accurate.
    while maximumRankChange > 0.001:
        iterations += 1
        maximumRankChange = 0

        for pageName in corpus:
            choiceProbability = 0
            for otherPage in corpus:
                #If it has no links, pick randomly
                if len(corpus[otherPage]) == 0:
                    choiceProbability += pageRanks[otherPage] * initialRank
                # Else if the other page has a link to the original page, then randomly pick from all the links on that page.
                elif pageName in corpus[otherPage]:
                    choiceProbability += pageRanks[otherPage] / len(corpus[otherPage])
            newRanks[pageName] = randomProbability + (damping_factor * choiceProbability)

        #Normalise to ensure nothing >1
        normalisedFactor = sum(newRanks.values())
        newRanks = {page: (rank / normalisedFactor) for page, rank in newRanks.items()}

        #Find maximum change
        for pageName in corpus:
            rankChange = abs(pageRanks[pageName] - newRanks[pageName])
            if rankChange > maximumRankChange:
                maximumRankChange = rankChange

        #Update pageRanks to reflect the new ranks
        pageRanks = newRanks.copy()

    return pageRanks
if __name__ == "__main__":
    main()
