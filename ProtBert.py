import os
os.environ['CURL_CA_BUNDLE'] = ''
from transformers import BertForMaskedLM, BertTokenizer, pipeline
tokenizer = BertTokenizer.from_pretrained("D:\ProtBert", do_lower_case=False )
model = BertForMaskedLM.from_pretrained("D:\ProtBert")
unmasker = pipeline('fill-mask', model=model, tokenizer=tokenizer)
print(unmasker('D L I P T S S K L V V [MASK] D T S L Q V K K A F F A L V T'))