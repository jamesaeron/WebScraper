from bs4 import BeautifulSoup
import requests
import os
import texttable
import csv


class Validation:
    def __init__(self):
        self.response = 0

    def ping(self, host):
        self.response = os.system("ping " + host)
        while True:
            if self.response == 0:
                return 1
            return 0


class Scrape:
    def __init__(self):
        self.scrapelist = []
        self.newlist = []
        self.row = 0
        self.textTable = texttable.Texttable()

    def write_csv(self):
        with open('m.csv', 'w') as WriteCSV:
            writing = csv.writer(WriteCSV, delimiter=",", lineterminator='\n')
            for eachChild in self.newlist:
                writing.writerow(eachChild)
        return

    def scraping(self, page):
        source = requests.get(page).text
        souping = BeautifulSoup(source, 'html.parser')
        candidate = souping.find(id='votes-by-voting-place-summary')
        d = candidate.find('tbody').find_all(text=True)
        for r in d:
            self.scrapelist.append(r.strip())
        while "" in self.scrapelist:
            self.scrapelist.remove("")
        del self.scrapelist[:3]
        self.newlist.insert(0, ['Candidates', 'Party', 'Votes', 'Percentages'])
        for self.row in range(self.row, len(self.scrapelist), 4):
            self.newlist.append(self.scrapelist[self.row:self.row + 4])
        self.textTable.add_rows(self.newlist)
        Scrape.write_csv(self)
        return self.textTable.draw()


class Message:
    def __init__(self, msg):
        self.msg = msg
        self.msglength = 0
        self.layout = ''

    def __str__(self):
        self.msglength = len(self.msg)
        h = ''.join(['<'] + ['~' * self.msglength] + ['>'])
        self.layout = h + '\n|' + self.msg + '|\n' + h
        return self.layout


class User:
    def __init__(self):
        self.validate = Validation()
        self.scrape = Scrape()
        self.hosts = ''
        self.hostconnector = ''
        self.webpage = ''
        self.outcome = ''

    def host(self):
        print(Message("Please enter the original website url first to validate if it can be access "
                    "e.g. www.google.com not the location of where you want to scrape"))
        self.hosts = str(input("Please type the Web URL: "))
        while True:
            if self.validate.ping(self.hosts) == 1:
                print('\n' * 50)
                use.transitive()
            else:
                use.host()
            break
        return

    def transitive(self):
        print(Message('Please enter the location where you want to scrape'))
        self.hostconnector = str(input('Please enter the connector for the url you have put in the first: '))
        self.webpage = 'http://' + self.hosts + self.hostconnector
        self.outcome = self.scrape.scraping(self.webpage)
        print(self.outcome)
        return


if __name__ == '__main__':
    use = User()
    use.host()
