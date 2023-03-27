import base_model

batch_size = 8
embeddings_size = 128

class LMModel_large_bs8_sl32_emb128(base_model.LMModel):
    def __init__(self):
        super(LMModel_large_bs8_sl32_emb128, self).__init__(18260, embeddings_size, 2, batch_size)
