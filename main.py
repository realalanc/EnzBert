import loader
import model
import ProtBertembedding

if __name__=='__name__':
    data = loader.dataloader()
    embedded_seq = ProtBertembedding.embedding_from_pretrained(data)
    model = model.BertClassifier()
    model.eval()
    output = model(data)

