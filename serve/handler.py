import os
import evmxHandler

_service = evmxHandler.EVMXHandler()

def handle(data, context):
    if not _service.initialized:
        _service.initialize(context)
        _service.word2idx = {v: k for k, v in _service.mapping.items()}

    if data is None:
        return None

    data = _service.preprocess(data)
    data = _service.inference(data)
    data = _service.postprocess(data)

    return data
