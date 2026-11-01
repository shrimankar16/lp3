# BT Practical 1 — Install MetaMask and Study Spending Ether per Transaction

---

## Aim
Install the MetaMask browser extension, create a wallet, and study how Ether (ETH) is spent per transaction including gas fees.

---

## Theory

### What is MetaMask?
MetaMask is a cryptocurrency wallet and gateway to blockchain applications. It is available as a browser extension (Chrome, Firefox, Brave, Edge) and as a mobile app. It allows users to:
- Store, send, and receive Ethereum (ETH) and ERC-20 tokens
- Interact with decentralized applications (dApps) directly from the browser
- Connect to multiple Ethereum networks (Mainnet, Testnets, custom RPC)

### What is Ether (ETH)?
Ether is the native cryptocurrency of the Ethereum blockchain. It is used to:
- Pay for transaction fees (gas fees)
- Transfer value between accounts
- Interact with smart contracts

### What is Gas?
Every operation on the Ethereum network requires computational work. **Gas** is the unit that measures this computational effort.

| Term | Definition |
|------|-----------|
| Gas Limit | Maximum units of gas you are willing to use for a transaction |
| Gas Price | Amount of ETH you pay per unit of gas (in Gwei; 1 Gwei = 10⁻⁹ ETH) |
| Transaction Fee | Gas Used × Gas Price |
| Base Fee | Minimum gas price set by the network (burned after EIP-1559) |
| Priority Fee (Tip) | Extra fee paid to miners/validators to prioritize your transaction |

### Transaction Fee Formula
```
Transaction Fee (ETH) = Gas Used × (Base Fee + Priority Fee)
```

**Example:**
- Gas Used = 21,000 (standard ETH transfer)
- Base Fee = 20 Gwei
- Priority Fee = 2 Gwei
- Total = 21,000 × 22 Gwei = 462,000 Gwei = 0.000462 ETH

---

## Steps to Install MetaMask

### Step 1 — Install the Extension
1. Open Google Chrome (or Brave/Firefox/Edge)
2. Go to: https://metamask.io/download/
3. Click **"Install MetaMask for Chrome"**
4. Click **"Add to Chrome"** → **"Add Extension"**
5. The MetaMask fox icon will appear in the browser toolbar

### Step 2 — Create a New Wallet
1. Click the MetaMask icon in the toolbar
2. Click **"Get Started"**
3. Click **"Create a New Wallet"**
4. Agree to the terms of use
5. Create a strong password (used to unlock the wallet locally)
6. Click **"Create"**

### Step 3 — Save the Secret Recovery Phrase
1. MetaMask will show you a **12-word Secret Recovery Phrase**
2. Write it down on paper and store it safely — this is the master key to your wallet
3. **Never share this phrase with anyone**
4. Confirm the phrase by selecting the words in the correct order
5. Click **"Confirm"** — wallet is now created

### Step 4 — Explore the Wallet Interface
After setup, you will see:
- Your **Account Address** (e.g., `0xAbCd...1234`) — a 42-character hexadecimal address
- Your **ETH Balance** (initially 0)
- The network selector (default: **Ethereum Mainnet**)
- Buttons: Buy, Send, Receive, Swap

---

## Steps to Connect to a Test Network (to practice without real ETH)

### Step 5 — Enable Test Networks
1. Click the network dropdown (top center, shows "Ethereum Mainnet")
2. Click **"Show/hide test networks"** → toggle ON
3. Select **"Sepolia Test Network"** (recommended testnet)

### Step 6 — Get Free Test ETH (Faucet)
1. Copy your wallet address by clicking on "Account 1"
2. Go to: https://sepoliafaucet.com/ or https://faucets.chain.link/sepolia
3. Paste your wallet address and request test ETH
4. Wait ~30 seconds — test ETH will appear in your MetaMask wallet

---

## Performing a Transaction and Studying Gas Fees

### Step 7 — Send ETH to Another Address
1. In MetaMask, click **"Send"**
2. Enter a recipient address (you can create a second account in MetaMask via the account icon → "Create Account")
3. Enter the amount (e.g., 0.001 ETH)
4. Click **"Next"**

### Step 8 — Study the Gas Fee Breakdown
On the confirmation screen, MetaMask shows:

```
Amount:       0.001 ETH
Gas Fee:      0.000042 ETH   ← this is what you pay the network
Total:        0.001042 ETH
```

Click **"Edit"** next to Gas Fee to see:
- **Low** — cheaper but slower confirmation
- **Market** — current average gas price (recommended)
- **Aggressive** — fastest confirmation, highest cost

You can also set custom values:
- **Max Base Fee** — max you'll pay as base fee
- **Priority Fee (Tip)** — tip to validators for faster processing

### Step 9 — Confirm and Track the Transaction
1. Click **"Confirm"** to send the transaction
2. MetaMask shows the transaction as **Pending**
3. Click on the transaction → **"View on Block Explorer"**
4. This opens **Etherscan** (https://sepolia.etherscan.io/) showing:
   - Transaction Hash
   - Block number it was included in
   - Gas Limit and Gas Used
   - Gas Price (Gwei)
   - Transaction Fee in ETH

---

## Observations — Ether Spent per Transaction

| Transaction Type | Gas Used | Approx Fee (at 20 Gwei) |
|------------------|----------|--------------------------|
| Simple ETH Transfer | 21,000 | 0.00042 ETH |
| ERC-20 Token Transfer | ~65,000 | 0.0013 ETH |
| Smart Contract Deployment | ~500,000–2,000,000 | 0.01–0.04 ETH |
| Uniswap Token Swap | ~150,000 | 0.003 ETH |

**Key Observations:**
- Gas fees are **not fixed** — they fluctuate based on network demand
- During peak hours, base fees can spike 10x–50x
- The ETH burned (base fee) is removed from circulation — reduces supply
- Only the priority fee (tip) goes to validators
- A failed transaction still consumes gas (you pay for the computation even if it reverts)

---

## Conclusion

MetaMask provides a user-friendly interface to interact with the Ethereum blockchain. Every transaction on Ethereum costs gas, calculated as `Gas Used × (Base Fee + Priority Fee)`. A standard ETH transfer uses exactly 21,000 gas units. More complex operations like smart contract interactions use significantly more gas. Test networks like Sepolia allow practice transactions without spending real ETH, making them ideal for development and learning.

---

## Key Terms Summary

| Term | Meaning |
|------|---------|
| Wallet | Software that stores private keys and manages accounts |
| Address | Public identifier of your account (0x...) |
| Private Key | Secret key that proves ownership — never share |
| Seed Phrase | 12-word backup to recover wallet |
| Gas | Unit of computational work |
| Gwei | Unit of ETH price (1 ETH = 10⁹ Gwei) |
| Nonce | Transaction count for an account (prevents replay attacks) |
| Testnet | Practice blockchain with fake ETH |
| Etherscan | Block explorer to view Ethereum transactions |
