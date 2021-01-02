import re
import ijson
import kss
import argparse
from namuwiki.extractor import extract_text


capture_values = [
  ("item.namespace", "string"),
  ("item.title", "string"),
  ("item.text", "string")
]
cleaning_first_patterns = [r"~~[^~]+~~"]
cleaning_first_patterns = [re.compile(pattern, re.IGNORECASE | re.MULTILINE) for pattern in cleaning_first_patterns]
cleaning_patterns = [r"\([^\)]+\)", r"/^#[0-9a-f]{3,6}$/i"]
cleaning_patterns = [re.compile(pattern, re.IGNORECASE | re.MULTILINE) for pattern in cleaning_patterns]
replace_patterns = {'\\n': "\n", "\\'": "'"}

"""
문장 분리
"""
def kss_sentence_seperator(file, text):
    for sent in kss.split_sentences(text):
        file.write(sent.replace('\n', '')+"\n")

def parse_namuwiki_json(path, limit=-1, debug=False):
  i = 0
  doc = {}
  with open(path) as f:
    for prefix, event, value in ijson.parse(f):

      if debug:
        print(prefix, event, value)
      if (prefix, event) in capture_values:
        doc[prefix[5:]] = value
      if (prefix, event, value) == ("item", "end_map", None):
        yield doc
        doc = {}
        i += 1

        if limit > 0 and i >= limit:
          break

def clean_text(text):
  for regex in cleaning_first_patterns:
    text = re.sub(regex, "", text)

  text = extract_text(text)

  for regex in cleaning_patterns:
    text = re.sub(regex, "", text)
  for k, v in replace_patterns:
    text = text.replace(k, v)
  return text

def get_argparser():
  """Build the argument parser for main."""
  parser = argparse.ArgumentParser(description='WikiExtractor')
  parser.add_argument('--dump_path', type=str, required=False,
                      default="/Volumes/My Passport for Mac/00_nlp/나무위키/docData200302.json")
  parser.add_argument('--output_file', type=str, required=False,
                      default= "./namuwiki.txt")
  return parser

if __name__=="__main__":
  """
  python3 NamuwikiExtractor.py --dump_path "/Volumes/My Passport for Mac/00_nlp/나무위키/docData200302.json" --output_file "./namuwiki.txt"
  """
  parser = get_argparser()
  args = parser.parse_args()

  file = open(args.output_file, 'w', encoding='utf-8')
  flag = True
  for doc in parse_namuwiki_json(args.dump_path):
    doc['title'] = clean_text(doc['title'])
    doc['text'] = clean_text(doc['text'])
    plain = doc['text'].replace('\n\n','\n')
    if plain.isspace() or len(plain)<20:
      continue
    if flag:
      file.write(doc['title'] + "\n")
      flag = False
    else:
      file.write("\n"+doc['title']+"\n")
    kss_sentence_seperator(file,plain)
