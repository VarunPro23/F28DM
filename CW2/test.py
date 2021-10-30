from lxml import etree
import glob

# Run an XPath query stored in a file against an XML document
def run_query(query_file, xml_doc):
    xpath_query = ''
    # open and read xpath query file
    with open(query_file, 'r') as file:
        lines = file.read().splitlines()

        for line in lines: 
            if not (line.startswith('#') or line == ""): 
                xpath_query = line
    
    if xpath_query != '':
        print('Query:', xpath_query)
        try:
            result = xml_doc.xpath(xpath_query)
        except etree.XPathEvalError:
                return False

        if isinstance(result, list) and len(result) > 0:
            return True
        elif str(result) != "":
            return True
    else:
        print('Query: No query provided yet.')


    return False

#Main Method
if __name__ == "__main__":
    xml_file = "data.xml"
    xmldoc = etree.parse(xml_file)
    
    xpath_error_counter = 0
    total_xpath = 0
    #run the xpath query from folder
    print('\nRun xPath queries\r\n')
    for query_file in glob.glob('xpaths/*.xpath'):
        total_xpath = total_xpath + 1
        if run_query(query_file, xmldoc):
             print('SUCCESS:', query_file, 'executes')
        else:
            print('FAIL:', query_file, 'to execute')
            xpath_error_counter = xpath_error_counter + 1
    
    if xpath_error_counter > 0:
        print(str(xpath_error_counter) + "/" + str(total_xpath) + " xpaths failed.")
        exit(1)
    elif total_xpath == 0:
        print("2 XPath files per group member are missing in xpaths folder.")
        exit(1)
