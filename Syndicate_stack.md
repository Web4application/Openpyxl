# Syndicate Stack (/en/docs/syndicate-stack/get-started/syndicate-stack)



The Syndicate Stack is made up of software created by Syndicate to integrate with existing well-known rollup solutions in the EVM ecosystem and beyond. Our stack combines custom-built components with industry-standard technology to deliver full-stack control, economic sovereignty, and community ownership while solving the key challenges of building and operating decentralized applications.

<div className="diagram">
    <img alt="Architecture Diagram" src={__img0} />
</div>

A **Syndicate appchain** is the full stack deployment that combines all these components:

### Transaction Flow: Write Path

{/* TODO: Create a more accurate diagram, removing for now */}

{/* <div className="diagram">
  ![Transaction Flow](/transaction-flow.svg)

  </div> */}

**Step-by-step:**

1. **User**: Initiates a transaction (wallet/dApp)
2. **Syndicate Mempool (optional)**: Collects and batches transactions
3. **Syndicate Sequencer**: Submits batched transactions to Syndicate Chain
4. **Syndicate Chain**: Onchain sequencing, ordering, permissions
5. **Syndicate Translator**: Prepares blocks for execution
6. **Rollup Framework**: Executes transactions (e.g., Arbitrum Nitro)
7. **Syndicate Proposer**: Submits data to the settlement chain
8. **Settlement Chain**: Finality and security (Base, Arbitrum One, Ethereum Mainnet, etc.)

## Core Components

### 0. Syndicate Mempool

*(Optional) Maintained by Syndicate*

The Mempool collects transactions prior to submission to a sequencer. It handles automatic batching, making transaction submission more efficient. It's an optional component, which allows chains to preserve decentralization and transaction privacy. You can always skip the mempool and sequence your own transactions if you'd like.

### 1. Syndicate Sequencer

*Maintained by Syndicate*

The Sequencer handles transaction submission to sequencing contracts. It collects transactions from users and submits them to Syndicate Chain according to the rules defined in the sequencing contracts. This component ensures transactions are properly ordered and formatted before they're passed to the execution environment.

### 2. Syndicate Chain

*Maintained by Syndicate*

Syndicate Chain is a dedicated blockchain that enables onchain sequencing for the entire ecosystem of appchains. It hosts sequencing smart contracts that define the rules and permissions for transaction ordering, establishing the fundamental rules that govern transaction flow while enabling each appchain to maintain its economic sovereignty.

### 3. Syndicate Translator

*Maintained by Syndicate*

The Translator integrates Syndicate Chain and the settlement chain. It ingests blocks from Syndicate Chain, combines them with settlement chain data according to defined rules, and prepares them in a canonical form for execution. The Translator effectively converts high-level sequencing decisions into a format that can be processed by the execution environment.

### 4. Rollup Framework

*Created by Offchain Labs, with expanding compatibility*

The Rollup Framework, currently powered by Arbitrum Nitro, is where transactions are actually processed. It takes the sequenced blocks from the Translator and executes their transactions, maintaining the chain's state and validating all state transitions. With full EVM compatibility, it processes transactions efficiently while ensuring they follow all protocol rules.

Through our Translator's flexible architecture, we are expanding support to include Optimism's OP Stack and additional execution environments in the future, while maintaining the same high standards for security and performance.

### 5. Syndicate Proposer

*Maintained by Syndicate*
The Proposer submits data to the settlement chain that is necessary for bridging and withdrawals. It ensures that state changes from the execution environment are properly committed to the settlement chain, maintaining security and finality across the system. The Proposer is currently TEE-based, but other verification methods will be added over time.

### 6. Settlement Chain

*Integration with existing L2 solutions*

The Settlement Chain, typically an established L2 like Base, Arbitrum One, or Ethereum Mainnet, provides the security and finality backbone for the appchain. It serves as the ultimate source of truth, ensuring transaction finality and data availability. By building on proven L1/L2 infrastructure, appchains inherit strong security guarantees while maintaining their own execution environment and economic sovereignty.

## End-to-End Appchain Management

While the Syndicate Stack is technically sophisticated, we've made it simple to operate. Our managed infrastructure handles all the complexity of running an appchain, from deployment to ongoing operations:

* **Infrastructure**: The Syndicate appchain stack provides a production-ready infrastructure layer that automatically manages all components including the Sequencer, Translator, and Proposer. It handles updates, monitoring, and scaling without requiring deep blockchain operational expertise.

* **Management Console**: Through our management console, you maintain full control over your appchain's economics and governance while we handle the technical operations. You can monitor performance, adjust sequencing rules, and manage network parameters through a simple interface.

This means you can focus on building your application and growing your ecosystem, while we ensure your appchain runs reliably and efficiently. Whether you're launching a gaming network, consumer application, or AI platform, you get the benefits of a custom blockchain without the operational overhead.

## Getting Started

The Syndicate Stack can be configured for different levels of customization and control:

1. **Standard Configuration** - Quick start with default settings. This is Arbitrum Nitro as the rollup framework + Base for settlement + ETH as a gas token + an allowlist sequencing module.
2. **Custom Configuration** - Tailor components to your specific needs. This is Arbitrum Nitro as the rollup frameework + any layer of your choosing for settlement + a custom gas token + an allowlist sequencing module
3. **Advanced Customization** - Implement specialized sequencing logic and economic mechanisms. This is Arbitrum Nitro as the rollup framework + any layer of your choosing for settlement + a custom gas token + custom sequencing modules

To begin building with the Syndicate Stack:

1. [Understand different sequencing approaches](/docs/syndicate-stack/get-started/sequencing-architectures) and how they impact key appchain benefits
2. [Explore Sequencing Modules](/docs/syndicate-stack/core-concepts/sequencing-modules) for transaction ordering
