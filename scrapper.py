import requests
import bs4 as bs

class Scrapper:    
    def search(self, query):
        """
        Search for the query of the user on the specific search engine.
        Input:
        - query: request by given user
        Output:
        - self.result: outcome of the search query
        """
        # Gets the request from the user
        self.req = requests.get(query)
        # Returns the text of the results from the search query
        self.result = self.req.text
        return self.result

    def save_results(self, results):
        """
        Saves the results of the search into a HTML file.
        Input:
        - results: results of the search
        Output:
        - self.backtrack: backtrack file with the saved results
        """
        with open("search_results.html", "w", encoding="utf-8") as self.backtrack:
            # Writes the results in the HTML file
            self.backtrack.write(results)
        return results in open("search_results.html", "r")


    def display(self, results_number, engine):
        """
        Displays the results from the search query.
        Input:
        - results_number: number results (links) of the search
        - engine: search engine to be used
        Output: None
        """
        # Reads the HTML file
        self.html_file = open('search_results.html', encoding="utf-8").read()
        # Parses the HTML file
        self.parser = bs.BeautifulSoup(self.html_file, 'html.parser')
        list = []
        # If the search engine to use is Google
        if "google" in engine.lower():
            for elem in self.parser.find_all("div", {"class": "ZINbbc xpd O9g5cc uUPGi"}):
                # Processes and adds each result from the HTML file to the list
                result = "Result: {0}".format(elem.text)
                list.append(result)
        # If the search engine to use is Yandex
        else:
            for elem in self.parser.find("ul", {"class": "serp-list serp-list_left_yes"}).find_all('a', {"class": 'link link_theme_outer path__item i-bem'}):
                # Processes and adds each result from the HTML file to the list
                result = "Result: {0}\n{1}".format(elem.text, elem.get('href'))
                list.append(result)

        for i in range(len(list)):
            print(list[i])
