# BT Practical 2 — Create Your Own Wallet Using MetaMask for Crypto Transactions

---

## Aim
Create a personal cryptocurrency wallet using MetaMask, understand its components, and demonstrate its use for crypto transactions on the Ethereum network.

---

## Theory

### What is a Crypto Wallet?
A cryptocurrency wallet does not actually store coins — it stores the **private key** that proves ownership of funds on the blockchain. There are two types:

| Type | Description | Example |
|------|-------------|---------|
| Custodial | A third party (exchange) holds your keys | Binance, Coinbase |
| Non-Custodial | You hold your own keys | MetaMask, Trust Wallet |

MetaMask is a **non-custodial, software wallet** — you have full control.

### Key Components of a Wallet

| Component | Description |
|-----------|-------------|
| Private Key | 256-bit secret number; proves ownership; signs transactions |
| Public Key | Derived from private key using elliptic curve cryptography |
| Wallet Address | Last 20 bytes of the public key hash (40 hex chars prefixed with 0x) |
| Secret Recovery Phrase | 12 or 24 random words (BIP-39 standard); can regenerate the private key |

### How Address is Derived
```
Private Key  →  (Elliptic Curve Multiplication)  →  Public Key
Public Key   →  (Keccak-256 Hash)               →  Take last 20 bytes
Last 20 bytes →  Prefix with 0x                  →  Wallet Address
```

### Types of Accounts in MetaMask
- **Externally Owned Account (EOA):** Controlled by a private key (your normal wallet account)
- **Contract Account:** Controlled by smart contract code (no private key)

---

## Steps to Create a Wallet

### Step 1 — Install MetaMask
1. Open **Google Chrome** browser
2. Navigate to: **https://metamask.io/download/**
3. Click **"Install MetaMask for Chrome"**
4. A Chrome Web Store page opens → Click **"Add to Chrome"**
5. Click **"Add Extension"** in the popup
6. MetaMask fox icon appears in the extensions bar (pin it for easy access)

### Step 2 — Launch and Initial Setup
1. Click the MetaMask fox icon
2. Welcome screen appears → Click **"Get Started"**
3. Two options appear:
   - **"Import Wallet"** → if you have an existing seed phrase
   - **"Create a Wallet"** → for a brand new wallet
4. Click **"Create a Wallet"**
5. Click **"I Agree"** on the data collection consent screen

### Step 3 — Set a Password
1. Enter a **strong password** (minimum 8 characters)
   - This password only unlocks MetaMask on this device
   - It does NOT recover your wallet if lost — the seed phrase does
2. Confirm the password
3. Accept the Terms of Use
4. Click **"Create"**

### Step 4 — Secure the Secret Recovery Phrase
1. MetaMask shows a locked card — Click **"CLICK HERE TO REVEAL SECRET WORDS"**
2. Your **12-word Secret Recovery Phrase** is displayed
   
   Example format (yours will be different):
   ```
   word1  word2  word3  word4
   word5  word6  word7  word8
   word9  word10 word11 word12
   ```
3. **Write these 12 words on paper in exact order** — store securely offline
4. **NEVER:**
   - Screenshot it
   - Store it in email or cloud
   - Share it with anyone — not even MetaMask support
5. Click **"Next"**

### Step 5 — Confirm the Recovery Phrase
1. MetaMask asks you to verify by clicking the words in the correct order
2. Select each word in sequence as it appeared
3. Click **"Confirm"**
4. Success screen: **"Congratulations! Your wallet is ready"**
5. Click **"All Done"**

---

## Exploring Your New Wallet

### Step 6 — Wallet Dashboard Overview

After creation you will see:

```
┌─────────────────────────────────────┐
│  Account 1                    ⋮     │
│  0xAbCd...1234          [Copy icon] │  ← Your wallet address
│                                     │
│         0 ETH                       │  ← Balance
│         $0.00 USD                   │
│                                     │
│  [Buy]  [Send]  [Receive]  [Swap]   │
└─────────────────────────────────────┘
```

| Element | Description |
|---------|-------------|
| Account Name | "Account 1" by default (can be renamed) |
| Address | Your 42-character public address |
| Balance | Current ETH balance |
| Network | Shown at top — "Ethereum Mainnet" by default |

### Step 7 — View Your Wallet Address
1. Click on **"Account 1"** name or the copy icon next to the address
2. Your full address is copied: e.g., `0xD8dA6BF26964aF9D7eEd9e03E53415D37aA96045`
3. This is your **public address** — safe to share for receiving funds
4. To see a QR code: Click **"Receive"** → QR code appears for scanning

### Step 8 — Create Additional Accounts
One seed phrase can generate multiple accounts:
1. Click the circular avatar icon (top right)
2. Click **"Create Account"**
3. Give it a name (e.g., "Savings", "Trading")
4. Each account has a different address but is controlled by the same seed phrase

---

## Performing a Crypto Transaction

### Step 9 — Add Test ETH (Sepolia Testnet)
To practice without spending real money:
1. Click the network dropdown → **"Show/hide test networks"** → enable
2. Select **"Sepolia Test Network"**
3. Copy your wallet address
4. Go to **https://sepoliafaucet.com/**
5. Paste your address → Click **"Send ETH"**
6. ~0.5 test ETH will arrive in ~30 seconds

### Step 10 — Send a Transaction
1. Click **"Send"**
2. In the recipient field, paste another address (e.g., Account 2 address)
3. Enter amount: `0.01 ETH`
4. Click **"Next"**
5. Review the transaction details:

```
From:       Account 1  (0xAbCd...1234)
To:         Account 2  (0xEfGh...5678)
Amount:     0.01 ETH
Gas Fee:    ~0.000042 ETH
Total:      0.010042 ETH
```

6. Click **"Confirm"**
7. Transaction status shows **"Pending"** → changes to **"Confirmed"**

### Step 11 — View Transaction on Etherscan
1. Click on the transaction in MetaMask activity tab
2. Click **"View on Block Explorer"**
3. Etherscan opens showing:

| Field | Value |
|-------|-------|
| Transaction Hash | Unique ID of this transaction |
| Status | Success |
| Block | Block number it was included in |
| From | Sender address |
| To | Receiver address |
| Value | 0.01 ETH |
| Transaction Fee | Gas Used × Gas Price |
| Gas Limit | 21,000 |
| Gas Used | 21,000 (100%) |

---

## Security Best Practices

| Practice | Why |
|----------|-----|
| Never share seed phrase | Anyone with it can drain your wallet |
| Use hardware wallet for large amounts | Keeps private key offline |
| Verify contract addresses before interacting | Prevents phishing |
| Lock MetaMask when not in use | Prevents unauthorized access |
| Use test networks for development | Avoids losing real ETH |
| Check the URL is metamask.io | Fake MetaMask sites steal seed phrases |

---

## Conclusion

A MetaMask wallet was successfully created with a unique public address and secured with a 12-word secret recovery phrase. The wallet operates on the Ethereum blockchain where transactions are signed with the private key, broadcast to the network, and permanently recorded on the blockchain. Test transactions were performed on the Sepolia testnet, demonstrating the full transaction lifecycle from initiation to confirmation on the block explorer.

---

## Viva Questions

**Q1. What is the difference between a private key and a wallet address?**  
A: The private key is a secret number used to sign transactions and prove ownership. The wallet address is derived from the public key (itself derived from the private key) and is safe to share publicly for receiving funds.

**Q2. What happens if you lose your seed phrase?**  
A: The wallet and all funds in it are permanently inaccessible. There is no "forgot password" mechanism — the seed phrase is the only recovery method.

**Q3. Can two people have the same wallet address?**  
A: Mathematically possible but practically impossible — the address space is 2¹⁶⁰, making collisions astronomically unlikely.

**Q4. What is the difference between Mainnet and Testnet?**  
A: Mainnet uses real ETH with real monetary value. Testnet (Sepolia, Goerli) uses fake ETH for testing — transactions are real blockchain operations but the ETH has no value.

**Q5. What is a nonce in a transaction?**  
A: A sequential counter for each account that prevents replay attacks. The nonce increments by 1 for every transaction sent from an address.
