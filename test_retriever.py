from retriever import retrieve_documents


def test_return_window():
    results = retrieve_documents("How long do I have to return an item?")
    assert any("30 days" in doc["content"] for doc in results)


def test_shipping():
    results = retrieve_documents("How long does express shipping take?")
    assert any("1 to 2 business days" in doc["content"] for doc in results)


def test_refund():
    results = retrieve_documents("How long do refunds take after approval?")
    assert any("5 to 7 business days" in doc["content"] for doc in results)


if __name__ == "__main__":
    test_return_window()
    test_shipping()
    test_refund()
    print("All retrieval tests passed!")
