"""Datasets and semantic attributes used in the experiments.

Each task defines one semantic attribute A(t) of a text tuple t (a class label or a 1-5 rating).
Queries (COUNT with a predicate on A, AVG of A, GROUP BY A) are evaluated on top of A.
"""
import os
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
N_DEFAULT = 2000
SEED = 20261103

TASKS = {
    "imdb": dict(file="imdb_test", labels=["negative", "positive"],
                 question="What is the sentiment of this movie review?"),
    "yelp": dict(file="yelp_test", labels=["1", "2", "3", "4", "5"], numeric=True,
                 question="How many stars (1-5) did the author of this Yelp review most likely give?"),
    "agnews": dict(file="agnews_test", labels=["world", "sports", "business", "science/technology"],
                   question="What is the topic of this news article?"),
    "emotion": dict(file="emotion_test", labels=["sadness", "joy", "love", "anger", "fear", "surprise"],
                    question="Which emotion does the author of this message express?"),
    "hate": dict(file="tweet_hate_test", labels=["not hateful", "hateful"],
                 question="Is this tweet hate speech against immigrants or women?"),
    "offensive": dict(file="tweet_offensive_test", labels=["not offensive", "offensive"],
                      question="Is this tweet offensive (insults, threats, profanity, or targeted abuse)?"),
    "amazon": dict(file="amazon_test", labels=["1", "2", "3", "4", "5"], numeric=True,
                   question="How many stars (1-5) did the author of this Amazon product review most likely give?"),
    # Enterprise case study: de-identified customer-service memos of returns (see enterprise/deidentify.py).
    "rma": dict(file=None, labels=["quality issue", "shipment issue", "customer", "others"],
                question="Based on this customer-service note about a return or refund, what is the main reason "
                         "category? quality issue = product defect, damage, missing or wrong parts, malfunction, noise; "
                         "shipment issue = delivery delay, lost or undelivered package, return to sender, wrong item "
                         "picked, stock issue; customer = changed mind, not as expected, ordered by mistake, cancel, "
                         "fraud; others = fees, VAT, customs, price difference or discount, compensation, test order."),
}
RMA_DEID = os.path.join(ROOT, ".private_rma", "rma_sample4000_deid.parquet")
RMA_L1 = {"Quality issue": 0, "Shipment issue": 1, "Customer": 2, "Others": 3}


def load_rma():
    """Only the de-identified text is ever read here. gold = the human-entered problem code mapped to level 1
    (-1 when missing or unknown); in the case study the oracle is an LLM, so gold is used only as a free labeler."""
    df = pd.read_parquet(RMA_DEID)
    pt = pd.read_csv(os.path.join(ROOT, "07_enterprise_opportunity", "repos", "acquisition", "starrocks", "data",
                                  "dim_pub_problem_type.tsv.gz"), sep="\t", dtype=str)
    lv1 = dict(zip(pt.problem_type_id, pt.problem_lv1_name))
    code = df.problem_type_id.map(lv1).map(RMA_L1).fillna(-1).astype(int)
    return pd.DataFrame({"tid": np.arange(len(df)), "text": df.memo_deid.astype(str).str.slice(0, 2500), "gold": code})


def load(name, n=N_DEFAULT):
    """Return a DataFrame with columns tid, text, gold (index into labels). Uniform sample without replacement."""
    if name == "rma":
        return load_rma()
    spec = TASKS[name]
    df = pd.read_parquet(os.path.join(RAW, spec["file"] + ".parquet"))[["text", "label"]]
    rng = np.random.default_rng(SEED)
    idx = rng.permutation(len(df))[: min(n, len(df))]
    df = df.iloc[np.sort(idx)].reset_index(drop=True)
    df["text"] = df["text"].astype(str).str.replace("<br />", " ", regex=False).str.slice(0, 2500)
    return pd.DataFrame({"tid": np.arange(len(df)), "text": df["text"], "gold": df["label"].astype(int)})
