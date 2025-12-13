import torch
import torch.nn as nn
from transformers import AutoModel


class SharedMTLModel(nn.Module):
    def __init__(
        self,
        model_name,
        num_types,
        num_manifestations,
        pos_weight_2=None,
        pos_weight_3=None,
    ):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        hidden_size = self.encoder.config.hidden_size
        self.num_types = num_types
        self.num_manifestations = num_manifestations

        self.dropout = nn.Dropout(0.2)

        self.head1 = nn.Linear(hidden_size, 1)
        self.head2 = nn.Linear(hidden_size, num_types)
        self.head3 = nn.Linear(hidden_size, num_manifestations)

        self.register_buffer(
            "pos_weight_2",
            pos_weight_2 if pos_weight_2 is not None else torch.tensor([]),
        )
        self.register_buffer(
            "pos_weight_3",
            pos_weight_3 if pos_weight_3 is not None else torch.tensor([]),
        )

    def forward(self, input_ids, attention_mask=None, labels=None):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        H = self.dropout(outputs.last_hidden_state[:, 0, :])

        logits1 = self.head1(H)
        logits2 = self.head2(H)
        logits3 = self.head3(H)
        logits = torch.cat([logits1, logits2, logits3], dim=-1)

        loss = None
        if labels is not None:
            labels = labels.float()
            y1_true = labels[:, :1]
            y2_true = labels[:, 1 : 1 + self.num_types]
            y3_true = labels[:, 1 + self.num_types :]

            device = logits1.device

            loss1 = nn.BCEWithLogitsLoss()(logits1, y1_true)

            if self.pos_weight_2.numel() > 0:
                loss2 = nn.BCEWithLogitsLoss(pos_weight=self.pos_weight_2.to(device))(
                    logits2, y2_true
                )
            else:
                loss2 = nn.BCEWithLogitsLoss()(logits2, y2_true)

            if self.pos_weight_3.numel() > 0:
                loss3 = nn.BCEWithLogitsLoss(pos_weight=self.pos_weight_3.to(device))(
                    logits3, y3_true
                )
            else:
                loss3 = nn.BCEWithLogitsLoss()(logits3, y3_true)

            loss = (loss1 + loss2 + loss3) / 3.0

        return {"loss": loss, "logits": logits}
