
from retriever import retrieve_documents


def test_paraphrased_refund_question():
    results = retrieve_documents(
        "When should I expect to get my money back?"
    )

    assert any(
        "5 to 7 business days" in doc["content"]
        for doc in results
    ), results


def test_express_shipping():
    results = retrieve_documents(
        "How quickly will an express order arrive?"
    )

    assert any(
        "1 to 2 business days" in doc["content"]
        for doc in results
    ), results


if __name__ == "__main__":
    test_paraphrased_refund_question()
    test_express_shipping()
    print("Semantic retrieval tests passed!")
