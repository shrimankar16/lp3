# BT Practical 5 — Business Network using Hyperledger

## Aim
Create a business network using Hyperledger Composer that models a commodity trading scenario with Traders, Commodities, and Trade transactions.

---

## Theory

### What is Hyperledger?
Hyperledger is an open-source blockchain project hosted by the Linux Foundation. Unlike public blockchains (Bitcoin, Ethereum), Hyperledger is designed for enterprise permissioned networks.

### Hyperledger Composer
A high-level development framework for building business networks on top of Hyperledger Fabric. A Composer business network has 4 components:

| Component | File | Purpose |
|-----------|------|---------|
| Model | `.cto` | Defines participants, assets, transactions, events |
| Logic | `.js` | JavaScript functions that run when transactions are submitted |
| Access Control | `.acl` | Who can read/write which resources |
| Queries | `.qry` | Named queries to retrieve data from the ledger |

---

## Project Structure

```
trade-network/
├── models/
│   └── trade.cto          ← Data model (participants, assets, transactions)
├── lib/
│   └── logic.js           ← Transaction logic (smart contract functions)
├── test/
│   └── logic.js           ← Automated tests
├── permissions.acl        ← Access control rules
├── queries.qry            ← Named queries
└── package.json           ← Project metadata
```

---

## Business Network Design

### Participants
- **Trader** — A buyer or seller with a unique ID, first name, and last name

### Assets
- **Commodity** — A tradeable good with a trading symbol, description, exchange, quantity, and current owner

### Transactions
- **Trade** — Transfers ownership of a Commodity from one Trader to another

### Events
- **TradeNotification** — Emitted every time a Trade transaction is executed

---

## How to Deploy Using Hyperledger Playground

The easiest way to run this without setting up a full Fabric environment is to use **Hyperledger Composer Playground** (browser-based).

### Step 1 — Open Playground
Go to: **https://composer-playground.mybluemix.net/**  
(Or run locally: `npm install -g composer-playground && composer-playground`)

### Step 2 — Create New Business Network
1. Click **"Deploy a new business network"**
2. Give it a name: `trade-network`
3. Choose **"empty-business-network"** as the template
4. Click **"Deploy"**

### Step 3 — Add the Model File
1. Click **"Model File"** in the left panel
2. Replace the contents with the code from `models/trade.cto`
3. Click **"Update"**

### Step 4 — Add the Script File
1. Click **"Script File"** (Add a file → Script File)
2. Replace the contents with the code from `lib/logic.js`
3. Click **"Update"**

### Step 5 — Update Access Control
1. Click **"Access Control"**
2. Replace with the contents of `permissions.acl`
3. Click **"Update"**

### Step 6 — Test the Network

#### Create Participants (Traders)
Click **"Test"** tab → **"Participant"** → **"Create New Participant"**

```json
{
  "$class": "org.example.trading.Trader",
  "tradeId": "TRADER1",
  "firstName": "Alice",
  "lastName": "Smith"
}
```

```json
{
  "$class": "org.example.trading.Trader",
  "tradeId": "TRADER2",
  "firstName": "Bob",
  "lastName": "Jones"
}
```

#### Create an Asset (Commodity)
Click **"Asset"** → **"Create New Asset"**

```json
{
  "$class": "org.example.trading.Commodity",
  "tradingSymbol": "WHEAT",
  "description": "Premium Wheat",
  "mainExchange": "Chicago",
  "quantity": 500,
  "owner": "resource:org.example.trading.Trader#TRADER1"
}
```

#### Submit a Trade Transaction
Click **"Submit Transaction"** → Select **"Trade"**

```json
{
  "$class": "org.example.trading.Trade",
  "commodity": "resource:org.example.trading.Commodity#WHEAT",
  "newOwner": "resource:org.example.trading.Trader#TRADER2"
}
```

#### Verify Ownership Changed
Click **"Asset"** → **"Commodity"** → Check that WHEAT's owner is now **TRADER2**

---

## Expected Output

```
Before Trade:
  WHEAT.owner = TRADER1 (Alice Smith)

After Trade Transaction:
  WHEAT.owner = TRADER2 (Bob Jones)

Event Emitted:
  TradeNotification { commodity: WHEAT }
```

---

## Running Tests Locally (Optional)

```bash
cd trade-network
npm install
npm test
```

Expected:
```
Trade Network
  ✓ should change commodity owner after a trade
  ✓ should have correct initial commodity quantity

2 passing
```

---

## Conclusion
A Hyperledger Composer business network was successfully created modeling a commodity trading scenario. The `.cto` model file defines the data structure, `logic.js` contains the transaction processor function that updates asset ownership on the ledger, and `permissions.acl` enforces role-based access control. The Trade transaction demonstrates how blockchain can provide an immutable, auditable record of asset ownership transfers between participants.
