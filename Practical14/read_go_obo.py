#import necessary libraries
import xml.dom.minidom
import xml.sax
import datetime
import xml.sax.handler

#First we use DOM to read xml file
start_time = datetime.datetime.now()            #Find the start time
DOMTree = xml.dom.minidom.parse('go_obo.xml')   #Parse the DOM tree
terms = DOMTree.getElementsByTagName('term')

#Initialize a mmax dictionary to store the results (Note: value of 'feature' is a **list** to store multiple answers)
mmax = {'molecular_function': {'count': 0, 'feature': []},
        'biological_process': {'count': 0, 'feature': []},
        'cellular_component': {'count': 0, 'feature': []}
}
for term in terms:
    id = term.getElementsByTagName('id')[0].firstChild.nodeValue                #Get related features
    name = term.getElementsByTagName('name')[0].firstChild.nodeValue
    namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    cnt = len(term.getElementsByTagName('is_a'))        #Count the number of <is_a>

    now_mmax = mmax[namespace]              #Extract information of now mmax dictionary
    mmax_feature = now_mmax['feature']
    mmax_cnt = now_mmax['count']
    if cnt > mmax_cnt:                      #Compare now count of <is_a> with now mmax count
        mmax_feature = [{'id': id, 'name': name}]
        mmax[namespace] = {'count': cnt, 'feature': mmax_feature}
    elif cnt == mmax_cnt:                   #If they are equal, append to the list
        mmax[namespace]['feature'].append({'id': id, 'name': name})
    
#Print the results
print('**DOM Parsing:**')
for namespace, info in mmax.items():
    print(f"Namespace: {namespace}")
    mmax_cnt = info['count']
    features = info['feature']
    print(f"<is_a> maximum count: {mmax_cnt}")
    for feature in features:
        print(f"\tTerm id: {feature['id']}, term name: {feature['name']}")
    print()
end_time = datetime.datetime.now()
duration = (end_time - start_time).total_seconds()
print(f"Time for DOM: {duration} seconds\n")


#Then we use the SAX method
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ''          #Basic information of terms
        self.id = ''
        self.name = ''
        self.namespace = ''
        self.cnt = 0                    #Count of <is_a> tag
        self.mmax = {'molecular_function': {'count': 0, 'feature': []},
                'biological_process': {'count': 0, 'feature': []},
                'cellular_component': {'count': 0, 'feature': []}
        }
    
    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == 'term':
            self.current_data = ''      #If a new <term> was met, reset all parameters
            self.id = ''
            self.name = ''
            self.namespace = ''
            self.cnt = 0
    
    def endElement(self, tag):
        if tag == 'term':
            #Remove possible strips before comparing
            self.id = self.id.strip()
            self.name = self.name.strip()
            self.namespace = self.namespace.strip()
            now_mmax = self.mmax[self.namespace]              #Extract information of now mmax dictionary
            mmax_feature = now_mmax['feature']
            mmax_cnt = now_mmax['count']
            if self.cnt > mmax_cnt:                      #Compare now count of <is_a> with now mmax count
                mmax_feature = [{'id': self.id, 'name': self.name}]
                self.mmax[self.namespace] = {'count': self.cnt, 'feature': mmax_feature}
            elif self.cnt == mmax_cnt:                   #If they are equal, append to the list
                self.mmax[self.namespace]['feature'].append({'id': self.id, 'name': self.name})
        elif tag == 'is_a':                     #If <is_a> tag is met, add 1 to cnt
            self.cnt += 1
    
    def characters(self, content):
        if self.current_data == 'id':
            self.id += content
        elif self.current_data == 'name':
            self.name += content
        elif self.current_data == 'namespace':
            self.namespace += content

start_time = datetime.datetime.now()
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler = GOHandler()
parser.setContentHandler(handler=handler)
parser.parse('go_obo.xml')
#Print the results
print('**SAX Parsing:**')
for namespace, info in handler.mmax.items():
    print(f"Namespace: {namespace}")
    mmax_cnt = info['count']
    features = info['feature']
    print(f"<is_a> maximum count: {mmax_cnt}")
    for feature in features:
        print(f"\tTerm id: {feature['id']}, term name: {feature['name']}")
    print()
end_time = datetime.datetime.now()
duration = (end_time - start_time).total_seconds()
print(f"Time for SAX: {duration} seconds")

#SAX is faster than DOM