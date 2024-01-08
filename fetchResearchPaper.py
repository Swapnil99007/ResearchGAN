import arxiv

class FetchResearchPaper:
    def __init__(self):
        pass

    def fetchResearchPaper(self):
        # Construct the default API client.
        arxivClient = arxiv.Client()

        # Search for the paper with ID "2401.01871v1"
        search_by_id = arxiv.Search(id_list=["2401.01871v1"])
        # Reuse client to fetch the paper.
        first_result = next(arxivClient.results(search_by_id))
        researchPaperTitle = first_result.title
        researchPaperSummary = first_result.summary
        researchData = tuple((researchPaperTitle, researchPaperSummary))

        return researchData