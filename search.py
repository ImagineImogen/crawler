import sys
import argparse
from scrapper import Scrapper

class Search(Scrapper):
    def __init__(self, query, results, engine):
        self.query = query
        self.results = results
        self.engine = engine

    def main(self):
        """
        Main function of the scrapper.
        Input:
        - self.query: request by given user
        - self.results: number of links to parse
        - self.engine: name of the search engine to use
        Output: None
        """
        self.query = '+'.join(self.query.split())
        # If the search engine to use is Yandex
        if "yan" in self.engine.lower():
            self.engine = 'https://yandex.ru/search/?text=' + self.query + '&' + 'numdoc=' + str(self.results)
        # If the search engine to use is Google
        elif "goo" in self.engine.lower():
            self.engine = 'https://www.google.ru/search?q=' + self.query + '&' + 'num=' + str(self.results)
        # If the search engine to use is something else
        else:
            print("Search engine not recognize.")
            
        s = self.search(self.engine)
        self.save_results(s)
        self.display(self.results, self.engine)
        return s

if __name__ == '__main__':
    if len (sys.argv) != 3:
        sys.exit('Usage: %s database-name' % sys.argv[0])
    query, results, engine = sys_argv[1], sys_argv[2], sys_argv[3]
    parser = argparse.ArgumentParser(description='Web scrapper in Python')
    parser.add_argument('--search', type=str, help='Search query', required=True)
    parser.add_argument('--links', type=int, help='Number of links', required=True)
    parser.add_argument('--engine', type=str, help='Search engine', required=True)
    args = parser.parse_args()

    s = Search(query, results, engine)
    s.main()
