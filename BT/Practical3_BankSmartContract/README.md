# BT Practical 3 — Bank Account Smart Contract on Sepolia Testnet

## Aim
Write and deploy a Solidity smart contract on a test network that allows a customer to deposit money, withdraw money, and check their balance.

---

## Theory

### What is a Smart Contract?
A smart contract is a self-executing program stored on the blockchain. It automatically enforces the terms coded into it without any intermediary (bank, lawyer, etc.).

| Property | Description |
|----------|-------------|
| Immutable | Once deployed, code cannot be changed |
| Transparent | Anyone can read the code on the blockchain |
| Trustless | Executes automatically — no human needed |
| Deterministic | Same inputs always produce same outputs |

### Solidity Basics Used
| Concept | Usage in this contract |
|---------|----------------------|
| `address` | Stores wallet addresses |
| `uint256` | Stores balance (non-negative integer) |
| `payable` | Allows function/address to receive ETH |
| `msg.sender` | Address of whoever called the function |
| `msg.value` | Amount of ETH (wei) sent with a transaction |
| `modifier` | Reusable condition check (onlyOwner) |
| `event` | Log entry stored permanently on blockchain |
| `require()` | Validates conditions; reverts if false |
| `view` | Read-only function — no gas cost when called externally |

### Wei vs ETH
```
1 ETH = 1,000,000,000,000,000,000 wei  (10^18)
1 Gwei = 1,000,000,000 wei             (10^9)
```
Solidity always works in **wei** internally.

---

## Contract Functions

| Function | Type | Description |
|----------|------|-------------|
| `deposit()` | `public payable` | Owner sends ETH to contract |
| `withdraw(uint256 amount)` | `public` | Owner withdraws ETH from contract |
| `getBalance()` | `public view` | Returns current balance in wei |

---

## How to Deploy and Test (Remix IDE)

### Step 1 — Open Remix IDE
1. Go to: **https://remix.ethereum.org/**
2. Remix is a browser-based Solidity IDE — no installation needed

### Step 2 — Create the Contract File
1. In the File Explorer (left panel), click the **"+"** icon
2. Name the file: `BankAccount.sol`
3. Paste the full Solidity code from `BankAccount.sol`

### Step 3 — Compile the Contract
1. Click the **"Solidity Compiler"** tab (second icon, left sidebar)
2. Select compiler version: **0.8.0** or higher
3. Click **"Compile BankAccount.sol"**
4. Green checkmark = compiled successfully

### Step 4 — Connect MetaMask to Sepolia Testnet
1. Open MetaMask
2. Switch network to **"Sepolia Test Network"**
3. Make sure you have test ETH (get from https://sepoliafaucet.com/)

### Step 5 — Deploy the Contract
1. Click the **"Deploy & Run Transactions"** tab (third icon)
2. Under **"Environment"**, select **"Injected Provider - MetaMask"**
3. MetaMask popup will ask to connect — click **"Connect"**
4. Your account address appears in the **"Account"** field
5. Ensure **"BankAccount"** is selected in the Contract dropdown
6. Click **"Deploy"**
7. MetaMask popup shows the transaction — click **"Confirm"**
8. Wait for confirmation (~15 seconds on Sepolia)
9. The deployed contract appears under **"Deployed Contracts"**

### Step 6 — Interact with the Contract

#### Deposit ETH
1. In the **"Value"** field at the top, enter `1` and set unit to **"Ether"**
2. Expand the deployed contract
3. Click the red **"deposit"** button (red = payable function)
4. MetaMask confirms the transaction
5. 1 ETH is now in the contract

#### Check Balance
1. Click the blue **"getBalance"** button (blue = view function, free)
2. Returns the balance in **wei**
   - Example: `1000000000000000000` = 1 ETH

#### Withdraw ETH
1. In the **"withdraw"** input field, enter the amount in wei
   - To withdraw 0.5 ETH enter: `500000000000000000`
2. Click **"withdraw"**
3. MetaMask confirms — ETH is sent back to your wallet

---

## Contract Address (after deployment)
After deploying, copy your contract address from Remix and view it on:  
**https://sepolia.etherscan.io/address/YOUR_CONTRACT_ADDRESS**

You will see:
- All transactions (deposits and withdrawals)
- Contract code (verified)
- Events emitted (Deposited, Withdrawn)

---

## Security Features in the Contract

| Feature | Implementation | Purpose |
|---------|---------------|---------|
| Owner restriction | `onlyOwner` modifier | Only account owner can deposit/withdraw |
| Zero-amount check | `require(amount > 0)` | Prevents zero-value transactions |
| Insufficient funds check | `require(amount <= balance)` | Prevents overdraft |
| Re-entrancy protection | Balance updated before transfer | Prevents re-entrancy attack |

---

## Sample Transaction Output

```
Transaction: Deposit 1 ETH
-----------------------------
From:       0xYourAddress
To:         0xContractAddress
Value:      1.0 ETH
Gas Used:   46,832
Gas Price:  20 Gwei
Fee:        0.00093664 ETH
Event:      Deposited(0xYourAddress, 1000000000000000000)

getBalance() → 1000000000000000000 wei (= 1 ETH)

Transaction: Withdraw 0.5 ETH
-----------------------------
Input:      500000000000000000 (wei)
Gas Used:   28,500
Fee:        0.00057 ETH
Event:      Withdrawn(0xYourAddress, 500000000000000000)

getBalance() → 500000000000000000 wei (= 0.5 ETH)
```

---

## Conclusion
A Solidity smart contract was successfully written and deployed on the Sepolia test network using Remix IDE and MetaMask. The contract allows the owner to deposit ETH (payable function), withdraw ETH (transfer back to owner), and view the balance (free view function). Security measures like owner-only access and balance checks prevent unauthorized access and invalid operations.
