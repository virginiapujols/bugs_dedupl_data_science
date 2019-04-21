from src.data import make_dataset


def test_read_xml_dataset():
    path = "/Users/virginiapujols/Documents/RIT/SEMESTER 4/Data science/FinalProject/dups/src/data/dataset/test_reports.xml"
    bug_reports = make_dataset.parse_xml_to_bug_reports(path)
    print(bug_reports[0].id)
    assert bug_reports[0].id != ""


test_read_xml_dataset()

