import src.data_preprocessing as data_prep


def test_read_xml_dataset():
    path = "/Users/virginiapujols/Documents/RIT/SEMESTER 4/Data science/FinalProject/bugs_dedupl_data_science/src/data/test_reports.xml"
    bug_reports = data_prep.parse_xml_to_bug_reports(path)
    print(bug_reports[0].id)
    assert bug_reports[0].id != ""


test_read_xml_dataset()

