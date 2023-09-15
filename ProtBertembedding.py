from transformers import BertModel, BertTokenizer
import re
def embedding_from_pretrained(sequence="A E T C Z A O"):
    tokenizer = BertTokenizer.from_pretrained("D:\ProtBert", do_lower_case=False)
    model = BertModel.from_pretrained("D:\ProtBert")
    sequence = sequence
    sequence_ = re.sub(r"[UZOB]", "X", sequence)
    encoded_input = tokenizer(sequence, return_tensors='pt')
    output = model(**encoded_input)
    output=output.pooler_output[0]
    print(output)
    print(len(output))  #len=1024
    return output

if __name__=='__main__':
    embedding_from_pretrained()
