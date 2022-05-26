from .scraper.scraper import Scraper

class Crawler(Scraper):
    def __init__(self, keyword) -> None:
        super().__init__(keyword)

    async def crawl(self):
        page = super().open_page()
        super().get_products()
        page_len = int(super().get_last_page_numer())

        for page in range(2, page_len+1):
            super().open_page(page)
            super().get_products()
        
        super().close_page()