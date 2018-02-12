import unittest
import flaskr


class EmbedReportTest(unittest.TestCase):
    def setUp(self):
        app = flaskr

    def tearDown(self):
        pass

    def test(target_sys, report_path, report_query):
        ReportClass = report_types[target_sys]
        r = ReportClass(report_path, report_query)
        ticket = r.get_ticket()
        print('ticket:%s' % ticket)
        url = r.get_full_url()
        print(url)


if __name__ == '__main__':
    from sci.models.superset import EmbedReport
    from superset import db
    reports = db.session.query(EmbedReport).all()
    for report in reports:
        _ = '=' * 10
        print(_ + 'Test ' + report.report_name + ":" + report.target_sys + _)
        test(report.target_sys, report.report_path, report.report_query)
