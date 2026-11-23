
from src.rag_pipeline import answer_question

test_questions = [
    {
        "question": "What are the payment terms in the agreement?",
        "expected_keyword": "payment"
    },
    {
        "question": "What are the termination conditions?",
        "expected_keyword": "termination"
    },
    {
        "question": "What confidentiality obligations are mentioned?",
        "expected_keyword": "confidential"
    },
    {
        "question": "What is the effective date of the agreement?",
        "expected_keyword": "October"
    }
]


def evaluate_rag():
    passed = 0

    for index, test in enumerate(test_questions, start=1):
        print(f"\nTest {index}: {test['question']}")

        result = answer_question(test["question"])
        answer = result["answer"]

        print("Answer:", answer)
        print("Sources:", result["sources"])

        if test["expected_keyword"].lower() in answer.lower():
            passed += 1
            print("Result: PASS")
        else:
            print("Result: REVIEW")

    print("\nEvaluation summary")
    print(f"Passed: {passed}/{len(test_questions)}")
    print(f"Keyword match rate: {passed / len(test_questions) * 100:.2f}%")


if __name__ == "__main__":
    evaluate_rag()
