# Quickstart (/en/docs/syndicate-stack/get-started/quickstart)







import { Accordion, Accordions } from "fumadocs-ui/components/accordion";

This guide walks you through the key configuration options for your new appchain. **Syndicate handles the deployment and infrastructure** - you just need to make the important decisions about how your chain should function.

## What You'll Configure

1. **[Set Chain Parameters](#1-set-chain-parameters)**: Define the basic settings for your appchain
2. **[Sequencing Modules](#2-sequencing-modules)**: How transactions are ordered and who can participate
3. **[Configure Fee Model](#3-configure-fee-model)**: How transaction fees work, including using custom tokens
4. **[Set Governance Parameters](#4-set-governance-parameters)**: How upgrades and critical actions are managed
5. **[Configure Execution Environment](#5-configure-execution-environment)**: Any specific execution needs
6. **[Choose Settlement Layer](#6-choose-settlement-layer)**: Which base layer (L1/L2) to use for settlement

Let's get started!

## 1. Set Chain Parameters

These foundational settings define your appchain's identity and how it connects to the broader ecosystem.

* **Chain Name**: Human-readable name for your chain (e.g., `my-appchain`).
* **Chain ID**: A unique numerical identifier for your chain. A Chain ID starting with `510` will be automatically assigned to your appchain.
* **Block Time:** The target time between blocks on your chain, in milliseconds. A good default is 1 second to ensure owners are not burdened with provisioning execution node (RPC) machines with unnecessarily high compute and storage requirements. *[Learn more](/docs/syndicate-stack/core-concepts/block-time)*

## 2. Sequencing Modules

Sequencing modules control who can submit transactions to your chain and in what order they're processed. This is one of the most powerful customization points for your appchain.

**Popular Configuration Options:**

| Module Type     | Options                  | Best For                         |
| --------------- | ------------------------ | -------------------------------- |
| **Permissions** | Allowlist                | Invite only chain                |
|                 | Token-gated              | Community-owned chain            |
|                 | Always open              | Public chain                     |
| **Ordering**    | First-come-first-served  | Simple, fair ordering            |
|                 | Fee priority             | Revenue optimization             |
|                 | Random                   | MEV protection                   |
| **Auction**     | Sealed-bid auction       | Competitive sequencing           |
| **Atomic**      | Cross-chain coordination | Complex multi-chain applications |

Our team will implement the selected modules based on your requirements. For more advanced customization, we can also build custom modules to your specifications.

*For more technical details on each module, see our [Sequencing Modules documentation](/docs/syndicate-stack/core-concepts/sequencing-modules).*

## 3. Configure Fee Model

Choose how transaction fees work on your chain. This includes which token is used for gas payments and how the economic model is structured.

**Fee Token Options:**

| Token Type       | Description                        | Best For                                 |
| ---------------- | ---------------------------------- | ---------------------------------------- |
| **ETH**          | Standard ETH for gas payments      | Simplicity and compatibility             |
| **Custom Token** | Your own ERC-20 as native currency | Community economics and custom use cases |

**Tip:**
Start simple (e.g., all fees to sequencers or treasury) and evolve your model as your community grows.

## 4. Set Governance Parameters

Define how upgrades and critical decisions will be managed on your appchain. Good governance ensures security while enabling future improvements.

**Governance Models:**

| Model            | Description                                  | Best For                      |
| ---------------- | -------------------------------------------- | ----------------------------- |
| **Single Admin** | One address controls all upgrades            | Early-stage or test chains    |
| **Multisig**     | Requires multiple signers to approve changes | Small teams or trusted groups |
| **DAO/Voting**   | Community voting for changes                 | Community-owned chains        |

**What you'll need to specify:**

* Governance model
* Admin address(es) or contract address
* Timelock period for changes (if any)

Note that you can change your governance model later as your project evolves, though this requires going through your initial governance process.

## 5. Configure Execution Environment

Your appchain runs on **Arbitrum Nitro** by default—an industry-leading Ethereum rollup. Support for other execution stacks (like OP Stack) is coming soon.

### What You Get with Arbitrum Nitro

* **Low Fees:** 10–100x cheaper than Ethereum mainnet, with further savings possible using data availability committees.
* **Ethereum Compatibility:** Use the same smart contracts, workflows, and tools (Solidity, Hardhat, Foundry, etc.) as on Ethereum.
* **Flexible Smart Contracts:** Deploy standard Solidity or high-performance WASM contracts using Stylus.
* **Interoperability:** Trustless bridging to Ethereum mainnet or EVM rollups and seamless integration with the broader Ethereum ecosystem.
* **Fully Managed Infrastructure:** We handle node operations, upgrades, and scaling so you can focus on your application logic.

**Note:** If you have specific requirements for precompiles, custom gas limits, or other advanced execution parameters, let us know during configuration. We will work with you to ensure your appchain meets your needs.

## 6. Choose Settlement Layer

The settlement layer is where your appchain ultimately anchors its state for security. This is an important decision that affects cost, security, and interoperability.

**Comparison of Settlement Options:**

<table>
  <thead>
    <tr>
      <th>
        Layer
      </th>

      <th>
        Security
      </th>

      <th>
        Cost
      </th>

      <th>
        Speed
      </th>

      <th>
        Best For
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <span
          style={{
          height: "30px",
          display: "flex",
          alignItems: "center",
          gap: "0.8em",
        }}
        >
          <div style={{ width: "20px" }}>
                        <img alt="Base Logo" src={__img0} placeholder="blur" />
          </div>

          <strong>
            Base
          </strong>
        </span>
      </td>

      <td>
        Posts data to Ethereum, but relies on centralized sequencer/validators
      </td>

      <td>
        Medium
      </td>

      <td>
        Fast
      </td>

      <td>
        Wide distribution
      </td>
    </tr>

    <tr>
      <td>
        <span
          style={{
          height: "30px",
          display: "flex",
          alignItems: "center",
          gap: "0.8em",
        }}
        >
          <div style={{ width: "20px" }}>
                        <img alt="Arbitrum Logo" src={__img1} placeholder="blur" />
          </div>

          <strong>
            Arbitrum
          </strong>
        </span>
      </td>

      <td>
        Trustless L2 security via fraud proofs, enforced by Ethereum.{" "}
        <strong>No sequencing fees if you settle to Arbitrum.</strong>
      </td>

      <td>
        Medium
      </td>

      <td>
        Fast
      </td>

      <td>
        DeFi and high-value apps
      </td>
    </tr>

    <tr>
      <td>
        <span
          style={{
          height: "30px",
          display: "flex",
          alignItems: "center",
          gap: "0.8em",
        }}
        >
          <div style={{ width: "20px" }}>
                        <img alt="Ethereum Logo" src={__img2} placeholder="blur" />
          </div>

          <strong>
            Ethereum
          </strong>
        </span>
      </td>

      <td>
        Native L1 security
      </td>

      <td>
        High
      </td>

      <td>
        Slower
      </td>

      <td>
        Highest security needs
      </td>
    </tr>
  </tbody>
</table>

You decide which settlement layer you want to use for your appchain. Our team will handle all the technical details of connecting your appchain to the chosen settlement layer.

## 7. Deploy

Once your appchain is deployed, you'll receive credentials and access to:

| Resource            | Description                                         |
| ------------------- | --------------------------------------------------- |
| **RPC Endpoint**    | `https://rpc.testnet.{chainName}.syndicate.io`      |
| **Explorer**        | `https://explorer.testnet.{chainName}.syndicate.io` |
| **Admin Console**   | For monitoring and management                       |
| **Support Channel** | For any questions or issues                         |

***Note:** We also offer custom subdomains for your RPC endpoint, such as `rpc.mydomain.com`.*

## 8. First Interactions

Once your appchain is live, you'll want to:

### Add your appchain to MetaMask:

1. Visit your chain's block explorer: `https://explorer.testnet.{chainName}.syndicate.io`
2. Click the **"Add to MetaMask"** button for one-click network setup.
3. For more details or alternative methods, see [Wallet Configuration](/docs/syndicate-stack/guides/wallet-configuration).

### Fund your chain owner wallet:

Send some native token (ETH or your custom token) to the chain owner wallet address.

This will let you interact with your new appchain right away.

## Next Steps

To dive deeper into customizing and optimizing your appchain, check out these resources:

* [Chain Setup](/docs/syndicate-stack/guides/chain-setup): Learn about all configurable parameters and advanced setup options for your chain.
* [Sequencing Modules](/docs/syndicate-stack/core-concepts/sequencing-modules): Explore the full range of sequencing logic and modules you can use to control transaction flow and permissions.
* [Framework Selection](/docs/syndicate-stack/core-concepts/execution-framework): Understand the different execution and settlement frameworks available and how to choose the best stack for your needs.

These guides will help you make the most of your Syndicate appchain and prepare for advanced deployments.
