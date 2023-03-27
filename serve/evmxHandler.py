import torch
from ts.torch_handler.base_handler import BaseHandler
from ts.utils.util import map_class_to_label

class EVMXHandler(BaseHandler):
    def preprocess(self, requests):
        data = requests[0]['body']['data']
        data = [int(str(self.word2idx[str(t)])) if t in self.word2idx.keys() else 0 for t in data]
        t = torch.zeros(8, len(data), dtype=int)
        t[0] = torch.tensor(data, dtype=int)
        return t

    def inference(self, data):
        with torch.inference_mode():
            results, _, _ = self.model(data)
        return results

    def postprocess(self, data):
        data = torch.argmax(data[0], dim=1)
        data = data.tolist()
        out = [self.mapping[str(t)] for t in data]
        return [out]
