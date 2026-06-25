# PPO (Proximal Policy Optimization)\n\nDetailed information and breakdown of PPO (Proximal Policy Optimization).\n\n## PPO Algorithm

```mermaid
graph TD;
    Policy --> Action
    Action --> Reward[Reward Model Score]
    Reward --> KL[KL Penalty vs Ref Model]
    KL --> Update[Policy Update]
```\n\n[Back to README](../README.md)