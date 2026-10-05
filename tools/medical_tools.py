from duckduckgo_search import DDGS


class MedicalTools:

    def __init__(self):

        self.sources = []

    def search(
        self,
        query: str,
        max_results: int = 5
    ):

        results = []

        self.sources = []

        search_query = (
            f"site:webmd.com {query}"
        )

        with DDGS() as ddgs:

            matches = ddgs.text(
                search_query,
                max_results=max_results
            )

            for item in matches:

                title = item.get(
                    "title",
                    ""
                )

                body = item.get(
                    "body",
                    ""
                )

                href = item.get(
                    "href",
                    ""
                )

                self.sources.append(
                    href
                )

                results.append(
                    f"Title: {title}\n"
                    f"Content: {body}\n"
                    f"Source: {href}"
                )

        return results

    def get_sources(self):

        return self.sources