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
    res = {}
    links = corpus[page]

    if len(links) == 0:
        value = 1 / len(corpus)
        for page in corpus:
            res.update({page: value})
    else:
        sizeOfLinks = len(links)
        sizeOfCorpus = len(corpus)

        for page in links:
            res[page] = damping_factor / sizeOfLinks

        for page in corpus:
            if page in res:
                res[page] += (1 - damping_factor)/sizeOfCorpus
            else:
                res[page] = (1 - damping_factor)/sizeOfCorpus
    return res



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pageRank = {page: 0 for page in corpus}
    corpusList = list(corpus.keys())

    currentPage = random.choice(corpusList)

    for i in range(n):
        pageRank[currentPage] += 1
        transitionProb = transition_model(corpus, currentPage, damping_factor)
        pages = list(transitionProb.keys())
        probilities = list(transitionProb.values())
        currentPage = random.choices(pages, weights=probilities, k=1)[0]

    for page in pageRank:
        pageRank[page] /= n
    return pageRank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pageRank = {page: 1 / len(corpus) for page in corpus}
    newPageRank = pageRank.copy()

    while True:
        change = 0
        for page in corpus:
            rankSum = 0
            for possibleLinker in corpus:
                if page in corpus[possibleLinker]:
                    rankSum += pageRank[possibleLinker] / len(corpus[possibleLinker])
                elif not corpus[possibleLinker]:
                    rankSum += pageRank[possibleLinker] / len(corpus)

            newRank = (1 - damping_factor) / len(corpus) + damping_factor * rankSum
            change = max(change, abs(newRank - newPageRank[page]))
            newPageRank[page] = newRank
        if change < 0.001:
            break

        pageRank = newPageRank.copy()

    return newPageRank


if __name__ == "__main__":
    main()
