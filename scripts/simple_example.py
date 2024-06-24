"""
TODO: Remove file after debugging
"""

from typing import cast

from datasets import Dataset, load_dataset
from dotenv import load_dotenv
from vidore_benchmark.evaluation.evaluate import evaluate_dataset
from vidore_benchmark.retrievers.jina_clip_retriever import JinaClipRetriever

load_dotenv(override=True)


def main():
    """
    Debugging script
    """
    my_retriever = JinaClipRetriever()

    dataset = cast(Dataset, load_dataset("vidore/shiftproject_test", split="test"))

    print("Dataset loaded")
    metrics = evaluate_dataset(my_retriever, dataset, batch_query=1, batch_doc=4)  # type: ignore

    print(metrics)


if __name__ == "__main__":
    main()
