from annotate_nifi import parse_and_annotate_nifi as parse_and_annotate
import sys
import pysolr
import json

json_doc=json.load(sys.stdin)
server='https://librairy.linkeddata.es/solr'

try:
    solr_papers = pysolr.Solr(server+'/cord19-papers', always_commit=True, timeout=120)
    solr_paragraphs = pysolr.Solr(server+'/cord19-paragraphs', always_commit=True, timeout=120)
except Exception:
    sys.stderr.write("Error trying to access solr repository" + str(Exception))
    exit()

try:
    annotated_document = parse_and_annotate(json_doc)
    if ('paper' in annotated_document):
        solr_papers.add(annotated_document['paper'])
    if ('paragraphs' in annotated_document):
        solr_paragraphs.add(annotated_document['paragraphs'])
except Exception as e:
    sys.stderr.write("Error trying to annotate the documents" + Exception)
    exit()
    
solr_papers.get_session().close()
solr_paragraphs.get_session().close()

sys.stdout.write(json.dumps(annotated_document))
