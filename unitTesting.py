from scraper import Validation, User, Scrape, Message
import unittest


class Test_Validation_Method(unittest.TestCase):
    def setUp(self):
        self.validate = Validation()

    def test_validation_response(self):
        self.assertTrue(hasattr(self.validate, 'response'))
        self.assertEqual(type(self.validate.response), int)

    def test_validation_ping(self):
        self.assertTrue(hasattr(self.validate, 'ping'))
        self.assertTrue(callable(getattr(self.validate, 'ping', None)))

    def test_validation_pingfunc(self):
        host_A = 'www.electionresults.govt.nz'
        icmpA = Validation.ping(self, host_A)
        self.assertEqual(icmpA, 1)


class Test_User_Method(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_user_hosts(self):
        self.assertTrue(hasattr(self.user, 'hosts'))
        self.assertEqual(type(self.user.hosts), str)

    def test_user_hostconnector(self):
        self.assertTrue(hasattr(self.user, 'hostconnector'))
        self.assertEqual(type(self.user.hostconnector), str)

    def test_user_webpage(self):
        self.assertTrue(hasattr(self.user, 'webpage'))
        self.assertEqual(type(self.user.webpage), str)

    def test_user_outcome(self):
        self.assertTrue(hasattr(self.user, 'outcome'))
        self.assertEqual(type(self.user.outcome), str)

    def test_user_host(self):
        self.assertTrue(hasattr(self.user, 'host'))
        self.assertTrue(callable(getattr(self.user, 'host', None)))

    def test_user_transitive(self):
        self.assertTrue(hasattr(self.user, 'transitive'))
        self.assertTrue(callable(getattr(self.user, 'transitive', None)))


class Test_Message_Method(unittest.TestCase):
    def setUp(self):
        self.msg = 'Hello'
        self.message = Message(self.msg)

    def test_message_length(self):
        self.assertTrue(hasattr(self.message, 'msglength'))
        self.assertEqual(type(self.message.msglength), int)

    def test_message_msg(self):
        self.assertTrue(hasattr(self.message, 'msg'))
        self.assertEqual(type(self.message.msg), str)

    def test_message_layout(self):
        self.assertTrue(hasattr(self.message, 'layout'))
        self.assertEqual(type(self.message.layout), str)

    def test_message_strfunc(self):
        self.assertTrue(hasattr(self.message, '__str__'))
        self.assertTrue(callable(getattr(self.message, '__str__', str)))


class Test_Scrape_Method(unittest.TestCase):
    def setUp(self):
        self.scrape = Scrape()

    def test_scrape_list(self):
        self.assertTrue(hasattr(self.scrape, 'scrapelist'))
        self.assertEqual(type(self.scrape.scrapelist), list)
        self.assertEqual(len(self.scrape.scrapelist), 0)

    def test_scrape_newlist(self):
        self.assertTrue(hasattr(self.scrape, 'newlist'))
        self.assertEqual(type(self.scrape.newlist), list)
        self.assertEqual(len(self.scrape.newlist), 0)

    def test_scrape_row(self):
        self.assertTrue(hasattr(self.scrape, 'row'))
        self.assertEqual(type(self.scrape.row), int)

    def test_scrape_csv(self):
        self.assertTrue(hasattr(self.scrape, 'write_csv'))
        self.assertTrue(callable(getattr(self.scrape, 'write_csv', None)))

    def test_scrape_page(self):
        import texttable
        self.scrapelist = []
        self.newlist = []
        self.row = 0
        self.textTable = texttable.Texttable()
        page = 'https://www.electionresults.govt.nz/electionresults_' \
               '2017/statistics/candidate-votes-by-voting-place-36.html'
        scrapePage = Scrape.scraping(self, page)
        self.assertEqual(scrapePage, self.textTable.draw())


if __name__ == '__main__':
    unittest.main(verbosity=3)
