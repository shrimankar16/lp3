# Survey Report on Types of Blockchains and Their Real-Time Use Cases

**Subject:** Blockchain Technology  
**Practical No.:** 4  

---

## Abstract

Blockchain is a distributed ledger technology that records transactions in an immutable, transparent, and decentralized manner. Since the introduction of Bitcoin in 2008, blockchain has evolved far beyond cryptocurrency into a foundational infrastructure for industries including finance, healthcare, supply chain, and governance. This report surveys the major types of blockchain networks — Public, Private, Consortium, and Hybrid — analyzing their architectural differences, consensus mechanisms, and real-world deployment across industries.

---

## 1. Introduction

A blockchain is a chain of blocks where each block contains:
- A set of transactions
- A cryptographic hash of the previous block
- A timestamp
- A nonce (proof of work) or validator signature

This linked structure makes tampering with any block computationally infeasible — altering one block would require recalculating all subsequent blocks across the majority of nodes.

### Core Properties of Blockchain

| Property | Description |
|----------|-------------|
| Decentralization | No single authority controls the network |
| Immutability | Recorded data cannot be altered or deleted |
| Transparency | All participants can verify transactions |
| Security | Cryptographic hashing prevents tampering |
| Consensus | Nodes agree on the state without trusting each other |

---

## 2. Types of Blockchains

Blockchain networks are broadly classified into four types based on access control and governance.

---

### 2.1 Public Blockchain

#### Definition
A fully open, permissionless blockchain where anyone can join, read data, submit transactions, and participate in consensus without requiring approval.

#### Key Characteristics
- Completely decentralized — no single owner
- All transactions are publicly visible
- Consensus achieved through Proof of Work (PoW) or Proof of Stake (PoS)
- Highly secure due to large number of nodes
- Slower and less energy-efficient than private blockchains
- Incentivizes participation through cryptocurrency rewards

#### Consensus Mechanisms Used
| Mechanism | How it works | Example |
|-----------|-------------|---------|
| Proof of Work (PoW) | Nodes compete to solve a cryptographic puzzle | Bitcoin |
| Proof of Stake (PoS) | Validators are chosen based on staked coins | Ethereum 2.0 |
| Delegated PoS (DPoS) | Token holders vote for delegates | EOS, TRON |

#### Real-Time Use Cases

| Use Case | Blockchain | Details |
|----------|-----------|---------|
| Cryptocurrency | Bitcoin (BTC) | Peer-to-peer digital currency; 400M+ users worldwide |
| Smart Contracts & DeFi | Ethereum (ETH) | $50B+ locked in DeFi protocols (Uniswap, Aave, Compound) |
| NFT Marketplaces | Ethereum, Solana | Digital ownership of art, music, gaming assets (OpenSea) |
| Decentralized Identity | Sovrin | Self-sovereign identity without central authority |
| Voting Systems | Voatz, Agora | Tamper-proof digital voting in elections |

#### Examples
- **Bitcoin:** First and largest public blockchain; processes ~7 transactions/second
- **Ethereum:** Programmable blockchain; hosts 3,000+ dApps
- **Solana:** High-speed public chain; processes 65,000 transactions/second

---

### 2.2 Private Blockchain

#### Definition
A permissioned blockchain where access is restricted to invited participants. A single organization controls who can join, read, and write to the network.

#### Key Characteristics
- Centralized control by one organization
- Faster transactions (fewer nodes to achieve consensus)
- Higher privacy — data visible only to authorized participants
- Lower energy consumption
- Used primarily for internal business processes
- Trust is placed in the controlling organization

#### Consensus Mechanisms Used
| Mechanism | Description |
|-----------|-------------|
| Practical Byzantine Fault Tolerance (PBFT) | Fast consensus; tolerates faulty nodes |
| Raft | Leader-based consensus for enterprise networks |
| Round Robin | Nodes take turns proposing blocks |

#### Real-Time Use Cases

| Use Case | Organization | Details |
|----------|-------------|---------|
| Internal Audit Trail | Enterprise IT | Immutable record of employee actions and data changes |
| Digital Asset Management | Banks | Tracking internal movement of financial instruments |
| HR Records | Accenture | Tamper-proof employee credential verification |
| Supply Chain (Internal) | Walmart (internal) | Tracking products within their own logistics network |
| Healthcare Records | Hospitals | Secure patient data management within a hospital system |

#### Examples
- **Hyperledger Fabric (IBM):** Most popular enterprise private blockchain; used by Walmart, Maersk, Nestlé
- **Corda (R3):** Designed specifically for financial institutions
- **Multichain:** Open-source private blockchain platform

---

### 2.3 Consortium Blockchain (Federated Blockchain)

#### Definition
A semi-decentralized blockchain governed by a group of organizations rather than a single entity or the general public. Multiple organizations share control and responsibility.

#### Key Characteristics
- Multiple organizations jointly manage the network
- More decentralized than private, more controlled than public
- Participants are pre-approved by the consortium
- Faster and more efficient than public blockchains
- Data can be selectively shared between members
- Governance handled by a committee

#### Consensus Mechanisms Used
| Mechanism | Description |
|-----------|-------------|
| PBFT | Used by Hyperledger Fabric |
| PoA (Proof of Authority) | Approved validators sign blocks — used in energy/finance consortia |
| Istanbul BFT | Used by Quorum (JPMorgan) |

#### Real-Time Use Cases

| Use Case | Consortium | Details |
|----------|-----------|---------|
| Banking & Payments | R3 Corda | 300+ banks including HSBC, Barclays, BNY Mellon |
| Trade Finance | Marco Polo Network | Cross-border trade finance among multiple banks |
| Healthcare Data Sharing | MedRec | Multiple hospitals sharing patient records securely |
| Food Safety | IBM Food Trust | Walmart, Nestlé, Carrefour tracking food supply chains |
| Energy Trading | Energy Web Chain | Utilities and renewable energy companies trading credits |
| Insurance | B3i | Reinsurance blockchain connecting global insurers |

#### Examples
- **Quorum (JPMorgan):** Enterprise Ethereum fork used by major banks; now part of ConsenSys
- **Hyperledger Fabric:** Modular consortium blockchain by the Linux Foundation
- **Energy Web Chain:** Sector-specific consortium for clean energy applications

---

### 2.4 Hybrid Blockchain

#### Definition
A combination of public and private blockchains — some data and processes are kept private while others are made publicly verifiable. Organizations choose what to expose publicly.

#### Key Characteristics
- Flexible — customizable privacy per use case
- Private transactions with public verification option
- Users can move between public and private environments
- Combines benefits of both types
- Most complex to implement and govern

#### Real-Time Use Cases

| Use Case | Platform | Details |
|----------|---------|---------|
| Government & Public Records | Dragonchain | Public verification with private data storage |
| Real Estate | Propy | Property records publicly verifiable, transaction details private |
| Retail Loyalty Programs | XinFin | Customer data private, reward points publicly auditable |
| Cross-Border Payments | Ripple (XRP) | Bank transactions private, settlement publicly recorded |
| Supply Chain | IBM + Maersk (TradeLens) | Shipping events public, business contracts private |

#### Examples
- **Dragonchain:** Hybrid blockchain by Disney (later open-sourced)
- **XinFin (XDC Network):** Enterprise hybrid blockchain for trade and finance
- **Ripple (XRP Ledger):** Partial decentralization for global payment settlement

---

## 3. Comparison of Blockchain Types

| Feature | Public | Private | Consortium | Hybrid |
|---------|--------|---------|------------|--------|
| Access | Open to all | Single org | Group of orgs | Mixed |
| Decentralization | Full | None | Partial | Partial |
| Speed | Slow | Fast | Moderate | Moderate |
| Scalability | Low | High | Moderate | Moderate |
| Privacy | None | High | Medium | Configurable |
| Energy Usage | High (PoW) | Low | Low | Low-Medium |
| Trust Model | Trustless | Trusted org | Trusted group | Mixed |
| Cost | High gas fees | Low | Low | Low-Medium |
| Transparency | Full | Internal only | Among members | Selective |
| Examples | Bitcoin, Ethereum | Hyperledger Fabric | R3 Corda, Quorum | XinFin, Dragonchain |

---

## 4. Real-World Industry Applications

### 4.1 Finance and Banking
- **Cross-border payments:** Ripple processes $1.5B+ daily in institutional transfers
- **DeFi:** Ethereum-based protocols like Uniswap handle $1B+ in daily trading volume
- **Central Bank Digital Currencies (CBDCs):** China's Digital Yuan, India's e-Rupee (private/hybrid blockchain)
- **Trade finance:** Marco Polo and Contour reduce letter of credit processing from 10 days to 24 hours

### 4.2 Supply Chain Management
- **IBM Food Trust (Consortium):** Walmart reduced food contamination trace time from 7 days to 2.2 seconds
- **Maersk TradeLens (Consortium):** Digitized shipping documents for 800+ logistics companies
- **De Beers (Private):** Tracr platform tracks every diamond from mine to retailer

### 4.3 Healthcare
- **MedRec (Consortium):** MIT-developed patient record sharing across hospitals
- **Chronicled:** Pharmaceutical supply chain to prevent counterfeit drugs
- **Change Healthcare:** Processes 50% of US medical claims on blockchain

### 4.4 Government and Identity
- **Estonia (Public/Hybrid):** 99% of government services on blockchain; e-residency for 90,000+ citizens
- **Dubai Blockchain Strategy:** Goal to process all government documents on blockchain
- **Self-Sovereign Identity (SSI):** Sovrin network for portable digital identities

### 4.5 Real Estate
- **Propy:** First legally binding real estate transaction recorded on blockchain (Ukraine, 2017)
- **RealT:** Tokenized real estate allowing fractional property ownership from $50

### 4.6 Energy
- **Power Ledger (Public):** Peer-to-peer solar energy trading in Australia and India
- **Energy Web Chain (Consortium):** 100+ energy companies managing renewable energy certificates

---

## 5. Challenges and Limitations

| Challenge | Description |
|-----------|-------------|
| Scalability | Public blockchains like Bitcoin handle only 7 TPS vs Visa's 24,000 TPS |
| Energy Consumption | Bitcoin mining uses ~150 TWh/year — comparable to Argentina |
| Regulatory Uncertainty | Laws vary widely across countries |
| Interoperability | Different blockchains cannot easily communicate |
| Smart Contract Vulnerabilities | Code bugs can lead to irreversible losses (e.g., $60M DAO hack) |
| Data Privacy (GDPR) | Immutability conflicts with "right to be forgotten" |
| Adoption Barriers | Legacy systems integration is complex and expensive |

---

## 6. Future Trends

- **Layer 2 Solutions:** Lightning Network (Bitcoin), Polygon (Ethereum) improve scalability
- **Cross-Chain Bridges:** Polkadot, Cosmos enable communication between blockchains
- **Web3:** Decentralized internet built on public blockchain infrastructure
- **CBDCs:** 130+ countries exploring Central Bank Digital Currencies
- **Blockchain + AI:** AI for smart contract auditing and anomaly detection
- **Quantum-resistant cryptography:** Preparing blockchains for post-quantum threats

---

## 7. Conclusion

Blockchain technology is not a one-size-fits-all solution. The choice of blockchain type depends on the specific requirements of an application:

- **Public blockchains** are ideal for trustless, open environments like cryptocurrency and DeFi
- **Private blockchains** suit single-organization needs requiring high speed and data privacy
- **Consortium blockchains** are best for industries where multiple competing organizations must share data (banking, healthcare, supply chain)
- **Hybrid blockchains** offer the flexibility needed for government and enterprise applications that require both privacy and public accountability

As blockchain matures, the boundaries between these types are blurring — most production systems today use elements of multiple types to balance decentralization, performance, privacy, and trust.

---

## References

1. Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System
2. Buterin, V. (2014). Ethereum Whitepaper
3. Hyperledger Foundation — https://www.hyperledger.org
4. IBM Food Trust — https://www.ibm.com/blockchain/solutions/food-trust
5. World Economic Forum (2020). Blockchain Beyond the Hype
6. Ethereum Foundation — https://ethereum.org
7. R3 Corda — https://www.r3.com
8. Energy Web Foundation — https://www.energyweb.org
