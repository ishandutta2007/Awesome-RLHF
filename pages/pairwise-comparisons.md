# Pairwise Comparisons (Bradley-Terry Model)\n\nDetailed information and breakdown of Pairwise Comparisons (Bradley-Terry Model).\n\n## Bradley-Terry Model

```mermaid
graph LR;
    Prompt --> A[Response A]
    Prompt --> B[Response B]
    A --> Eval[Evaluator]
    B --> Eval
    Eval --> Choice[Chosen vs Rejected]
```\n\n[Back to README](../README.md)