import torch
from ts.torch_handler.base_handler import BaseHandler
from ts.utils.util import map_class_to_label

bs = 8
class EVMXHandler(BaseHandler):
    def preprocess(self, requests):
        data = requests[0]['body']['data']
        data = [int(str(self.word2idx[str(t)])) if t in self.word2idx.keys() else 0 for t in data]
        data = torch.tensor(data)
        t = torch.zeros(bs-1, len(data), dtype=int)
        return torch.cat((data.unsqueeze(dim=0), t))

    def inference(self, data):
        with torch.inference_mode():
            results, _, _ = self.model(data)
        return results[0]

    def postprocess(self, data):
        data = data.argmax(dim=-1)
        data = data.tolist()
        out = [self.mapping[str(t)] for t in data]
        return [out]
